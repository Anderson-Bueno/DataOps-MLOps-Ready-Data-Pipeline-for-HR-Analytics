from pathlib import Path

import numpy as np
import pandas as pd


RAW_PATH = Path("data/raw/hr_raw.csv")


def generate_hr_data(n_rows: int = 1000, random_state: int = 42) -> pd.DataFrame:
    np.random.seed(random_state)

    df = pd.DataFrame({
        "employee_id": range(1, n_rows + 1),
        "age": np.random.randint(18, 66, size=n_rows),
        "gender": np.random.choice(["Masculino", "Feminino", "Outro"], size=n_rows, p=[0.48, 0.48, 0.04]),
        "education": np.random.choice(
            ["Ensino Médio", "Graduação", "Pós-graduação", "Mestrado"],
            size=n_rows,
            p=[0.25, 0.45, 0.25, 0.05]
        ),
        "salary": np.random.normal(loc=6500, scale=2200, size=n_rows).round(2),
        "psychometric_score": np.random.normal(loc=72, scale=12, size=n_rows).round(2)
    })

    # Inserir salários negativos
    invalid_salary_idx = np.random.choice(df.index, size=12, replace=False)
    df.loc[invalid_salary_idx, "salary"] = -np.abs(df.loc[invalid_salary_idx, "salary"])

    # Inserir idades inválidas
    invalid_age_idx = np.random.choice(df.index, size=14, replace=False)
    df.loc[invalid_age_idx[:7], "age"] = 15
    df.loc[invalid_age_idx[7:], "age"] = 85

    # Inserir valores ausentes
    missing_age_idx = np.random.choice(df.index, size=42, replace=False)
    missing_score_idx = np.random.choice(df.index, size=57, replace=False)
    missing_education_idx = np.random.choice(df.index, size=19, replace=False)

    df.loc[missing_age_idx, "age"] = np.nan
    df.loc[missing_score_idx, "psychometric_score"] = np.nan
    df.loc[missing_education_idx, "education"] = np.nan

    # Inserir coluna inesperada
    df["temporary_column"] = np.random.choice(["A", "B", "C"], size=n_rows)

    # Inserir duplicidades
    duplicate_rows = df.sample(n=25, random_state=random_state)
    df = pd.concat([df, duplicate_rows], ignore_index=True)

    return df


def main():
    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)

    df = generate_synthetic_hr_data()
    df.to_csv(RAW_PATH, index=False)

    print("Dataset gerado com sucesso.")
    print(f"Arquivo salvo em: {RAW_PATH}")
    print(f"Total de registros gerados: {len(df)}")


if __name__ == "__main__":
    main()
