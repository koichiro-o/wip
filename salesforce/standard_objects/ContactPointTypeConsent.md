#### ContactPointTypeConsent

Represents consent for a contact point type, such as email or phone. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is available if Data Protection and Privacy is enabled.

##### Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

```
BusinessBrandId
CaptureContactPointType
CaptureDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a contact
point type. this is a relationship field. This field is available in API version 53.0 and
later.

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
Required. Indicates how you captured consent. Possible values are:

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


-----

```
CaptureSource
ContactPointType
DataUsePurposeId
DoubleConsentCaptureDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online
form.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Represents the contact method you want to apply consent to. Possible
values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the record for data use purpose that you want to associate this consent
with.

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


-----

```
EffectiveFrom
EffectiveTo
EngagementChannelType

```

**Description**
Date when double opt-in was captured.

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
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required if a `ContactPointType isn’t selected. Represents the contact`
method you want to apply consent to. Possible values are:

**•** `Billboard`

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `SMS`

**•** `Social`

**•** `Web`

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
PartyId

```

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

**Description**
Name of the contact point type consent record.

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


-----

```
PartyRoleId
PrivacyConsentStatus

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Represents the record based on the Individual object you want to
associate consent with.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Party Role for the individual you want to associate consent with.
This is a polymorphic relationship field. This field is available in API version 53.0
and later.

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
Required. Identify whether the individual associated with this record agrees to
this form of contact. Possible values are:

**•** `NotSeen`

**•** `Seen`

**•** `OptIn`

**•** `OptInPending—Available in API version 58.0 and later.`

**•** `OptOut`

**•** `OptOutPending—Available in API version 58.0 and later.`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent (API version 47.0)**
Change events are available for the object.

**ContactPointTypeConsentHistory**

History is available for tracked fields of the object.

**ContactPointTypeConsentOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointTypeConsentShare**

Sharing is available for the object.
