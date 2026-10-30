
# Loan Default & Credit Risk Analytics

An end-to-end Data Analytics project using **Python, Pandas, NumPy, Matplotlib, Seaborn, MySQL, SQL, and Power BI** to analyze historical loan defaults, explore credit risk factors, and visualize portfolio performance.

## Project Overview

This project analyzes 255,347 loan records to understand historical default patterns and relationships with borrower and loan characteristics.

The analysis focuses on:
- Loan portfolio performance
- Credit score and default patterns
- Debt-to-income (DTI) analysis
- Income and employment analysis
- Loan purpose analysis
- Rule-based risk segmentation
- Power BI dashboard development

## Technologies Used

- **Python:** Data cleaning and analysis
- **Pandas & NumPy:** Data processing
- **Matplotlib & Seaborn:** Exploratory visualizations
- **MySQL & SQL:** Database management and analysis
- **Power BI & DAX:** Interactive dashboards
- **Git & GitHub:** Version control

## Dataset

**Source:** [Loan Default Prediction — Kaggle](https://www.kaggle.com/datasets/nikhil1e9/loan-default)

| Metric | Value |
|---|---|
| Total Loans | 255,347 |
| Total Columns | 18 |
| Historical Default Rate | 11.61% |
| Defaulted Loans | Approximately 30,000 |

## Python Source Code

All Python scripts are available in the `src` folder.

| File | Description | Source Code |
|---|---|---|
| Data Inspection | Dataset structure and quality checks | [View Code](src/data_inspection.py) |
| Data Cleaning | Data preprocessing | [View Code](src/data_cleaning.py) |
| EDA Analysis | Exploratory data analysis | [View Code](src/eda_analysis.py) |
| Risk Factor Analysis | Historical credit risk patterns | [View Code](src/risk_factor_analysis.py) |
| MySQL Data Import | Import cleaned data into MySQL | [View Code](src/mysql_data_import.py) |

## SQL Source Code

SQL queries are used to explore loan portfolio performance and historical default patterns.

**SQL File:** [View Complete SQL Source Code](sql/loan_risk_analysis.sql)

**Database:** `loan_risk_analytics`

**Table:** `loans`

## Power BI Dashboard

The Power BI report contains two pages.

### 1. Loan Portfolio Overview

![Loan Portfolio Overview](dashboard/screenshots/loan-portfolio-overview.jpeg)

Includes:
- Total Loans
- Total Loan Amount
- Defaulted Loans
- Default Rate
- Loans by Loan Purpose
- Default Rate by Employment Type
- Default Rate by Loan Purpose

### 2. Credit Risk & Manual Review

![Credit Risk & Manual Review](dashboard/screenshots/credit-risk-manual-review.jpeg)

Includes:
- Default Rate by Credit Score Group
- Default Rate by DTI Group
- Default Rate by Income Group
- Default Rate by Risk Points
- Loans by Review Priority
- Default Rate by Review Priority
- Loans by Risk Points

### Dashboard Files

- [Power BI Dashboard (.pbix)](dashboard/Loan_Default_Credit_Risk_Analytics.pbix)
- [Dashboard PDF](dashboard/Loan_Default_Credit_Risk_Dashboard.pdf)

## Project Structure

```text
Loan-Default-Credit-Risk-Analytics/
├── dashboard/
│   ├── Loan_Default_Credit_Risk_Analytics.pbix
│   ├── Loan_Default_Credit_Risk_Dashboard.pdf
│   └── screenshots/
├── sql/
│   └── loan_risk_analysis.sql
├── src/
│   ├── data_inspection.py
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   ├── risk_factor_analysis.py
│   └── mysql_data_import.py
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the GitHub repository.
2. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Download the dataset from Kaggle and place it in the `data` folder.
4. Run the Python analysis scripts.
5. Configure MySQL locally to run the database import.
6. Open the `.pbix` file in Power BI Desktop.

## Key Takeaways

- Explored historical default patterns across borrower and loan characteristics.
- Used Python and SQL for data analysis.
- Created rule-based risk groups for exploratory manual review.
- Developed two interactive Power BI dashboard pages.

**Note:** Risk Points and Review Priority are rule-based exploratory categories, not validated default predictions.

## Project Demo

A Power BI dashboard walkthrough is available as a screen-recorded demonstration shared on LinkedIn.

---

**Domain:** Banking & Financial Services (BFSI)  
**Project Type:** Data Analytics & Business Intelligence
