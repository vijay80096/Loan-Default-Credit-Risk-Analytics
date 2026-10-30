
import pandas as pd
import numpy as np
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent
input_file = BASE_DIR / "data" / "Loan_default.csv"
output_file = BASE_DIR / "data" / "loan_cleaned.csv"

# Load dataset
df = pd.read_csv(input_file)

print("===== BEFORE CLEANING =====")
print("Shape:", df.shape)
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())
print("Duplicate Loan IDs:", df["LoanID"].duplicated().sum())

# Remove duplicate records and duplicate Loan IDs
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["LoanID"])

# Remove unnecessary spaces from column names
df.columns = df.columns.str.strip()

# Clean categorical text columns
categorical_cols = df.select_dtypes(include=["object"]).columns.drop(
    "LoanID", errors="ignore"
)

for col in categorical_cols:
    df[col] = df[col].astype("string").str.strip()
    df[col] = df[col].replace("", pd.NA)

# Convert invalid numeric values to missing
numeric_cols = df.select_dtypes(include=np.number).columns

df[numeric_cols] = df[numeric_cols].replace(
    [np.inf, -np.inf], np.nan
)

# Remove records without valid target labels
df = df[df["Default"].isin([0, 1])].copy()

# Report remaining missing values (don't fill blindly)
print("\nMissing Values After Basic Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\n===== AFTER CLEANING =====")
print("Shape:", df.shape)
print("Duplicate Rows:", df.duplicated().sum())
print("Duplicate Loan IDs:", df["LoanID"].duplicated().sum())
print("Default Rate:", round(df["Default"].mean() * 100, 2), "%")
print("\nCleaned dataset saved:", output_file)
