# EPID731 - Day 2

This directory contains the materials for **Day 2** of the short course **EPID731: Analysis Of Electronic Health Record (EHR) Data**.

The focus of Day 2 is on accessing and analyzing EHR data using the R programming language. The Jupyter Notebook [`EPID731_Accessing_EHR_Data.ipynb`](https://colab.research.google.com/github/FritscheLab/EPID731/blob/main/Day2/EPID731_Accessing_EHR_Data.ipynb) provides a hands-on introduction to this topic.

> **Note for Live Session:** Participants should open the notebook in Google Colab by clicking the link above or the "Open in Colab" badge at the top of the notebook.

---

## Bonus Material: White Rabbit

For those interested in a deeper dive into data quality assessment, the [`EPID731_BonusWhiteRabbit.ipynb`](https://colab.research.google.com/github/FritscheLab/EPID731/blob/main/Day2/EPID731_BonusWhiteRabbit.ipynb) notebook provides a tutorial on using the White Rabbit tool.

[White Rabbit](httpss://www.ohdsi.org/analytic-tools/whiterabbit-for-etl-design/) is a software tool from OHDSI designed to help prepare for the Extraction, Transformation, and Loading (ETL) of longitudinal healthcare databases into the OMOP Common Data Model (CDM). Its main function is to scan source data (from text files or databases) and generate a detailed report on tables, fields, and values. This report is crucial for designing the ETL process and can be used with its companion tool, Rabbit-In-a-Hat, for mapping the source data to the OMOP CDM.

The notebook covers how to use White Rabbit to scan source data and interpret the data quality report. This is an optional but highly recommended exercise for a more comprehensive understanding of EHR data analysis and preparation for the OMOP CDM.
