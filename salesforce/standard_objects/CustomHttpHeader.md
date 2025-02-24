#### CustomHttpHeader

```


**•** no (Norwegian)

**•** pt_BR (Portuguese (Brazil))

**•** ru (Russian)

**•** sv (Swedish)

**•** th (Thai)

**•** zh_CN (Chinese (Simplified))

**•** zh_TW (Chinese (Traditional))

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The name of the resource. Specify up to 100 characters.

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


Represents a custom HTTP header that provides context information from Salesforce such as region, org details, or the role of the person
viewing the external object. This object is available in API version 43.0 and later.


-----

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
Description
HeaderFieldName
HeaderFieldValue
IsActive
ParentId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A text description of the header field’s purpose.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the header field. The name must contain at least one alphanumeric character or
underscore. It can also include: ! # $ % & ' * + - . ^ _ ` | ~

**Type**
string

**Properties**
Filter, Sort

**Description**
A formula that resolves to the value for the header. The values in the formula must evaluate
to a string. If the formula resolves to null and an empty string, the header isn’t sent.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom HTTP header is available to use.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
ID of the entity that the custom HTTP header is related to.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ExternalDataSource, NamedCredential

##### Usage

For each OData external data source, define up 10 HTTP headers to request data.

Note: HTTP headers aren’t supported on named credentials.
