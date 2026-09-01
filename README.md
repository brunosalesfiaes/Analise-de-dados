# 📊 Análise de Dados e Big Data

Projeto desenvolvido para estudar e aplicar conceitos de **Análise de Dados, SQL, Banco de Dados, Python, ETL e Big Data**, utilizando uma base de dados fictícia com informações de clientes e suas contribuições.

O projeto começa com uma base de **5.000 clientes** e tem como objetivo evoluir para cenários com milhões de registros, permitindo estudar diferentes estratégias de armazenamento, processamento e análise de dados.

---

## 🎯 Objetivo

O objetivo deste projeto é desenvolver, de forma prática, um fluxo completo de dados:

```text
Dados brutos
     ↓
Armazenamento
     ↓
SQL / MySQL
     ↓
Tratamento dos dados
     ↓
Análise exploratória
     ↓
Python / Pandas
     ↓
Visualização
     ↓
Big Data / Apache Spark
```

Além de servir como projeto de estudo, a aplicação prática permite compreender como diferentes tecnologias podem ser utilizadas para trabalhar com grandes volumes de informações.

---

## 📦 Base de Dados

A primeira versão do projeto possui **5.000 clientes fictícios**.

Cada registro possui:

| Campo               | Descrição                      |
| ------------------- | ------------------------------ |
| `id_cliente`        | Identificador único do cliente |
| `nome`              | Nome fictício                  |
| `telefone`          | Número de telefone fictício    |
| `valor_contribuido` | Valor contribuído no mês       |
| `forma_pagamento`   | PIX, Espécie ou Não contribuiu |

Os valores de contribuição variam entre:

```text
R$ 0,00 → R$ 100,00
```

Onde:

* `R$ 0,00` representa clientes que não contribuíram;
* `R$ 100,00` representa o limite máximo utilizado na simulação.

> ⚠️ Todos os dados utilizados neste projeto são fictícios e foram gerados exclusivamente para fins educacionais.

---

# 🗂️ Estrutura do Projeto

```text
Analise-de-dados/
│
├── dados/
│   ├── base_clientes_import.csv
│   └── base_clientes.csv
│
├── clienets/
│   ├── criar_banco.sql
│   ├── criar_tabelas.sql
│   ├── importar_clientes.sql
│
│
└── README.md
```

---

# 🛠️ Tecnologias

As principais tecnologias utilizadas e planejadas são:

* 🗄️ MySQL
* 🔎 SQL
* 🐍 Python
* 🐼 Pandas
* 📊 Excel
* ⚡ Apache Spark
* 🐳 Docker
* 🔧 Git
* 🌐 GitHub

---

# 🗄️ Banco de Dados

O banco de dados utilizado inicialmente é o **MySQL**.



---

# 🔎 Consultas SQL

O projeto será utilizado para praticar desde consultas SQL básicas até consultas mais avançadas.

### Total de clientes

```sql
SELECT COUNT(*) AS total_clientes
FROM clientes;
```

### Total arrecadado

```sql
SELECT SUM(valor_contribuido) AS total_arrecadado
FROM clientes;
```

### Média das contribuições

```sql
SELECT AVG(valor_contribuido) AS media_contribuicao
FROM clientes
WHERE valor_contribuido > 0;
```

### Arrecadação por forma de pagamento

```sql
SELECT
    forma_pagamento,
    COUNT(*) AS quantidade,
    SUM(valor_contribuido) AS total
FROM clientes
GROUP BY forma_pagamento;
```

### Ranking dos maiores contribuintes

```sql
SELECT
    nome,
    telefone,
    valor_contribuido
FROM clientes
WHERE valor_contribuido > 0
ORDER BY valor_contribuido DESC
LIMIT 10;
```

---

# 🐍 Análise com Python

Após o armazenamento dos dados no MySQL, o projeto será expandido utilizando **Python e Pandas**.

Exemplo:

```python
import pandas as pd

df = pd.read_csv("dados/clientes.csv")

print(df.head())
print(df.info())
print(df.describe())
```

Serão utilizadas operações como:

```python
groupby()
agg()
sort_values()
value_counts()
query()
loc[]
```

O objetivo é reproduzir e ampliar as análises realizadas inicialmente através do SQL.

---

# 🔄 ETL

Uma das principais etapas do projeto será a implementação de um processo de **ETL — Extract, Transform and Load**.

## Extract

Os dados serão obtidos a partir de arquivos:

```text
Excel
CSV
```

## Transform

Os dados poderão passar por processos de:

* Tratamento de valores nulos;
* Remoção de duplicidades;
* Padronização de nomes;
* Padronização dos telefones;
* Validação dos valores;
* Padronização da forma de pagamento;
* Identificação de inconsistências.

