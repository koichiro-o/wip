#### VoiceVendorLine

```

**Description**
The version of the Service Cloud Voice tenant configuration. Available in API
version 51.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The account key of the vendor.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the vendor.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The name of the telephony vendor.


Represents a user’s phone number reserved with the vendor.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.


-----

##### Fields

**Field Name**
```
CallUsageInSecondsLastMonth
OwnerId
PhoneNumber
ShouldRecord
Status

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
An org’s total call usage last month in seconds.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the phone number.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
phone

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique vendor phone number.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
UserId
VoiceVendorInfoId

##### Associated Objects

```

**Description**
Specifies whether the number is currently active or released.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user using the phone number.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Dialer vendor.

This is a relationship field.

**Relationship Name**
VoiceVendorInfo

**Relationship Type**
Lookup

**Refers To**
VoiceVendorInfo


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceVendorLineOwnerSharingRule**

Sharing rules are available for the object.

**VoiceVendorLineShare**

Sharing is available for the object.


-----
