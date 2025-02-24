#### ServiceResourceOwnerSharingRule

Represents the rules for sharing a service resource with user records other than the owner or anyone above the owner in the role hierarchy.
This object is available in API version 38.0 and later.


-----

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)

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

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

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

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A service resource owned by a User in the source
Group triggers the rule to give access.


-----

```
Name
ServiceResourceAccessLevel
UserOrGroupId

```

**Type**
string

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
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

