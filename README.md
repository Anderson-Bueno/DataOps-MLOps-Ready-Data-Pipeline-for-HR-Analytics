# DataOps Pipeline for HR Analytics

**Da qualidade de dados à fundação confiável para MLOps**

---

## 🔎 Visão Geral

Este repositório apresenta a construção de um **pipeline de DataOps para HR Analytics**, com foco em **pré-processamento, validação, tratamento e preparação de dados** aplicados a um contexto de Recursos Humanos e avaliação psicotécnica.

O projeto foi desenvolvido para demonstrar como dados brutos, inconsistentes e potencialmente enviesados podem ser transformados em um **ativo analítico confiável, rastreável e pronto para alimentar análises e modelos de Machine Learning**.

> **Princípio-chave:** sem DataOps, não existe MLOps.

Este projeto não tem como foco principal o deploy de um modelo preditivo, mas sim a criação da **fundação de dados necessária** para que etapas posteriores de modelagem, monitoramento e MLOps sejam executadas com maior segurança, consistência e reprodutibilidade.

---

## 📌 Problema de Negócio

Organizações que trabalham com dados de Recursos Humanos frequentemente enfrentam problemas estruturais de qualidade de dados, como:

| Problema | Impacto no Negócio |
|---|---|
| Valores ausentes | Indicadores incompletos e análises enviesadas |
| Registros duplicados | Agregações distorcidas e contagens incorretas |
| Valores inválidos, como salário negativo | KPIs inconsistentes e conclusões equivocadas |
| Ausência de validação de schema | Falhas silenciosas no pipeline |
| Tipos de dados inconsistentes | Erros em análises, modelos e integrações |
| Falta de rastreabilidade | Baixa confiança nos dados tratados |

Esses problemas comprometem análises descritivas, diagnósticas, preditivas e prescritivas, além de enfraquecer qualquer tentativa de inferência causal ou tomada de decisão baseada em dados.

### Pergunta central do projeto

> Como transformar dados brutos e inconsistentes de RH em uma base analítica confiável, validada, versionada e preparada para fluxos futuros de Machine Learning e MLOps?

---

## 🎯 Objetivos

Os principais objetivos deste projeto são:

- Construir um pipeline de DataOps para validação e tratamento de dados;
- Identificar problemas de qualidade em dados brutos;
- Aplicar regras explícitas de validação;
- Corrigir inconsistências, duplicidades e valores inválidos;
- Separar dados brutos de dados processados;
- Gerar um dataset limpo e versionado;
- Criar uma base confiável para análises e modelagem preditiva;
- Demonstrar boas práticas de rastreabilidade e reprodutibilidade.

---

## ✅ O que este projeto entrega

Este projeto entrega uma fundação de DataOps para HR Analytics, incluindo:

- ingestão de dados brutos;
- inspeção exploratória da qualidade dos dados;
- validação de schema e tipos de dados;
- identificação de valores ausentes;
- detecção de registros duplicados;
- tratamento de valores inválidos;
- aplicação de regras explícitas de qualidade;
- separação entre dados brutos e processados;
- geração de dataset limpo e versionado;
- pipeline modular reutilizável;
- artefatos prontos para análises e modelagem;
- documentação das decisões técnicas adotadas.

O foco desta versão é garantir que a base de dados esteja **confiável, rastreável e preparada para consumo analítico**.

---

## 🚧 Fora do escopo desta versão

Esta versão concentra-se na camada de **DataOps e preparação confiável dos dados**.

Não fazem parte do escopo principal desta versão:

- deploy em cloud;
- API de inferência em produção;
- monitoramento de drift;
- feature store;
- CI/CD completo;
- model registry em ambiente produtivo;
- retreinamento automatizado de modelos.

Esses itens fazem parte do roadmap natural de evolução para uma arquitetura MLOps completa.

---

## 🏗️ Arquitetura do Pipeline

```text
data/raw
   ↓
schema validation
   ↓
data quality gates
   ↓
cleaning & imputation
   ↓
deduplication
   ↓
data/processed
   ↓
artifacts
   ↓
modeling-ready dataset
