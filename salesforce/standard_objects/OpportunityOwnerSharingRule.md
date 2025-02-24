#### OpportunityOwnerSharingRule

Represents a rule for sharing an opportunity with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Fields

```
```
Description
DeveloperName
GroupId
Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to Rule Name in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Opportunities owned by users in the source
group trigger the rule to give access.

**Type**
string


-----

```
OpportunityAccessLevel
UserOrGroupId

##### Usage

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to Label on the user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group. The target user or group is being given
access.


Use this object to manage the sharing rules for opportunities. General sharing and Territory-related sharing use this object.

SEE ALSO:

Case

_[Metadata API Developer Guide: SharingRules](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)_
