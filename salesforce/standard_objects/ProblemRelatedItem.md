#### ProblemRelatedItem

Represents a junction object that relates a Problem to an Asset. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Asset ID that’s linked to the Problem.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset


-----

```
Comment
ImpactLevel
ImpactType
Name
ProblemId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the problem as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The related item’s impact on the problem.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `High.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The effect of the problem-related item on business operations.

Possible values are:

**•** `Business-Blocking`

**•** `Not Business-Blocking`

**•** `Partially Business-Blocking`

The default value is `Business-Blocking.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the problem-related item.

**Type**
reference


-----

**Properties**
Create, Filter, Group, Sort

**Description**
The Problem ID that’s related to the Asset.

This field is a relationship field.

**Relationship Name**
Problem

**Relationship Type**
Lookup

**Refers To**
Problem

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProblemRelatedItemChangeEvent on page 67**
Change events are available for the object.

**ProblemRelatedItemFeed on page 54**
Feed tracking is available for the object.

**ProblemRelatedItemHistory on page 62**
History is available for tracked fields of the object.
