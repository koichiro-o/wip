#### VoiceMailGreeting

Represents a custom greeting message that plays upon reaching a user’s voicemail. This object is available in API version 41.0 and later.


-----

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
MediaContentId
Name
OwnerId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration of the voicemail greeting message in seconds.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the greeting is the user’s default greeting (true) or not (false).

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the related content document.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the voicemail greeting message.

**Type**
reference


-----

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the voicemail greeting message owner.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceMailGreetingOwnerSharingRule**

Sharing rules are available for the object.

**VoiceMailGreetingShare**

Sharing is available for the object.
