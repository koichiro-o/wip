#### MessagingEndUser

```

This is a relationship field.

**Relationship Name**
MessagingTemplate

**Relationship Type**
Lookup

**Refers To**
MessagingTemplate

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Namefield, Sort

**Description**
Name of the error. Maximum length is 80 characters.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
System modification time for the Messaging delivery error log.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The kind of event that occurred. Possible values include:

**•** `Error` (Default)

**•** `Warning`


Represents a single address—such as a phone number or Facebook page—communicating with a single Messaging channel. This
object is available in API version 40.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AccountId
ContactId
 HasInitialResponseSent
 IsFullyOptedIn

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Account associated with this Messaging end user. Available in API version 43.0 and
later.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated Contact. Available in API version 43.0 and later.

This field is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an initial response has been sent to the Messaging end user (true) or
not (false).

**Type**
boolean


-----

```
IsOptedOut
IsoCountryCode
LastReferencedDate
LastViewedDate
LeadId

```

**Properties**
Defaulted on create, Filter, Sort

**Description**
Indicates whether the Messaging end user has opted in to receiving messages (true) or
not (false). This field compares the related messaging channel’s consent requirement to
the user’s consent status; if the user’s status meets the channel’s required consent level,
`IsFullyOptedIn` is set to `true. Available in API version 48.0 and later.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Messaging end user has opted out of receiving messages. Available
in API version 48.0 and earlier. Use `MessagingConsentStatus` and
`IsFullyOptedIn` instead.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ISO country code associated with the Messaging end user.

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
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference


-----

```
Locale
MessageType
MessagingChannelId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated lead. Available in API version 57.0 and later.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of message. Possible values are:

**•** `AppleBusinessChat—Represents Apple Messages for Business.`

**•** `Custom—Represents Bring Your Own Channel. Available in API version 58.0 and later.`

**•** `EmbeddedMessaging—Represents Messaging for In-App and Web. Available in`
API version 50.0 and later.

**•** `Facebook`

**•** `Phone`

**•** `Text`

**•** `Voice`

**•** `WhatsApp`

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
MessagingConsentStatus
MessagingPlatformKey
Name
OwnerId

```

**Description**
The ID of the Messaging channel associated with the Messaging end user.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The consent status of the messaging user. This field is available in API version 48.0 and later.
Possible values are:

**•** `DoublyOptedIn`

**•** `ExplicitlyOptedIn`

**•** `ImplicitlyOptedIn`

**•** `OptedOut`

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**

The phone number, Facebook page ID, or unique key associated with this Messaging end
user.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Messaging end user. Because this field is editable, we don’t recommend
referencing it in automation. Instead, use the Messaging Platform Key.

**Type**
reference


-----

```
 ProfilePictureUrl

##### Associated Objects

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner associated with this Messaging end user.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The URL of the Messaging end user's profile picture.


This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**MessagingEndUserChangeEvent (API version 62.0)**
Change events are available for the object.

**MessagingEndUserHistory**

History is available for tracked fields of the object.

**MessagingEndUserOwnerSharingRule**

Sharing rules are available for the object.

**MessagingEndUserShare**

Sharing is available for the object.
