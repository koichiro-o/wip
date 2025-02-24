#### WorkGoalCollaborator

Represents collaborators on a WorkGoal object. This doesn’t include WorkGoal followers, which is handled by Chatter Feed Follow
functionality. This object has been deprecated as of API version 35.0. Use the Goal object to query information about WDC goals.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
InvitationDate
State

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date that a user was invited to become a collaborator (nill if the user was not
invited).

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the state of the collaborating user. Whether the user has not responded,
joined, or declined collaboration. The possible values are:


-----

```
UserId
WorkGoalId

##### Associated Objects

```


**•** PendingResponse: a user who was invited to collaborate but hasn’t joined
or declined

**•** Joined: a user who is collaborating on a goal (joined/commit)

**•** Declined: a user who declined to collaborate on a goal

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The collaborating user.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The WorkGoal object that this collaborator is a part of.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkGoalCollaboratorHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)
