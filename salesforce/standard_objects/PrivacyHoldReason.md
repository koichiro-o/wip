#### PrivacyHoldReason

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the Privacy Hold was added to the record.


Represents the business or legal purpose for why a record has a Privacy Hold. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available for users with the Privacy Center license and the Manage Privacy Hold user permission.

##### Fields

```
Detail
LastReferencedDate
LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The details of the Privacy Hold Reason, such as the business or legal purpose for the hold.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime


-----

```
Name
OwnerId
