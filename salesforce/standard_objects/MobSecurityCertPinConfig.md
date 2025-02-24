#### MobSecurityCertPinConfig

Configuration of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available
in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

##### Fields

```
CertificateHash
DeveloperName
DomainName
IsEnabled
IsSubdomainIncluded

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique identifier for the certificate.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the domain.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The default value is False.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The default value is False.


-----

```
Language
MasterLabel
MobilePlatform
MobileSecurityAssignmentId
NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The two-to five-character code that represents the language and locale ISO.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the mobile security pin.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The mobile operating system.

Possible values are:

**•** `Android`

**•** `iOS`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the ID of the mobile security assignment.

This is a relationship field.

**Relationship Name**
MobileSecurityAssignment

**Relationship Type**
Lookup

**Refers To**
MobileSecurityAssignment

**Type**
string


-----

```
SeverityLevel
Type

```

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

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The severity level of a mobile security policy.

Possible values are:

**•** `Critical`

**•** `Error`

**•** `Info`

**•** `Warn`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of pin

Possible values are:

**•** `AuthServer—Authentication Server`

**•** `Resource—Resource`


-----
