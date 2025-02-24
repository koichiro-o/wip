#### BusinessProcessDefinition

Setup object that stores information about stages in a customer lifecycle map. The stages are associated with surveys and questions
created using Salesforce Surveys. This object is reserved for internal use, and is available in API version 49.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
BusinessProcessGroupId
DeveloperName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the customer lifecycle map associated with the stage.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the stage.


-----

```
Language
MasterLabel
ProcessDescription

```

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

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the stage.

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the stage.


-----

```
SequenceNumber

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The position of the stage in the associated customer lifecycle map.

