#### ChannelObjectLinkingRule

Represents a rule for linking a channel interaction with an object (such as Lead or Contact). This object is available in API version 47.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field**
```
 ActionForNoRecordFound
 ActionForSingleRecordFound
 ChannelType
 Description

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Action to take when no matching records are found.

Possible values are:

**•** `CreateNewRecordAndLink—Create Record and Link (Recommended)`

**•** `PromptAgent—Prompt Agent`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Action to take when one matching record is found.

Possible values are:

**•** `AutoLink—Auto-Link Record (Recommended)`

**•** `PromptAgent—Prompt Agent`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of channel used for this rule.

Possible values are:

**•** `FacebookMessenger`

**•** `Phone`

**•** `Text`

**•** `WeChat`

**•** `WhatsApp`

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
DeveloperName
IsLinkedRecordOpenedAsSubTab
IsRuleActive
Language

```

**Description**
The description for this linking rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to open the linked record as a subtab when the link is established.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the rule is active.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this linking rule.

Possible values are:


-----

```
MasterLabel

```


**•** `ar—Arabic`

**•** `bg—Bulgarian`

**•** `cs—Czech`

**•** `da—Danish`

**•** `de—German`

**•** `el—Greek`

**•** `en_GB—English (UK)`

**•** `en_US—English`

**•** `es—Spanish`

**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `hr—Croatian`

**•** `hu—Hungarian`

**•** `in—Indonesian`

**•** `it—Italian`

**•** `iw—Hebrew`

**•** `ja—Japanese`

**•** `ko—Korean`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pl—Polish`

**•** `pt_BR—Portuguese (Brazil)`

**•** `pt_PT—Portuguese (European)`

**•** `ro—Romanian`

**•** `ru—Russian`

**•** `sk—Slovak`

**•** `sl—Slovene`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `tr—Turkish`

**•** `uk—Ukrainian`

**•** `vi—Vietnamese`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
string


-----

```
 ObjectToLink
 RuleName
