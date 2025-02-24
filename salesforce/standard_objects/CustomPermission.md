#### CustomPermission

Represents a permission created to control access to a custom process or app, such as sending email. This object is available in API
version 31.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

##### Fields

```
Description
DeveloperName

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the custom permission. Limit: 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the custom permission in the API. This name can contain
only underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The label corresponds
to Name in the user interface. Limit: 80 characters.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no DeveloperName is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.


-----

```
IsLicensed
IsProtected
Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When enabled (true) indicates that the appropriate Salesforce license is required
before accessing the permission. This field is available in API version 50.0 and
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom permission is protected (true) or not (false).
Protected components that have been installed in other organizations can’t be
linked to or referenced by components created in the subscriber organization.
A developer can delete a protected component contained in a managed package
in a future release of the package without worrying about failing installations.
However, after a component is marked as unprotected and is released globally,
the developer can’t delete it. The default value is `false. This field is available`
in API version 50.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the custom permission. Valid values are:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`


-----

```
MasterLabel
NamespacePrefix

##### Usage

```


**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th The Salesforce user interface is fully translated to Thai, but Help is`
in English.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The custom permission label, which corresponds to Label in the user interface.
Limit: 80 characters.

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
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.


Use the CustomPermission object to determine users’ access to custom permissions.


-----

For example, to query all permission sets where the Button1 permission is enabled:
```
SELECT Id, DeveloperName,
(select Id, Parent.Name, Parent.Profile.Name from SetupEntityAccessItems)
FROM CustomPermission
WHERE DeveloperName = 'Button1'

```
To query all permission sets and profiles with custom permissions:
```
SELECT Assignee.Name, PermissionSet.Id,
PermissionSet.Profile.Name,
PermissionSet.isOwnedByProfile,
PermissionSet.Label
FROM PermissionSetAssignment
WHERE PermissionSetId
IN (SELECT ParentId
  FROM SetupEntityAccess
  WHERE SetupEntityType =
'CustomPermission')

```
To query for all SetupEntityAccess rows with custom permissions:
```
SELECT Id,ParentId,Parent.Name, SetupEntityId
FROM SetupEntityAccess
WHERE SetupEntityType='CustomPermission'
AND ParentId
IN (SELECT Id
  FROM PermissionSet
  WHERE isOwnedByProfile = false)

```
SEE ALSO:

CustomPermissionDependency

PermissionSet

Profile

SetupEntityAccess
