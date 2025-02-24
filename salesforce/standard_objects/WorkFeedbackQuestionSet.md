#### WorkFeedbackQuestionSet

Represents a set of questions being asked. The question set is used to link all the individual requests where different recipients were
asked the same set of questions on the same subject.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)


-----

In the WDC performance application, a question set defines the type of summaries and their due dates that will accompany the deployment
of a specific performance summary cycle.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
DueDate
FeedbackType
Name
OwnerId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date that this specific question set is expected to be submitted by the
recipient. This field applies only to performance summaries.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The description of the collection of questions that are written in context to the
type of recipient answering them, relative to the subject of the summary. This
field applies only to performance summaries.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the question set. Maximum length is 225 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkFeedbackQuestionSet.


-----

```
PerformanceCycleId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a question set is associated to a performance summary cycle, then that cycle
ID is referenced in this field. This field applies only to performance summaries.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkFeedbackQuestionSetOwnerSharingRule**

Sharing rules are available for the object.

**WorkFeedbackQuestionSetShare**

Sharing is available for the object.
