
USE loan_risk_analytics;


SELECT
    COUNT(*) AS total_loans,
    COUNT(DISTINCT LoanID) AS unique_loan_ids,
    SUM(`Default`) AS defaulted_loans,
    COUNT(*) - SUM(`Default`) AS non_defaulted_loans
FROM loans;



SELECT
    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage
FROM loans;



SELECT
    `Default`,
    COUNT(*) AS total_loans,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM loans),
        2
    ) AS percentage
FROM loans
GROUP BY `Default`
ORDER BY `Default`;




SELECT
    LoanPurpose,
    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage
FROM loans
GROUP BY LoanPurpose
ORDER BY default_rate_percentage DESC;



SELECT
    EmploymentType,
    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage
FROM loans
GROUP BY EmploymentType
ORDER BY default_rate_percentage DESC;



SELECT
    Education,
    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage
FROM loans
GROUP BY Education
ORDER BY default_rate_percentage DESC;



SELECT
    CASE
        WHEN CreditScore < 500 THEN 'Below 500'
        WHEN CreditScore < 600 THEN '500-599'
        WHEN CreditScore < 700 THEN '600-699'
        WHEN CreditScore < 800 THEN '700-799'
        ELSE '800+'
    END AS credit_score_group,

    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage

FROM loans
GROUP BY credit_score_group
ORDER BY MIN(CreditScore);



SELECT
    CASE
        WHEN DTIRatio < 0.20 THEN 'Low DTI'
        WHEN DTIRatio < 0.35 THEN 'Moderate DTI'
        WHEN DTIRatio < 0.50 THEN 'High DTI'
        ELSE 'Very High DTI'
    END AS dti_group,

    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage

FROM loans
GROUP BY dti_group
ORDER BY MIN(DTIRatio);



SELECT
    CASE
        WHEN Age < 25 THEN '18-24'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '35-44'
        WHEN Age < 55 THEN '45-54'
        ELSE '55+'
    END AS age_group,

    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage

FROM loans
GROUP BY age_group
ORDER BY MIN(Age);


SELECT
    CASE
        WHEN Income < 30000 THEN 'Below 30K'
        WHEN Income < 60000 THEN '30K-59K'
        WHEN Income < 90000 THEN '60K-89K'
        ELSE '90K+'
    END AS income_group,

    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage

FROM loans
GROUP BY income_group
ORDER BY MIN(Income);




SELECT
    CASE
        WHEN InterestRate < 5 THEN 'Below 5%'
        WHEN InterestRate < 10 THEN '5%-9.99%'
        WHEN InterestRate < 15 THEN '10%-14.99%'
        ELSE '15% and above'
    END AS interest_rate_group,

    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage

FROM loans
GROUP BY interest_rate_group
ORDER BY MIN(InterestRate);



SELECT
    LoanTerm,
    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage
FROM loans
GROUP BY LoanTerm
ORDER BY LoanTerm;



SELECT
    HasMortgage,
    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage
FROM loans
GROUP BY HasMortgage;



SELECT
    HasCoSigner,
    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage
FROM loans
GROUP BY HasCoSigner;



SELECT
    MaritalStatus,
    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage
FROM loans
GROUP BY MaritalStatus
ORDER BY default_rate_percentage DESC;



SELECT
    `Default`,
    COUNT(*) AS total_loans,
    ROUND(AVG(Income), 2) AS average_income,
    ROUND(AVG(LoanAmount), 2) AS average_loan_amount,
    ROUND(AVG(CreditScore), 2) AS average_credit_score,
    ROUND(AVG(DTIRatio), 3) AS average_dti,
    ROUND(AVG(InterestRate), 2) AS average_interest_rate
FROM loans
GROUP BY `Default`;


SELECT
    LoanID,
    CreditScore,
    DTIRatio,
    InterestRate,

    (
        CASE WHEN CreditScore < 600 THEN 1 ELSE 0 END +
        CASE WHEN DTIRatio >= 0.40 THEN 1 ELSE 0 END +
        CASE WHEN InterestRate >= 15 THEN 1 ELSE 0 END
    ) AS risk_points,

    CASE
        WHEN (
            CASE WHEN CreditScore < 600 THEN 1 ELSE 0 END +
            CASE WHEN DTIRatio >= 0.40 THEN 1 ELSE 0 END +
            CASE WHEN InterestRate >= 15 THEN 1 ELSE 0 END
        ) >= 2 THEN 'High Risk'

        WHEN (
            CASE WHEN CreditScore < 600 THEN 1 ELSE 0 END +
            CASE WHEN DTIRatio >= 0.40 THEN 1 ELSE 0 END +
            CASE WHEN InterestRate >= 15 THEN 1 ELSE 0 END
        ) = 1 THEN 'Medium Risk'

        ELSE 'Low Risk'
    END AS risk_category,

    `Default`

FROM loans
ORDER BY risk_points DESC;



SELECT
    CASE
        WHEN (
            (CreditScore < 600) +
            (DTIRatio >= 0.40) +
            (InterestRate >= 15)
        ) >= 2 THEN 'High Risk'

        WHEN (
            (CreditScore < 600) +
            (DTIRatio >= 0.40) +
            (InterestRate >= 15)
        ) = 1 THEN 'Medium Risk'

        ELSE 'Low Risk'
    END AS risk_category,

    COUNT(*) AS total_loans,
    SUM(`Default`) AS defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS default_rate_percentage

FROM loans
GROUP BY risk_category
ORDER BY default_rate_percentage DESC;



SELECT
    LoanID,
    Income,
    LoanAmount,
    CreditScore,
    DTIRatio,
    InterestRate,
    `Default`
FROM loans
ORDER BY LoanAmount DESC
LIMIT 20;



SELECT
    COUNT(*) AS total_loans,
    SUM(LoanAmount) AS total_loan_amount,
    ROUND(AVG(LoanAmount), 2) AS average_loan_amount,
    SUM(`Default`) AS total_defaulted_loans,
    ROUND(AVG(`Default`) * 100, 2) AS overall_default_rate,
    ROUND(AVG(CreditScore), 2) AS average_credit_score,
    ROUND(AVG(DTIRatio), 3) AS average_dti,
    ROUND(AVG(InterestRate), 2) AS average_interest_rate
FROM loans;


