#### ApptBundleAggrPolicy

Policy that defines how the property values of the bundle members are aggregated and assigned to the bundle. This object is available
in API version 54.0 and later.


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
AggregationAction
AggregationFieldType
AggregationOrder

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The aggregation action to be performed.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The target field type in the bundle to which the aggregation is directed.

Possible values are:

**•** `Boolean`

**•** `Date`

**•** `Numeric`

**•** `Picklist`

**•** `Picklist-Multi`

**•** `Skills`

**•** `String`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Nillable, Sort, Update


-----

```
BundleFieldName
BundleMemberAddiFieldName
BundleMemberFieldName
BundlePolicyId

```

**Description**
The order the aggregation is triggered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the target field in the bundle where the value is taken from the bundle member.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of an additional source field that is connected to the initial source field in the bundle
member from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the source field in the bundle member from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy


-----

```
ConstantValue
DateValue
DoesAllowDuplicateStrings
DownscaleSortDirection
FilterCriteriaId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The constant value that is used in the aggregation.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents how the date value will be determined.

Possible values are:

**•** `End of Day`

**•** `Now`

**•** `Null`

**•** `Start of Day`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to allow the same string to appear more than once when using the
'Sum based on Bundle Members' action type.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Applies only if the Set Downscaled Duration action is set. The downscaling sorting direction
of the bundle member service appointments, according to their duration.

Possible values are:

**•** `Ascending`

**•** `Descending`

**Type**
reference


-----

```
LastReferencedDate
LastViewedDate
MaxBundleDuration
Name

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The active recordset filter criteria used for aggregating the bundle members.

This is a relationship field.

**Relationship Name**
FilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

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

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum bundle duration that can be accumulated from the bundle members (after
downscaling).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
ShouldUpdateOnCreationOnly
