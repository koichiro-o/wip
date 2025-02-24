#### NavigationLinkSet

Represents the navigation menu in an Experience Cloud site. A navigation menu consists of items that users can click to go to other
parts of the site. This object is available in API version 35.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```
`create(),` `delete(),` `update(), and` `upsert()` are available in API version 45.0 and later.

##### Special Access Rules

Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.


-----

##### Fields

**Field Name**
```
DeveloperName
Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

Create and Update are available in API version 45.0 and later.

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

Create, Defaulted on create, Nillable, and Update are available in API version 45.0
and later.

**Description**
Language for the navigation menu. Valid values are:

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

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`


-----

```
MasterLabel
NetworkId
