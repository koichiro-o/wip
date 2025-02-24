#### VoiceCallList

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes callers spent in the IVR system on inbound calls for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of transcription messages for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes agents spent talking to callers on outbound calls for a given
day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
For inbound calls, the total number of minutes callers spent in the queue waiting for a given
day.


Represents a prioritized list of numbers to call.

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
IsActive
Name
OwnerId

##### Associated Objects

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the call list is active or not.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the call list.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the call list owner.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceCallListOwnerSharingRule**

Sharing rules are available for the object.

**VoiceCallListShare**

Sharing is available for the object.
