#### LearningContent

Represents a Trailhead or enablement site (myTrailhead) module assigned to a user in Workforce Engagement or Learning Paths. This
object also represents a Trailhead module or video in an Enablement program exercise. This object is available in API version 54.0 and
later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
**•** The org must have a Workforce Engagement license.

**•** The user must have at least one Workforce Engagement permission set assigned to them: Workforce Engagement Admin, Workforce
Engagement Analyst, Workforce Engagement Planner, Workforce Engagement Agent.

**•** For an enablement site (myTrailhead) module, the org must have a Sales Enablement license.

**•** For a Trailhead module or video in an Enablement program, the org must have an Enablement license.


-----

##### Fields

**Field**
```
ApiName
AvailablePointCount
ContainsAssessmentType
ContentType
ContentUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The module's human-readable API name, such as pure-aloe-sales-strategies.

**Type**
int

**Properties**
Group, Nillable

**Description**
The maximum points that a user can earn on their profile by completing the module. This
value is the sum of points that the content creator assigns to the module’s units.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**
Specifies the type of assessment that the content’s units include.

Possible values are:

**•** `MultipleChoiceQuiz—All the content’s units have multiple-choice quizzes.`

**•** `HandsOnChallenge—At least one unit has a hands-on challenge.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**
The type of content assigned to the user.

Possible values are:

**•** `All—The content is any supported type.`

**•** `Module—The content is a Trailhead or enablement site (myTrailhead) module.`

**•** `VideoLesson—The content is a video that's specified in the Enablement workspace`
in Digital Experiences and is used in an Enablement program.

**Type**
url


-----

```
Description
DurationCount
ExternalId
ImageUrl
IsPublic

```

**Properties**
Group, Nillable

**Description**
The absolute URL to the content, such as
```
  https://purealoe.my.trailhead.com/en/content/sales-team-enablement/modules/pure-aloe-sales-strategies.

```
**Type**
string

**Properties**
Nillable

**Description**
The module’s description.

**Type**
int

**Properties**
Group, Nillable

**Description**
The total time, in minutes, for a learner to complete all units in the module. This value is the
sum of the estimated times that the content creator assigns to the module’s units.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The GUID that Trailhead uses to reference the module.

**Type**
url

**Properties**
Group, Nillable

**Description**
The absolute URL to the module’s badge art image file.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group

**Description**
Indicates whether the content is public Trailhead content (true) or private enablement
site (myTrailhead) content (false).


-----

```
Title

```
SEE ALSO:

PersonTraining
