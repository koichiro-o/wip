#### ProducerCommission

Represents a producer's commission for an insurance policy. The commission can be calculated from the commissionable transactions
or can be populated from an external system. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CommissionableAmount
CommissionAmount
CommissionScheduleId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount on which the commission is applied. This can be a transaction amount or a
portion of the premium.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The calculated commission amount for the insurance policy transaction.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the associated Commission Schedule, which is the commission calculation tied to
the product or producer.

This is a relationship field.

**Relationship Name**
CommissionSchedule

**Relationship Type**
Lookup

**Refers To**
CommissionSchedule


-----

```
InsurancePolicyAssetId
InsurancePolicyCoverageId
InsurancePolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The insured item for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicyAsset

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyAsset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the policy coverage for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicyCoverage

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyCoverage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The insurance policy for which the commission was calculated.

This is a relationship field.

**Relationship Name**
InsurancePolicy

**Relationship Type**
Lookup


-----

```
InsurancePolicyTransactionId
LastReferencedDate
LastViewedDate
MaxCommissionAmount

```

**Refers To**
InsurancePolicy

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The transaction for which the commission record was created.

This is a relationship field.

**Relationship Name**
InsurancePolicyTransaction

**Relationship Type**
Lookup

**Refers To**
InsurancePolicyTransaction

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission calculated for the product or producer for a commissionable
event. Constrains the output from the commission schedule.


-----

```
MinCommissionAmount
Name
OwnerId
ParentProducerCommissionId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission calculated for the product or producer for a commissionable
event. Constrains the output from the commission schedule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the producer commission.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The original commission record that was adjusted or modified.

This is a relationship field.

**Relationship Name**
ParentProducerCommission

**Relationship Type**
Lookup


-----

```
PaymentDatetime
ProcessingProducerId
ProducerId
ProducerProductionCode

```

**Refers To**
ProducerCommission

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the commission was paid.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The producer who performed the commissionable event.

This is a relationship field.

**Relationship Name**
ProcessingProducer

**Relationship Type**
Lookup

**Refers To**
Producer

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The producer, broker, brokerage, or other user who receives the commission.

This is a polymorphic relationship field.

**Relationship Name**
Producer

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Producer

**Type**
string


-----

```
SourceSystem
SourceSystemIdentifier
Status
Type

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The production code for the producer who performs the commissionable event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The system from which the producer commission record was sourced.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the producer commission record in the source system. This field is unique within
your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of the commission payment.

Possible values are:

**•** `Disputed`

**•** `Paid`

**•** `Pending`

**•** `Reversed`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of commission paid to a producer, account, or contact for a commissionable
transaction.

Possible values are:

**•** `Advance`


-----

**•** `Bonus`

**•** `Chargeback`

**•** `Commission`

**•** `Contingent Commission`
