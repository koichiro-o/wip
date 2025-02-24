#### ContactPointEmail

Represents a contact’s email, which is associated with an individual or person account. This object is available in API version 48.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ActiveFromDate
ActiveToDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s email became active.

**Type**
date


-----

```
BestTimeToContactEndTime
BestTimeToContactStartTime
BestTimeToContactTimezone
EmailAddress
EmailDomain
EmailLatestBounceDateTime

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s email is no longer active.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest time to contact the individual.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest time to contact the individual.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The timezone applied to the best time to contact the individual.

**Type**
email

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The email address of the contact.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain of the contact’s email, which is everything after the @ sign.

**Type**
dateTime


-----

```
EmailLatestBounceReasonText
EmailMailBox
IsPrimary
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when an email failed to reach its recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the email didn’t reach its recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A subset of the contact’s email, which is everything before the @ sign.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s email is their primary email (true) or not (false).

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


-----

```
Name
OwnerId
ParentId
UsageType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Required. The name of the contact point email record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

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
The ID of the contact’s parent. Only an individual or account can be a contact’s parent.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

**Description**
Specify the usage type of this email. For instance, whether it’s a work email or a temporary
email.

Possible values are:

**•** `Home`

**•** `Temp`

**•** `Work`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointEmailHistory**

History is available for tracked fields of the object.

**ContactPointEmailOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointEmailShare**

Sharing is available for the object.
