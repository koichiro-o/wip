#### BusinessProcessGroup

Setup object that stores information about customer lifecycle maps. Customer lifecycle maps are used to track the scores provided by
customers across their lifecycle using Salesforce Surveys. This object is reserved for internal use, and is available in API version 49.0 and
later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
CustomerSatisfactionMetric
Description

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents the question type that measures the customers' Net Promote Score or satisfaction
score across their lifecycle.

Possible values are:

**•** `NPS`

**•** `Rating`

**Type**
textarea


-----

```
DeveloperName
Language

```

**Properties**
Nillable

**Description**
Description of the customer lifecycle map.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name the customer lifecycle map.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the MasterLabel.

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

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`


-----

```
MasterLabel
