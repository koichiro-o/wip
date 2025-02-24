#### CommSubscriptionConsent

Represents a customer’s consent to a communication subscription. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
With certain page layout and field-level security settings, some fields aren't visible or editable.

```
BusinessBrandId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a communication
subscription. This is a relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand


-----

```
CommSubscriptionChannelTypeId
ConsentCapturedDateTime
ConsentCapturedSource
ConsentGiverId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated communication subscription channel type record.

This is a relationship field.

**Relationship Name**
CommSubscriptionChannelType

**Relationship Type**
Lookup

**Refers To**
CommSubscriptionChannelType

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when the customer’s consent was captured.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Source through which consent was captured. For example, user@example.com
or www.example.com.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the person who gave consent to the communication subscription on behalf of the
contact point.

Note: If the contact point gave consent, don't use `ConsentGiverId.`

This is a polymorphic relationship field.

**Relationship Name**
ConsentGiver


-----

```
ContactPointId
DataUsePurposeId
EffectiveFromDate

```

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact point, such as an Individual or person account, associated with the
communication subscription consent.

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
Represents the record for data use purpose that you want to associate this consent with.
This field is available in API version 57.0 and later.

This is a relationship field.

**Relationship Name**
DataUsePurpose

**Relationship Type**
Lookup

**Refers To**
DataUsePurpose

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Date when consent starts.


-----

```
EffectiveToDate
EngagementChannelTypeId
LastReferencedDate
LastViewedDate
Name

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when consent ends. This field is restricted by field-level security.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the contact method you want to apply consent to. This field is available in API
version 57.0 and later.

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

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
PartyId
PartyRoleId

```

**Description**
Required. Name of the communication subscription consent record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this customer.

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
Filter, Group, Nillable, Sort

**Description**
Represents the record based on the Individual object that you want to associate consent
with. This field is available in API version 57.0 and later.

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
The ID of the Party Role for the individual you want to associate consent with. This is a
polymorphic relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
PartyRole


-----

```
PrivacyConsentStatus

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
Customer, Seller

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Identifies whether the individual or person account associated with this record agrees to
this form of contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`

**•** `OptInPending—Available in API version 58.0 and later.`

**•** `OptOut`

**•** `OptOutPending—Available in API version 58.0 and later.`

**•** `Seen`

The default value is `NotSeen. This field is available in API version 57.0 and later.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommSubscriptionConsentChangeEvent (API version 49.0)**
Change events are available for the object.

**CommSubscriptionConsentFeed**

Feed tracking is available for the object.

**CommSubscriptionConsentHistory**

History is available for tracked fields of the object.

**CommSubscriptionConsentOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionConsentShare**

Sharing is available for the object.
