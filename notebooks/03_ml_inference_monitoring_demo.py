# Databricks notebook source
# Demo: inference output + basic monitoring patterns.

from pyspark.sql import functions as F

features = spark.table("demo.ml.patient_features")

# Synthetic score only for demonstration; replace with real model inference.
scored = (
    features
    .withColumn(
        "risk_score",
        F.least(
            F.lit(0.99),
            F.col("prior_encounter_count") * F.lit(0.08)
            + F.col("avg_length_of_stay_days") * F.lit(0.02),
        ),
    )
    .withColumn("scored_at", F.current_timestamp())
)

scored.write.format("delta").mode("overwrite").saveAsTable("demo.ml.patient_risk_scores")

# Simple monitoring metrics
monitor = scored.agg(
    F.count("*").alias("records_scored"),
    F.avg("risk_score").alias("avg_score"),
    F.sum(F.col("risk_score").isNull().cast("int")).alias("null_score_count"),
)

monitor.show(truncate=False)

# Production monitoring should also consider:
# - feature missingness and distribution drift
# - prediction distribution drift
# - inference failures and latency
# - model performance when labels/outcomes arrive
# - approval/retraining policy
