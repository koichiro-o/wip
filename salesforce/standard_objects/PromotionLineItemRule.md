#### PromotionLineItemRule

Lists compound conditions about a promotion. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
AssociatedReferenceId

```

**Type**
Reference


-----

```
AssociatedType
Name
OperatorType

```

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated reference.

**Relationship Name**
AssociatedReference

**Relationship Type**
Lookup

**Refers To**
PromotionQualifier, PromotionTarget

**Type**
Picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies the type of object the rule is associated with.

Possible values are:

**•** `PromotionQualifier`

**•** `PromotionTarget`

**Type**
String

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the promotion rule.

**Type**
Picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Operator type for promotion line item rule.

Possible values are:

**•** `EQUAL_TO`

**•** `GREATER_THAN`

**•** `GREATER_THAN_OR_EQUAL_TO`

**•** `LESS_THAN`

**•** `LESS_THAN_OR_EQUAL_TO`


-----

```
OwnerId
Type
TypeReferenceId

```


**•** `NOT_EQUAL_TO`

The default value is `EQUAL_TO.`

**Type**
Reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
Picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the type on which the rule is being applied.

Possible values are:

**•** `Price`

**•** `Product`

**•** `ProductCategory`

**Type**
Reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the type.

**Relationship Name**
TypeReference

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory


-----

```
TypeValue

```

**Type**
String

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Value of the type selected.

