# 8. 60-Minute Mock Case Study Interview

Use this as a timed practice session.

## 0–5 min — Scenario

**Interviewer:**

> A 10-hospital health system uses Epic, Oracle, SQL Server, multiple SFTP vendors, and manually exported CSV files. Reporting is inconsistent and AI initiatives are blocked by slow access to trusted data. Design a modern Azure platform. They want an initial production release in 12 weeks.

### Candidate should begin with discovery

Ask 6–10 questions before drawing architecture.

Good questions:

1. Which Epic sources are available—Clarity, Caboodle, FHIR?
2. What are the latency requirements by use case?
3. What volume/growth should we design for?
4. Which feeds contain PHI?
5. What Azure network/security standards already exist?
6. What is the current SFTP volume and failure rate?
7. Which downstream reports cannot be interrupted?
8. Is there an existing ADLS/Databricks/Fabric footprint?
9. Who owns production operations after handoff?
10. Which AI use case is highest priority?

## 5–15 min — Draw target architecture

Expected structure:

Sources → ingestion → secure landing → Bronze → Silver → Gold → BI/AI/sharing

Cross-cutting:

- private networking
- managed identity
- Key Vault
- Unity Catalog
- monitoring
- GitHub Actions
- Terraform

## 15–25 min — Failure / resilience follow-up

**Interviewer:**

> One SFTP feed sends 20,000 files nightly. The pipeline fails after 16,000 files. What happens?

Strong answer should include:

- file manifest/control table
- immutable landing
- idempotent writes
- retry failed/unprocessed files only
- checksum or unique file key
- alerting
- replay capability
- reconciliation

## 25–35 min — AI/ML follow-up

**Interviewer:**

> The hospital wants a readmission-risk model. How would you enable it?

Strong answer:

1. define decision/action and prediction horizon,
2. create trusted Gold/feature data,
3. prevent leakage,
4. use reproducible features,
5. track experiments with MLflow,
6. validate metrics and subgroup behavior,
7. deploy batch first if daily action is enough,
8. monitor input drift and model performance,
9. define retraining and approval process.

Follow-up:

> Why not real-time?

Answer:

> “If care managers act once per day, nightly scoring is simpler and sufficient. I would only add real-time complexity if the operational workflow benefits.”

## 35–45 min — Security / governance

**Interviewer:**

> Data scientists need patient data. How do you prevent unnecessary PHI exposure?

Mention:

- curated approved datasets
- least privilege
- Unity Catalog
- masking/tokenization when appropriate
- separate raw vs curated access
- audit logs
- environment separation
- approved purpose/use case

## 45–52 min — Delivery plan

Candidate proposes:

### Weeks 1–2

Discovery + source assessment + network/security decisions.

### Weeks 2–4

Landing zone + IaC + CI/CD + first-source connectivity.

### Weeks 4–7

Bronze/Silver/Gold reusable patterns + priority feeds.

### Weeks 7–9

Data quality + reconciliation + AI feature dataset.

### Weeks 9–11

Parallel run + performance/security testing + runbooks.

### Week 12

Production cutover + handoff + backlog for phase 2.

## 52–57 min — Leadership

**Interviewer:**

> You have two data engineers and one cloud engineer. How do you divide work?

Strong response:

- architecture lead owns critical decisions and reviews
- cloud engineer: networking/IaC/platform controls
- data engineers: ingestion/transformation/data quality
- pair on high-risk components
- common standards/templates
- daily unblock/risk review
- PR/design reviews

## 57–60 min — Candidate questions

Ask:

- Which modernization bottleneck causes the most delay today?
- How much of the architecture playbook already exists?
- What does a successful handoff to the integration team look like?
- Which AI use cases are most important to clients today?
