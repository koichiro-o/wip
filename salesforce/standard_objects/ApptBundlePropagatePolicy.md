#### ApptBundlePropagatePolicy

Policy that defines which property values are inherited from the bundle to the bundle members or are assigned as constant values in
the bundle members. This object is available in API version 55.0 and later.


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
AdditionalConstantValue
BundleFieldName
BundleMemberFieldName
BundlePolicyId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The additional constant value that is connected to the initial constant value to be added to
the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the source field in the bundle from which the value is taken.

Possible values are: All default and custom Service Appointment fields.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the target field in the bundle member where the value is inherited from the bundle.

Possible values are: All default and custom Service Appointment fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
ConstantValue
DateValue
LastReferencedDate
LastViewedDate

```

**Description**
ID of the parent bundle policy.

This field is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The constant value to be added to the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents how the date value is determined.

Possible values are:

**•** `End of Day`

**•** `Now`

**•** `Null`

**•** `Start of Day`

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
ShouldAddConstantValue
ShouldUpdateOnAdd
ShouldUpdateOnRemove
ShouldUpdateOnUnbundle

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
The name of the appointment bundle propagation policy.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable adding a constant value to the bundle members.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when they are
added to the bundle.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when they are
removed from the bundle.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to enable updating the fields of the bundle members when performing
the Unbundle action.


-----
