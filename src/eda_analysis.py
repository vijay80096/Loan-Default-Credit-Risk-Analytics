
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data" / "loan_cleaned.csv")

# Credit Score Segmentation
df["CreditScoreGroup"] = pd.cut(
    df["CreditScore"],
    bins=[0, 580, 670, 740, 850],
    labels=["Poor", "Fair", "Good", "Excellent"],
    include_lowest=True
)

# Default Rate by Credit Score Group
credit_risk = (
    df.groupby("CreditScoreGroup", observed=True)["Default"]
    .agg(["count", "mean"])
    .reset_index()
)

credit_risk["DefaultRate"] = (
    credit_risk["mean"] * 100
).round(2)

print("\n===== CREDIT SCORE RISK ANALYSIS =====")
print(credit_risk[["CreditScoreGroup", "count", "DefaultRate"]])

# Visualization
sns.set_theme(style="whitegrid")

plt.figure(figsize=(9, 5))

sns.barplot(
    data=credit_risk,
    x="CreditScoreGroup",
    y="DefaultRate"
)

plt.title("Loan Default Rate by Credit Score Group")
plt.xlabel("Credit Score Group")
plt.ylabel("Default Rate (%)")

plt.tight_layout()
plt.show()
