# DataOps & MLOps-Ready Data Pipeline for HR Analytics

> **De dados brutos inconsistentes a ativos analíticos confiáveis, escaláveis e prontos para produção**

Este repositório apresenta a construção de um **pipeline de pré-processamento, validação e preparação de dados** aplicado a um contexto de **Recursos Humanos e avaliação psicotécnica**, com foco em **qualidade de dados, rastreabilidade e prontidão para análises avançadas e modelos preditivos**.

O projeto foi concebido como um **case estratégico de DataOps**, servindo como **fundação confiável** para todo o espectro analítico, **Descritivo, Diagnóstico, Preditivo e Prescritivo**, e como base para futuras práticas de **MLOps**.

---

## 📌 Contexto do Problema

Organizações frequentemente possuem dados de RH com **inconsistências estruturais**, como:

* valores ausentes
* registros duplicados
* valores inválidos (ex.: salários negativos)
* ausência de validações de esquema e regras de negócio

Esses problemas **inviabilizam análises confiáveis**, distorcem indicadores estratégicos e comprometem qualquer iniciativa de **modelagem preditiva ou inferência causal**.

**Pergunta central do projeto**:

> *Como transformar dados brutos e inconsistentes em um ativo analítico confiável, reprodutível e pronto para escalar?*

---

## 🎯 Objetivos

* Construir um **pipeline de DataOps** para tratamento e validação de dados
* Garantir **qualidade, consistência e rastreabilidade**
* Preparar o dataset para:

  * análises descritivas e diagnósticas
  * modelagem preditiva
  * inferência causal
* Entregar **artefatos finais prontos para produção**

---

## 🔍 Abordagem Metodológica

O projeto cobre explicitamente o **ciclo analítico completo**:

### ✔ 1. Entendimento e Análise Exploratória (EDA)

* Inspeção de distribuição das variáveis
* Identificação de padrões, outliers e inconsistências
* Avaliação de impacto dos problemas nos indicadores

### ✔ 2. Validação de Qualidade de Dados (DataOps)

Definição de **regras explícitas de qualidade** (*data quality gates*):

* Salário ≥ 0
* Idade dentro de faixa plausível
* Ausência de duplicados
* Taxa de valores ausentes controlada
* Validação de schema e tipos

### ✔ 3. Limpeza e Tratamento

* Remoção ou correção de valores inválidos
* Tratamento de duplicados
* Estratégias de imputação justificadas por contexto e impacto analítico

### ✔ 4. Preparação para Modelagem

* Dataset final estruturado e versionado
* Features prontas para consumo por modelos
* Base adequada para análises causais e preditivas

---

## 🛠 Ferramentas e Tecnologias

### Linguagem & Análise

* **Python**
* **Pandas, NumPy**
* **Jupyter Notebook**

### Engenharia de Dados / DataOps

* Estrutura modular (`src/`)
* Separação de dados brutos e processados
* Versionamento de artefatos
* Regras de validação explícitas

### Práticas de MLOps (fundação)

* Pipeline reprodutível
* Artefatos prontos para versionamento de modelos
* Estrutura compatível com:

  * MLflow
  * Feature Store
  * CI/CD

---

## 🧠 Justificativa das Escolhas Técnicas

* **Pipeline modular** → facilita escalabilidade, testes e automação
* **Regras de qualidade explícitas** → evitam falhas silenciosas em produção
* **Separação raw/processed** → princípio fundamental de DataOps
* **Versionamento de dados** → reprodutibilidade e auditoria
* **Notebook + código** → equilíbrio entre exploração e engenharia

Essas escolhas refletem **mentalidade de produção**, não apenas exploração analítica.

---

## 📦 Outputs Finais (Entregáveis)

* `data/processed/dataset_clean_v1.csv`

  * dataset validado e pronto para análises e modelos
* Pipeline de pré-processamento reprodutível
* Relatório analítico com:

  * problemas identificados
  * decisões tomadas
  * impacto das correções

---

## 📊 Insights Acionáveis

* Dados de RH sem validação podem gerar **indicadores enviesados**
* Valores inválidos (ex.: salários negativos) distorcem médias e distribuições
* Qualidade de dados é **pré-requisito** para:

  * modelos preditivos confiáveis
  * inferência causal válida
  * decisões estratégicas baseadas em dados

👉 **Insight-chave**:

> *Sem DataOps, não existe MLOps.*

---

## 🚀 Como o Projeto Foi Entregue (Deploy)

Embora o escopo seja local, o projeto foi estruturado como **pronto para produção**:

### Estrutura de entrega

```
data/raw        → dados brutos
data/processed  → dados tratados e versionados
src/            → pipeline reutilizável
artifacts/      → prontos para versionamento de modelos
```

### Arquitetura de Produção (conceitual)

* **Airflow**: orquestração do pipeline
* **Spark**: escalabilidade do pré-processamento
* **AWS S3**: zonas raw / processed
* **Terraform**: infraestrutura como código
* **CI/CD**: validações automáticas de qualidade em PRs

---

## 🛣 Roadmap

* [ ] Feature engineering avançado
* [ ] Modelagem preditiva
* [ ] Experiment tracking com MLflow
* [ ] Feature Store
* [ ] Deploy automatizado (CI/CD)
* [ ] Monitoramento de dados e modelos
