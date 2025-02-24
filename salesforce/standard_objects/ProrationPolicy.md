#### ProrationPolicy

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

**•** In orgs that aren't Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the in-app guidance.

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The actual translated label of the in-app guidance.


Defines how the price of a subscription is divided into time periods and how the price is calculated for each time period. This object is
available in API version 55.0 and later.

The proration policy defines whether partial periods are allowed and how remainder amounts are handled.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search()

 Special Access Rules

```
This object is available when Subscription Management is enabled.


-----

##### Fields

**Field**
```
ArePartialPeriodsAllowed
LastReferencedDate
LastViewedDate
Name
ProrationPolicyType

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a subscription can be canceled partway through a period.

Set the value to True if a subscription can be canceled partway through a period. Otherwise,
set the value to `false.`

For example, if the proration period is monthly and this field is `true, then customers can`
cancel a subscription partway through the month. If the proration period is monthly and
this field is `false, then the subscription is canceled at the end of the current month.`

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list viewLastReferencedDate but
not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the proration policy.

**Type**
picklist


-----

```
RemainderStrategy
