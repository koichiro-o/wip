#### LearningItemSubmission

Represents a link to a resource, such as a video recording, that a user submits as part of a Feedback Request exercise in an Enablement
program. For peer and manager feedback, this resource can be a recording of a user’s sales patch. For Einstein Coach feedback, this
resource can be a video call, and Einstein generates feedback from the call’s transcription. This object is available in API version 59.0 and
later, but Einstein Coach is available only in API version 61.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
A learning item submission record is created when users take an Enablement program that includes a Feedback Request exercise for
peer and manager feedback.

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** To access exercises that use Einstein Coach, the Use Einstein Coach permission is required. This permission is enabled by default as
part of the Access Einstein Coach permission set, which comes with the Enablement add-on license.

##### Fields

```
CallId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the video call that a user submits for Einstein Coach feedback. Einstein generates
feedback for the user based on the call’s transcription. This field is a polymorphic relationship
field.

Available in API version 61.0 and later.

**Relationship Name**
Call


-----

```
LearningItemId
OwnerId
Url

```

**Relationship Type**
Lookup

**Refers To**
VideoCall

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the LearningItem record for the Feedback Request exercise, where the `Type` of
the learning item is `LearningPractice. This field is a relationship field.`

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the learning item submission. This field is a polymorphic relationship
field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
URL of the content that a user submits for peer and manager feedback. For example, a link
to a video recording of a sales rep’s practice pitch.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemSubmissionOwnerSharingRule on page 64**
Sharing rules are available for the object.

**LearningItemSubmissionShare on page 66**
Sharing is available for the object.
