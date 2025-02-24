#### DsarPolicyLog

Represents the history of Data Subject Access Request (DSAR) policy execution requests. This log records the status and results of executed
DSAR policies for a customer. This object is available in API version 50.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.

##### Fields

```
CompletionDateTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the data subject access request was completed. Available in API
version 51.0 and later.


-----

```
DataSubjectId
DeletedDateTime
DeveloperName
DownloadedDateTime
DsarError

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15–18 character ID of the data subject making the request. Available in API version 51.0
and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the file generated for the data subject’s request is deleted. Available
in API version 51.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the policy.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date and time when the data subject downloaded the file generated at
their request. Available in API version 51.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents an error in generating the file for the data subject access request. Available in
API version 51.0 and later.


-----

```
DsarPolicyId
FileURL
Language

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the DSAR policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the DSAR policy execution. The URL links to a downloadable file that contains
the customer data.

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
RequestDateTime
RequestStatus
RequestUserId

```


**•** `zh_TW—Chinese (Traditional)`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the policy.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when a data subject requested access to their data in the org. Available
in API version 51.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the policy execution.

Possible values are:

**•** `Complete`

**•** `Deleted`

**•** `Downloaded`

**•** `Expired`

**•** `Failed`

**•** `In Progress`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the org employee or admin making the request on behalf of the data subject.
Available in API version 51.0 and later.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as the object.

**DsarPolicy**

Sharing is available for the object.
