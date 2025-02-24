#### DataWeaveResource

Represents the DataWeaveScriptResource class that is generated for all DataWeave scripts. This object is available in API version 58.0
and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update()

 Fields

```
```
ApiVersion
BodyLength

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The API version of this component.

**Type**
int


-----

```
ContentType
DeveloperName
IsGlobal
IsProtected
Language

```

**Properties**
Filter, Group, Sort

**Description**
Size of the DataWeave script (in bytes).

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Possible value:

**•** `dwl: The metadata file for the DataWeave scripts that are deployed to an org.`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When set to true, the generatedDataWeaveScriptResource class is global. The
default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Not used

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the MasterLabel.


-----

```
MasterLabel
NamespacePrefix

##### Usage

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The name of the resource.

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


Although the `DataWeaveResource` object supports the create and update field properties, a runtime exception occurs if you try
to create, update, or delete using the API. Instead, use the Salesforce Extensions for Visual Studio Code.
