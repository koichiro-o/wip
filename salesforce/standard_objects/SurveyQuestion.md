#### SurveyQuestion

Represents a question in a survey.

##### Supported Calls
```
describeLayout()describeSObjects()getDeleted(), getUpdated(), query(), retrieve()

```
Note: You can’t define custom fields for the SurveyQuestion object using the Object Manager.

##### Fields

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the SurveyQuestion. The API name must be unique within a particular
version of the survey.


-----

```
IsDeprecated
Name
PageDisplayOrder
PageName
QuestionChoiceCount
QuestionName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the question was deleted from the survey.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Up to the first 250 characters of the label for the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the page is displayed. This field is available in API version 54.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the page. This field is available in API version 52.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of choices for the question. This field is available in API version 62.0 and later.

**Type**
textarea

**Properties**
Nillable

**Description**
The label for the question.


-----

```
QuestionOrder
QuestionType
RelatedQuestionId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question is displayed.

The label for the page. This field is available in API version 52.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of question. Possible values include:

**•** `Boolean—This value is available in API v49.0 and later.`

**•** `CSAT`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `FreeText`

**•** `Image`

**•** `Matrix—This value is available in API v55.0 and later.`

**•** `MultipleChoice`

**•** `MultiSelectPicklist`

**•** `NPS`

**•** `Number`

**•** `Picklist`

**•** `RadioButton`

**•** `StackRank`

**•** `Rating`

**•** `ShortText—This value is available in API v49.0 and later.`

**•** `Slider`

**•** `Toggle`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
SubQuestionDisplayOrder
 SurveyPageId
 SurveyVersionId
ValidationType

##### Associated Objects

```

**Description**
The ID of the parent question. This field is blank when the question itself is the parent question.
This field is available in API v55.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question is displayed within the parent question. This field is available
in API v55.0 and later, with Feedback Management - Starter and Feedback Management Growth licenses.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Lookup to the SurveyPage that contains the question.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyVersion that the question belongs to.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The validations available for the short-text question. Possible values include:

**•** Custom - Cu

**•** Number - Nu


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**SurveyQuestionChangeEvent on page 67**
Change events are available for the object.
