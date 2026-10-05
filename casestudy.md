Yes. I converted the themes from the three AWS ML exam PDFs into **Azure Databricks-style interview questions** that are much closer to what your friend could face in a healthcare modernization case study.

The source material repeatedly tests model registry, approval workflows, bias monitoring, feature stores, CI/CD, RAG, fraud/anomaly detection, class imbalance, concept drift, ingestion, sensitive-data handling, and networking. AWS Certified Machine Learning … AWS Certified Machine Learning …

## 1. Model Registry / MLOps

**Interview question:**  
“A hospital data science team is building several readmission and no-show prediction models. How would you manage model versions and promote only approved models to production?”

**Strong answer:**

> “I would use MLflow experiment tracking and model registry. Every training run should capture parameters, metrics, code version, feature definitions and artifacts. The selected model would be registered, validated against technical and clinical thresholds, reviewed through an approval gate, and only then promoted to production.”

Then mention:

```text
Experiment
   ↓
MLflow Tracking
   ↓
Candidate Model
   ↓
Model Registry
   ↓
Validation
   ↓
Approval
   ↓
Production
```

Follow-up questions they may ask:

- How do you roll back a bad model?
- How do you know which data trained version 12?
- What if two teams use the same model?
- How do you separate dev/test/prod?

The AWS source has a very similar scenario involving a central model registry and model versions. AWS Certified Machine Learning …

---

## 2. Manual Approval Before Production

**Question:**  
“How would you ensure that an ML model cannot automatically reach production without review?”

Strong answer:

> “I would separate training from production promotion. CI/CD can train and evaluate the model automatically, but production deployment should require an explicit approval step. The approval decision should be auditable and tied to model version, test results, data quality results, and business or clinical sign-off.”

Possible flow:

```text
Train
 ↓
Evaluate
 ↓
Register
 ↓
Quality Gate
 ↓
Human Approval
 ↓
Deploy
```

The source explicitly includes a manual approval workflow where only approved models can be deployed. AWS Certified Machine Learning …

---

## 3. Model Drift

**Question:**  
“A model had strong performance for six months, but its F1 score has started falling. What would you investigate?”

Strong answer:

> “I would not immediately retrain. First I would identify whether the problem is data drift, concept drift, label-quality changes, feature pipeline changes, population changes, or an upstream data-quality issue.”

He should distinguish:

**Data drift**  
Input distribution changed.

**Concept drift**  
Relationship between features and target changed.

**Model performance drift**  
Production performance deteriorated.

Then investigate:

- feature distributions
- missing values
- class balance
- prediction distribution
- ground truth quality
- precision
- recall
- F1
- subgroup performance
- recent pipeline changes

The source includes exactly this pattern: an XGBoost model whose F1 score declines significantly after months of stability, with concept drift identified as a possible cause. AWS Certified Machine Learning …

---

## 4. Bias and Fairness in Healthcare AI

**Question:**  
“How would you monitor bias in a clinical prediction model?”

Good answer:

> “Overall accuracy is not enough. I would evaluate performance across clinically and operationally relevant subgroups and monitor whether prediction quality changes over time.”

He should mention:

- precision/recall by subgroup
- false-positive and false-negative rates
- demographic parity where appropriate
- equal opportunity considerations
- training data representation
- drift
- governance
- human review

Important:

> “The appropriate fairness metric depends on the use case and clinical risk.”

The source includes an explicit bias-drift monitoring scenario. AWS Certified Machine Learning …

---

## 5. Feature Store

**Question:**  
“Why would you use a Feature Store?”

Strong answer:

> “A Feature Store helps standardize and reuse features across teams, improve lineage, reduce duplicated feature logic, and prevent inconsistencies between training and inference.”

Example healthcare features:

```text
patient_age
prior_admission_count_90d
ed_visit_count_30d
days_since_last_discharge
chronic_condition_count
recent_abnormal_lab_count
medication_count
```

Flow:

```text
Silver/Gold
    ↓
Feature Engineering
    ↓
Feature Tables
    ↓
Training
    ↓
Inference
```

Key phrase:

> “The same feature definition should ideally be used during both training and serving.”

