#### BrandTemplate

```
Letterhead for HTML EmailTemplate.

##### Supported Calls


**Description**
Required. The user-facing label of the set of branding properties.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix with a 15 character limit. You
can refer to a component in a managed package by using
the namespacePrefix__componentName notation. The namespace prefix can have
one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix. `NamespacePrefix is null if the publisher is Salesforce.`

```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

##### Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
Description

```

**Type**
string


-----

```
DeveloperName
IsActive
Name
NamespacePrefix

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the letterhead. Limited to 1000 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is Letterhead Unique Name.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the letterhead is available for use (true) or not (false). Label is Active.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the template as it appears in the user interface. Limited to 255 characters. Label is
**Brand Template Name.**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can


-----

```
 Value

##### Usage

```

refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
textarea

**Properties**
Create, Update

**Description**
The contents of the letterhead, in HTML, including any logos.


Use this object to brand EmailTemplate records with your letterhead. You can also set a brand template to active or inactive. For example,
if you have five different marketing brands, you can maintain each different brand in one template, and assign to the appropriate
EmailTemplate.

SEE ALSO:

EmailTemplate
