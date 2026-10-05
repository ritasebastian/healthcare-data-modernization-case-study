# 9. Whiteboard Cheat Sheet

Draw this first:

```text
                    HEALTH SYSTEM SOURCES

 Epic   Clarity   Caboodle   FHIR   Oracle   SFTP   CSV
   \       |         |        |       |       |      /
                    INGESTION
                       |
          ADF / API / CDC / SFTP / Auto Loader
                       |
                       v
                ADLS / LANDING
                       |
                       v
                 BRONZE / RAW
                       |
                       v
               SILVER / CLEAN
                       |
                       v
                GOLD / CURATED
                /      |       \
               /       |        \
          BI/Fabric   AI/ML   Secure Sharing
```

Write around it:

```text
Private Endpoints
Managed Identity
Key Vault
Unity Catalog
Purview
Monitoring
GitHub Actions
Terraform
```

## 90-second explanation

> “I would use source-specific ingestion patterns into a secure Azure landing zone, preserve source-faithful data in Bronze, standardize and quality-check in Silver, then publish business-ready Gold datasets for analytics, AI/ML and secure sharing. Security, governance, CI/CD and monitoring are cross-cutting concerns rather than later add-ons. I would migrate in phases and validate with reconciliation and parallel runs before cutover.”

## Keywords worth using naturally

- incremental
- idempotent
- replayable
- observable
- governed
- least privilege
- source-aligned
- business-ready
- reconciliation
- handoff
- pragmatic
