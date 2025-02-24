#### SurveyQuestionScore

Represents the aggregate of responses for the following question types: date, multiple choice, picklist, radio, ranking, rating, scoring,
[slider, and Net Promoter Score[®] (NPS[®]).](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/product-specific-terms/net-promoter-and-nps.pdf)

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), undelete()

```
Note: You can’t define custom fields for the SurveyQuestionScore object using the Object Manager.

##### Fields

```
CumulativeScore
DateResponse
Name

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the responses provided by all the participants for a question of the following types:
rating, scoring, and slider. For a question of the type ranking, sum of the weights provided
by all the participants for each item.

Note: This field is only applicable for the overall score type.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date selected by one or more participants for a question of the type date.

Note: This field is only applicable for the individual score type.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
For an overall score type record:

**•** Name of a question.

**•** Name of an item in a question of the type ranking.

For an individual score type record:


-----

```
QuestionChoiceId
QuestionDeveloperName
QuestionId
QuestionName
QuestionSkippedCount

```


**•** Name of an item in a question of the type ranking.

**•** Name of a question of the type date.

**•** Response provided by one or more participants for questions of the following types:
picklist, multiple choice, rating, ranking, score, slider, NPS.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the answer choice selected by one or more participants. For an individual
score type record, this field is applicable for questions of the following types: picklist, radio,
multi choice, ranking and rating. For an overall score type record, this field is applicable for
questions of the type ranking.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the question for which response is recorded. The API name must be unique
within a particular version of the survey.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the question for which response is recorded.

**Type**
textarea

**Properties**
Nillable

**Description**
Name of the question for which response is recorded.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
ResponseCount
ResponseValue
Score

```

**Description**
Number of participants who didn’t respond to the question.

Note: This field is only applicable for the overall score type.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
For an overall score type record, number of participants who responded to the question. For
an individual score type record, number of participants who selected a particular answer
choice.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Answer choice selected by one or more participants for a question of the following types:
rating, slider, score, NPS. Rank provided by the participant for an item in a question of the
type ranking.

Note: This field is only applicable for the individual score type.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
For an individual score type record, percentage of participants who selected a particular
answer choice.

Note: For questions of the type ranking, the percentage of participants who have
provided the same rank to an item.

For overall score type record:

**•** Average score of questions of the following question types: rating, scoring, and slider.

**•** Score of an NPS type question.

**•** Average weight provided by all participants for each item in question of the type ranking.

**•** Number of participants who responded to the question for the following question types:
date, radio, multi choice, and picklist.


-----

```
 ScoreType
 SurveyId
 SurveyInvitationId
 SurveyVersionId
