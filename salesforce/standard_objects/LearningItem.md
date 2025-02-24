#### LearningItem


The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The module’s title.


Represents an item that requires users to take action, including a Learning Paths entry, an Enablement program, or an exercise with
linked content in an Enablement program. For Learning Paths, users are assigned a learning item to complete. For Enablement programs
and exercises, users are assigned a program or can self-enroll in shared programs. This object is available in API version 58.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=sf.prm_support_license_template.htm&language=en_US)

##### Fields

```
CustomLearningItemTypeId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
EnablementProgramId
OwnerId

```

**Description**
The ID of a learning item type record if this learning item represents a custom exercise type
in an Enablement program. This field is required when the `Type` field’s value is
```
  CustomContent.

```
This field is a relationship field.

Available in API version 62.0 and later.

**Relationship Name**
CustomLearningItemType

**Relationship Type**
Lookup

**Refers To**
LearningItemType

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of an Enablement program that contains the outcome, milestone, or exercise.

This field is a relationship field.

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the owner of the program. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
Type

##### Associated Objects

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of learning item. Possible values are:

**•** `CustomContent—Custom exercise content in an Enablement program, such as a`
screen flow, content from external repositories, or other custom content sources. Available
in API version 62.0 and later.

**•** `EnablementProgram`

**•** `LearningContent—Trailhead module`

**•** `LearningLesson—Lesson exercise in an Enablement program`

**•** `LearningLink—Audio Recording, Document, Scheduled Event, or Other exercise`
in an Enablement program

**•** `LearningPractice—Feedback Request exercise in an Enablement program`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LearningItemOwnerSharingRule on page 64 (API version 60.0)**
Sharing rules are available for the object.

**LearningItemShare on page 66 (API version 60.0)**
Sharing is available for the object.
