# Databricks notebook source
# MAGIC %sql
# MAGIC show databases

# COMMAND ----------

# MAGIC %sql
# MAGIC use data_repository

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sample_data

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sample_data

# COMMAND ----------

# MAGIC %pip install koalas==0.32.0

# COMMAND ----------

pip install openpyxl

# COMMAND ----------

pip install ipykernel

ipython kernel install --user --name=venv

# COMMAND ----------

import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
data = pd.read_excel('Employees.xlsx')

# Visualize the data
data.plot(kind='bar')  # plot type using histograme
plt.show()

# COMMAND ----------


