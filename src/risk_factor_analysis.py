
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / "data" / "loan_cleaned.csv")

# Income Segmentation
df["IncomeGroup"] = pd.cut(
    df["Income"],
    bins=[0, 30000, 60000, 100000, float("inf")],
    labels=["Low", "Lower-Middle", "Upper-Middle", "High"],
    include_lowest=True
)

# Debt-to-Income Ratio Segmentation
df["DTIGroup"] = pd.cut(
    df["DTIRatio"],
    bins=[0, 0.2, 0.4, 0.6, float("inf")],
    labels=["Low DTI", "Moderate DTI", "High DTI", "Very High DTI"],
    include_lowest=True
)

def analyze_default(column):
    result = (
        df.groupby(column, observed=True)["Default"]
        .agg(
            TotalLoans="count",
            DefaultedLoans="sum",
            DefaultRate="mean"
        )
        .reset_index()
    )

    result["DefaultRate"] = (
        result["DefaultRate"] * 100
    ).round(2)

    print(f"\n===== DEFAULT RATE BY {column} =====")
    print(result)

    return result

income = analyze_default("IncomeGroup")
dti = analyze_default("DTIGroup")
employment = analyze_default("EmploymentType")

# Create charts
sns.set_theme(style="whitegrid")

for title, result, column in [
    ("Income Group", income, "IncomeGroup"),
    ("Debt-to-Income Ratio", dti, "DTIGroup"),
    ("Employment Type", employment, "EmploymentType")
]:
    plt.figure(figsize=(9, 5))

    sns.barplot(
        data=result,
        x=column,
        y="DefaultRate"
    )

    plt.title(f"Loan Default Rate by {title}")
    plt.xlabel(title)
    plt.ylabel("Default Rate (%)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()
