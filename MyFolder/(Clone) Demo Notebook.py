# Databricks notebook source
print('Hello world :)')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 'HELLO WORLD :)' AS C

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Hello world :)

# COMMAND ----------

# MAGIC %run ./setup/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls("/")

# COMMAND ----------

display(files)

# COMMAND ----------


