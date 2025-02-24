#### QuestionSubscription

Represents a subscription for a user following a Question. This object is available in API version 24.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
CommunityId
Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the zone associated with the Question the user is following. This field
can’t be updated.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort


-----

```
QuestionCreatedDate
QuestionId
SubscriberId

##### Usage

```

**Description**
The name of the question subscription.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Required. Creation date of the Question which the user is following. This field can’t
be updated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the Question which the user is following. This field can’t be updated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the User who is following the Question. This field can’t be updated.


Things to consider when following a Question:

**•** A user can only follow questions that they have permission to view.

**•** Administrators and users with the “Modify All Data” permission can configure other users to follow questions that the other user has
read access to.

**•** Administrators and users with the “Modify All Data” permission can configure users to stop following questions.

Queries on QuestionSubscription:

**•** Users with the “Read” permission on Question can see which questions other users are following.

**•** A query must include a LIMIT clause and the limit can’t exceed 1,000.

**•** A query using a `WHERE` clause can only filter by fields on Question.
