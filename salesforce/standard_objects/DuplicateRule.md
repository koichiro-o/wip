#### DuplicateRule

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of record items in the set.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ParentId represents the parent of a duplicate rule or duplicate job. A ParentId is polymorphic.
The label is Parent. This field is available in API versions 42.0 and later.


Represents a duplicate rule for detecting duplicate records.

##### Supported Calls
```
describeSObjects(), describeLayout(), query(), retrieve(), search()

 Special Access Rules

```
As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

##### Fields

```
DeveloperName
IsActive

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name for the duplicate rule.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean


-----

```
Language
LastViewedDate
MasterLabel
NamespacePrefix

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a duplicate rule is active (true) or not (false). This field is
read only.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language for the duplicate rule.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. This
field is available in API version 41.0 or later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the duplicate rule.

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


-----

```
SobjectSubtype
sObjectType

##### Usage

```

installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The subtype of object the duplicate rule is defined for. This field is available in
API version 39.0 or later.

Possible values are:

**•** `None`

**•** `PersonAccount`

The default value is `None.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of object the duplicate rule is defined for.

Possible values are:

**•** `Account`

**•** `Contact`

**•** `Individual`

**•** `Lead`


You can use the API to view a duplicate rule’s details. To create, edit, or delete duplicate rules, use the UI.

Use DuplicateRule to get the sObject type.

DuplicateRule is unavailable in some orgs.
