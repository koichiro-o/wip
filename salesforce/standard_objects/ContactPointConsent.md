#### ContactPointConsent

Represents a customer's consent to be contacted via a specific contact point, such as an email address or phone number. This object is
available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

```
BusinessBrandId
CaptureContactPointType
CaptureDate
CaptureSource

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a contact point. This
is a relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand

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

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when consent was captured.

**Type**
string


-----

```
ContactPointId
DataUsePurposeId
DoubleConsentCaptureDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online form.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact point record through which the customer is consenting to be contacted.

This is a polymorphic relationship field.

**Relationship Name**
ContactPoint

**Relationship Type**
Lookup

**Refers To**
ContactPointAddress, ContactPointEmail, ContactPointPhone

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data use purpose record that you want to associate this consent with.

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
Create, Filter, Nillable, Sort, Update

**Description**
Date when double opt-in was captured.


-----

```
EffectiveFrom
EffectiveTo
EngagementChannelTypeId
LastReferencedDate
LastViewedDate
Name

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when consents starts.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date when consent ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

ID of the engagement channel record through which the customer is consenting to be
contacted.

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


-----

```
OwnerId
PartyRoleId
PrivacyConsentStatus

```

**Description**
Name of the contact point type consent record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the account owner associated with this customer.

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
The ID of the Party Role for the individual you want to associate consent with. This is a
polymorphic relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
PartyRole

**Relationship Type**
Lookup

**Refers To**
Customer, Seller

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Identifies whether the individual or person account associated with this record
agrees to this form of contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`


-----

**•** `OptInPending—Available in API version 58.0 and later.`

**•** `OptOut`

**•** `Seen`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointConsentHistory**

History is available for tracked fields of the object.

**ContactPointConsentOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointConsentShare**

Sharing is available for the object.
