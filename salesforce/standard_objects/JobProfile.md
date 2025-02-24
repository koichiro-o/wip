#### JobProfile

Represents a job profile used for shift scheduling. This object is available in API versions 47.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service or Workforce Engagement must be enabled.

##### Fields

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed a related record.


-----

```
LastViewedDate
Name
OwnerId

##### Associated Objects

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the current user last viewed this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the job profile.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the job profile.


This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**JobProfileFeed**

Feed tracking is available for the object.

**JobProfileHistory**

History is available for tracked fields of the object.

**JobProfileOwnerSharingRule**

Sharing rules are available for the object.

**JobProfileShare**

Sharing is available for the object.
