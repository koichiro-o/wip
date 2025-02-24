#### GenAiFunctionDefinition

Represents an agent action. This object is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, Agents must be enabled in your org.

##### Fields

```
Description
DeveloperName
InvocationTarget

```

**Type**
textarea

**Properties**
Create, Update

**Description**
A description explaining the general purpose and domain of the action.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this object.

**Type**
picklist


-----

```
InvocationTargetType
IsConfirmationRequired
IsLocal
Language

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Target invocation used by invocation operations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Invocable action types used by invocation operations.

Possible values are:

**•** `apex`

**•** `flow`

**•** `generatePromptResponse`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether confirmation is required for this action.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is a calculated field and is set to true if this action is an edited version of a standard
action.

The default value is `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the GenAiFunctionDefinition. The value for this field is the language value
of the org.


-----

```
MasterLabel
NamespacePrefix
ParentId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the generative AI action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the GenAiFunctionDefinition.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the object that owns the action.

This field is a relationship field.

**Relationship Name**
Parent

**Refers To**
GenAiPlannerFunctionDef

