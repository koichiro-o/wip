#### ProductComponentGroup

Represents the logical grouping of associated products in a bundle and the products’ arrangement policy (group cardinality). This object
is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is available when Industries EPC or Subscription Management is enabled.

##### Fields

```
Description
LastReferencedDate
LastViewedDate
MaxBundleComponents
MinBundleComponents

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Describes the group items of a product bundle feature. For example, a group’s contents can
be the associated products that accompany a main product in a bundle.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a related record or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user indirectly accessed this record (LastReferencedDate), but
not viewed it.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of associated products allowed in a group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Name
OwnerId
ParentProductId
Sequence

```

**Description**
The minimum number of associated products allowed in a group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the product component group. Maximum length is 255 characters (of any type).

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique identifier of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier associated with the main product record.

This field is a relationship field.

**Relationship Name**
ParentProduct

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
int


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the arrangement of the order products when configuring a bundle or set.
