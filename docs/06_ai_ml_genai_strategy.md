# 6. AI/ML + GenAI Strategy

This section is intentionally deeper because AI/ML is a likely area of interest for the candidate.

## The architecture story

Do not start AI/ML with a model.

Start with trusted data:

```text
EHR / Claims / FHIR / Labs / SFTP
        ↓
Bronze (source faithful)
        ↓
Silver (clean + standardized)
        ↓
Gold (analytics-ready)
        ↓
Feature tables / training datasets
        ↓
ML training + tracking
        ↓
Model registry / approval
        ↓
Batch or real-time inference
        ↓
Monitoring + feedback
```

## Example healthcare AI/ML use cases

Use examples carefully and frame them as decision-support unless the engagement explicitly calls for clinical decision-making.

Potential use cases:

- hospital readmission risk
- length-of-stay prediction
- appointment no-show prediction
- claim denial prediction
- staffing/demand forecasting
- anomalous billing/transaction detection
- patient outreach prioritization
- document classification/extraction
- care-management cohort prioritization

## Example feature set — readmission risk

Possible features:

- prior admissions in 30/90/365 days
- recent ED visits
- length of stay
- diagnosis groups
- comorbidity count
- medication count
- age band
- discharge disposition
- missed appointments
- recent lab abnormalities

Avoid using sensitive attributes casually; feature use must be governed and justified.

## ML lifecycle on Databricks

### 1. Feature engineering

PySpark/SQL generates reproducible features from curated data.

### 2. Experiment tracking

MLflow tracks:

- parameters
- metrics
- artifacts
- model versions
- dataset/version references

### 3. Registry / approval

Promote approved models through controlled stages/environments.

### 4. Inference

Choose based on latency:

#### Batch

Good for:

- nightly risk scoring
- weekly population health models
- denial prediction before downstream processing

#### Near-real-time / streaming

Use only when business value requires fast action.

Examples:

- operational alerting
- rapidly changing event streams

### 5. Monitoring

Monitor both the pipeline and the model:

- input data quality
- feature drift
- prediction distribution drift
- missing features
- latency
- failure rate
- model performance when labels arrive

## Batch vs streaming answer

> “I would not default to streaming. If a care-management team acts on a daily work queue, a reliable nightly batch is often cheaper and simpler. I would use streaming only when the decision truly benefits from low latency.”

## Training vs inference separation

Training is typically heavier and less frequent.

Inference is optimized for reliable repeated execution.

Keep separate controls for:

- compute
- credentials
- data access
- deployment
- monitoring

## Feature Store concept

A feature store helps make features:

- reusable
- versioned
- discoverable
- consistent between training and inference

Interview message:

> “The biggest value is avoiding training-serving skew and repeated feature logic across teams.”

## GenAI / RAG opportunities

Potential non-diagnostic examples:

- search over policies/runbooks
- technical documentation assistant
- data dictionary/Q&A assistant
- summarization of approved operational documents
- data-mapping assistant with human review
- analyst SQL/code assistant

### RAG architecture pattern

```text
Approved documents / metadata
        ↓
chunk + enrich + govern
        ↓
vector/search index
        ↓
retrieval
        ↓
LLM
        ↓
answer + citations + access checks
```

## GenAI safety/governance points

Mention:

- access controls must apply before retrieval
- prevent unauthorized PHI exposure
- log prompts/outputs appropriately
- human review for high-impact workflows
- evaluation against hallucination and groundedness
- approved model/provider usage
- data retention and contractual constraints

## MLOps / CI-CD story

```text
GitHub PR
  ↓
unit/data tests
  ↓
training job
  ↓
MLflow metrics
  ↓
quality threshold
  ↓
model approval
  ↓
deploy batch/serving endpoint
  ↓
monitor
```

## Model quality questions

Be prepared to discuss:

- precision vs recall
- false positive/false negative impact
- ROC-AUC is not enough
- calibration
- class imbalance
- cross-validation
- temporal leakage
- fairness and subgroup performance
- drift
- explainability

## Healthcare-specific ML judgment

Good answer:

> “Before optimizing accuracy, I would define who acts on the prediction, what action is expected, how quickly they can act, and what the cost of false positives and false negatives is. That determines the model objective, threshold and deployment pattern.”

## AI/ML director-level answer

> “My responsibility would be to create the trusted data and MLOps foundation so AI teams can move faster without bypassing security or governance. I would standardize feature pipelines, experiment tracking, model promotion, monitoring, and approved data access, then choose batch or real-time inference based on the operational decision—not based on technology preference.”
