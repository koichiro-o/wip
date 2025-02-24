#### ApexClass

```
Represents an Apex class.

##### Supported Calls


**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
```
  00530000009M943.

```
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search()update(), upsert()

##### Fields

```
```
ApiVersion
Body
BodyCrc

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this class. Every class has an API version specified at creation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Apex class definition.

Limit: 1 million characters.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update


-----

```
IsValid
LengthWithoutComments
Name
NamespacePrefix

```

**Description**
The CRC (cyclic redundancy check) of the class or trigger file.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether any dependent metadata has changed since the class was last compiled
(true) or not (false). The default value is `false.`

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Length of the class without comments.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Name of the class.

Limit: 255 characters

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


-----

```
Status

##### Usage

```


**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The current status of the Apex class. The following string values are valid:

**•** `Active—The class is active.`

**•** `Deleted—The class is marked for deletion. This is useful for managed packages,`
because it allows a class to be deleted when a managed package is updated.

**•** `Inactive—This option is unused and is only supported for ApexTrigger. For more`
[information, see the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/)


Although Apex classes and triggers have the Create and Update field properties, a runtime exception occurs if you try to create, update,
or delete them using the API. Instead, use the Salesforce Extensions for Visual Studio Code or the Ant Migration Tool to create or update
[Apex classes or triggers. Apex classes and triggers can’t be created, edited, or deleted in a production org. See Deploying Apex.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_deploying.htm)

SEE ALSO:

ApexTrigger

_[Developer Guide: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/)_
