#### ActiveScratchOrg

Represents an active scratch org. This object is available in API version 41.0 and later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update()

 Fields

```
```
Description
Edition
ExpirationDate
Features

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of this scratch org.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The org edition of this scratch org. Possible values are Group, Developer,
```
  Enterprise, and Professional. This field is read only.

```
**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the scratch org expires. This field is read only.

**Type**
textarea

**Properties**
Nillable

**Description**
The features enabled in this scratch org, such as MultiCurrency. See the
_Salesforce DX Developer Guide for the full list of valid features. This field is read_
only.


-----

```
HasSampleData
LastLoginDate
LastReferencedDate
LastViewedDate
Name
Namespace

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the scratch org contains sample data. If set to `true, the`
sample data is similar to the data in a Salesforce free trial org.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date of the last user login to the scratch org. This field is read only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record. This field is read only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, and LastReferenceDate isn’t null, the user accessed this
record or list view indirectly. This field is read only.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The auto-generated ID of this scratch org. This field is read only.

**Type**
string


-----

```
OrgName
OwnerId
ScratchOrg
ScratchOrgInfoId
SignupEmail
SignupInstance

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace associated with this scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the scratch org. This field is read only.

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns this scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The org ID of the scratch org. This field is read only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The id of the associated ScratchOrgInfo object. This field is read only.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the Administration user. This field is read only.

**Type**
string


-----

```
SignupTrialDays
SignupUsername
Snapshot

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce instance on which this scratch org resides. This field is read only.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of days between the scratch org's creation and expiration. This field
is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username of the Administration user of the scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this scratch org was created from a scratch org snapshot, then this field contains
either the name or ID of the snapshot. Specifically, the name corresponds to the
`Name` field of the snapshot’s record in the OrgSnapshot standard object; the ID
corresponds to the record ID.

If this scratch org wasn’t created from a snapshot, this field is empty. This field is
read only.

This field is available in API version 61.0 and later.


Salesforce automatically creates an instance of this object after a ScratchOrgInfo record moves to the Active state. The new
`ActiveScratchOrg` gets many of its field values from the ScratchOrgInfo object with which it’s associated.

When you delete an `ActiveScratchOrg` record, its associated scratch org is deleted and its associated `ScratchOrgInfo`
record is moved to the Deleted state.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**ActiveScratchOrgFeed**

Feed tracking is available for the object.

**ActiveScratchOrgHistory**

History is available for tracked fields of the object.

**ActiveScratchOrgShare**

Sharing is available for the object.

SEE ALSO:

ScratchOrgInfo

NamespaceRegistry

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.sfdx_dev.meta/sfdx_dev)_
