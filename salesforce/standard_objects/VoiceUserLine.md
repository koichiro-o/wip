#### VoiceUserLine

Represents a user’s forwarding phone number.

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
IsCustomCallerId
IsVerified
Name
OwnerId
PhoneNumber

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the number is a custom caller ID (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**

The name of the phone number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user who owns the phone number.

**Type**
phone

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The user’s phone number.


-----

```
UserId
VendorVerifiedCallerIdKey
VoiceVendorInfoId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the user using the phone number.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

The ID for a custom phone number provided by the Sales Dialer service provider.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the related Sales Dialer service provider.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceUserLineOwnerSharingRule**

Sharing rules are available for the object.

**VoiceUserLineShare**

Sharing is available for the object.
