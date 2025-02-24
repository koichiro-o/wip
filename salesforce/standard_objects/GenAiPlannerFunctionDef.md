#### GenAiPlannerFunctionDef

Represents a relationship between the agent planner service and agent actions. This object is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, Agents must be enabled in your org.

##### Fields

```
PlannerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
Plugin

```

**Description**
This field is a relationship field.

**Relationship Name**
Planner

**Relationship Type**
Lookup

**Refers To**
GenAiPlannerDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A set of actions that contextualize the agent planner service.

