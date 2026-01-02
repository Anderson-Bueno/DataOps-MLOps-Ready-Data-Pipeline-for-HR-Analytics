# DataOps & MLOps-Ready Data Pipeline for HR Analytics

## 🔎 Overview

This repository presents the construction of a **DataOps pipeline for data preprocessing, validation, and preparation**, applied to a **Human Resources and psychometric assessment** context.

The project focuses on **data quality, traceability, and reproducibility**, serving as a **reliable foundation** for the entire analytical spectrum:

- Descriptive
- Diagnostic
- Predictive
- Prescriptive

It was intentionally designed as a **strategic DataOps case study**, forming the groundwork for subsequent **MLOps** workflows.

> **Key Principle:** Without DataOps, there is no MLOps.

---

## 📌 Business Problem

Organizations often face **structural data quality issues** in HR datasets:

| Problem | Business Impact |
|--------|-------------------|
| Missing Values | Biased indicators |
| Duplicate Records | Distorted aggregations |
| Invalid Values (e.g., negative salary) | Incorrect KPIs |
| Lack of Schema Validation | Silent failures |

These issues **prevent reliable analysis**, compromise **predictive modeling**, and weaken **causal inferences**.

**Central project question:**

> *How to transform raw and inconsistent data into a reliable, scalable, and production-ready analytical asset?*

---

## 📚 Context & Sources

This project is based on a **formally defined business problem**, accompanied by data and analytical artifacts that ensure **traceability** between context, observed data, and technical decisions.

Core supporting sources:

- **Business Problem Definition (Project 2 – Data Science Academy)**  
  Document establishing the HR context, the use of a psychometric test, and the explicit goal of **preprocessing data with quality issues** to enable reliable analysis.

- **Employee Dataset (fictional data)**  
  Dataset containing variables such as age, gender, education, salary, and psychometric score.  
  The dataset presents **real quality issues** like missing values, duplicates, and invalid entries, directly motivating DataOps practices.

- **Exploratory Data Analysis & Treatment Notebook**  
  Artifact documenting the **EDA** process, identification of data problems, treatment decisions, and impact of corrections.  
  The notebook serves as an **analytical audit trail**, connecting exploration, decision, and operationalization.

These artifacts ensure the pipeline is not abstract or generic, but the **direct operationalization of a realistic business problem**, with aligned data, decisions, and deliverables.

---

## 🎯 Objectives

- Build a **DataOps pipeline** for data validation and treatment
- Ensure **quality, consistency, and traceability**
- Prepare datasets for:
  - Descriptive and diagnostic analysis
  - Predictive modeling
  - Causal inference
- Deliver **production-ready data artifacts**

---

## 🔍 Methodological Approach

The project explicitly covers the **end-to-end analytical cycle**.

### 1️⃣ Exploratory Data Analysis (EDA)
- Distribution inspection
- Outlier and inconsistency detection
- Impact assessment on business indicators

### 2️⃣ Data Quality Validation (DataOps)
Definition of **explicit data quality gates**:

- Salary ≥ 0
- Age within plausible range
- No duplicate records
- Controlled missing value rate
- Schema and data type validation

### 3️⃣ Cleaning & Treatment
- Correction or removal of invalid values
- Deduplication
- Context-driven imputation strategies

### 4️⃣ Preparation for Modeling
- Final structured and versioned dataset
- Features ready for model consumption
- Base suitable for predictive and causal analysis

---

## 🛠 Tools & Technologies

### Data & Analysis
- Python
- Pandas, NumPy
- Jupyter Notebook

### Data Engineering / DataOps
- Modular pipeline (`src/`)
- Separation between raw and processed data
- Artifact versioning
- Explicit validation rules

### Foundation for MLOps
- Reproducible pipeline
- Model-ready artifacts
- Compatibility with:
  - MLflow
  - Feature Stores
  - CI/CD

---

## 🧠 Technical Justification

| Decision | Justification |
|-------|---------------|
| Modular pipeline | Scalability, testing, automation |
| Explicit quality rules | Prevention of silent failures |
| Raw/processed separation | Core DataOps principle |
| Data versioning | Reproducibility and auditing |
| Notebook + code | Balance between exploration and engineering |

These choices reflect a **production-oriented mindset**, not just exploratory analysis.

---

## 📦 Final Deliverables

- `data/processed/dataset_clean_v1.csv`  
  - Validated dataset ready for analysis and modeling
- Reproducible preprocessing pipeline
- Analytical report including:
  - Identified problems
  - Decisions made
  - Impact of corrections

---

## 📊 Actionable Insights

- Unvalidated HR data leads to **biased decisions**
- Invalid values distort metrics and aggregations
- **Data quality is a prerequisite** for:
  - Reliable predictive models
  - Valid causal inference
  - Strategic decisions

> **Insight:** DataOps enables MLOps — not the other way around.

---

## 🚀 Production & Deployment Readiness

Though executed locally, the project is structured as **production-ready**.

### Data Zones

```text
data/raw        → raw data
data/processed  → validated and versioned data
src/            → reusable pipeline logic
artifacts/      → model-ready assets
```

---

## 🔧 Model Delivery & Consumption

This repository delivers the model as a **reusable, production-ready service**, following MLOps practices.

### 📦 Model Packaging

After training, the model is:

- Versioned as an artifact (`models/latest.joblib`)
- Registered via **MLflow** with:
  - Parameters
  - Metrics
  - Artifacts
- Prepared for API consumption

This process ensures **reproducibility, auditing, and rollback**.

---

### 🚀 Delivery Form

The model is available as a **REST service**, exposed via **FastAPI** and containerized with **Docker**.

**Available endpoints:**

```http
GET  /health     # service status check
POST /predict    # online inference
```
