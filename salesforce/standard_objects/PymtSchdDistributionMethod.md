#### PymtSchdDistributionMethod

Indicates how the total payment is divided into partial payments. This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with Subscription Management.

##### Fields

```
Description

```

**Type**
textarea


-----

```
DistributionCount
DistributionMethodType
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
User-entered description of the payment schedule distribution method.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number of payment schedule items for the payment schedule. The payment schedule
items are used to distribute the payment schedule’s total payment into partial payments.

Possible values are:

**•** `1—Full distribution. Currently, each payment schedule must have exactly one payment`
schedule item.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Distribution method time interval.

Possible values are:

**•** `FullDistribution—The the full amount on the payment schedule is distributed`
to a single payment schedule item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
User-entered name for the payment schedule distribution method.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

