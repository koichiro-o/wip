#### CommissionScheduleAssignment

Represents the commission calculation applicable to a specific product or producer for one or multiple commissionable events.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CommissionableEventType
CommissionScheduleId

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
The event that results in the commission calculation.

Possible values are:

**•** `Contracting`

**•** `Endorsement`

**•** `Issue Policy`

**•** `Policy Issuance`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated Commission Schedule, which is the commission calculation tied to
the product or producer.

This is a relationship field.

**Relationship Name**
CommissionSchedule


-----

```
EffectiveEndDate
EffectiveStartDate
LastReferencedDate
LastViewedDate
MaxCommissionAmount

```

**Relationship Type**
Lookup

**Refers To**
CommissionSchedule

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date when the Commission Schedule is in effect for the product or producer.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first date when the Commission Schedule is in effect for the product or producer.

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
event. Constrains the output from the Commission Schedule.


-----

```
MaxCommissionRate
MinCommissionAmount
MinCommissionRate
Name
ProducerId

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission rate that a producer receives for a commissionable event.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission calculated for the product or producer for a commissionable
event. Constrains the output from the Commission Schedule.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission rate that a producer receives for a commissionable event.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the Commission Schedule Assignment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The producer, broker, brokerage, or other user who receives the commission.

This is a relationship field.

**Relationship Name**
Producer

**Relationship Type**
Lookup


-----

```
Product2Id

##### Associated Objects

```

**Refers To**
Producer

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product for which commissions are calculated.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommissionScheduleAssignmentChangeEvent on page 67**
Change events are available for the object in API version 62.0 and later.

**CommissionScheduleAssignmentFeed**

Feed tracking is available for the object.

**CommissionScheduleAssignmentHistory**

History is available for tracked fields of the object.

**CommissionScheduleAssignmentOwnerSharingRule on page 64**
Sharing rules are available for the object.

**CommissionScheduleAssignmentShare on page 66**
Sharing is available for the object.
