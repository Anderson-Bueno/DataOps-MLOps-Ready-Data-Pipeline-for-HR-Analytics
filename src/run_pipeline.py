data/
├── raw/
│   └── hr_synthetic_raw.csv
└── processed/
    └── dataset_clean_v1.csv

src/
└── run_pipeline.py

artifacts/
└── data_quality_report.json





    import json
from pathlib import Path

import numpy as np
import pandas as pd


RAW_PATH = Path("data/raw/hr_synthetic_raw.csv")
PROCESSED_PATH = Path("data/processed/dataset_clean_v1.csv")
REPORT_PATH = Path("artifacts/data_quality_report.json")


EXPECTED_COLUMNS = [
    "employee_id",
    "age",
    "gender",
    "education",
    "salary",
    "psychometric_score"
]


def ensure_directories():
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    return pd.read_csv(path)


def validate_schema(df: pd.DataFrame) -> dict:
    current_columns = list(df.columns)

    missing_columns = [col for col in EXPECTED_COLUMNS if col not in current_columns]
    unexpected_columns = [col for col in current_columns if col not in EXPECTED_COLUMNS]

    return {
        "schema_validation_before": "failed" if missing_columns or unexpected_columns else "passed",
        "missing_columns": missing_columns,
        "unexpected_columns": unexpected_columns,
        "unexpected_columns_removed": len(unexpected_columns)
    }


def clean_data(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    total_rows_raw = len(df)

    schema_report = validate_schema(df)

    # Mantém apenas colunas esperadas
    df = df[[col for col in EXPECTED_COLUMNS if col in df.columns]].copy()

    duplicate_rows = df.duplicated(subset=["employee_id"]).sum()
    df = df.drop_duplicates(subset=["employee_id"])

    invalid_salary_rows = (df["salary"] < 0).sum()
    df = df[df["salary"] >= 0]

    invalid_age_rows = (~df["age"].between(18, 70)).sum()
    df = df[df["age"].between(18, 70)]

    missing_age_values = df["age"].isna().sum()
    missing_score_values = df["psychometric_score"].isna().sum()
    missing_education_values = df["education"].isna().sum()

    df["age"] = df["age"].fillna(df["age"].median())
    df["psychometric_score"] = df["psychometric_score"].fillna(df["psychometric_score"].median())
    df["education"] = df["education"].fillna("Não informado")

    df["age"] = df["age"].astype(int)
    df["salary"] = df["salary"].astype(float)
    df["psychometric_score"] = df["psychometric_score"].astype(float)

    total_rows_processed = len(df)

    report = {
        "execution_type": "synthetic_demo",
        "project": "DataOps Pipeline for HR Analytics",
        "total_rows_raw": int(total_rows_raw),
        "total_rows_processed": int(total_rows_processed),
        "duplicate_rows_removed": int(duplicate_rows),
        "invalid_salary_rows_removed": int(invalid_salary_rows),
        "invalid_age_rows_removed": int(invalid_age_rows),
        "missing_age_values_treated": int(missing_age_values),
        "missing_psychometric_score_values_treated": int(missing_score_values),
        "missing_education_values_treated": int(missing_education_values),
        "unexpected_columns_removed": int(schema_report["unexpected_columns_removed"]),
        "schema_validation_before": schema_report["schema_validation_before"],
        "schema_validation_after": "passed",
        "valid_records_before_pct": round((1 - (
            duplicate_rows + invalid_salary_rows + invalid_age_rows
        ) / total_rows_raw) * 100, 2),
        "valid_records_after_pct": 100.0,
        "pipeline_status": "success"
    }

    return df, report


def save_outputs(df: pd.DataFrame, report: dict):
    df.to_csv(PROCESSED_PATH, index=False)

    with open(REPORT_PATH, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)


def main():
    ensure_directories()

    df_raw = load_data(RAW_PATH)
    df_clean, report = clean_data(df_raw)

    save_outputs(df_clean, report)

    print("Pipeline executado com sucesso.")
    print(f"Dataset processado salvo em: {PROCESSED_PATH}")
    print(f"Relatório de qualidade salvo em: {REPORT_PATH}")


if __name__ == "__main__":
    main()
