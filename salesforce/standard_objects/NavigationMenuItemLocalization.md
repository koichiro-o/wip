#### NavigationMenuItemLocalization

Represents the translated value of a navigation menu item in an Experience Cloud site. This object is available in API version 36.0 and
later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.


-----

##### Fields

**Field Name**
```
Language
NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The language of the translated navigation menu item. The picklist contains the
following supported languages:

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

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th The Salesforce user interface is fully translated to Thai, but Help is`
in English.

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


-----

```
ParentId
Value
