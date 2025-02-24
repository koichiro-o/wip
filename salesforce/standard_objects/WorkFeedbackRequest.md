#### WorkFeedbackRequest

Represents a single feedback request on a subject or topic (question) to a single recipient in the feedback application. In the case of
offered feedback, WorkFeedbackRequest represents feedback that is offered about a subject. In the performance application,
WorkFeedbackRequest represents a request for feedback on a set of questions from a question set, on a subject—for the recipient to
complete and submit.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Additional Considerations and Related Objects

```
**•** After a request’s state is changed to Submitted, fields can’t be changed, except for LastSharedDate and IsUnreadByOwner.

**•** If LastRemindDate is updated, a reminder notification will be sent to the request’s recipient (only possible when request is in Draft
state).

**•** When a new request is created, a notification is sent to the recipient.

**•** When a recipient of a request submits their feedback (Draft->Submitted), a notification will be sent to requester (except for offered
feedback).

**•** Requester cannot modify the subject of the question set after a request is created.

**•** For offered feedback (to user, to manager, or both), the person who is offering feedback is both the creator of WorkFeedbackRequest
as well as the recipient.


-----

##### Fields

**Field Name**
```
AdHocFeedback
AdHocQuestion
Description
FeedbackRequestState
FeedbackType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort

**Description**
The content of the feedback.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort

**Description**
The content of the feedback question.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the WorkFeedbackRequest.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The current state of the feedback request. Allowed picklist values are:

**•** Draft

**•** Submitted

**•** Declined

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies the type of request. Picklist values that are used for performance
summaries:

**•** Unspecified


-----

```
IsDeployed
IsShareWithSubject
IsUnreadByOwner
IsUnsolicited

```


**•** Peer Summary

**•** Self Summary

**•** Manager Summary

**•** Skip Level Summary

Picklist values that are used for feedback:

**•** Personal

**•** Unsolicited to User

**•** Unsolicited to Manager

**•** Unsolicited to User and Manager

**•** On Topic

The type of the feedback determines the sharing and visibility rules that are
applied to answers.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, the feedback is part of a deployed performance summary cycle.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, the feedback is shared with the summary subject.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, the submitted request has not been seen by the requester.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, the feedback request is unsolicited feedback offered to another user.`


-----

```
LastReferencedDate
LastRemindDate
LastSharedDate
LastViewedDate
Name
OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkFeedbackRequest.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time a reminder was sent to the recipient of this draft request.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time this request was shared with another user or group.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkFeedbackRequest. If this value is null, this record might have been only
referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the WorkFeedbackRequest.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
PerformanceCycleId
QuestionSetId
RecipientId
RelatedObjectId
SharingScope

```

**Description**
ID of the owner of the WorkFeedbackRequest.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used by performance summaries to link to a summary cycle. This field applies
only to performance summaries.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Question set associated with the current request.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User asked to provide feedback on the subject.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Specifies a record in the system that this feedback request is related to. Used by
ad-hoc feedback to gather feedback in the context of an opportunity or WDC
goal.

Used by performance summaries to link to a summary cycle.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The users that see the feedback. `SharingScope` can have the following
values:


-----

```
SubjectId
SubmitFeedbackToId
SubmittedDate

##### Associated Objects

```


**•** Nobody

**•** Subject

**•** Manager

**•** SubjectAndManager

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user that this request (or offer) is about.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the person this performance summary feedback request (and its
respective answers) is shared with. It’s also the ID of the person who owns the
requested subject’s manager summary request. This field applies only to
performance summaries.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time (in case it was reopened by admin) this request was submitted by
the recipient. This field applies only to performance summaries.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkFeedbackRequestFeed**

Feed tracking is available for the object.

**WorkFeedbackRequestOwnerSharingRule**

Sharing rules are available for the object.

**WorkFeedbackRequestShare**

Sharing is available for the object.


-----
