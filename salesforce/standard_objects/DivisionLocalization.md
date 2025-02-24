#### DivisionLocalization

When the Translation Workbench is enabled for your organization, the DivisionLocalization object provides the translation of the label
for a division.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
**•** Your organization must be using Professional, Enterprise, Developer, Unlimited, or Performance Edition and be enabled for the
Translation Workbench.

**•** To view this object, you must have the “View Setup and Configuration” permission.

##### Fields

```
Language
NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**
The language for this translated label.

**Type**
string

**Properties**
Filter, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```

-----

```
 ParentId
 Value

##### Usage

```

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the Division associated with the label that is being translated.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated label for the division. Label is Translation.


Use this object to translate the labels of your divisions into the different languages supported by Salesforce.
