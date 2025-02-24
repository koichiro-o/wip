#### ApptBundlePolicySvcTerr

Represents a link between the BundlePolicy and the ServiceTerritory. This object is available in API version 54.0 and later.

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
LastReferencedDate

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

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

**Type**
dateTime


-----

```
LastViewedDate
Name
ServiceTerritoryId

```

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
The name of the appointment bundle service territory.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

