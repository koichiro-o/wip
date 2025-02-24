#### PermissionSetGroup

Represents a group of permission sets and the permissions within them. Use permission set groups to organize permissions based on
job functions or tasks. Then, you can package the groups as needed. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeObject(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Summer ’20 and later, to view this object, users must have one of these permissions:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

To edit this object, users must have the Manage Profiles and Permission Sets permission.

##### Fields

```
Description

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
DeveloperName
HasActivationRequired
Language

```

**Description**
The Permission Set Group description.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The permission set group name used in the API.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the permission set group requires an associated active session (true) or
not (false). The default value is false. This field is available in API version 53.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The Permission Set Group language.

Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexican)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazilian)

**•** `ru` (Russian)

**•** `sv` (Swedish)


-----

```
MasterLabel
NamespacePrefix
Status

##### Usage

```


**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The permission set group label for the aggregated permissions.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The permission set group namespace prefix.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates permission set group recalculation status.

**•** `Updated. The group is current.`

**•** `Outdated. The group requires recalculation.`

**•** `Updating. The group is in recalculation mode.`

**•** `Failed. The group recalculation failed.`


Use the PermissionSetGroup object to query existing permission set groups and to find which aggregated permissions are included in
the group.

For example, to search for all object permissions in a permission set group named StandardAccountingUsers:
```
SELECT SObjectType
FROM ObjectPermissions
WHERE Parent.PermissionSetGroup.DeveloperName = 'StandardAccountingUsers'

```
To create a permission set group using REST API, you can submit a POST request.


-----
