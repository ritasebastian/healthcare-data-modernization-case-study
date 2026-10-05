# 2. Architecture Walkthrough

![Healthcare Data Modernization Architecture](../assets/healthcare-data-modernization-architecture.png)

## 1. Source systems

Typical hospital environment:

- Epic Clarity
- Epic Caboodle
- FHIR APIs
- LIS / lab systems
- PACS / radiology
- pharmacy
- claims / revenue cycle
- SQL Server / Oracle / PostgreSQL
- CSV / Excel
- SFTP / vendor file drops
- REST/SOAP APIs
- manual exports

### Interview message

> “I would not force every source into a single ingestion pattern. The source capability and business latency requirement determine the appropriate design.”

## 2. Ingestion & connectivity

### Azure Data Factory

Good fit for:

- orchestration,
- connectors,
- SFTP,
- database extraction,
- scheduling,
- dependency management.

### Self-hosted integration runtime

Use when secure connectivity is required to on-prem/private source systems.

### Incremental patterns

Choose among:

- CDC,
- updated timestamp watermark,
- sequence number,
- file manifest,
- API continuation tokens,
- Auto Loader/file discovery.

### Reliability rules

Every ingestion design should answer:

- Can it resume?
- Is it idempotent?
- Can we replay safely?
- Can we prove what was processed?
- How do we detect duplicates?
- How do we alert operators?

## 3. Azure landing zone

Include:

- Azure VNet
- private endpoints
- managed identity
- Key Vault
- Defender / security monitoring
- ADLS Gen2
- least-privilege RBAC

Keep storage and compute access private where possible.

## 4. Databricks medallion layers

### Bronze — immutable/source-aligned

Store source-faithful data plus metadata:

- ingestion timestamp
- source system
- file name
- batch ID
- extraction timestamp
- source checksum when useful

Purpose:

- replay
- audit
- debugging
- lineage

### Silver — standardized/clean

Typical work:

- deduplication
- standard column naming
- data type enforcement
- timestamp normalization
- code mapping
- null handling
- quality rules
- de-identification/tokenization where required
- incremental MERGE

### Gold — business-ready

Examples:

- patient encounters
- population health cohorts
- readmission metrics
- physician/facility measures
- revenue-cycle analytics
- AI/ML feature tables
- partner-ready data products

## 5. Consumption & sharing

Internal:

- Power BI / Fabric
- Databricks SQL
- ML/AI workflows
- operational applications

External:

- Delta Sharing
- Fabric external sharing
- secure API/data product

The key principle is **governed sharing instead of uncontrolled file copying**.

## 6. Cross-cutting platform services

- Unity Catalog
- Purview
- Azure Monitor / Log Analytics
- GitHub
- GitHub Actions
- Terraform/Bicep
- audit logs
- data-quality dashboards

## Five-minute architecture answer

> “The environment starts with healthcare source systems such as Epic Clarity, Caboodle, FHIR APIs, ancillary databases, claims platforms, files and SFTP feeds. I would choose ingestion patterns based on source capability and latency, using ADF for orchestration/connectivity and Databricks for scalable transformation where that combination adds value. Data lands unchanged in a controlled Bronze layer for replay and auditability, is standardized and quality-checked in Silver, and becomes business-ready in Gold for analytics, AI/ML and governed external sharing. The platform is protected with private networking, managed identities, Key Vault, RBAC and audit logging, governed through Unity Catalog/Purview, deployed through GitHub Actions and Terraform, and monitored with operational and data-quality controls. Migration would be phased and validated with parallel runs before cutover.”
