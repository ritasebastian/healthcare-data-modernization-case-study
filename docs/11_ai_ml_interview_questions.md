# 11. AI/ML Interview Question Bank

## 1. How would you prepare healthcare data for ML?

Talk about:

- curated Gold data
- point-in-time correct features
- missing values
- leakage prevention
- code standardization
- data lineage
- reproducibility

## 2. What is feature engineering?

> Transforming raw/curated data into model-ready signals that represent useful predictive behavior.

Give examples such as prior admission count or recent ED visits.

## 3. What is training-serving skew?

When features are calculated differently during model training and production inference.

Feature-store/reusable feature logic can reduce it.

## 4. Batch or real-time inference?

Decide using business latency.

- daily outreach list → batch
- immediate operational intervention → possibly streaming/real-time

## 5. Why MLflow?

- experiment tracking
- parameters
- metrics
- artifacts
- model versioning/registry workflow

## 6. How do you monitor a model?

Monitor:

- pipeline health
- input data quality
- feature drift
- prediction drift
- latency
- outcome metrics when labels arrive

## 7. How do you handle class imbalance?

Discuss:

- proper metrics
- threshold selection
- precision/recall
- resampling/weights when appropriate
- business cost of errors

## 8. What is data leakage?

Using information during training that would not be available at prediction time.

Healthcare example: using post-discharge information to predict readmission at discharge time.

## 9. How do you make a model production-ready?

Need more than accuracy:

- reproducible pipeline
- versioned features/data
- model registry
- deployment workflow
- monitoring
- rollback
- documentation
- owner
- retraining policy

## 10. How would GenAI fit this platform?

Good non-diagnostic examples:

- data catalog assistant
- runbook assistant
- source mapping assistant
- internal technical knowledge search
- document summarization with citations

Mention RAG, access control, grounding and auditability.

## 11. What would you say if the client asks for “real-time AI everywhere”?

> “I would first identify which decision needs low latency. Real-time architectures increase cost and operational complexity, so I would use them only where the business workflow benefits.”

## 12. How do you talk about responsible AI?

Discuss:

- purpose and human workflow
- appropriate data use
- bias/fairness review
- explainability when needed
- access controls
- monitoring
- human oversight for high-impact decisions
