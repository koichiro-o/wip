#### EnblProgramTaskDefinition

Represents an outcome, a milestone, or an exercise in an Enablement program. A program task is also known as a program item. This
object is available in API version 60.0 and later.

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
CompositeMilestoneType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of logic to use for evaluating the activity from two Enablement measures in a
composite milestone.

Possible values are:

**•** `Addition`

**•** `Division`

**•** `Percentage`


-----

```
CustomEnblPgmTaskSubCategoryId
Day
Description
EnablementProgramId

```

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the EnblProgramTaskSubCategory record associated with a custom exercise type.
This field is required when the TaskSubCategory field’s value is CustomExercise.

This field is a relationship field.

Available in API version 62.0 and later.

**Relationship Name**
CustomEnblPgmTaskSubCategory

**Relationship Type**
Lookup

**Refers To**
EnblProgramTaskSubCategory

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The day of the program when the item is due, relative to the program's start date. For example,
if a user is expected to complete an exercise where they watch a product demo by day 2,
this field’s value is 2. For an outcome, this field specifies the number of days the full program
takes. For example, if your program lasts 60 days, the value of this field is 60 for the outcome.
This field’s value contributes to the program’s due date that users see when they take the
program.

**Type**
textarea

**Properties**
Create

**Description**
A summary of the outcome, milestone, or exercise that’s visible to users when they take the
program.

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
EnblProgramSectionId
IsMilestoneAnOutcome
LearningItemId

```

**Description**
The ID of the Enablement program that contains the outcome, milestone, or exercise. This
field is a relationship field.

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of an optional program section that contains the milestone or exercise. This field is a
relationship field.

**Relationship Name**
EnblProgramSection

**Relationship Type**
Lookup

**Refers To**
EnblProgramSection

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the program item is the program’s final outcome (true) or an incremental
milestone (false). The default value is `false.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the learning item record for the outcome, milestone, or exercise. This field is a
relationship field.

**Relationship Name**
LearningItem


-----

```
MilestoneTarget
MinimumSampleSize
Name
SequenceNumber

```

**Relationship Type**
Lookup

**Refers To**
LearningItem

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The target value for a user to achieve to get credit for completing the outcome or milestone.
The unit depends on the specific measure used with the outcome or milestone. For example,
if the measure is the dollar amount of all closed opportunities, then the field value is measured
in dollars.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records to evaluate when calculating progress for an outcome or milestone
that uses an average-based measure. Use this field with MilestoneTarget. For example,
if you want users to achieve an average deal size of $50,000 after closing 4 deals, then this
field’s value is `4` and `MilestoneTarget` is `50000.`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the outcome, milestone, or exercise that’s visible to users when they take the
program.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
A number that specifies the order of the milestone or exercise, relative to other milestones
or exercises that have the same due date in the program or in the same section, starting at
0. This number determines the order of items that users see for that day in the program.


-----

```
TaskCategory
TaskSubCategory

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of program item. Possible values are:

**•** `Exercise`

**•** `Milestone`

`Milestone` is used for both the program’s final outcome and incremental milestones.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of exercise. This value determines the content associated with the exercise. For
example, if the field value is `Video, the exercise must reference video content from the`
Enablement workspace in the Digital Experiences app. The `LearningItemId` field
specifies the reference to that video content. Possible values are:

**•** `ActionItem`

**•** `AudioRecording`

**•** `CustomExercise—Available in API version 62.0 and later.`

**•** `Document`

**•** `FeedbackRequest`

**•** `Other`

**•** `OtherExercise`

**•** `ScheduledEvent`

**•** `TextLesson`

**•** `Trailhead`

**•** `Video`

