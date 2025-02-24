#### ContractLineOutcomeData

Represents the contract line outcome’s captured data. It stores the data that was captured between the contract line outcome’s start
date and end date. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

**•** Field Service must be enabled.

**•** Entitlements must be enabled.

##### Fields

**Field**
```
CalculatedValue
CaptureDate
ContractLineOutcomeId
KeyPerformanceIndicator

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value calculated based on the contract line outcome’s calculation method and the
captured data.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the data was captured.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The contract line outcome associated with the contract line outcome data record.

This field is a relationship field.

**Relationship Name**
ContractLineOutcome

**Relationship Type**
Lookup

**Refers To**
ContractLineOutcome

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
LastReferencedDate
LastViewedDate
Name
Value

##### Associated Objects

```

**Description**
The key performance indicators (fields or asset attributes) that define the contract line
outcome’s compliance status.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome data record was last modified. Its UI label
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome data record was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the contract line outcome data record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual value of the key performance indicator.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineOutcomeDataChangeEvent on page 67**
Change events are available for the object.

**ContractLineOutcomeDataFeed on page 54**
Feed tracking is available for the object.


-----

**ContractLineOutcomeDataHistory on page 62**
History is available for tracked fields of the object.

**ContractLineOutcomeDataOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ContractLineOutcomeDataShare on page 66**
Sharing is available for the object.
