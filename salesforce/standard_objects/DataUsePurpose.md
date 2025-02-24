#### DataUsePurpose

Represents the reason for contacting a prospect or customer, such as for billing, marketing, or surveys. This object is available in API
version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if Data Protection and Privacy is enabled.


-----

##### Fields

**Field Name**
```
CanDataSubjectOptOut
Description
LastReferencedDate
LastViewedDate
LegalBasisId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the customer can decline contact for the described
purpose.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the purpose for contacting a customer.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced (LastReferencedDate)
and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifies the legal basis record associated with the data use purpose.

This is a relationship field.


-----

```
Name
OwnerId
PurposeId

```

**Relationship Name**
LegalBasis

**Relationship Type**
Lookup

**Refers To**
DataUseLegalBasis

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Identifies the reason for contacting a customer. For example, billing or
marketing.

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
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of an object containing data specific to the data use purpose.

This is a polymorphic relationship field.

**Relationship Name**
Purpose

**Relationship Type**
Lookup


-----

**Refers To**
Asset, CareProgram, CareRegisteredDevice, or Product2

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**DataUsePurposeChangeEvent (API version 62.0)**
Change events are available for the object.

**DataUsePurposeHistory**

History is available for tracked fields of the object.

**DataUsePurposeOwnerSharingRule**

Sharing rules are available for the object.

**DataUsePurposeShare**

Sharing is available for the object.
