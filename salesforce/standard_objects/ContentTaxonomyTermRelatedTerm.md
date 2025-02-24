#### ContentTaxonomyTermRelatedTerm

Represents the relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete()

```

-----

##### Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

##### Fields

```
ContentTaxonomyId
ContentTaxonomyTermId
ContentTaxonomyTrmRelaTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the content taxonomy to which the term belongs.

This field is a relationship field.

**Relationship Name**
ContentTaxonomy

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomy object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the primary term that has a relationship with another term.

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTerm object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the type of relationship between the two taxonomy terms.


-----

```
RelatedContentTaxonomyTermId

##### Usage

```

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTrmRelaType

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTermRelationshipType object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the term that is related to the primary term.

This field is a relationship field.

**Relationship Name**
RelatedContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTerm object


To relate a term to another term in a content taxonomy, use this object in addition to the ContentTaxonomyTerm object. This object
can’t be updated. You can only create and delete it.

SEE ALSO:

ContentTaxonomyTerm
