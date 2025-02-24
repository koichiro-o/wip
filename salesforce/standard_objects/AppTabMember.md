#### AppTabMember

Represents the list of tabs for each of the available apps. This object is available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
AppDefinitionId
DurableId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The ID of the `AppDefinition` object.

This is a relationship field.

**Relationship Name**
AppDefinition

**Relationship Type**
Lookup

**Refers To**
AppDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
SortOrder
TabDefinitionId
WorkspaceDriverField

```

**Description**

A unique virtual Salesforce ID for the color.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number used to sort this tab in the application.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The ID of the `TabDefinition` object.

This is a relationship field.

**Relationship Name**
TabDefinition

**Relationship Type**
Lookup

**Refers To**
TabDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Refers to the workspace mapping in the `CustomApplication Metadata`
API object.

