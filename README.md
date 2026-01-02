# Pipeline de DataOps para HR Analytics - Da Qualidade de Dados à Fundação para MLOps

## 🔍 Visão Geral

Este repositório apresenta a construção de um **pipeline completo de DataOps** para pré-processamento, validação e preparação de dados, aplicado a um contexto estratégico de **Recursos Humanos e avaliação psicotécnica**.

O projeto tem como foco **qualidade de dados, rastreabilidade e reprodutibilidade**, servindo como **fundação confiável** para todo o ciclo analítico: desde análises descritivas até modelagem preditiva e prescritiva.

> **Princípio-chave:** sem DataOps, não existe MLOps.

## 📌 Problema de Negócio

Organizações frequentemente enfrentam **problemas estruturais de qualidade de dados** em bases de RH que comprometem análises confiáveis:
- Valores ausentes e registros duplicados
- Valores inválidos (ex.: salário negativo)
- Ausência de validação de schema
- Impacto direto em KPIs e decisões estratégicas

**Pergunta central:** *Como transformar dados brutos e inconsistentes em um ativo analítico confiável, escalável e pronto para produção?*

## 🎯 Objetivos

- Construir um **pipeline de DataOps** para validação e tratamento de dados
- Garantir **qualidade, consistência e rastreabilidade**
- Preparar datasets para análises e modelagem preditiva
- Entregar **artefatos de dados prontos para produção**

## 🛠 Tecnologias Utilizadas

- **Python** (Pandas, NumPy)
- **Jupyter Notebook** para análise exploratória
- **Pipeline modular** com separação raw/processed
- **Práticas de versionamento** e qualidade de dados
- **Compatível com MLOps** (MLflow, Feature Stores, CI/CD)

## 📁 Estrutura do Projeto

```
data/
├── raw/           # Dados brutos originais
└── processed/     # Dados validados e versionados

src/               # Pipeline modular e reutilizável
artifacts/         # Ativos prontos para modelagem
notebooks/         # Análise exploratória e documentação
```

## 🔍 Abordagem Metodológica

1. **Análise Exploratória de Dados (EDA)**
   - Inspeção de distribuições e detecção de inconsistências
   - Avaliação de impacto nos indicadores de negócio

2. **Validação de Qualidade de Dados**
   - Definição de data quality gates explícitos
   - Validação de schema, faixas de valores e unicidade

3. **Limpeza e Tratamento**
   - Correção de valores inválidos
   - Estratégias de imputação contextual
   - Deduplicação de registros

4. **Preparação para Modelagem**
   - Dataset final estruturado e versionado
   - Features prontas para consumo por modelos

## 📦 Entregáveis

- `data/processed/dataset_clean_v1.csv` - dataset validado e pronto para uso
- Pipeline de pré-processamento reprodutível
- Relatório analítico com problemas identificados e decisões tomadas
- Modelo empacotado como serviço (com MLflow e FastAPI)

## 🚀 Model Delivery & Consumption

O modelo é entregue como **serviço reutilizável e pronto para produção**:

- **Empacotamento**: Versionado como artefato (`models/latest.joblib`)
- **Registro**: MLflow com parâmetros, métricas e artefatos
- **Consumo**: API REST via FastAPI com endpoints:
  - `GET /health` - verificação de status
  - `POST /predict` - inferência online

## 📊 Insights e Conclusões

- Dados de RH sem validação levam a **decisões enviesadas**
- **Qualidade de dados é pré-requisito** para modelos preditivos confiáveis
- DataOps viabiliza MLOps — não o contrário
- Pipeline estruturado para escalabilidade e produção

## 🔧 Como Usar

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute a análise exploratória nos notebooks/
4. Utilize o pipeline modular em src/ para processamento
5. Consulte a documentação para deploy do modelo como API

---

**Status do Projeto**: ✅ Concluído e pronto para produção  