## Load

Após o tratamento, os dados serão carregados no banco:

```text
Excel / CSV
     ↓
Python
     ↓
Tratamento
     ↓
MySQL
```

---

# 📊 Análises

Entre as análises planejadas estão:

### Clientes

* Quantidade total de clientes;
* Quantidade de clientes que contribuíram;
* Quantidade de clientes que não contribuíram;
* Percentual de participação;
* Ranking dos maiores contribuintes.

### Financeiro

* Total arrecadado;
* Média das contribuições;
* Maior contribuição;
* Menor contribuição;
* Arrecadação via PIX;
* Arrecadação em espécie.

### Distribuição

* Distribuição dos valores contribuídos;
* Quantidade de clientes por faixa de contribuição;
* Concentração da arrecadação;
* Comparação entre PIX e espécie.

---

# 📈 Evolução para Big Data

Após concluir as análises utilizando os 5.000 registros iniciais, o projeto será expandido para trabalhar com volumes maiores de dados.

### Primeira etapa

```text
5.000 clientes
```

### Segunda etapa

```text
5.000 clientes
×
12 meses

= 60.000 registros
```

### Terceira etapa

```text
100.000 clientes
×
60 meses

= 6.000.000 registros
```

O objetivo é observar como diferentes tecnologias se comportam conforme o volume de dados aumenta.

---

# ⚡ Apache Spark

Na etapa de Big Data, será utilizado o **Apache Spark** para processamento distribuído.

Exemplo:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AnaliseContribuicoes") \
    .getOrCreate()

df = spark.read.csv(
    "dados/clientes.csv",
    header=True,
    inferSchema=True
)

df.show()
```

Serão estudados conceitos como:

* Spark DataFrames;
* Transformations;
* Actions;
* `groupBy`;
* Agregações;
* Joins;
* Particionamento;
* Processamento distribuído;
* Performance.

---

# 🐳 Docker

Futuramente o ambiente poderá ser executado utilizando Docker.

Arquitetura planejada:

```text
             ┌──────────────┐
             │ Excel / CSV  │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │    Python    │
             │     ETL      │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │    MySQL     │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ Apache Spark │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │  Análises /  │
             │  Dashboard   │
             └──────────────┘
```

---

# 🧠 Conceitos estudados

## Banco de Dados

* Modelagem de dados;
* SQL;
* MySQL;
* Chaves primárias;
* Índices;
* Agregações;
* Consultas complexas.

## Análise de Dados

* Análise exploratória;
* Limpeza de dados;
* Estatística;
* Indicadores;
* Visualização;
* Identificação de padrões.

## Python

* Pandas;
* DataFrames;
* Manipulação de dados;
* Automação;
* ETL.

## Big Data

* Grandes volumes de dados;
* Processamento distribuído;
* Apache Spark;
* Particionamento;
* Paralelismo;
* Performance.

---

# 🛣️ Roadmap

* [x] Gerar base fictícia com 5.000 clientes
* [ ] Converter base para CSV
* [ ] Criar banco MySQL
* [ ] Criar tabela de clientes
* [ ] Importar os 5.000 registros
* [ ] Criar consultas SQL básicas
* [ ] Criar consultas SQL avançadas
* [ ] Realizar análise exploratória
* [ ] Implementar ETL com Python
* [ ] Criar visualizações
* [ ] Criar dashboard
* [ ] Criar histórico de múltiplos meses
* [ ] Gerar milhões de registros
* [ ] Implementar Apache Spark
* [ ] Comparar Pandas × MySQL × Spark
* [ ] Implementar Docker
* [ ] Documentar resultados e métricas

---

# 📚 Objetivo do Projeto

Este projeto tem como principal finalidade desenvolver experiência prática com o ciclo completo de dados, desde sua geração e armazenamento até seu processamento e análise.

```text
                 DADOS
                   │
                   ▼
              INGESTÃO
                   │
                   ▼
             ARMAZENAMENTO
                   │
                   ▼
                ETL
                   │
                   ▼
             PROCESSAMENTO
                   │
                   ▼
               ANÁLISE
                   │
                   ▼
             VISUALIZAÇÃO
                   │
                   ▼
              BIG DATA
```

O projeto será desenvolvido de forma incremental, permitindo acompanhar a evolução das técnicas utilizadas conforme o volume e a complexidade dos dados aumentam.

---

## 👨‍💻 Autor

**Bruno Sales**

Projeto desenvolvido para fins de estudo e prática em:

**Análise de Dados • SQL • Python • ETL • Big Data • Engenharia de Dados**

---

## ⚠️ Dados

Este projeto utiliza exclusivamente **dados fictícios**.

Nenhum dado pessoal real deve ser utilizado neste projeto.

