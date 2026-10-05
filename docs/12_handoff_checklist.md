# 12. Production Handoff / Go-Live Checklist

## Architecture

- [ ] Architecture diagram approved
- [ ] Source inventory complete
- [ ] Data flow documented
- [ ] Dependency map complete
- [ ] ADRs / major design decisions captured

## Security

- [ ] RBAC reviewed
- [ ] Managed identities/service principals configured
- [ ] Secrets stored in Key Vault
- [ ] Private connectivity validated
- [ ] Audit logging enabled
- [ ] PHI access reviewed

## Data

- [ ] Bronze/Silver/Gold ownership defined
- [ ] Data-quality rules documented
- [ ] Reconciliation complete
- [ ] Schema-drift process documented
- [ ] Retention rules documented

## Operations

- [ ] Monitoring dashboards exist
- [ ] Alerts route to an owned channel/team
- [ ] Retry/replay procedure documented
- [ ] Incident runbook tested
- [ ] SLA/SLO expectations documented
- [ ] On-call/support ownership agreed

## CI/CD + IaC

- [ ] Terraform/Bicep source controlled
- [ ] GitHub Actions pipeline working
- [ ] Dev/test/prod promotion process documented
- [ ] Rollback procedure documented

## AI/ML (if applicable)

- [ ] Feature definitions documented
- [ ] Training dataset/version reproducible
- [ ] Experiment tracking enabled
- [ ] Model approval owner defined
- [ ] Inference monitoring enabled
- [ ] Drift/performance review process defined

## Handoff test

Ask:

> “Can the receiving team deploy, monitor, recover, troubleshoot and modify the platform without depending on the original implementation team?”

If not, handoff is incomplete.
