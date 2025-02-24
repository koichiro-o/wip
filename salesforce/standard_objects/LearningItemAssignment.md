#### LearningItemAssignment

Represents the assignment of a Learning Paths entry to users or groups or the enrollment of an Enablement program for a specific user.
This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.


-----

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=sf.prm_support_license_template.htm&language=en_US)

##### Fields

```
AssigneeId
AssignmentStatus
DueDate
EnrollmentType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or group assigned to the learning item. This field is a relationship field.

**Relationship Name**
Assignee

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of assigning an Enablement program to a user. Possible values are:

**•** `Failed`

**•** `InProgress`

**•** `Succeeded`

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the assignment is due for the user or group.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


-----

```
IsOverdue
LearningItemId
OwnerId

```

**Description**
The type of enrollment for a user in an Enablement program. Possible values are:

**•** `Assigned`

**•** `SelfEnrolled`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the assigned learning item is overdue (true) or not (false). The default
value is `false.`

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the learning item. This field is a relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
ID of the user who assigned the learning item. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
StartDate

##### Usage

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The date that the learning item was assigned to the user or group.


You can assign a learning item to a user programmatically by querying the program and user, and then inserting a record into
LearningItemAssignment.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemAssignmentOwnerSharingRule on page 64 (API version 60.0)**
Sharing rules are available for the object.

**LearningItemAssignmentShare on page 66 (API version 60.0)**
Sharing is available for the object.
