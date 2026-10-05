# 4. Healthcare / Epic / FHIR Primer

## Epic Clarity

Clarity is commonly used as a relational reporting database fed from the Epic operational environment.

Typical data domains:

- patient
- encounter
- provider
- diagnosis
- procedure
- medication
- appointment
- orders/results

Interview focus: Clarity schemas can be large and complex; discovery, mapping and validation are important.

## Epic Caboodle

Caboodle is Epic’s enterprise analytics warehouse layer. It is generally more analytics-oriented and standardized than raw operational structures.

## FHIR

FHIR is a healthcare interoperability standard that represents clinical concepts as resources.

Common resources:

- Patient
- Encounter
- Observation
- Condition
- Medication / MedicationRequest
- Practitioner
- Procedure

### Architectural message

FHIR does not automatically replace all EHR extraction. Use it where it matches the use case, source capability, and latency needs.

## Clinical data quality examples

- patient identifier is present and valid
- encounter has a valid patient relationship
- discharge date is not before admission date
- code values are recognized
- timestamps are in expected timezone/format
- duplicate encounters are detected
- late-arriving updates are handled

## Data mapping analyst collaboration

A strong architecture lead works with mapping/domain specialists to:

1. profile source fields,
2. map source semantics to target model,
3. define business rules,
4. identify data-quality exceptions,
5. reconcile with source owners,
6. sign off before cutover.

## Example domain model

```text
fact_encounter
  encounter_id
  patient_id
  provider_id
  facility_id
  admit_ts
  discharge_ts
  encounter_type

+ dim_patient
+ dim_provider
+ dim_facility
+ dim_diagnosis
+ dim_date
```

## Important interview behavior

If you do not know an Epic-specific table name, do not bluff.

Say:

> “I would validate the source model with the client’s Epic reporting team and mapping analysts rather than assuming the same implementation across health systems.”
