#### LiveChatObjectAccessDefinition

Represents the parent record for one or more LiveChatObjectAccessConfig objects. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, enable Chat. To see the list of objects you can find or create in the UI using this API, enable the "Turns on findOrCreate
in chat API" permission. You can find this permission in the Chat Settings page of the Setup UI.

##### Fields

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter


-----

```
Language
MasterLabel

```


**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language for labels displayed
in an application.

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
Create, Filter, Group, Sort, Update


-----

**Description**
The label for this object's record. This display value is the internal label that doesn’t get
translated.
