#### AIApplication

Represents an AI application such as Einstein Prediction Builder. This object is available in API version 50.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
DeveloperName
Language

```

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


-----

```
MasterLabel
NamespacePrefix
Status

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the application. Possible values are:

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
Label that identifies the AI application throughout the Salesforce user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the application if installed with a managed package.

**Type**
picklist


-----

```
Type
