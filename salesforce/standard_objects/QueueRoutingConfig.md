#### QueueRoutingConfig

Represents the settings that determine how work items are routed to agents. This object is available in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), query(), retrieve(), update()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
CapacityPercentage

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of an agent’s capacity for work items that’s consumed by a specific type of
work item from this service channel.

For example, you might give phone calls a capacity percentage of `100. If an agent receives`
a phone call, the agent won’t receive new work items until the call ends, because at that
point the agent’s capacity will have reached 100%.


-----

```
CapacityWeight
DeveloperName
DropAdditionalSkillsTimeout
IsAttributeBased

```

This field is available in API version 33.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity for work items that’s consumed by a work item from this
service channel.

For example, if an agent has a capacity of `6, and cases are assigned a capacity weight of` `2,`
an agent can be assigned up to 3 cases before the agent is at capacity and can’t receive new
work items.

This field is available in API version 33.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group Nillable, Sort, Update

**Description**

The number of seconds to wait before a skill marked as Additional Skill is dropped from
Omni-Channel routing. The case is then routed to the best-matched agent even if they don’t
have all the skills.

**Type**
boolean


-----

```
Language
MasterLabel
OverflowAssigneeId
PausedCapacityPercentage
PausedCapacityWeight

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this routing is attribute-based. Available in API version 45.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the presence status.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the presence status.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user or queue that’s set as the Overflow Assignee.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of an agent’s capacity for work items that’s consumed by a paused work
item from this service channel.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity for work items that’s consumed by a paused work item
from this service channel.


-----

```
PushTimeout
RoutingModel
RoutingPriority
ServiceChannelId
