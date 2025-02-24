#### UserSetupEntityAccess

Represents the enabled custom permissions of the running user. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
DeveloperName
DurableId
KeyPrefix

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the custom permission in the API.

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field isn't used.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first 3 characters of the `SetupEntityId.`


-----

```
LastCacheUpdate
NamespacePrefix
SetupEntityId

##### Usage

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The last modified date and time of the running user's info.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that’s associated with the custom permission. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the custom permission assigned to the user.


API users without the View Setup and Configuration permission can use this object to check their assigned custom permissions.
