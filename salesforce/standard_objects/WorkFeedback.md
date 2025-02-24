#### WorkFeedback

```

**Relationship Name**
ServiceChannel

**Relationship Type**
Lookup

**Refers To**
ServiceChannel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The foreign key to the ServiceTerritory object.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The skill value.


Represents the answer to a question that a person was asked via a feedback request. Also used to store offered feedback without linking
it to a particular question.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
undelete(), update(), upsert()

```

-----

##### Additional Considerations and Related Objects

**•** Ownership is transferred to the requester on submit for certain types (ad-hoc feedback).

**•** The record is read-only after the request that it’s linked to is set to Submitted.

**•** You can’t link a feedback object to a request unless you are the recipient.

**•** The question that the feedback is linked to must be part of the same question set that the request is linked to.

##### Fields

```
Feedback
Name
OwnerId
QuestionId
RequestId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains either the free-form text of the answer, or the choice selected by the
user. Max length is 65536.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the WorkFeedback record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the WorkFeedback record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The question this answer applies to. When this feedback is linked to a request of
an unsolicited type, the question ID is null.

**Type**
reference


-----

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the request this response belongs to, in case of offered feedback.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkFeedbackOwnerSharingRule**

Sharing rules are available for the object.

**WorkFeedbackShare**

Sharing is available for the object.
