#### BrandingSet

Represents the definition of a set of branding properties for an Experience Builder site, as defined in the Theme panel in Experience
Builder. This object is available in API version 40.0 and later.

##### Supported Calls

create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

##### Special Access Rules

The BrandingSet type is available when at least one of the following is enabled in your org: Digital Experiences, Surveys, or Lightning
Experience. All users, including unauthenticated guest users, can access this type.

##### Fields

```
Description
DeveloperName
Language
MasterLabel

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the set of branding properties.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. API name of the BrandingSet object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the branding set.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
NamespacePrefix
