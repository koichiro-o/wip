#### DocumentRecipient

Connects a Service Report to a Digital Signature. This object is available in API version 55.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
DigitalSignatureId
DigitalSignatureUrl
DocumentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Digital Signature to be used on the Service Report.

This field is a relationship field.

**Relationship Name**
DigitalSignature

**Relationship Type**
Lookup

**Refers To**
DigitalSignature

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Link to request signature from Experience Cloud site.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The document sent to the recipient.

This field is a polymorphic relationship field.

**Relationship Name**
Document

**Relationship Type**
Lookup

**Refers To**
ServiceReport


-----

```
DocumentRecipient
LastReferencedDate
LastViewedDate
OwnerId

```
QuoteDocumentId


**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number automatically assigned to a new record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object. ID of the creator of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


-----

```
RecipientId
SignatureIdentifier
SignatureStatus

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote document sent to the recipient.

This field is a relationship field.

**Relationship Name**
QuoteDocument

**Refers To**
QuoteDocument

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The recipient to sign the document.

This field is a polymorphic relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
Contact, User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier that associates `DocumentRecipient` with a signature Lightning
web component (LWC) on the report page layout, telling you where on the report the
signature goes.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the signature. The default value is `Completed. Possible values are:`

**•** `Completed`

**•** `Skipped`


-----

```
SignatureStatusReason
Status
StatusReason

##### Associated Objects

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
An explanation for the signature status. For example, a reason why the signature was skipped.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the document recipient record.

Possible values are:

**•** `Completed`

**•** `Declined`

**•** `Delivered`

**•** `None`

**•** `Sent`

The default value is `None.`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The final status reason.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**DocumentRecipientFeed on page 54**
Feed tracking is available for the object.

**DocumentRecipientOwnerSharingRule on page 64**
Sharing rules are available for the object.

**DocumentRecipientShare on page 66**
Sharing is available for the object.


-----
