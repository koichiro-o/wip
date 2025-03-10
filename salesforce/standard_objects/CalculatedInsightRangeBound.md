#### CalculatedInsightRangeBound

Stores the information required to calculate a range-bound data insight. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if a B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
InsightName
LastReferencedDate
LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Name of the calculated insight.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime


-----

```
LowerBoundRange
Name
Operator
OwnerId

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The lower limit of the calculated insight.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated name of the insight.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Operation used to calculate the insight based on the upper bound range and lower bound
range.

Possible values are:

**•** `EQUAL_TO`

**•** `GREATER_THAN`

**•** `GREATER_THAN_EQUAL_TO`

**•** `LESS_THAN`

**•** `LESS_THAN_EQUAL_TO`

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the insight.


-----

```
SalesStoreId
UpperBoundRange

##### Associated Objects

```

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
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the webstore associated with the insight benchmarks.

This field is a relationship field.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The upper limit of the calculated insight.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalculatedInsightRangeBoundOwnerSharingRule on page 64**
Sharing rules are available for the object.

**CalculatedInsightRangeBoundShare on page 66**
Sharing is available for the object.


-----
