#### CategoryNode

Represents a tree of Solution categories.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
**•** Customer Portal users can't access this object.

**•** Attempting to delete a CategoryNode that has children (referred by CategoryNode.Parent), or is referred to elsewhere, causes a
failure.


-----

##### Fields

**Field**
```
 MasterLabel
ParentId
 SortOrder
 SortStyle

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the category node.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent of this node, if any.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the sort order of child CategoryNode objects.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the sort order is alphabetical or custom.


A CategoryNode defines a category of solutions. In the user interface, you can edit category definitions from Setup by entering Solution
`Categories` in the `Quick Find` box, then selecting Solution Categories.

SEE ALSO:

CategoryData

Solution


-----
