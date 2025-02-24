#### OmniSupervisorConfig

Represents the Omni-Channel supervisor configuration for an assigned group of supervisors. This object is available in API version 41.0
and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve() update(), upsert()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With


-----

```
IsTimelineHidden
Language
MasterLabel
SkillVisibility

```

this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true, hides the agent timeline from the supervisors assigned to this supervisor`
configuration. The default value is `false.`

This field is available in API version 53.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of this supervisor configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
A unique label name for this supervisor configuration. The name must begin with a letter.
The name can contain alphanumeric characters and underscores. The name can’t contain
spaces, two consecutive underscores, or end with an underscore. The name appears as Omni
Supervisor Configuration Name in the UI.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Determines which work items based on skills are visible to the supervisors assigned to this
supervisor configuration. Possible values are:

**•** `AllSkills` — Show work items with all skill requirements selected in this supervisor
configuration.


-----

**•** `AnySkill — Show work items with at least one skill requirement selected in this`
supervisor configuration.

This field is available in API version 53.0 and later.
