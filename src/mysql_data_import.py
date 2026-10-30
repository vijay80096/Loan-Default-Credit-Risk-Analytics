
import pandas as pd
import mysql.connector
from pathlib import Path
from getpass import getpass

# =====================================
# 1. FILE PATH
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "loan_cleaned.csv"

# =====================================
# 2. LOAD DATASET
# =====================================

if not CSV_PATH.exists():
    print("CSV file not found:", CSV_PATH)
    raise SystemExit(1)

df = pd.read_csv(CSV_PATH)

print("===== LOAN DATA IMPORT =====")
print("Total CSV Records:", len(df))
print("Total Columns:", len(df.columns))

# =====================================
# 3. MYSQL CONNECTION
# =====================================

password = getpass("Enter loan_analyst MySQL Password: ")

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="loan_analyst",
        password=password,
        database="loan_risk_analytics",
        connection_timeout=20
    )

    print("\nMySQL Connected Successfully!")

except mysql.connector.Error as err:
    print("\nMySQL Connection Failed:", err)
    raise SystemExit(1)

cursor = conn.cursor()

try:
    # =====================================
    # 4. CHECK EXISTING RECORDS
    # =====================================

    cursor.execute("SELECT COUNT(*) FROM loans")
    existing = cursor.fetchone()[0]

    print("Existing MySQL Records:", existing)

    if existing > 0:
        print("Import stopped to prevent duplicate records.")
        raise SystemExit(1)

    # =====================================
    # 5. PREPARE INSERT QUERY
    # =====================================

    columns = df.columns.tolist()

    column_names = ", ".join(
        f"`{col}`" for col in columns
    )

    placeholders = ", ".join(
        ["%s"] * len(columns)
    )

    query = f"""
        INSERT INTO loans ({column_names})
        VALUES ({placeholders})
    """

    # Convert missing values into SQL NULL
    df = df.astype(object).where(pd.notna(df), None)

    # =====================================
    # 6. BATCH IMPORT
    # =====================================

    batch_size = 5000

    for start in range(0, len(df), batch_size):

        batch = df.iloc[start:start + batch_size]

        records = list(
            batch.itertuples(index=False, name=None)
        )

        cursor.executemany(query, records)
        conn.commit()

        imported = min(start + batch_size, len(df))

        print(
            f"Imported {imported:,} / {len(df):,} records"
        )

    # =====================================
    # 7. VERIFY IMPORT
    # =====================================

    cursor.execute("SELECT COUNT(*) FROM loans")
    total = cursor.fetchone()[0]

    print("\n===== IMPORT SUMMARY =====")
    print("CSV Records:", len(df))
    print("MySQL Records:", total)

    if total == len(df):
        print("\nData Import Completed Successfully!")
    else:
        print("\nWarning: Record count mismatch!")

except mysql.connector.Error as err:
    conn.rollback()
    print("\nImport Error:", err)
    print("Previously committed batches may remain in MySQL.")

finally:
    cursor.close()
    conn.close()
