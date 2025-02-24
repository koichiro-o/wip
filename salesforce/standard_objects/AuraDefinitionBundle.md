#### AuraDefinitionBundle

Represents a Lightning Aura component definition bundle, such as a component or application bundle. A bundle contains a Lightning
Aura component definition and all its related resources. This object is available in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
ApiVersion
Description
DeveloperName

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this bundle. Every bundle has an API version specified at
creation.

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text description of the bundle. Maximum size of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the record in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is automatically generated but you can supply
your own value if you create the record using the API.


-----

```
Language
MasterLabel
NamespacePrefix

```

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no DeveloperName is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the MasterLabel.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Master label for the Lightning bundle. This internal label doesn’t get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.


-----

##### Usage

[For more information, see the Lightning Aura Components Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.lightning.meta/lightning/)
