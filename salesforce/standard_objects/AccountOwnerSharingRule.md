#### AccountOwnerSharingRule

Represents the rules for sharing an account with a User other than the owner.

Note: To programmatically update owner sharing rules, we recommend that you use Metadata API. Contact Salesforce customer
support to enable access to this object for your org.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Customer Portal users can't access this object.


-----

##### Fields

**Field**
```
 AccountAccessLevel
 CaseAccessLevel
 ContactAccessLevel
Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value isn’t valid for creating or updating.)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group for all child cases. The
possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A value that represents the type of access granted to the target Group, UserRole, or User for
any associated contacts. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

Note: When DefaultContactAccess is set to Controlled by Parent,
you can’t create or update this field.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
DeveloperName
GroupId
OpportunityAccessLevel
Name

```

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
The ID representing the source group. An Account owned by a User in the source Group
triggers the rule to give access.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group for any associated
Opportunity. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
string


-----

```
 UserOrGroupId

##### Usage

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to Label on the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.


Use this object to manage the sharing rules for accounts. General sharing and territory management-related sharing use this object. For
example, the following code creates an account owner sharing rule between two public groups, which can also contain portal users.
```
AccountOwnerSharingRule rule = new AccountOwnerSharingRule();
rule.setName("RuleName"); // Set the sharing rule name
rule.setDeveloperName("RuleDeveloperName"); // Set the sharing rule developer name
rule.setGroupId("00Gx00000000000"); // Set the group of users to share records from
rule.setUserOrGroupId("00Gx00000000001"); // Set the group of users to share records to
rule.setAccountAccessLevel("Edit");
rule.setOpportunityAccessLevel("Read");
rule.setCaseAccessLevel("None");
connection.create(rule);

```
[Note: The original territory management feature is now unavailable. For more information, see The Original Territory Management](https://help.salesforce.com/articleView?id=The-original-Territory-Management-module-will-be-retired-in-the-Summer-20-release&language=en_US&type=1)
[Module Will Be Retired in the Summer ’21 Release. The information in this topic applies to the original territory management](https://help.salesforce.com/articleView?id=The-original-Territory-Management-module-will-be-retired-in-the-Summer-20-release&language=en_US&type=1)
feature only, and not to Enterprise Territory Management.

SEE ALSO:

Account

AccountShare

_[Metadata API Developer Guide: SharingRules](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)_
