#### AuthorizationFormConsent

Represents the date and way in which a user consented to an authorization form. This object is available in API version 46.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if Data Protection and Privacy is enabled.

##### Fields

```
AuthorizationFormTextId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The authorization form text that the Individual consented to.


-----

```
ConsentCapturedDateTime
ConsentCapturedSource
ConsentCapturedSourceType
ConsentGiverId

```

This is a relationship field.

**Relationship Name**
AuthorizationFormText

**Relationship Type**
Lookup

**Refers To**
AuthorizationFormText

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. The date and time that consent was given.

**Type**
string

**Properties**
Create, Filter, Group, Nillable Sort, Update

**Description**
Required. The source through which consent was captured. For example,
user@example.com, www.example.com.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The source type through which consent was captured. For example,
phone, email, or website.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the person consenting to the authorization form.

This is a polymorphic relationship field.

**Relationship Name**
ConsentGiver


-----

```
DocumentVersionId
LastReferencedDate
LastViewedDate
Name

```

**Relationship Type**
Lookup

**Refers To**
Account, CareProgramEnrollee, Contact, Individual, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the document version for which consent is given.

This is a relationship field.

**Relationship Name**
DocumentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
OwnerId
RelatedRecordId
Status

```

**Description**

Required. The name of the authorization form consent.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The ID of the owner of the account associated with this customer.

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

The ID of a record showing consent of an authorization form.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Visit

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the authorization form.

Possible values are:

**•** `Rejected`

**•** `Seen`


-----

```
PartyId

##### Associated Objects

```


**•** `Signed`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
This field was removed in API version 47.0. UseConsentGiverId instead.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AuthorizationFormConsentChangeEvent (API version 47.0)**
Change events are available for the object.

**AuthorizationFormConsentHistory**

History is available for tracked fields of the object.

**AuthorizationFormConsentOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormConsentShare**

Sharing is available for the object.
