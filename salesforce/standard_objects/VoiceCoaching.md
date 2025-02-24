#### VoiceCoaching

Represents a call that is using call monitoring.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
OwnerId
RelatedRecordId
TraineeId

##### Associated Objects

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the manager monitoring the call.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the call list owner.

**Type**
reference

**Properties**
Filter, Group, Sort, Unique

**Description**
The ID of the call list owner.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.


-----

**VoiceCoachingOwnerSharingRule**

Sharing rules are available for the object.

**VoiceCoachingShare**

Sharing is available for the object.
