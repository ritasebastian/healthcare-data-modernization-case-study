# Terraform / IaC Interview Notes

The point in the interview is not to memorize every Azure resource block. Explain why IaC matters.

## Why Terraform/Bicep

- repeatable environments
- peer-reviewed infrastructure changes
- reduced configuration drift
- easier dev/test/prod parity
- documented security/network decisions
- faster future engagements through reusable modules

## Example module structure

```text
terraform/
  modules/
    network/
    databricks/
    storage/
    key_vault/
    private_endpoints/
  environments/
    dev/
    test/
    prod/
```

## Good interview statement

> “I would turn recurring architecture patterns into reusable modules, but I would avoid making a giant inflexible framework. The module boundary should reflect what is truly reusable across clients.”
