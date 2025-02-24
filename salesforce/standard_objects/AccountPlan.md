#### AccountPlan

Represents customer information with measurable objectives and executable steps to proactively manage and grow customer relationships.
This object is available in API version 62.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
This object is available if sales account plans are turned on.

##### Fields

```
AccountChallenges
AccountCmptvWeaknesses

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The key obstacles to the growth of the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The shortcomings that hinder the account’s ability to outperform competitors in the market.


-----

```
AccountCompetitiveStrengths
AccountCompetitors
AccountId
AccountIndustryTrends
AccountInternalRiskRating

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The abilities of the account to outperform their competitors in the market.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The businesses or companies that offer similar products or services and compete for the
same target market as the account.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Account record.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The shifts in the pattern of the industry that are specific to the account.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The rating that’s assigned to assess the risk level of the account. To access this field, you must
have an FSC Sales or a Financial Services Cloud Extension license.


-----

```
AccountPrfmIndicators
AccountStrategicPriorities
AccountVision
CallingStrategy
CallingStrategyNotes
EndDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The key performance indicators used by the account to measure the success and effectiveness
of a product or service.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The key priorities of the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The long-term value statement of the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
How frequently the relationship team meets with the account. To access this field, you must
have an FSC Sales or a Financial Services Cloud Extension license.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The outline of the format and organization of account meetings. To access this field, you
must have an FSC Sales or a Financial Services Cloud Extension license.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
FlexCard
LastReferencedDate
LastViewedDate
Name
Notes

```

**Description**
The end date of the account plan.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Omnistudio FlexCard. To access this field, you must have an FSC Sales or a Financial
Services Cloud Extension license.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly. For example,
accessed through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate isn’t null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the account plan.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The notes or observations for the account plan.


-----

```
OwnerId
RelationshipOpportunities
RelationshipStrengths
RelationshipSummary
RelationshipThreats

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the account plan.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The list of sales or potential deal opportunities in the relationship with the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The strengths in the relationship with the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A concise overview of the relationship dynamics with the account. To access this field, you
must have an FSC Sales or a Financial Services Cloud Extension license.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The possible concerns in the relationship with the account.


-----

```
RelationshipWeaknesses
StartDate
Status

##### Associated Objects

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The shortcomings in the relationship with the account.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the account plan.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of the account plan.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `Not Started`

The default value is `Not Started.`


This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountPlanChangeEvent on page 67**
Change events are available for the object.

**AccountPlanOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AccountPlanShare on page 66**
Sharing is available for the object.


-----
