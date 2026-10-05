# Databricks notebook source
# Demo: simple healthcare-style feature engineering + MLflow tracking.
# Synthetic/illustrative only. Not a clinical model.

from pyspark.sql import functions as F

# COMMAND ----------
enc = spark.table("demo.silver.encounter")

features = (
    enc.groupBy("patient_id")
    .agg(
        F.countDistinct("encounter_id").alias("prior_encounter_count"),
        F.avg(F.datediff("discharge_ts", "admit_ts")).alias("avg_length_of_stay_days"),
        F.max("discharge_ts").alias("last_discharge_ts"),
    )
    .fillna({"avg_length_of_stay_days": 0.0})
)

features.write.format("delta").mode("overwrite").saveAsTable("demo.ml.patient_features")

# COMMAND ----------
# Pseudocode-style MLflow example; adapt imports/estimators to the environment.

import mlflow

with mlflow.start_run(run_name="readmission_demo"):
    mlflow.log_param("feature_table", "demo.ml.patient_features")
    mlflow.log_param("note", "Synthetic interview demo only")
    # model.fit(...)
    # mlflow.log_metric("validation_auc", auc)
    # mlflow.sklearn.log_model(model, "model")

# Interview talking points:
# 1. Define the business decision and prediction point first.
# 2. Prevent temporal leakage.
# 3. Make feature computation reproducible.
# 4. Track dataset/model lineage.
# 5. Choose batch vs real-time based on the action latency.
