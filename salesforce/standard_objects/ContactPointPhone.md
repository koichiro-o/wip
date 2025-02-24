#### ContactPointPhone

Represents a contact’s phone number, which is associated with an individual or person account. This object is available in API version
48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ActiveFromDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ActiveToDate
AreaCode
BestTimeToContactEndTime
BestTimeToContactStartTime
BestTimeToContactTimezone
ExtensionNumber

```

**Description**
The date when the contact’s phone number became active.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s phone number is no longer active.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The area code of the phone number’s location for the contact.

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
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
FormattedInternationalPhoneNumber
FormattedNationalPhoneNumber
IsBusinessPhone
IsFaxCapable
IsPersonalPhone
IsPrimary

```

**Description**
The phone number extension for the contact.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The internationally recognized format for the contact’s phone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The nationally recognized format for the contact’s phone number.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a business number (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a fax number (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a personal number (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
IsSmsCapable
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Description**
Indicates whether a contact’s phone number is their primary number (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number can receive text messages (true) or not
(false).

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
Filter, Group, idLookup, Nillable, Sort

**Description**
Required. The name of the contact point phone record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

This is a polymorphic relationship field.


-----

```
ParentId
PhoneType
PreferenceRank
TelephoneNumber

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
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of phone number for the contact.

Possible values are:

**•** `Home`

**•** `Mobile`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify how this phone numbers ranks in terms of preference among the contact’s other
phone numbers.

**Type**
phone


-----

```
UsageType

##### Associated Objects

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The phone number for the contact.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify the usage type of this number. For instance, whether it’s a work phone or a home
phone.

Possible values are:

**•** `Home`

**•** `Temp`

**•** `Work`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointPhoneHistory**

History is available for tracked fields of the object.

**ContactPointPhoneOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointPhoneShare**

Sharing is available for the object.
