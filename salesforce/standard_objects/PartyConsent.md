#### PartyConsent

Represents consent preferences for an individual. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Action
CaptureContactPointType
CaptureDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The action that the Individual is consenting to.

Possible values are:

**•** `CrossDevice`

**•** `DataCollection`

**•** `Reidentification`

**•** `Segment`

**•** `ShareData`

**•** `Target`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Indicates how you captured consent.

Possible values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

**Type**
dateTime


-----

```
CaptureSource
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when consent was captured.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online form.

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
Name of the party consent record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the account owner associated with this customer.

This is a polymorphic relationship field.


-----

```
PartyId
PrivacyConsentStatus

```

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Represents the record based on the Individual object you want to associate consent
with.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Identifies whether the individual associated with this record agrees to this form of
contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`

**•** `OptInPending—Available in API version 58.0 and later.`

**•** `OptOut`

**•** `OptOutPending—Available in API version 58.0 and later.`

**•** `Seen`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PartyConsentChangeEvent**

Change events are available for the object.

**PartyConsentFeed**

Feed tracking is available for the object.

**PartyConsentHistory**

History is available for tracked fields of the object.

**PartyConsentOwnerSharingRule**

Sharing rules are available for the object.

**PartyConsentShare**

Sharing is available for the object.
