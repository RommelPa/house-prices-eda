# House Prices — Exploratory Data Analysis

## Project Overview

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on the Ames Housing dataset to understand the main factors influencing residential property prices.

The objective is to explore the dataset, evaluate data quality, analyze feature distributions, identify relationships between variables, and detect anomalies before building predictive models.

Dataset source:
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

---

## Dataset

The Ames Housing dataset contains information about residential home sales in Ames, Iowa.

Observations: **1460 houses**
Features: **81 variables describing house characteristics**

The dataset includes both numerical and categorical variables describing aspects such as:

* house quality
* living area
* garage size
* location
* construction year

---

## Exploratory Analysis Workflow

The analysis follows a structured EDA process:

1. Data Overview
2. Data Quality Audit
3. Feature Distribution Analysis
4. Correlation Analysis
5. Outlier Detection
6. EDA Summary and Insights

---

## Key Insights

Key findings from the analysis:

* **OverallQual** (overall house quality) is the strongest predictor of house prices
* **GrLivArea** (above ground living area) has a strong positive correlation with price
* Several variables related to **house size** strongly influence house value
* **Neighborhood** significantly impacts property prices
* Extreme outliers were detected and removed to improve analysis stability

---

## Project Structure

```
house-prices-eda
│
├── data
│   ├── raw   
│
├── notebooks
│
├── src
│
├── reports
│   └── 06_eda_summary.html
│
└── docs
```

---

## Full Analysis Report

The complete exploratory analysis can be viewed here:

reports/06_eda_summary.html