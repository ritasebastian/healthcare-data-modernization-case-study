# 5. Security, HIPAA & Governance

## Security principles

- least privilege
- minimum necessary access
- defense in depth
- encryption in transit and at rest
- private connectivity where possible
- managed identity/service principal authentication
- secrets in Key Vault
- comprehensive audit logging
- separation of duties
- environment isolation

## Key architecture controls

### Private networking

Use VNet/private endpoints to reduce unnecessary public exposure.

### Managed identities

Prefer managed/service identities over credentials embedded in scripts.

### Key Vault

Store and rotate secrets, keys, and certificates centrally.

### RBAC / Unity Catalog

Grant only required access.

Example:

- ingestion service: write Bronze
- engineer: read/write development schemas
- analyst: read Gold only
- ML service: read approved feature/model data

## HIPAA interview language

Avoid:

> “Using Azure/Databricks makes us HIPAA compliant.”

Prefer:

> “HIPAA compliance depends on the full technical, administrative, contractual and operational control environment. My architecture would support that program with strong access controls, encryption, auditing, private connectivity, data minimization and documented operating procedures.”

## PHI handling

Consider:

- classification
- masking/tokenization where appropriate
- restricted raw zones
- approved use cases
- row/column-level controls when required
- audit logging
- retention policies
- secure sharing

## Purview + Unity Catalog

### Unity Catalog

Strong for Databricks-centric permissions and lineage.

### Microsoft Purview

Useful for broader enterprise cataloging, classification, lineage and governance across systems.

## Security review questions

Be ready for:

- How do you stop analysts from reading raw PHI?
- How are service credentials rotated?
- How do you audit who accessed a table?
- How do you isolate dev from prod?
- How do you handle external partner access?
- How do you revoke access quickly?
