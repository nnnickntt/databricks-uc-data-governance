# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

df = spark.table("session_14_unity_catalog.patient_billing")

# COMMAND ----------

# MAGIC %md
# MAGIC # Example : Hashing

# COMMAND ----------

hashing ={
    'hash':hash('citizen_id'),
    'xxhash':xxhash64('citizen_id'),
    'sha256':sha2(('citizen_id'),256)
}

hash_df =(
    df.withColumns(hashing)
    .select('citizen_id','hash','xxhash','sha256')
)

# COMMAND ----------

hash_df.limit(5).display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Example : Encryption & Decryption
# MAGIC
# MAGIC - Mock Key 16 digits =  "1234567890123456"
# MAGIC - .cast(string) : convert binary to string

# COMMAND ----------

enc_keys = "1234567890123456"
enc_df = (
    df
    .withColumn('encrypt',aes_encrypt('citizen_id',lit(enc_keys)))
    .withColumn('decrypt',aes_decrypt('encrypt',lit(enc_keys)).cast('string'))
    .select('citizen_id','encrypt','decrypt')
)
enc_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC #Storing Security Keys (databricks.sdk)
# MAGIC
# MAGIC - Secret management helps you keep keys and secrets safe.
# MAGIC
# MAGIC     - A scope is like a folder where you organize and store your keys and secrets.

# COMMAND ----------

from databricks.sdk import *
from databricks.sdk.runtime import dbutils
from databricks.sdk.service.workspace import AclPermission

# COMMAND ----------

# Instace object
workspace_obj = WorkspaceClient()

# COMMAND ----------

# Create Scope
workspace_obj.secrets.create_scope(scope='hospital_key')

# COMMAND ----------

# Store the encryption key as a secret in the scope
workspace_obj.secrets.put_secret(scope='hospital_key',key = 'hospital_encrypt_key',string_value='1234567890123456')

# COMMAND ----------

workspace_obj.secrets.list_scopes()
workspace_obj.secrets.list_secrets(scope ='hospital_key')

# COMMAND ----------

# MAGIC %md
# MAGIC #Restrict access to security keys for a user group using ACL permissions

# COMMAND ----------

# Grant READ permission to 'admins' group for the secret scope
workspace_obj.secrets.put_acl(scope='hospital_key',principal='admins',permission=AclPermission("READ"))

# COMMAND ----------

# MAGIC %md
# MAGIC # Encrypt data with secret key and save to table for future use
# MAGIC
# MAGIC - Encrypt PII data to restrict access by other teams or workgroups and protect sensitive data

# COMMAND ----------

# Get Secret Key
secret_key = dbutils.secrets.get('hospital_key','hospital_encrypt_key')

# COMMAND ----------

enc_df = (
   df.withColumn("citizen_id",aes_encrypt(col("citizen_id"),lit(secret_key)))
)
enc_df.display()

# COMMAND ----------

enc_df.write.mode("overwrite").saveAsTable("session_14_unity_catalog.patient_billing_enc")