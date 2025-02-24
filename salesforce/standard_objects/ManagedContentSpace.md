#### ManagedContentSpace

Represents the complete instance of a Salesforce CMS workspace that stores managed content. Users and groups with designated
permissions can access and manage the content in a CMS workspace. This object is available in API version 56.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
ManagedContentSpace is available when the Digital Experiences app is enabled.

##### Fields


ApiName


**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique API name of an enhanced Salesforce CMS workspace. Name requirements:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can’t end with an underscore

**•** can’t contain two consecutive underscores


-----

```
DefaultLanguage
Description
LastReferencedDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default language for the Salesforce CMS workspace.

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
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the Salesforce CMS workspace.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name

```

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the Salesforce CMS workspace.

