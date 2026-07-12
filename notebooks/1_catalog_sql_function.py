# Databricks notebook source
# MAGIC %run ./_ddl

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from session_14_unity_catalog.patient_billing
# MAGIC limit 5

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC # **Example : Create Column Function (Scalar)**
# MAGIC
# MAGIC - Result : Return discount(baht/30)

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace function session_14_unity_catalog.get_discount(baht int)
# MAGIC returns int
# MAGIC language sql
# MAGIC return ceil(baht/30)

# COMMAND ----------

# MAGIC %sql
# MAGIC select full_name ,bill_amount_baht,session_14_unity_catalog.get_discount(bill_amount_baht) as discount
# MAGIC from session_14_unity_catalog.patient_billing

# COMMAND ----------

# MAGIC %md
# MAGIC # **Example : Create Table Function (Table)**
# MAGIC
# MAGIC - Result: Returns a table with patient_id, full_name, bill_amount_baht, and payment_status filtered by payment_status = 'Paid'

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace function session_14_unity_catalog.get_payment_status(status string)
# MAGIC returns table( patient_id string ,full_name string ,bill_amount_baht int,payment_status string)
# MAGIC language sql
# MAGIC return (
# MAGIC     select patient_id,full_name,bill_amount_baht,payment_status
# MAGIC     from session_14_unity_catalog.patient_billing
# MAGIC     where payment_status = status
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from session_14_unity_catalog.get_payment_status('Paid')