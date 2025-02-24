#### LearningPractice

Represents a Feedback Request exercise in an Enablement program. Users can submit a sample of their work and request feedback from
their peers and managers. Or, users can submit a video call and Einstein Coach generates feedback from the call’s transcription. This
object is available in API version 59.0 and later, but Einstein Coach feedback is available only in API version 61.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** To access exercises that use Einstein Coach, the Use Einstein Coach permission is required. This permission is enabled by default as
part of the Access Einstein Coach permission set, which comes with the Enablement add-on license.

##### Fields

```
Description
InviteeQuantity

```

**Type**
string

**Properties**
Filter, Sort

**Description**
Instructions to the user to provide context for completing the Feedback Request exercise.
For example, `Record yourself giving a sales pitch and request`
```
  feedback from your peers.

```
**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of peers or managers that the user is required to invite for giving feedback when
`Type` is PeerFeedback. Each peer or manager receives an invitation to the assessment
survey associated with the Feedback Request exercise.

When `Type` is `AIFeedback, this value is always` `1.`


-----

```
LearningItemId
Name
PromptTemplate
SurveyId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the LearningItem record for the Feedback Request exercise. The value must be
unique. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the Feedback Request exercise. For example, `Practice Your Sales`
```
  Pitch.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The prompt template to use with this exercise when `Type` is `AIFeedback.`

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the assessment survey that’s sent to peers and managers when `Type` is
```
  PeerFeedback. This field is a relationship field.

```
**Relationship Name**
Survey

**Relationship Type**
Lookup


-----

```
Type