The AWS material specifically tests creating a feature group, ingesting records, and then using those features for training. AWS Certified Machine Learning …

---

## 6. Training-Serving Skew

Possible follow-up:

> “What happens if the training pipeline calculates age one way but the production API calculates it differently?”

Answer:

> “That creates training-serving skew. Model behavior becomes inconsistent because production features no longer match the feature definitions used during training.”

Mitigation:

- centralized feature logic
- versioned features
- automated validation
- Feature Store
- shared transformation code

---

## 7. Class Imbalance

The fraud example in your PDF contains an imbalanced dataset. AWS Certified Machine Learning …

Healthcare version:

**Question:**  
“Only 2% of patients are readmitted within 30 days. The model has 98% accuracy. Is that good?”

Correct response:

> “Not necessarily. A model predicting ‘no readmission’ for every patient would already achieve 98% accuracy.”

Then discuss:

- precision
- recall
- F1
- PR-AUC
- ROC-AUC
- confusion matrix
- threshold selection

Possible techniques:

- class weighting
- over/under-sampling
- stratified splitting
- threshold tuning

And most importantly:

> “Metric selection should reflect the business or clinical cost of false positives and false negatives.”

---

## 8. Precision vs Recall

Interviewer:

> “For a serious clinical deterioration model, which is more important: precision or recall?”

Good answer:

> “Often recall becomes very important because missing a truly high-risk patient may have a significant clinical cost. But I would not choose a metric without discussing workflow impact and false-alert burden with clinicians.”

This shows judgment.

---

## 9. Feature Engineering

The uploaded source includes categorical/numerical transformation and one-hot encoding scenarios. AWS Certified Machine Learning … AWS Certified Machine Learning …

Healthcare question:

> “How would you prepare hospital data for ML?”

Possible transformations:

```text
Gender/category → encoding
Diagnosis codes → grouped clinical categories
Timestamps → hour/day/week features
Patient history → counts over windows
Labs → latest/min/max/trend
Free text → embeddings
Highly skewed amounts → log transforms
Numeric fields → scaling when required
```

Mention that trees and neural networks have different preprocessing needs.

---

## 10. Data Leakage

This one is extremely important in healthcare.

Question:

> “How do you prevent data leakage?”

Example:

Predict 30-day readmission.

Bad feature:

```text
follow_up_visit_after_discharge
```

That happened after prediction time.

Good answer:

> “Every feature must be available at the exact time the prediction is supposed to be made.”

Mention:

- point-in-time correctness
- temporal train/test splits
- no future information
- Feature Store lineage

---

## 11. RAG / Generative AI

Your AWS source has a RAG scenario involving semantic search of documents. AWS Certified Machine Learning …

Likely healthcare interview:

> “Design an internal GenAI assistant for hospital policies and clinical documentation.”

Strong architecture:

```text
Documents
   ↓
Ingestion
   ↓
Cleaning
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Search
   ↓
Retriever
   ↓
LLM
   ↓
Grounded Response + Citations
```

He should mention:

- document-level authorization
- PHI controls
- prompt injection
- citations
- hallucinations
- audit logs
- human review
- model access controls

---

## 12. Embeddings

Question:

> “What is an embedding?”

Simple Director-level answer:

> “An embedding is a numerical vector representation of content that captures semantic meaning. Similar concepts tend to have vectors close to each other, which enables semantic search.”

The source explicitly tests embeddings, RAG, tokens and temperature. AWS Certified Machine Learning …

---

## 13. RAG vs Fine-Tuning

Question:

> “Would you fine-tune an LLM using hospital policy documents?”

Strong answer:

> “Not automatically. If the goal is to answer questions over changing proprietary documents, RAG is usually preferable because the knowledge remains external, easier to update, easier to cite, and more governable.”

Fine-tuning is better when changing:

- behavior
- style
- task specialization

rather than simply injecting frequently changing knowledge.

---

## 14. Hallucination Risk

Question:

> “How do you reduce hallucination in healthcare GenAI?”

Answer:

- RAG
- trusted sources
- citations
- low-confidence handling
- guardrails
- restricted prompts
- human validation
- monitoring
- avoid unsupported medical recommendations

