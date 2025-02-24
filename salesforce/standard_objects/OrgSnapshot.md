#### OrgSnapshot

Represents a snapshot of a scratch org. Snapshots capture the state of a scratch org so that you can use it to quickly spin up new scratch
orgs using its configuration. This object is available in API version 61.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
A snapshot must belong to the Dev Hub org that you’re using to create the scratch org. You must enable the scratch org snapshot
feature in your Dev Hub org using Setup.

##### Fields

```
Content

```

**Type**
picklist


-----

```
Description
Error
ExpirationDate
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A free-form text field (maximum 255 characters) for you to enter a description of this scratch
org snapshot.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the scratch org snapshot expires.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate isn’t null, the user accessed this record or list view indirectly.


-----

```
OwnerId
Provider
ProviderSnapshot
ProviderSnapshotVersion
SnapshotName

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the scratch org snapshot.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
For internal use only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For internal use only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
For internal use only.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the scratch org snapshot. This field value is unique within your org.


-----

```
SourceOrg
Status

##### Associated Objects

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The org ID of the scratch org that the snapshot was created from.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the snapshot.

Possible values are:

**•** `Active—The snapshot is created and can be used to create scratch orgs.`

**•** `Error—The snapshot couldn’t be created.`

**•** `Expired—The snapshot has expired.`

**•** `In Progress—The snapshot is in the process of being created.`

**•** `New—The snapshot creation request has been received.`

The default value is `New.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrgSnapshotFeed on page 54**
Feed tracking is available for the object.

**OrgSnapshotHistory on page 62**
History is available for tracked fields of the object.

**OrgSnapshotShare on page 66**
Sharing is available for the object.
