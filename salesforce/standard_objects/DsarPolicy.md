#### DsarPolicy

Represents a Data Subject Access Request (DSAR) policy created in the Privacy Center managed package. DSAR policies anonymize or
transfer personal data from your org at your customer’s request. This object is available in API version 50.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.

##### Fields

```
Description
DeveloperName

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the policy. The description is limited to 255 characters.

**Type**
string


-----

```
IsActive
Language

```

**Properties**
Filter, Group, Sort

**Description**
Developer name of the policy.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this policy can be used (true) or not (false) for data subject (customer)
requests. The default value is `false.`

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


-----

```
MasterLabel

##### Associated Objects

```


**•** `zh_TW—Chinese (Traditional)`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the policy.


This object has the following associated objects. Unless noted, they are available in the same API version as the object.

**DsarPolicyLog**

Sharing is available for the object.
