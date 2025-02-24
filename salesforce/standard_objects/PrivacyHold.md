#### PrivacyHold


**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the price book entry that this price book entry adjustment is associated with.


Represents a Privacy Hold that indicates that a record should be preserved from masking or deletion by Data Management policies in
Privacy Center. This object is available in API version 59.0 and later.

Use Privacy Hold with Data Management policies in Privacy Center. Add a condition to your policy to exclude records with an active
Privacy Hold status from masking or deletion actions.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available for users with the Privacy Center license and the Manage Privacy Hold user permission.

##### Fields

```
EndDate
IsActive

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the Privacy Hold ends.

**Type**
boolean


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if Privacy Hold is active on the record.

The default value is `false.`

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
The name of the Privacy Hold.

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

**Refers To**
Group, User


-----

```
PrivacyHoldReasonId
ReferenceRecordId
ReferenceRecordType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the associated Privacy Hold Reason.

This field is a relationship field.

**Relationship Name**
PrivacyHoldReason

**Relationship Type**
Lookup

**Refers To**
PrivacyHoldReason

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the record marked for the Privacy Hold.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, Lead, User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of object the record with the Privacy Hold is associated with.

Possible values are:

**•** `Account`

**•** `Contact`

**•** `Individual`

**•** `Lead`

**•** `User`


-----

```
RegisteredDate
