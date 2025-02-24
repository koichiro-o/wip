#### CategoryData

Represents a logical grouping of Solution records.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
CategoryNodeId
IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the CategoryNode associated with the solution.

**Type**
boolean

**Properties**
Defaulted on create, Filter


-----

```
 RelatedSobjectId

##### Usage

```

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the solution related to the category.


This object allows you to assign one or more categories to a Solution. It is an intermediate data table with two foreign keys that defines
the relationship between a CategoryNode and a Solution record.

CategoryData has two foreign keys:

**•** The first foreign key, `CategoryNodeId, refers to the ID of a CategoryNode.`

**•** The other foreign key, `RelatedSobjectId, refers to a Solution ID.`

This is a many-to-many relationship, so there can be multiple rows returned with a `CategoryNodeId. A Solution can be associated`
with multiple categories.

SEE ALSO:

Overview of Salesforce Objects and Fields
