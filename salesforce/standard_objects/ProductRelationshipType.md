#### ProductRelationshipType

Defines the relationship between two sales transaction items. For example, defines a relationship between a bundle and a bundle
component. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

 Special Access Rules

```
In version 58.0 and later, this object is available when B2B Commerce, B2C Commerce, or Subscription Management is enabled.

In version 57.0, this object is available when B2B Commerce or B2C Commerce is enabled.

##### Fields

```
AssociatedProductRoleCat

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


-----

```
LastReferencedDate
LastViewedDate
MainProductRoleCat
Name

```

**Description**
The position category that the associated product plays in the relationship.

Possible values are:

**•** `AddOnComponent—The associated product is an add-on.`

**•** `BundleComponent` — The associated product is part of a bundle.

**•** `SetComponent` — The associated product is part of a set.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate), but
not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The position category that the main product plays in the relationship.

Possible values are:

**•** `AddOn—The parent of the add-on.`

**•** `Bundle—The bundle parent.`

**•** `Set—The set parent.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the relationship between two product items.


-----
