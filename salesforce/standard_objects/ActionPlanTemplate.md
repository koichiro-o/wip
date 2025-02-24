#### ActionPlanTemplate

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of this action plan item.


Represents the instance of an action plan template. This object is available in API version 44.0 and later.

##### Supported Calls
```
create()delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(), undelete(), update(), upsert(),

 Fields

```
```
ActionPlanType
Description

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

This action plan template’s type. Possible values are:

**•** `Industries`

**•** `Sales—This value is available in API version 63.0 and later with the Sales`
Action Plans add-on license and the Sales Action Plans default permission
set.

**•** Service

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The description of this action plan template.


-----

```
IsAdHocItemCreationEnabled
IsLocked
LastReferencedDate
LastViewedDate
MayEdit
Name

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users can add tasks or other items to generated action plans
(true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template is locked or not. The default value is
```
  false.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user referenced this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date on which a user viewed this record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this action plan template can be edited or not. The default
value is `false.`

**Type**
string


-----

```
OwnerId
Status
TargetEntityType

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of this action plan template.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user who owns this action plan template. This field is a polymorphic
relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The status of this action plan template.

Possible values are:

**•** `Draft`

**•** `Final—Published`

**•** `Obsolete`

**•** `ReadOnly`

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Restricted picklist, Sort

**Description**

The parent object this action plan template relates to.

Possible values are organized by the API version in which they were introduced.
Values are available in all versions after introduction unless noted otherwise.

API Version 62.0 and later with Financial Services:

**•** `AccountPlanObjective`


-----

**•** `FinancialDeal`

**•** `PartyProfile`

API Version 62.0 and later with Public Sector Solutions:

**•** `ApplicationFormEvaluation`

**•** `VettingEvaluation`

API version 60.0 and later with Education Cloud

**•** `ProgramEnrollment`

API version 58.0 and later with Health Cloud

**•** `CareBarrier`

API version 58.0 and later with Nonprofit Cloud:

**•** `Benefit`

**•** `Program`

API Version 58.0 and later with Public Sector Solution and Education Cloud:

**•** `ApplicationDecision`

**•** `ApplicationReview`

**•** `Benefit`

**•** `Program`

API Version 56.0 and later with Automotive Cloud:

**•** `Account`

**•** `Asset`

**•** `Asset Account Participant`

**•** `Asset Contact Participant`

**•** `Asset Milestone`

**•** `Fleet`

**•** `Lead`

**•** `Opportunity`

**•** `Record Alert`

**•** `Vehicle`

**•** `Case`

**•** `Claim`

**•** `Contact`

API Version 58.0 and later with Grantmaking:

**•** `ApplicationDecision`

**•** `ApplicationReview`

**•** `Benefit`

**•** `Budget`

**•** `BudgetAllocation`


-----

```
UniqueName

```


**•** `CareBarrier`

**•** `FundingAward`

**•** `FundingAwardAmendment`

**•** `FundingAwardRequirement`

**•** `FundingDisbursement`

**•** `FundingOpportunity`

**•** `Program`

API Version 52.0 and later:

**•** `BusinessLicenseApplication`

**•** `IndividualApplication`

**•** `PublicComplaint`

**•** `RegulatoryCodeViolation`

**•** `ViolationEnforcementAction`

API Version 47.0 and later:

**•** `BusinessMilestone`

**•** `Claim`

**•** `InsurancePolicy`

**•** `InsurancePolicyCoverage`

**•** `PersonLifeEvent`

**•** `Visit`

API Version 46.0 and later:

**•** `Campaign—Unsupported for Grantmaking.`

**•** `Case`

**•** `Contact`

**•** `Contract`

**•** `Lead`

**•** `Opportunity`

**•** `Custom objects with activities enabled`

API Version 44.0 and later:

Account

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for this action plan template. This field is unique within your
organization.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanTemplateOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.financial_services_cloud_object_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanTemplateShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.financial_services_cloud_object_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
