#### ContentTaxonomyTerm

Represents a term in a content taxonomy. Terms describe what content is or how it's used, and they’re organized in parent-child
relationships in the taxonomy hierarchy. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), undelete(), update(), upsert()

 Special Access Rules

```
To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

##### Fields

```
Description
DeveloperName

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the content taxonomy term. This description appears in the API and in the
Content Taxonomy tab in the Digital Experiences App. The maximum length is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique name of the content taxonomy term in the API. This field is unique within your
organization. The name:

**•** must be 80 characters or fewer

**•** must begin with a letter


-----

```
ExternalId
Name

##### Usage

```


**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can't end with an underscore

**•** can't contain 2 consecutive underscores

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The external ID of the content taxonomy term.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content taxonomy term. The name must be between 2 and 255 characters
long.


To include a term in a taxonomy, you must also use the objects ContentTaxonomyRelatedTerm and ContentTaxonomy. If you create
only a ContentTaxonomyTerm, then the term isn’t considered part of the taxonomy, and isn't visible. To relate this term to another term
in your taxonomy, use the object ContentTaxonomyTermRelatedTerm.

SEE ALSO:

ContentTaxonomy

ContentTaxonomyRelatedTerm

ContentTaxonomyTermRelatedTerm
