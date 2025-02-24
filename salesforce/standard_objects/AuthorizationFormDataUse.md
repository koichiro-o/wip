#### AuthorizationFormDataUse

Represents the data use consented to in an authorization form. This object is available in API version 46.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if Data Protection and Privacy is enabled.

##### Fields

```
AuthorizationFormId

```

**Type**
reference


-----

```
DataUsePurposeId
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the associated authorization form record.

This is a relationship field.

**Relationship Name**
AuthorizationForm

**Relationship Type**
Lookup

**Refers To**
AuthorizationForm

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Identifies the data use purpose record associated with the authorization
form.

This is a relationship field.

**Relationship Name**
DataUsePurpose

**Relationship Type**
Lookup

**Refers To**
DataUsePurpose

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


-----

```
Name
OwnerId

##### Associated Objects

```

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced (LastReferencedDate)
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the authorization form data use.

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


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormDataUseChangeEvent (API version 62.0)**
Change events are available for the object.

**AuthorizationFormDataUseHistory**

History is available for tracked fields of the object.

**AuthorizationFormDataUseOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormDataUseShare**

Sharing is available for the object.


-----