Very important phrase:

> “An LLM should not be treated as the system of record.”

---

## 15. CI/CD for ML

The source has a scenario where new training data triggers model retraining and deployment. AWS Certified Machine Learning …

Azure version:

```text
GitHub
   ↓
Pull Request
   ↓
Tests
   ↓
GitHub Actions
   ↓
Databricks Job
   ↓
Train
   ↓
MLflow
   ↓
Registry
   ↓
Approval
   ↓
Deploy
```

Question:

> “Would every new data file automatically deploy a new model?”

Good answer:

> “No. New data may trigger evaluation or retraining, but deployment should depend on validation thresholds and governance rules.”

Excellent distinction.

---

## 16. Batch vs Real-Time Inference

Question:

> “Would you deploy all healthcare models as real-time endpoints?”

Answer:

> “No. Latency requirement should determine architecture.”

Examples:

**Batch**

- overnight readmission score
- population health
- claims risk
- appointment no-show prediction

**Real-time**

- interactive clinical application
- immediate fraud detection
- point-of-care recommendation

Director language:

> “I would choose the simplest inference pattern that satisfies the clinical SLA.”

---

## 17. ML Data Pipeline

Question:

> “Describe the data pipeline for a readmission model.”

Good answer:

```text
Epic Clarity
Lab
Claims
FHIR
  ↓
ADF / Databricks
  ↓
Bronze
  ↓
Silver
  ↓
Gold
  ↓
Feature Engineering
  ↓
Feature Store
  ↓
Training
  ↓
MLflow
  ↓
Registry
  ↓
Inference
```

Then include monitoring feedback:

```text
Predictions
     ↓
Actual Outcomes
     ↓
Performance Monitoring
     ↓
Retraining Decision
```

---

## 18. Data Quality Before ML

The source includes data preparation of incomplete CSV files. AWS Certified Machine Learning …

Question:

> “What happens if ML data is poor quality?”

He should say:

> “Model quality cannot exceed the quality and representativeness of its data.”

Check:

- missingness
- duplicates
- schema drift
- impossible values
- freshness
- distribution changes
- label quality

Example:

```text
admission_date > discharge_date
```

clearly invalid.

---

## 19. Duplicate Detection

Your material includes duplicate detection as an ML/data-processing problem. AWS Certified Machine Learning …

Healthcare version:

> “Two hospital feeds may represent the same patient. How do you handle duplicates?”

Possible answer:

- deterministic keys if available
- MRN/facility IDs
- probabilistic matching if necessary
- survivorship rules
- auditability

Mention that healthcare identity matching is sensitive and should not simply rely on one weak attribute.

---

## 20. Sensitive Data in AI

The source includes identifying and removing sensitive data from an ML workload. AWS Certified Machine Learning …

Question:

> “Before sending clinical text to a GenAI model, how would you handle PHI?”

Strong answer:

> “First determine whether PHI is actually required for the use case. Apply minimum-necessary principles. If not required, de-identify or redact it before the AI processing path.”

Also:

- private endpoints
- access controls
- encryption
- audit logs
- approved model endpoints
- data retention controls

---

## 21. Secure AI Environment

Question:

> “How would you isolate ML workloads?”

Mention:

```text
VNet
Private Endpoints
Managed Identity
Key Vault
RBAC
Unity Catalog
Encrypted Storage
Audit Logs
Controlled Egress
```

Do not say:

> “Because it is in Azure, it is secure.”

Say:

> “Security is architectural, not automatic.”

---

## 22. Anomaly Detection

The PDFs include fraud anomaly detection after data aggregation. AWS Certified Machine Learning …

Healthcare version:

> “Hospital claims have unusual patterns. How would you find anomalies?”

Approaches:

- statistical thresholds
- Isolation Forest
- clustering
- autoencoder
- supervised fraud model if labels exist

But first ask:

> “Do we have labeled historical anomalies?”

That determines whether supervised or unsupervised learning is appropriate.

---

## 23. Supervised vs Unsupervised

Question:

> “When would you use unsupervised anomaly detection?”

Answer:

