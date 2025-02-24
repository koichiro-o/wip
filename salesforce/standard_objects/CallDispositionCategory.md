#### CallDispositionCategory

Represents the call outcome of a phone call that is used in reports and branching criteria for cadences. This object is available in API
version 47.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
Category

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


-----

```
DeveloperName
Language

```

**Description**
The name of the call outcome.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the call category.

Possible values are:

**•** `da—Danish`

**•** `de—German`

**•** `en_US—English`

**•** `es—Spanish`

**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`

**•** `ja—Japanese`

**•** `ko—Korean`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`


-----

```
 MasterLabel
