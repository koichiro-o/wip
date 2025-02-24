#### EnablementProgramDefinition

Represents Enablement program information in Metadata API. This object is available in API version 61.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.


-----

##### Fields

**Field**
```
DeveloperName
EnablementProgramId
Language
MasterLabel

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Enablement program to reference in Metadata API.

This field is a relationship field.

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string


-----

```
NamespacePrefix

```

**Properties**
Filter, Group, Sort

**Description**
Label for this EnablementProgramDefinition value. This display value is the internal label
that doesn't get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
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

**•** In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Available in API version 62.0 and later.

