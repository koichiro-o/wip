#### RelatedListDefinition

```
Represents information about a related list. A related list specifies a set of records for a related object, based on specific criteria. This
object is available in API version 55.0 and later.

##### Supported Calls
```
describeSObjects(), query()

```

-----

##### Special Access Rules

This object is read-only.

##### Fields

**Field**
```
DefaultSort
DurableId
EntityDefinitionId
IsCustomizable

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The default sort string for the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier for the related list. Always retrieve this value before using it, as the value
can change from one release to the next. Simplify queries by using this field instead of making
multiple queries.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the entity containing the related list.

This is a relationship field.

**Relationship Name**
EntityDefinition

**Relationship Type**
Lookup

**Refers To**
EntityDefinition

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
IsDescribable
IsLayoutable
Label
ParentEntityDefinitionId

```

**Description**
Indicates whether columns on the related list can be customized (true) or not (false).

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can appear in describeLayout call results (true)
or not `(false).`

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related list can be assigned to a layout `(true)` or not `(false).`

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the ParentEntityDefinition that’s associated with the rows in the related list.

This is a relationship field.

**Relationship Name**
ParentEntityDefinition

**Relationship Type**
Lookup

**Refers To**
EntityDefinition


-----

```
RelatedListId
RelatedListName

##### Usage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related list.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the related list in the API.


**Find all available related lists for a given entity, for example, an Account record.**
```
  SELECT DurableId, Label, RelatedListName FROM RelatedListDefinition WHERE
  ParentEntityDefinitionId = 'Account'
