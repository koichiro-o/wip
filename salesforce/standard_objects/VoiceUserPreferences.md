#### VoiceUserPreferences

Represents the number the user displays when making outbound calls. This object is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
CallerIdType
DeskPhoneNumber
OwnerId

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The number displayed for outbound calls. The possible values are:

**•** VendorLine

**•** CompanyNumber

**•** LocalPresence

**•** CustomCallerId

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A separate phone number users can utilize as part of a call bridge.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the phone number owner.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceUserPreferencesOwnerSharingRule**

Sharing rules are available for the object.

**VoiceUserPreferencesShare**

Sharing is available for the object.


-----
