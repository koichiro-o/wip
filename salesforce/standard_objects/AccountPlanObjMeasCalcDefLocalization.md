#### AccountPlanObjMeasCalcDefLocalization

Represents the translated value of the definition of a target object, rollup field, and logic for calculating the current value of a sales
account plan objective measure. This object is available in API version 63.0 and later when the Translation Workbench is enabled.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted()getUpdated()query(), retrieve(), update(),
upsert()

 Special Access Rules

```
**•** Your organization must be using Lightning Experience with Sales Cloud in Enterprise, Performance, Unlimited, and Einstein 1 Sales
Edition editions.

**•** Translation Workbench must be enabled for your org.

**•** Sales account plans must be turned on.

**•** Users with the Customize Application or Manage Translation permission can create or update AccountPlanObjMeasCalcDef translations.

##### Fields


Language
```
NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language the AccountPlanObjMeasCalcDef is translated into.

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

-----

```
 ParentId
Value

##### Usage

```

The namespace prefix can have one of these values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related account plan objective measure calculation definition. This field is a
relationship field.

**Type**
textarea

**Properties**
Create, Filter, Sort, update

**Description**
The translated label of the account plan objective measure calculation definition.


Translate the labels of your account plan objective measure calculation definitions for supported languages .
