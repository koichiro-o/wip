#### ColorDefinition

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the CollabUserEngmtRecordLink object.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabUserEngagementMetric record.


Represents the color-related metadata for a custom tab. This object is available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), query()

```

-----

##### Fields

**Field Name**
```
Color
Context
DurableId
TabDefinitionId
Theme

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The color described in web color RGB format—for example, “00FF00”.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The color context, which determines whether the color is the main color (or
primary) for the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A unique virtual Salesforce ID for the color.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The `TabDefinition` ID.

This is a relationship field.

**Relationship Name**
TabDefinition

**Relationship Type**
Lookup

**Refers To**
TabDefinition

**Type**
string


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**

The icon’s theme.
