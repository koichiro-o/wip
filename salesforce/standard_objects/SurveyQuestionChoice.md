#### SurveyQuestionChoice

Represents an answer choice that a participant can select for a survey question.

##### Supported Calls
```
describeLayout(), getDeleted(), getUpdated(), query(), retrieve()

```
Note: You can’t define custom fields for the SurveyQuestionChoice object using the Object Manager.

##### Fields

```
DeveloperName
DisplayOrder
IsDeprecated
Name

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique API name of the SurveyQuestionChoice object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question choice is displayed within the parent question. This field is
available in API v55.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a question choice was deleted from the survey.

**Type**
string


-----

```
QuestionId
SurveyVersionId

##### Associated Objects

```

**Properties**
Filter, Group, idLookup, Sort

**Description**
A label for the question choice that appears in the UI.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyQuestion object that this choice belongs to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the survey that this question choice belongs to.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionChoiceChangeEvent on page 67**
Change events are available for the object.
