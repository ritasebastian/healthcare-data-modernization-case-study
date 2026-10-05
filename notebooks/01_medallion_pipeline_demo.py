# Databricks notebook source
# Demo: Bronze -> Silver -> Gold pattern for interview practice.
# This is intentionally simple and illustrative, not production healthcare logic.

from pyspark.sql import functions as F

# COMMAND ----------
# Example source file ingestion
bronze = (
    spark.read
    .option("header", True)
    .csv("/Volumes/demo/raw/encounters/*.csv")
    .withColumn("ingestion_ts", F.current_timestamp())
    .withColumn("source_system", F.lit("DEMO_EHR"))
)

bronze.write.format("delta").mode("append").saveAsTable("demo.bronze.encounter_raw")

# COMMAND ----------
# Standardize + deduplicate
silver = (
    spark.table("demo.bronze.encounter_raw")
    .withColumn("patient_id", F.trim("patient_id"))
    .withColumn("encounter_id", F.trim("encounter_id"))
    .withColumn("admit_ts", F.to_timestamp("admit_ts"))
    .withColumn("discharge_ts", F.to_timestamp("discharge_ts"))
    .filter(F.col("patient_id").isNotNull())
    .filter(F.col("encounter_id").isNotNull())
    .dropDuplicates(["encounter_id"])
)

silver.write.format("delta").mode("overwrite").saveAsTable("demo.silver.encounter")

# COMMAND ----------
# Simple business-ready aggregate

gold = (
    spark.table("demo.silver.encounter")
    .groupBy("facility_id")
    .agg(
        F.countDistinct("encounter_id").alias("encounter_count"),
        F.countDistinct("patient_id").alias("patient_count"),
    )
)

gold.write.format("delta").mode("overwrite").saveAsTable("demo.gold.facility_encounter_summary")

# Interview talking points:
# - Bronze preserves source-aligned data and lineage metadata.
# - Silver standardizes, validates and deduplicates.
# - Gold is purpose-built for analytics or downstream consumers.
# - Production design should use incremental/idempotent logic rather than overwrite.
