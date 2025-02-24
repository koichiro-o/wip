#### PrivacyRequest

See details and monitor the status of Data Subject Access Requests made in Privacy Center. This object is available in API version 54.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.

##### Fields

```
CompletedDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
RelatedRecord

```

**Description**
The date and time when the request was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Privacy Request.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string


-----

```
StartedDateTime
Status
TargetRecord
Type

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data Subject Access Request (DSAR) or Right to Be Forgotten request (RTBF) record
related to the request.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was started.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the status of the request.

Possible values are:

**•** `Approved`

**•** `Cancelled`

**•** `Completed`

**•** `Created`

**•** `In Progress`

**•** `Rejected`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record that is listed in the request.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the type of request that was made.

Possible values are:


-----

**•** `DSAR`

**•** `GlobalOptOut`

**•** `RTBF`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyRequestFeed on page 54**
Feed tracking is available for the object.

**PrivacyRequestHistory on page 62**
History is available for tracked fields of the object.

**PrivacyRequestOwnerSharingRule on page 64**
Sharing rules are available for the object.

**PrivacyRequestShare on page 66**
Sharing is available for the object.
