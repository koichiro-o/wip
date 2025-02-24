#### WorkFeedbackQuestion

Represents a free-form text type or multiple choice question within a set of questions.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Choices
Detail

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
New-line separated list of valid choices for multiple choice questions. Maximum
length is 1000 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
IsConfidentialAnswer
IsOptional
Name
Number
OwnerId

```

**Description**
Detailed instructions on how to answer the question.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Answers to questions marked confidential will not be shared with the subject of
the review. This field applies only to performance summaries.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If this option is selected, the question is optional and isn’t required to be answered.
This field applies only to performance summaries.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A short description of the question, which can be used as a header for reports
and Calibration.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order of the question that is displayed within the question set, such as
question number three in a question set that has five questions.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkFeedbackQuestion.


-----

```
QuestionSetId
Text
Type

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The question set this question is a part of.

**Type**
textarea

**Properties**
Create, Update

**Description**
The body of the question. Max length is 16384 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Allows for either a free-form text answer or a multiple choice question defined
by new-line separate choices in the ‘Choices’ field. Valid picklist values are:

**•** MultipleChoice

**•** FreeText

**•** Rating


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkFeedbackQuestionOwnerSharingRule**

Sharing rules are available for the object.

**WorkFeedbackQuestionShare**

Sharing is available for the object.
