# Databricks notebook source
# MAGIC %md
# MAGIC # Example : Mask Decrypt Function
# MAGIC
# MAGIC - If you belong to the "admins" group, you can view the decrypted citizen_id; otherwise, the encrypted value is shown.
# MAGIC - PROS: Protects sensitive PII data.

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace function session_14_unity_catalog.citizen_decryption(citizen_id string)
# MAGIC returns string
# MAGIC language sql
# MAGIC return case when is_member('admins') then aes_decrypt(citizen_id,secret('hospital_key','hospital_encrypt_key')) else citizen_id end

# COMMAND ----------

# MAGIC %sql 
# MAGIC alter table session_14_unity_catalog.patient_billing_enc alter column citizen_id set mask session_14_unity_catalog.citizen_decryption

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from session_14_unity_catalog.patient_billing_enc

# COMMAND ----------

# MAGIC %md
# MAGIC # Review Table Masking and Row Filters
# MAGIC
# MAGIC - View all column masks and row filters applied to `session_14_unity_catalog.patient_billing_enc` (col_name = Row Filter , Column Masks).
# MAGIC - Alternatively, review these settings in the Catalog UI.

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended session_14_unity_catalog.patient_billing_enc