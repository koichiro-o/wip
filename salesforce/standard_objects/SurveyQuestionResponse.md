#### SurveyQuestionResponse

Represents a participant’s answer to a specific question.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
Note: You can’t define custom fields for the SurveyQuestionResponse object using the Object Manager.


-----

##### Fields

**Field**
```
 ChoiceValue
 Datatype
 DateTimeValue
 DateValue

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Response provided by a participant for the following question types:

**•** Multiple choice

**•** Picklist

**•** Radio

**•** Ranking

**Type**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The data type of the question response. Possible values are:

**•** `Boolean` This value is available in API v49.0 and later.

**•** `Date`

**•** `Double`

**•** `Int`

**•** `Number`

**•** `String`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Response provided by a participant for a question of the type date time.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Response provided by a participant for a question of the type date.


-----

```
InvitationId
IsTrueOrFalse
NumberValue
QuestionChoiceId
QuestionId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the SurveyInvitation that was sent to the survey participant.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Response provided by a participant for a question type which has only two possible values:
True and False.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Response provided by a participant for the following question types:

**•** Net Promoter Score (NPS)

**•** Rating

**•** Score

**•** Slider

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of SurveyQuestionChoice that a participant chose in response to a question.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the SurveyQuestion that a participant provided an answer for.


-----

```
 Rank
 ResponseId
 ResponseShortText
 ResponseValue
 SurveyVersionId

##### Associated Objects

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rank provided by a participant for an answer choice for the ranking question type.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyResponse that is the parent of this SurveyQuestionResponse.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Up to the first 250 characters of the response provided by a participant for a text type question.

**Type**
textarea

**Properties**
Nillable

**Description**
Response provided by a participant for a question.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyVersion that the response belongs to.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionResponseChangeEvent on page 67**
Change events are available for the object.


-----
