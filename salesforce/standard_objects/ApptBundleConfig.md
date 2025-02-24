#### ApptBundleConfig

```

**Description**
The name of the appointment bundle aggregation policy.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to update the field in the bundle only when it is created.


Represents the general parameters that define the behavior of the bundle. This object is available in API version 54.0 and later.

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
AddToBundleStatuses

```

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses of service appointment that are allowed to be bundled.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`


-----

```
BundleStatusesToPropagate
CriteriaForAutoUnbundlingId

```


**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The bundle statuses that when updated are inherited by the bundle members.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The criteria that causes a bundle service appointment to be unbundled.

This is a relationship field.

**Relationship Name**
CriteriaForAutoUnbundling

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria


-----

```
DoesAddTravelTime
DoesDeleteEmptyBundles
EmptyBundleStatus
LastReferencedDate
LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If the bundle members aren’t in the same location, add travel time between them to the
bundle’s duration according to their sort order. The default value is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If the bundle has no remaining bundle members, the bundle is deleted.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status from the Canceled category that a bundle service appointment changes to if it
has no remaining bundle members, but still appears in the appointment list.

Possible values are determined by the org’s statuses.

The default value is None.

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
MemberStatusesNotToPropagate
Name
OwnerId

```

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The bundle member statuses that aren’t overridden when the bundle's status is updated.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Appointment Bundle Config.

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


-----

```
RemoveFromBundleStatuses
StatusOnRemovalFromBundle
StatusesNotToUpdateOnUnbundle

```

**Type**
multipicklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses of service appointments that are allowed to be removed from a bundle.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status that a service appointment is given when it’s removed from a bundle.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.

**Type**
multipicklist


-----

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The statuses that aren’t updated when a bundle is unbundled.

Possible values are:

**•** `Accepted`

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Rejected`

**•** `Scheduled`

The default value is None.
