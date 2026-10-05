# 1. Case Study Strategy

## What the interviewer is testing

They are not only testing whether you know Databricks. They want to see whether you can:

- enter an unfamiliar health-system environment,
- ask the right discovery questions,
- identify risks and dependencies,
- design a realistic Azure target state,
- explain tradeoffs,
- protect PHI,
- lead engineers,
- speak to CIO/VP-level stakeholders,
- modernize incrementally rather than recklessly,
- and leave behind something the next team can operate.

## The response framework

Use this every time:

**Discover → Assess → Design → Secure → Build → Migrate → Validate → Operate → Handoff**

### Discover

Ask about:

- source systems: Epic Clarity, Caboodle, SQL Server, Oracle, FHIR APIs, LIS, PACS, pharmacy, claims, files, SFTP;
- data volume and growth;
- batch vs near-real-time needs;
- refresh schedules and SLAs;
- PHI/PII classification;
- current network topology;
- authentication methods;
- downstream reports, models and partner feeds;
- support model and operational ownership;
- current pain points and failure history.

### Assess

Create a source inventory with:

| Area | What to capture |
|---|---|
| Source | system, owner, technology |
| Connectivity | DB, API, FHIR, SFTP, file |
| Frequency | real-time, hourly, nightly |
| Volume | rows/files/GB per day |
| Sensitivity | PHI, PII, non-sensitive |
| Reliability | failure rate, retries, manual steps |
| Consumer | BI, AI/ML, operational app, partner |
| Modernization priority | high / medium / low |

### Design

Separate the target architecture into:

1. connectivity and ingestion,
2. landing/storage,
3. transformation,
4. governance,
5. security,
6. observability,
7. serving/sharing,
8. CI/CD + IaC.

### Secure

Mention security from the beginning, not as an afterthought:

- private networking,
- managed identities/service principals,
- Key Vault,
- least privilege,
- Unity Catalog,
- encryption in transit and at rest,
- audit logging,
- PHI minimization/de-identification where appropriate.

### Build & Migrate

Prefer phased modernization:

1. establish landing zone,
2. onboard one representative source,
3. prove pattern,
4. validate quality/security/operations,
5. migrate additional feeds,
6. parallel run,
7. cut over,
8. retire legacy process when safe.

### Validate

Validate both technically and functionally:

- row counts,
- hash/checksum where useful,
- duplicates,
- nulls,
- freshness,
- schema drift,
- reconciliation totals,
- clinical/business rules,
- downstream report parity.

### Operate & Handoff

A platform is not finished when the pipeline runs once.

Deliver:

- monitoring,
- alerts,
- runbooks,
- ownership matrix,
- incident procedures,
- deployment docs,
- data lineage,
- recovery procedures,
- SLAs/SLOs,
- known limitations,
- support handoff.

## Strong opening answer

> “Before selecting technologies, I would begin with technical discovery. I need to understand the source landscape, data volumes, refresh requirements, PHI classification, network constraints, downstream consumers, operational SLAs, and the client’s support model. From there I would design a secure landing zone, choose source-specific ingestion patterns, standardize processing in Databricks, implement governance and observability, then migrate incrementally with reconciliation and parallel-run validation before cutover.”

## What to avoid

Avoid statements like:

- “Everything should be streaming.”
- “We should immediately eliminate SFTP.”
- “Databricks makes the environment HIPAA compliant.”
- “Just restart the failed pipeline.”
- “We can migrate every source at once.”
- “One tool should handle everything.”

Director-level answers should show judgment, not tool enthusiasm.
