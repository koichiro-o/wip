#### PrivacyRTBFRequest

Represents a Right to Be Forgotten Request made in Privacy Center. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.

##### Fields

```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the customer’s Right to Be Forgotten request.


-----

```
JobRecord
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID that is processed by the Right to Be Forgotten request.

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Right to Be Forgotten request.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


-----

```
PolicyNameId
Status

##### Associated Objects

```

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Right to Be Forgotten policy applied to this request.

This field is a relationship field.

**Relationship Name**
PolicyName

**Relationship Type**
Lookup

**Refers To**
PrivacyPolicyDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the status of the request.

Possible values are:

**•** `Cancelled`

**•** `Complete`

**•** `Error`

**•** `Pending`

**•** `Scheduled`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyRTBFRequestHistory on page 62**
History is available for tracked fields of the object.

**PrivacyRTBFRequestOwnerSharingRule on page 64**
Sharing rules are available for the object.

**PrivacyRTBFRequestShare on page 66**
Sharing is available for the object.


-----
