#### ApptBundleSortPolicy

Policy that defines the properties by which the bundle members are sorted within the bundle. Can also be used in the automatic mode
for determining the order of the automatic selection of bundle members. This object is available in API version 54.0 and later.

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
BundlePolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy


-----

```
LastReferencedDate
LastViewedDate
Name
SortDirection
SortFieldName

```

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the appointment bundle sort policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The order of the appointments in a bundle

Possible values are:

**•** `Ascending`

**•** `Descending`

**Type**
picklist


-----

```
SortOrder
SortType

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the field in the service appointment used for sorting the bundle members.

Possible values are: All default and custom Service Appointment fields.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The order of fields used for sorting the bundle members.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The applied sort type for arranging the bundle. Sort for Automatic Bundling defines the order
that automated bundling uses to examine the candidate service appointments to be bundled.
Sort Within a Bundle defines the order of bundle members. It’s also used when you unbundle
to define the order that the service appointments are scheduled on the Gantt.

Possible values are:

**•** `SortForAutomaticBundling—Sort For Automatic Bundling`

**•** `SortWithinaBundle—Sort Within a Bundle`

