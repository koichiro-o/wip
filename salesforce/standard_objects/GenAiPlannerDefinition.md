#### GenAiPlannerDefinition

Represents an agent planner service that uses a large language model (LLM) and a reasoning strategy to decompose a given task into
smaller subtasks, identify the most suitable actions for each subtask, and invoke them. This object is available in API version 60.0 and
later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, Agents must be enabled in your org.


-----

##### Fields

**Field**
```
Capabilities
Description
DeveloperName
Language
MasterLabel
NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A set of tags associated with the agent planner service definition.

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A description explaining the general purpose and domain of the agent planner service
definition.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the GenAiPlannerDefinition. The value for this field is the language value
of the org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the agent planner service definition.

**Type**
string


-----

```
PlannerType

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the GenAiPlannerDefinition.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A particular approach to problem solving that is given as prompt instructions to a large
language model (LLM).

Possible values are:

**•** `AiCopilot__ReAct—Uses a reactive planning strategy to solve problems with the`
LLM. This strategy consists of prompting the LLM to generate the next step in response
to an event and the current context. It differs from a sequential planner in that it doesn’t
plan more than one step ahead of time.

**•** `AiCopilot__SequentialPlannerIntentClassifier—Uses an intent`
classifier prompt and a sequential planner prompt. With each text input, the planner
asks the LLM to generate a step-by-step plan to finish the goal. It plans first, then executes.

