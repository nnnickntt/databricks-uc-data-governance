# Databricks notebook source
# MAGIC %md
# MAGIC # Example : Dynamic View
# MAGIC
# MAGIC - Column Masking: The full_name field is conditionally masked using is_member('admins') - admin users see the actual name, while non-admins see '***MASKED***'
# MAGIC
# MAGIC - Row-Level Filtering (RLF): The WHERE doctor_email = current_user() clause restricts each user to only see their own patient records (where the doctor_email matches their login)

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view session_14_unity_catalog.vw_patient_billing_enc as 
# MAGIC select 
# MAGIC     case 
# MAGIC         when is_member('admins')  then full_name
# MAGIC         else 'MASKED'
# MAGIC     end as full_name,
# MAGIC     patient_id,
# MAGIC     age,
# MAGIC     diagnosis,
# MAGIC     allergies,
# MAGIC     doctor_assigned,
# MAGIC     citizen_id,
# MAGIC     bill_amount_baht,
# MAGIC     insurance_provider,
# MAGIC     payment_status,
# MAGIC     doctor_email
# MAGIC from session_14_unity_catalog.patient_billing_enc
# MAGIC where doctor_email = current_user()

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from session_14_unity_catalog.vw_patient_billing_enc

# COMMAND ----------

# MAGIC %md
# MAGIC # Dynamic View
# MAGIC
# MAGIC > **Problem** : If the workspace contains many tables, you would need to create multiple views ?
# MAGIC
# MAGIC > **Solution** : Why not create a function for _**column masking**_ and _**row-filtering**_ to enable automatic masking and row-level filtering when querying statements?

# COMMAND ----------

# MAGIC %md
# MAGIC # Example : Column Masking Function
# MAGIC
# MAGIC - The `full_name` column is masked based on user group membership: _adminss_ (for study case) see the real name, others see 'MASKED'.
# MAGIC - Use an ALTER TABLE statement to apply the masking function to the `full_name` column.
# MAGIC > If you need to update the masking logic, simply modify the function—no need to re-alter the table.

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace function session_14_unity_catalog.masking(col string)
# MAGIC returns string
# MAGIC language sql
# MAGIC return case when is_member('adminss') then col else 'MASKED' end

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table session_14_unity_catalog.patient_billing_enc alter column full_name set mask session_14_unity_catalog.masking

# COMMAND ----------

# MAGIC %md
# MAGIC # Example : Row Filtering Function

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace function session_14_unity_catalog.row_filter(dotor_email string)
# MAGIC returns boolean
# MAGIC language sql
# MAGIC return dotor_email = current_user()

# COMMAND ----------

# MAGIC %sql
# MAGIC alter table session_14_unity_catalog.patient_billing_enc set row filter session_14_unity_catalog.row_filter on (doctor_email)

# COMMAND ----------

# MAGIC %md
# MAGIC # Check Result
# MAGIC Query `session_14_unity_catalog.patient_billing_enc` to check column masking and row-level filtering:
# MAGIC
# MAGIC - **Column Masking:** The `full_name` column is automatically masked—_adminss_ see real names, others see 'MASKED'.
# MAGIC - **Row-Level Filtering:** Only records where `doctor_email` matches the _current user's login_ are visible.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from session_14_unity_catalog.patient_billing_enc