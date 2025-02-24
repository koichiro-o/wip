#### ContractLineOutcome

Represents information on a contract line outcome’s captured data and other related parameters that are used when capturing data.
This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
**•** Field Service must be enabled.

**•** Entitlements must be enabled.

##### Fields

```
CalculationMethod
CaptureFrequency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The method used for calculating the contract line outcome’s captured data to determine
the outcome value. Select Average or As Captured to calculate the contract line
outcome. Average calculates the outcome value based on the average of all data captured
to date. As Captured calculates the outcome value based on the asset’s current data at
the time of the compliance check.

Possible values are:

**•** `AsCaptured`

**•** `Average`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The frequency at which data capturing and contract compliance check for the contract line
outcome occurs.

Possible values are:

**•** `Daily`

**•** `Monthly`


-----

```
ComplianceStatus
ContractLineItemId
Description

```


**•** `Weekly`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates if the criteria were met. Compliant–The outcome is compliant with the contract.
Not Compliant–The outcome isn’t compliant with the contract. Not Available–The outcome’s
compliance information isn’t available yet. Invalid–The outcome isn’t valid because the
option selected for the Criteria Field of the recordset filter criteria was deleted. To restart the
calculation, create a new contract line outcome.

Possible values are:

**•** `Compliant`

**•** `Invalid`

**•** `NotAvailable`

**•** `NotCompliant`

The default value is `NotAvailable.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The contract line item associated with the contract line outcome.

This field is a relationship field.

**Relationship Name**
ContractLineItem

**Relationship Type**
Lookup

**Refers To**
ContractLineItem

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the contract line outcome.


-----

```
EndDate
LastReferencedDate
LastViewedDate
Name
NextDataCaptureDate
OwnerId

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The contract line outcome's data capture end date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome was last modified. Its UI label is Last
Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the contract line outcome.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date of the next data capture and compliance check based on the capture frequency.
The date is auto-populated and updated after each capture

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
RecordsetFilterCriteriaId
ServiceContractId

```

**Description**
The contract line outcome’s owner. By default, the owner is the user who created the contract
line outcome record. Its UI label is Contract Line Outcome Owner.

This field is a polymorphic relationship field.

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
The ID of the recordset filter criteria in which the contract line outcome’s conditions are
defined.

This field is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The service contract associated with the contract line item and the contract line outcome.

This field is a relationship field.

**Relationship Name**
ServiceContract

**Relationship Type**
Lookup

**Refers To**
ServiceContract


-----

```
StartDate

##### Usage

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The contract line outcome's data capture start date.


Use this object to define the data capture frequency and other related parameters that are used when capturing data in order to evaluate
a service contract’s compliance.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineOutcomeChangeEvent on page 67**
Change events are available for the object.

**ContractLineOutcomeFeed on page 54**
Feed tracking is available for the object.

**ContractLineOutcomeHistory on page 62**
History is available for tracked fields of the object.

**ContractLineOutcomeOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ContractLineOutcomeShare on page 66**
Sharing is available for the object.

SEE ALSO:

ContractLineOutcomeData
