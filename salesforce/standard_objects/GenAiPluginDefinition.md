#### GenAiPluginDefinition

Represents an agent topic, which is a category of actions related to a particular job to be done by AI agents. This object is available in
API version 62.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, Agents must be enabled in your org.

##### Fields

```
Description

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The description of the topic.


-----

```
DeveloperName
IsLocal
Language
MasterLabel
NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the API name of the topic. Can contain only underscores and alphanumeric
characters and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field is a calculated field and is set to true if this topic is an edited version of a standard
topic.

The default value is `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the topic.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the topic.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of these values.


-----

```
ParentId
PluginType
Scope
