#### ApptBundlePolicy

Policy that defines how the bundling of service appointments should be handled. This object is available in API version 54.0 and later.

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
BundleEndTimeFieldName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
BundleStartTimeFieldName
CanAllowSchleDepndInBundle
ConstantTimeValue
FilterCriteriaId

```

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the name of the field used
for entering the end time of the bundle.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the name of the field used
for entering the start time of the bundle.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is reserved for future use.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If IsTimeCalcByBundleDurationField is true, this field represents the total time of the bundle
as a preset constant value.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The active recordset filter criteria used for the bundle members. Only service appointments
that meet the criteria can be bundled.

This is a relationship field.

**Relationship Name**
FilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria


-----

```
IsAutomaticBundling
IsManualBundling
IsTimeCalcByBundleDurationFld
LastReferencedDate
LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the policy is relevant for automatic bundling.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the policy is relevant for manual bundling.

The default value is ‘false’.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the bundle’s duration is validated. If true, the bundle’s start time is subtracted
from the bundle’s end time. If the result is a negative value, it uses ConstantTimeValue as
the bundle’s duration.

The default value is ‘false’.

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

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.


-----

```
LimitAmountOfBundleMembers
LimitDurationOfBundle
Name
OwnerId
Priority

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of bundle members that can be included in a bundle.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum duration of a bundle.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the bundle policy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

**Description**
The priority level that this bundle policy should be given when the bundle policies are
analyzed using the automatic mode.
