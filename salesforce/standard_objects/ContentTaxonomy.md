#### ContentTaxonomy

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user following the tag on the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


Represents a content taxonomy, which is used to classify and organize Salesforce CMS content. To create a hierarchy of terms in a content
taxonomy, use this object in addition to the ContentTaxonomyTerm, ContentTaxonomyRelatedTerm, and
ContentTaxonomyTermRelatedTerm objects. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.


-----

##### Fields

**Field**
```
Description
Language
Name

```
SEE ALSO:

ContentTaxonomyRelatedTerm

ContentTaxonomyTerm


**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the content taxonomy. This description appears in the API and in the Content
Taxonomy tab in the Digital Experiences App. The maximum length is 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content taxonomy.


ContentTaxonomyTermRelatedTerm

ContentTaxonomyTermRelationshipType