> “When reliable labels are unavailable or incomplete and we want to surface unusual patterns for investigation.”

Do not claim anomaly = fraud.

Important:

> “An anomaly is a candidate for investigation, not proof of wrongdoing.”

---

## 24. Model Selection

The source tests choosing algorithms based on the problem type. AWS Certified Machine Learning …

Interview question:

> “Would you start with a neural network for tabular hospital data?”

Good answer:

> “Not necessarily. I would establish a simple baseline first. Gradient-boosted trees often perform very well on structured tabular data and are easier to explain and operationalize.”

Shows pragmatism.

---

## 25. Regression Metrics

The source includes choosing MAE for apartment-price prediction. AWS Certified Machine Learning …

Healthcare version:

> “You predict length of stay in days. What kind of ML problem is this?”

Answer:

Regression.

Possible metrics:

- MAE
- RMSE

Explain:

> “MAE gives an easily understandable average absolute error, while RMSE penalizes large errors more heavily.”

---

## 26. Overfitting

The source contains an overfitting-style neural network scenario where validation performance improves and later degrades. AWS Certified Machine Learning …

Question:

> “Training accuracy keeps improving but validation performance declines. What is happening?”

Answer:

Overfitting.

Possible solutions:

- early stopping
- regularization
- dropout
- simpler model
- more data

---

## 27. Learning Rate

The source also includes oscillating training and validation losses. AWS Certified Machine Learning …

Question:

> “Loss oscillates rather than converging. What might you inspect?”

Answer:

- learning rate too high
- optimizer
- normalization
- batch size

---

## 28. AI Architecture Tradeoff

A very likely Director question:

> “The client wants AI in phase one. Would you prioritize AI immediately?”

Strong answer:

> “AI value depends on a trustworthy data foundation. I would identify one bounded AI use case that can deliver early value while simultaneously building the reusable data, governance and MLOps foundation.”

That is exactly the kind of pragmatic answer this role wants.

---

## 29. Director-Level AI Governance

Question:

> “Who owns whether an AI model is safe enough to deploy?”

Do not say:

> “The data scientist.”

Better:

> “Deployment should be governed jointly. Engineering validates technical reliability, data science validates model quality, security validates controls, and business or clinical owners validate whether the model is appropriate for the intended workflow.”

---

## 30. Full AI/ML Case Study They Could Give Him

This is the one I would practice the most:

> **A hospital wants to predict 30-day readmissions and later build a GenAI assistant. Data currently exists in Epic Clarity, Caboodle, FHIR APIs, SFTP feeds and CSV files. Design the data and AI platform.**

He should structure the response:

**1. Discovery**

Ask:

- business objective?
- prediction timing?
- source systems?
- PHI?
- data quality?
- labeled outcomes?
- latency?
- users?
- scale?

**2. Data platform**

```text
Clarity / FHIR / SFTP / Lab / Claims
              ↓
         ADF / Databricks
              ↓
           Bronze
              ↓
           Silver
              ↓
            Gold
```

**3. ML platform**

```text
Gold
 ↓
Feature Engineering
 ↓
Feature Store
 ↓
MLflow
 ↓
Model Registry
 ↓
Validation
 ↓
Approval
 ↓
Batch / Online Prediction
```

**4. GenAI**

```text
Policies / Clinical Documents
          ↓
        RAG
          ↓
   Vector Search
          ↓
         LLM
```

**5. Security**

```text
Private networking
Managed Identity
Key Vault
RBAC
Unity Catalog
Audit Logs
Encryption
PHI controls
```

**6. Operations**

```text
GitHub Actions
Terraform
Monitoring
Drift
Data Quality
Model Performance
Rollback
```

**7. Business outcome**

Finish with:

> “The result is not just a model. It is a governed and reusable healthcare data and AI platform where future models can be delivered safely without rebuilding ingestion, security and deployment from scratch.”

That is a **very strong Director-level closing statement**.

For the next preparation step, I would have him practice these questions **out loud**, especially numbers **1, 3, 5, 7, 11, 15, 16, 20, 28 and 30**. Those ten cover most of the AI/ML thinking this role is likely to test.
