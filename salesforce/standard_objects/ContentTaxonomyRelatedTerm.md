#### ContentTaxonomyRelatedTerm

Represents the relationship between a term and the content taxonomy to which the term belongs. This object is available in API version
63.0 and later.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), undelete()

```

-----

##### Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

##### Fields

```
ContentTaxonomyId
ContentTaxonomyTermId

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
The ID of the term that belongs to the content taxonomy.

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTerm object


-----

##### Usage

To include a term in a taxonomy, you must use this object in addition to the ContentTaxonomyTerm and ContentTaxonomy objects.

SEE ALSO:

ContentTaxonomy

ContentTaxonomyTerm
