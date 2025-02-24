#### EnblProgramTaskProgress

Represents a user’s progress towards completing an outcome, a milestone, or an exercise in an Enablement program. This object is
available in API version 60.0 and later.

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
CompletedDateTime
CompletedOnDay

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the user completed the outcome, milestone, or exercise.

**Type**
int


-----

```
CompletedPercent
ContributingRecordCount
DueDate
EnblProgramTaskDefinitionId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days that the user took to complete the outcome, milestone, or exercise.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of the outcome, milestone, or exercise that’s complete.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records that qualify for a user’s progress towards completing an outcome or
milestone. To qualify, the activity must meet the criteria that the corresponding Enablement
measure defines for specific objects, fields, and field values.

Available in API version 61.0 and later.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date the outcome, milestone, or exercise is due.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the outcome, milestone, or exercise definition. This field is a relationship field.

**Relationship Name**
EnblProgramTaskDefinition

**Relationship Type**
Lookup

**Refers To**
EnblProgramTaskDefinition


-----

```
IsCompleted
IsNoLongerTracking
LearningItemProgressId
MilestoneComputationResult
ProgressStatus

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the outcome, milestone, or exercise is complete (true) or not (false). The
default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the user hasn’t completed the outcome or milestone and 30 days have elapsed since the
program’s due date, the value is `true. Otherwise, the value is` `false. The default value`
is `false. For details, see Completion Statuses in Enablement Analytics.`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record that tracks the user's progress through the program that includes this
outcome, milestone, or exercise. This field is a relationship field.

**Relationship Name**
LearningItemProgress

**Relationship Type**
Lookup

**Refers To**
LearningItemProgress

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Derived from the associated EnblProgramTaskDefinition record. For example, if a milestone
has a single measure A with a result of 5, this field’s value is 5.

**Type**
picklist


-----

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the outcome, milestone, or exercise progress. Possible values are:

**•** `Behind`

**•** `Completed Late`

**•** `Completed On Time`

**•** `No Longer Tracking`

**•** `Not Completed`

**•** `Overdue`

[For details, see Completion Statuses in Enablement Analytics.](https://help.salesforce.com/s/articleView?id=sf.enablement_analytics_completion_statuses.htm&language=en_US)
