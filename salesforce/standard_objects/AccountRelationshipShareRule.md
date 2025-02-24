#### AccountRelationshipShareRule

Represents the rule that determines which object records are shared, how they are shared, the account relationship type that shares the
records, and the level of access granted to the records. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(). describeSObjects(), query(), retrieve(), update(). upsert()

 Fields

```
```
AccessLevel
AccountToCriteriaField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of access granted by the share rule. Valid values are:

**•** `Read` (Read Only)

**•** `Edit` (Read/Write)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Criteria that must be met for the data to be shared.

Possible values are:

**•** `Account.OwnerId`

**•** `Account.ParentId`

**•** `Campaign.OwnerId`

**•** `Case.AccountId`

**•** `Case.OwnerId`

**•** `Contact.AccountId`


-----

```
Description
DeveloperName

```


**•** `Contact.OwnerId`

**•** `Lead.ConvertedAccountId`

**•** `Lead.OwnerId`

**•** `Lead.PartnerAccountId`

**•** `Opportunity.AccountId`

**•** `Opportunity.OwnerId`

**•** `Opportunity.PartnerAccountId`

**•** `Order.AccountId`

**•** `Order.ActivatedById`

**•** `Order.CompanyAuthorizedById`

**•** `Order.OwnerId`

**•** `PartnerFundAllocation.CreatedById`

**•** `PartnerFundAllocation.ChannelPartnerId`

**•** `PartnerFundAllocation.OwnerId`

**•** `PartnerFundClaim.CreatedById`

**•** `PartnerFundClaim.OwnerId`

**•** `PartnerFundRequest.ChannelPartnerId`

**•** `PartnerFundRequest.CreatedById`

**•** `PartnerFundRequest.OwnerId`

**•** `PartnerMarketingBudget.CreatedById`

**•** `PartnerMarketingBudget.ChannelPartnerId`

**•** `PartnerMarketingBudget.OwnerId`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A meaningful explanation of the sharing rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the record in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
This field is automatically generated but you can supply your own value if you create the
record using the API.


-----

```
EntityType
Language
MasterLabel
NamespacePrefix

```

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of data shared by this rule. Values are:

**•** `Account`

**•** `Campaign`

**•** `Case`

**•** `Contact`

**•** `Lead`

**•** `Opportunity`

**•** `Order`

**•** `PartnerFundAllocation`

**•** `PartnerFundClaim`

**•** `PartnerFundRequest`

**•** `PartnerMarketingBudget`

**Type**
picklist

**Properties**
Create, Defaulted on create. Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the account relationship share rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label assigned to the sharing rule to identify it.

**Type**
string


-----

```
StaticFormulaCriteria
Type
