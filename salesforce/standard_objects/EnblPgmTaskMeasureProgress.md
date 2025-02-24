#### EnblPgmTaskMeasureProgress

Represents a user’s progress through the object and field requirements that an Enablement measure defines for an outcome or milestone
in an Enablement program. This object is available in API version 61.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

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
ContributingRecordCount
EnblProgramTaskMeasureId
EnblProgramTaskProgressId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records that qualify for a user’s progress towards completing an outcome or
milestone. To qualify, the activity must meet the criteria that the corresponding Enablement
measure defines for specific objects, fields, and field values.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record that represents the connection between a specific Enablement measure
and a specific milestone or outcome in an Enablement program.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskMeasure

**Relationship Type**
Lookup

**Refers To**
EnblProgramTaskMeasure

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
MeasureComputationResult

```

**Description**
ID of the record that represents the progress through the milestone or outcome.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskProgress

**Relationship Type**
Master-detail

**Refers To**
EnblProgramTaskProgress (the master object)

**Type**
double

**Properties**
Filter, Sort

**Description**
The calculated progress through the measure’s requirements for a milestone or outcome.
For example, if the measure is the dollar amount of all closed opportunities, then the field
value is measured in dollars.

For a composite milestone or a composite outcome, this value represents the progress
through only one measure associated with the milestone or outcome.

