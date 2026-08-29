# Data Cleaning & Analysis

A practical repository for learning and applying **data cleaning, preprocessing, exploration, and analysis** using Python and the Pandas ecosystem.

The repository is designed to grow over time as a personal data engineering and analytics workspace, starting with data cleaning and gradually expanding into more advanced data workflows.

---

## 🎯 Purpose

The main goal of this repository is to build strong practical skills in working with real-world datasets.

The focus is on understanding how to:

* Inspect and understand datasets
* Identify data quality issues
* Clean and preprocess raw data
* Handle missing values
* Detect and handle duplicates
* Fix inconsistent data
* Convert and validate data types
* Work with strings and categorical data
* Detect and investigate outliers
* Transform and reshape datasets
* Perform exploratory data analysis (EDA)
* Extract useful information from data
* Document the data preparation process

The emphasis is on **understanding the reasoning behind each transformation**, not just applying Pandas functions.

---

##

---

## 🧰 Tools & Technologies

### Current

* Python
* Pandas
* NumPy
* Jupyter Notebook

### Planned

The repository will gradually expand toward tools and technologies commonly used in modern data workflows, including:

* SQL
* Data Visualization
* Statistics
* Data Validation
* ETL / ELT concepts
* Data Pipelines
* dbt
* Apache Airflow
* Docker
* Cloud Data Services

These technologies will be added progressively through practical projects.

---

## 🧹 Data Cleaning Workflow

The general workflow followed in this repository is:

```text
Raw Dataset
     │
     ▼
Understand the Data
     │
     ▼
Inspect Data Quality
     │
     ▼
Handle Missing Values
     │
     ▼
Handle Duplicates
     │
     ▼
Fix Data Types
     │
     ▼
Standardize Values
     │
     ▼
Handle Outliers
     │
     ▼
Transform Data
     │
     ▼
Validate the Result
     │
     ▼
Clean Dataset
```

The exact workflow depends on the dataset and its business context.

---

## 📊 Datasets

This repository contains practical exercises and cleaning projects based on different types of datasets, including:

* Cafe Sales
* E-commerce
* Netflix
* Online Food
* Airbnb
* Credit Risk
* Exam Data

Each dataset is treated as a separate practical exercise with its own cleaning requirements.

---

## 🔎 What I Practice

### Data Inspection

```python
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.columns
df.dtypes
```

### Data Cleaning

* Missing values
* Duplicates
* Incorrect data types
* Inconsistent values
* Invalid records
* Formatting problems
* String normalization

### Data Transformation

* Filtering
* Sorting
* Grouping
* Aggregation
* Merging
* Joining
* Concatenation
* Reshaping
* Feature creation

### Data Analysis

After cleaning the data, the next step is to explore it and answer questions such as:

* What are the most common categories?
* What trends exist?
* Which groups perform better?
* Are there unusual values?
* What relationships exist between variables?

---

## 🚀 Future Direction

This repository is intentionally built to evolve.

The long-term direction is:

```text
Python
   │
   ▼
Pandas
   │
   ▼
Data Cleaning
   │
   ▼
Data Analysis
   │
   ▼
SQL
   │
   ▼
ETL / ELT
   │
   ▼
Data Pipelines
   │
   ├── Airflow
   ├── dbt
   └── Docker
   │
   ▼
Data Engineering
   │
   ▼
Cloud Data Platforms
```

The goal is not to turn this repository into a collection of random notebooks.

Instead, it will gradually become a **practical record of the process from raw data to reliable, usable data**.

---

## 📌 Current Status

**Stage:** Data Cleaning & Pandas

The repository is actively evolving. New datasets, techniques, analysis notebooks, and data engineering workflows will be added over time.

---

## 🗺️ Roadmap

* [x] Python fundamentals for data work
* [x] Pandas fundamentals
* [ ] Advanced Pandas
* [ ] Data Cleaning patterns
* [ ] Exploratory Data Analysis
* [ ] Data Visualization
* [ ] Statistics fundamentals
* [ ] SQL
* [ ] ETL / ELT
* [ ] Data Validation
* [ ] Data Pipelines
* [ ] Airflow
* [ ] dbt
* [ ] Docker
* [ ] Cloud Data Engineering
* [ ] End-to-end Data Engineering Projects

---

## 📚 Philosophy

> **Don't just clean the data. Understand why it is dirty, what the problem means, and whether the transformation actually makes the data better.**

This repository is primarily a learning and experimentation workspace, with an emphasis on practical skills, reproducibility, and progressively better data workflows.

---

## 👤 Author

**Kirollos**

Software Development → Data Engineering

This repository represents my ongoing journey toward building practical skills in data analysis and data engineering.
