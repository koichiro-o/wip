#### VoiceMailContent

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The area code of the phone number.


Represents a voicemail message left by a caller to the context user.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
DurationInSeconds
FirstHeardDateTime
MediaContentId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration of the voicemail message in seconds.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time and date when the user first listened to the voicemail message.

**Type**
reference


-----

```
Name
OwnerId
VoiceCallId

##### Associated Objects

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
[The ID of the related media content, a ContentDocument. The record counts](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_contentdocument.htm)
toward your org’s file storage quota.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the voicemail message.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the voicemail message.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the related Dialer call.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceMailContentOwnerSharingRule**

Sharing rules are available for the object.

**VoiceMailContentShare**

Sharing is available for the object.
