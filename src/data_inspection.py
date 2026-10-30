
import pandas as pd

# Load dataset
df = pd.read_csv("data/Loan_default.csv")

print("===== DATASET OVERVIEW =====")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDefault Distribution:")
print(df["Default"].value_counts())

print("\nDefault Rate (%):")
print(round(df["Default"].mean() * 100, 2))
