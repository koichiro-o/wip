#### OrgDeleteRequest

Represents a request to delete a developer edition (DE) org. This object is available in API version 42.0 and later. It is available only in
Developer and Database.com editions.


-----

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Name
OwnerId
RequestType

##### Associated Objects

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of this OrgDeleteRequest object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
The ID of the user who initiated the org delete request.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies whether you want to deactivate or reactivate the org. When you
deactivate an org, you have 30 days to change your mind and reactivate it. After
30 days, the org is locked, and you must contact Salesforce Customer Support
to reactivate it. After 60 days, the org is permanently deleted from Salesforce
servers.

Valid values:

**•** `Deactivate`

**•** `Reactivate`


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**OrgDeleteRequestOwnerSharingRule**

Sharing rules are available for the object.

**OrgDeleteRequestShare**

Sharing is available for the object.


-----
