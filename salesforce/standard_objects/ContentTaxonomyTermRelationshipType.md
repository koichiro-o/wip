#### ContentTaxonomyTermRelationshipType

Represents the type of relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To view this object, users need the permission View Content Taxonomy enabled.


-----

##### Fields

**Field**
```
ContentTaxonomyTrmRelaCatg
Description
Name

##### Usage

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Category of the relationship type.

Possible values are:

**•** `HasBroader`

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the relationship type.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the relationship type.


ContentTaxonomyRelationshipType can’t be created, updated, or deleted. In API version 63.0, the default category for the relationship
type is HasBroader.
