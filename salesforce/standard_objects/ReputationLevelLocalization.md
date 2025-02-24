#### ReputationLevelLocalization

Represents the translated value of a reputation level. Reputation level localization only applies for reputation levels in Experience Cloud
sites. This object is available in API version 35.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
This object is available only if digital experiences is enabled in your org and reputation is enabled in your Experience Cloud site.

##### Fields

```
Language

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The language the reputation level is translated into. The picklist contains the
following fully-supported languages:

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


-----

```
NamespacePrefix
ParentId
Value
