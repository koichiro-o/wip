#### CampaignInfluence

Represents the association between a campaign and an opportunity in Customizable Campaign Influence. This object is available in API
version 37.0 and later.


-----

[Note: This information applies only to Customizable Campaign Influence and not to Campaign Influence 1.0 .](https://help.salesforce.com/s/articleView?id=sf.campaigns_influence_original.htm&language=en_US)

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, Customizable Campaign Influence must be enabled. Customer Portal users can’t access this object.

##### Fields

```
CampaignId
CampaignMemberId
ContactId
Influence

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the campaign that’s related to the opportunity.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the campaign member related to the opportunity. Not available in the
UI.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the contact on the associated opportunity.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update


-----

```
ModelId
OpportunityContactRoleId
OpportunityId
RevenueShare

##### Usage

```

**Description**

The percentage of the Amount field for the related opportunity that’s attributed
to the campaign.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the campaign influence model that’s related to the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The opportunity contact role ID of the related opportunity. Not available in the
UI.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related opportunity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of revenue from the related opportunity attributed to the campaign.


Use this object to create campaign influence records for your custom campaign influence models. Don’t create campaign influence
records for the Primary Campaign Source model. Records added to the Primary Campaign Source model via the API are deleted when
the model is recalculated.


-----
