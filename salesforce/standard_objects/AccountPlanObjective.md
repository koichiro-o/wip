#### AccountPlanObjective

Represents strategic objectives or initiatives pursued by a relationship team with a customer to enhance customer engagement and
satisfaction. This object is available in API version 62.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if sales account plans are turned on.

##### Fields

```
AccountPlanId
AccountPlanObjCategoryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account plan associated with the objective.

This field is a relationship field.

**Relationship Name**
AccountPlan

**Relationship Type**
Master-detail

**Refers To**
AccountPlan

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The category associated with the account plan objective. To access this field, you must have
an FSC Sales or a Financial Services Cloud Extension license.

This field is a relationship field.

**Relationship Name**
AccountPlanObjCategory


-----

```
Description
EndDate
ExternalStakeholderId
LastInteractionSumGenDate
LastReferencedDate

```

**Refers To**
AccountPlanObjectiveCategory

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the account plan objective.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date of the account plan objective.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer stakeholder contact associated with the account plan objective. The relationship
team collaborates with the customer stakeholder to achieve a specific objective. To access
this field, you must have an FSC Sales or a Financial Services Cloud Extension license.

This field is a relationship field.

**Relationship Name**
ExternalStakeholder

**Refers To**
Contact

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the most recent interaction summary was generated using Einstein Generative
AI. To access this field, you must have an FSC Sales or a Financial Services Cloud Extension
license.

**Type**
dateTime


-----

```
LastViewedDate
Name
ObjectiveInteractionSummary
ObjectiveOwnerId

```

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the account plan objective.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The summary of interactions that occur with the account in relation to the account plan
objective. To access this field, you must have an FSC Sales or a Financial Services Cloud
Extension license.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The owner user associated with the objective.

This field is a relationship field.

**Relationship Name**
ObjectiveOwner

**Refers To**
User


-----

```
OwnerId
Priority
StartDate
Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the level of importance placed on achieving the objective associated with the
account plan. To access this field, you must have an FSC Sales or a Financial Services Cloud
Extension license.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the account plan objective.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the status of the account plan objective.

Possible values are:

**•** `Closed`


-----

**•** `In Progress`

**•** `New`

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountPlanObjectiveChangeEvent on page 67**
Change events are available for the object.

**AccountPlanObjectiveHistory on page 62**
History is available for tracked fields of the object.

**AccountPlanObjectiveOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AccountPlanObjectiveShare on page 66**
Sharing is available for the object.
