#### AccountTerritorySharingRule

Represents the rules for sharing an Account within a territory.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Customer Portal users can’t access this object.

##### Fields

```
AccountAccessLevel
CaseAccessLevel
ContactAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target group for all child cases of
the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A value that represents the type of access granted to the target group for all related contacts
on the account. The possible values are:

**•** `None`

**•** `Read`


-----

```
Description
DeveloperName
GroupId
Name

```


**•** `Edit`

Note: This field is read only.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available in
API version 29.0 and later.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to Rule Name in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Accounts owned by users in the source territory trigger
the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to Label on the user interface.


-----

```
OpportunityAccessLevel
UserOrGroupId

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target group for all opportunities
associated with the account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the user or group being given access, or, if a territory ID, the users assigned
to that territory.


Use this object to manage the sharing rules for a particular object. General sharing and territory-related sharing use this object.

SEE ALSO:

Account

AccountShare
