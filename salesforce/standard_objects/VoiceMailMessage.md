#### VoiceMailMessage

Represents a prerecorded voicemail message.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
DurationInSeconds
IsDefault

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration of a prerecorded voicemail message in seconds.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
MediaContentId
Name
OwnerId

##### Associated Objects

```

**Description**
Specifies whether the message is the context user’s default voicemail drop
message.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the file.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the prerecorded voicemail message.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the prerecorded voicemail message.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceMailMessageOwnerSharingRule**

Sharing rules are available for the object.

**VoiceMailMessageShare**

Sharing is available for the object.
