#### AccountPlanObjMeasCalcDef

Represents the definition of a target object, rollup field, and logic for calculating the current value of a sales account plan objective
measure. This object is available in API version 63.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
This object is available if sales account plans are turned on.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
A summary of the calculation definition that’s visible to users when they select the definition
for an account plan objective measure.

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

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language of the calculation
definition.

**Type**
string


-----

```
NamespacePrefix
RollupType
Status

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this calculation definition. This display value is the internal label that doesn't get
translated.

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
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The method for calculating the account plan objective measure’s current value from records
that match the calculation definition and any optional conditions.

Possible values are:

**•** `Count`

**•** `Max`

**•** `Min`

**•** `Sum`

In Setup, this field’s label is Calculation Type.

**Type**
picklist


-----

```
TargetField
TargetObject
ValueType

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

Only active calculation definitions are available for users to select when they specify an
account plan objective measure.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The field on `TargetObject` to use for calculating the account plan objective measure’s
current value. Rollup fields on the Campaign, Case, Contact, or Opportunity object are
supported.

In Setup, this field’s label is Rollup Field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object to use for calculating the account plan objective measure’s current value.

Possible values are:

**•** `Campaign`

**•** `Case`

**•** `Contact`

**•** `Opportunity`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The data type for calculating the account plan objective measure’s current value.

Possible values are:

**•** `Currency`


-----

**•** `Number`

**•** `Percent`
