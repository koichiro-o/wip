#### ApptBundleAggrDurDnscale

Sums the duration of the bundle members, reduced by a predefined percentage. This object is available in API version 54.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

##### Fields

```
BundleAggregationPolicyId
FromBundleMemberNumber
LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent appointment bundle aggregation policy.

This is a relationship field.

**Relationship Name**
BundleAggregationPolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundleAggrPolicy

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The number of the first bundle member to which the downscale is applied.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


-----

```
LastViewedDate
MaxReduction
Name
PercentageOfReduction
ToBundleMemberNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum reduction that can be applied to a bundle member.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the appointment bundle aggregation downscale policy.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The percentage of duration reduction.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of the last bundle member to which the downscale is applied.

