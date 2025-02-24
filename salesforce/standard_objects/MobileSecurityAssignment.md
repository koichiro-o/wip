#### MobileSecurityAssignment

Represents the assignment of mobile security policies to a profile. The policies apply to the Salesforce mobile app with Enhanced Mobile
App Security enabled. This object is available in API version 54.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

##### Fields

```
DeveloperName
Language
MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

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
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language of the
MobileSecurityAssignment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
NamespacePrefix
ProfileId

```

**Description**
Label for this MobileSecurityAssignment value. This display value is the internal label that
doesn't get translated.

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

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The profile ID that the mobile security policies are assigned to.

This field is a relationship field.

**Relationship Name**
Profile

**Refers To**
Profile

