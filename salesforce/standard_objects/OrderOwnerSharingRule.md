#### OrderOwnerSharingRule

Represents a rule which determines order sharing access for the order’s owners.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
CreatedById
CreatedDate
Description
DeveloperName
GroupId

```

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the creator of the order owner sharing rule.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date when the order owner sharing rule was created.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the order owner sharing rule. Maximum length is 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the developer of the order owner sharing rule.

**Type**
reference


-----

```
Id
LastModifiedById
LastModifiedDate
Name
OrderAccessLevel
SystemModstamp

```

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group whose orders are shared.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**
ID of the order owner sharing rule.

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the user who last modified the order owner sharing rule.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date when the order owner sharing rule was last modified.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**
Name of the order owner sharing rule. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Access level for the order owner sharing rule.

**Type**
dateTime


-----

```
UserOrGroupId

##### Usage

```

**Properties**
Defaulted on create, Filter, Sort

**Description**
System modification time for the order owner sharing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group with whom order access is shared.


Use this object to manage the sharing rules for orders. For example, the following code creates an order owner sharing rule between
two public groups, which can also contain portal users.
```
OrderOwnerSharingRule rule = new OrderOwnerSharingRule();
rule.setName("RuleName"); // Set the sharing rule name
rule.setDeveloperName("RuleDeveloperName"); // Set the sharing rule developer name
rule.setGroupId("00Gx00000000000"); // Set the group of users to share records from
rule.setUserOrGroupId("00Gx00000000001"); // Set the group of users to share records to
rule.setOrderAccessLevel("Edit");
connection.create(rule);

```
SEE ALSO:

_[Metadata API Developer Guide: SharingRules](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)_
