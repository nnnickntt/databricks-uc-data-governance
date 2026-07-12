# Databricks notebook source
# MAGIC %sql
# MAGIC create schema if not exists workspace.session_14_unity_catalog

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

data = [
    ("pat001", "John Doe", 45, "Diabetes Type II", "Penicillin", "Dr.Nawin", "1-1111-11111-11", 15400, "AIB", "Pending","nicknick@mail.com"),
    ("pat002", "Somchai Rakdee", 32, "COVID-19", "None", "Dr.Piti", "1-3333-11111-11", 8200, "Krungthep", "Paid","nicknick@gmail.com"),
    ("pat003", "Jane Smith", 28, "Hypertension", "Aspirin", "Dr.Arm", "1-1111-22222-11", 3500, "Muangthong", "Pending","nicknick@gmail.com"),
    ("pat004", "Napat Chaiyaporn", 54, "Asthma", "Sulfa", "Dr.Valen", "1-5555-11111-11", 12000, "AIA", "Paid","nicknicknuttiwut@gmail.com"),
    ("pat005", "Suda Phongchai", 39, "Migraine", "Ibuprofen", "Dr.Nawin", "1-1111-66666-11", 4100, "Bangkok Life", "Pending","nicknick@gmail.com"),
    ("pat006", "Michael Lee", 60, "Heart Disease", "None", "Dr.Arm", "1-1111-11111-11", 20000, "AIB", "Paid","Arm@gmail.com"),
    ("pat007", "Pimchanok Srisuk", 25, "COVID-19", "Paracetamol", "Dr.Piti", "1-7777-11111-11", 9000, "Krungthep", "Pending","nicknicknuttiwut@gmail.com"),
    ("pat008", "David Brown", 47, "Diabetes Type I", "Insulin", "Dr.Valen", "1-1111-88888-11", 17000, "AIA", "Paid","nicknicknuttiwut@gmail.com"),
    ("pat009", "Somsak Thongdee", 36, "Hypertension", "None", "Dr.Nawin", "1-1111-11111-00", 3800, "Muangthong", "Pending","nicknick@gmail.com"),
    ("pat010", "Linda Chan", 52, "Asthma", "Penicillin", "Dr.Piti", "1-1111-11111-77", 11500, "Bangkok Life", "Paid","nicknicknuttiwut@gmail.com"),
    ("pat010", "Linda Chan", 52, "Asthma", "Penicillin", "Dr.Piti", "1-5554-66666-11", 11500, "Bangkok Life", "Paid","nicknicknuttiwut@gmail.com")
]

schema = StructType([
    StructField("patient_id", StringType(), True),
    StructField("full_name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("diagnosis", StringType(), True),
    StructField("allergies", StringType(), True),
    StructField("doctor_assigned", StringType(), True),
    StructField("citizen_id", StringType(), True),
    StructField("bill_amount_baht", IntegerType(), True),
    StructField("insurance_provider", StringType(), True),
    StructField("payment_status", StringType(), True),
    StructField("doctor_email", StringType(), True)
])

df = spark.createDataFrame(data, schema)
df.write.mode("overwrite").saveAsTable("workspace.session_14_unity_catalog.patient_billing")

# COMMAND ----------

print(
    """
schema workspace.session_14_unity_catalog has been created
table session_14_unity_catalog.patient_billing has been created
    """
)