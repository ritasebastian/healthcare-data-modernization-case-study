# 3. Azure + Databricks Deep Dive

## ADF vs Databricks

A mature answer is not “always use both.”

### ADF strengths

- broad connectivity
- SFTP/file movement
- orchestration
- scheduling
- self-hosted integration runtime
- lightweight copy activities

### Databricks strengths

- PySpark transformations
- large-scale joins/aggregations
- Delta Lake
- notebooks/jobs/workflows
- SQL analytics
- ML/AI
- complex incremental pipelines

### Strong answer

> “I use ADF primarily for connectivity/orchestration and Databricks for scalable transformation and advanced processing, but I would avoid duplicating orchestration unnecessarily. The client’s operating model and existing standards matter.”

## Delta Lake concepts to know

- ACID transactions
- schema enforcement
- schema evolution
- MERGE/upserts
- time travel/version history
- reliable batch and streaming tables

## Incremental processing

### Watermark

Example concept:

```sql
WHERE updated_at > :last_successful_watermark
  AND updated_at <= :current_cutoff
```

Update the watermark only after a successful committed load.

### CDC

Useful when source supports change capture and the business requires fresher updates.

### File ingestion

Maintain manifest/control metadata:

| file_name | checksum | received_at | status | processed_at |
|---|---|---|---|---|
| lab_001.csv | abc123 | ... | SUCCESS | ... |

## Idempotency

A production pipeline should be safely rerunnable.

Techniques:

- Delta MERGE
- dedupe keys
- source change sequence
- processed-file table
- deterministic partitioning
- transactional control-table update

## Failure scenario

**Question:** 100 GB nightly feed fails after 70 GB.

**Answer:**

> “I would not restart blindly. I would persist file/batch-level processing state, identify the last committed unit of work, retry only unprocessed or failed items, and ensure downstream writes are idempotent. Checkpoints and control metadata allow recovery without double-processing. The operator should also receive enough telemetry to understand exactly what failed and why.”

## Performance thinking

Discuss when relevant:

- right-size compute
- avoid unnecessary shuffles
- filter early
- partition only when it helps
- optimize small files
- cache selectively
- incremental instead of full reload
- use SQL/Photon where appropriate
- validate cost and SLA together

## Dev / Test / Prod

Prefer isolated environments with:

- separate credentials
- separate storage boundaries
- environment-specific configuration
- CI/CD promotion
- infrastructure as code
- approval gates

## Unity Catalog

Use for:

- catalogs/schemas/tables
- centralized permissions
- lineage
- governed sharing
- auditability

Common interview point:

> “Analysts should not need direct access to raw PHI-heavy Bronze data if their job only requires curated Gold datasets.”
