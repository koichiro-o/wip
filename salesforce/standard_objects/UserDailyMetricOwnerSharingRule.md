#### UserDailyMetricOwnerSharingRule

Represents the rules for sharing the user daily metric with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Sales Engagement must be enabled.

##### Fields

```
AccessLevel
Description
DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines the level of access users have to records. Values are:

**•** `Read` (read only)

**•** `Edit` (read/write)

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the sharing rule. Maximum length is 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a


-----

```
GroupId
Name
UserOrGroupId

##### Usage

```

letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the source group. Records that are owned by users in the source group trigger
the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the sharing rule as it appears in the UI. Maximum length is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that you are granting access to.


Use this object to manage the sharing rules for cases. General sharing and territory management-related sharing use this object.

SEE ALSO:

UserDailyMetric

_[Metadata API Developer Guide: SharingRules](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)_
