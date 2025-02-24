#### VoiceCallQualityFeedback

Represents feedback given by a Sales Dialer user about the quality of a VoiceCall .

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
FeedbackText
FeedbackType
OwnerId
VoiceCallId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The detailed feedback about a call left by a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The feedback category (Call could not connect, Audio lagged, etc.) selected by
a user.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user leaving the feedback.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related VoiceCall.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**VoiceCallQualityFeedbackOwnerSharingRule**

Sharing rules are available for the object.

**VoiceCallQualityFeedbackShare**

Sharing is available for the object.
