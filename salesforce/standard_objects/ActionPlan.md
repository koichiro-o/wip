#### ActionPlan

Represents the instance of an action plan, a set of tasks created from an action plan template. This object is available in API version 44.0
and later.

##### Supported Calls
```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()undelete()update()upsert()

 Fields

```
```
ActionPlanState

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The status of work being done for the action plan.

Possible values are:

**•** `Canceled`


-----

```
ActionPlanTemplateVersionId
ActionPlanType
IsLocked
IsUsingHolidayHours

```


**•** `Complete`

**•** `In Progress`

**•** `Not Started`

The default value is `Not Started.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the version of the action plan template used to create this action plan.
At creation, the referenced action plan template must be in the published state.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The action plan’s type.

Possible values are:

**•** `Industries`

**•** `Sales—This value is available in API version 63.0 and later with the Sales`
Action Plans add-on license and the Sales Action Plans default permission
set.

**•** `Service`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the action plan is locked or not.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether task completion dates have been calculated by incrementing
the task offset for each non-work day, excluding recurring holidays.


-----

```
LastReferencedDate
LastViewedDate
MayEdit
Name
OwnerId
StartDate

```

**Type**
dateTime

**Properties**
Filter, Nllable, Sort

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

Indicates whether the action plan can be edited or not.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the action plan.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The ID of the user who owns this record.

**Type**
date

**Properties**
Create, Default on create, Filter, Group, Sort


-----

```
TargetId

##### Associated Objects

```

**Description**

The start date of the action plan.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the parent object record that relates to this action plan.

For API version 63.0 and later, supported parent objects are Account,
AccountPlanObjective, Applicant, ApplicationForm, ApplicationFormProduct,
Asset, BusinessLicense, BusinessMilestone, Campaign, Case, ChangeRequest,
Claim, Contact, Contract, FinancialGoal, Incident, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent, Problem,
ResidentialLoanApplication, WorkOrder, and WorkOrderLineItem.

For API version 62.0 and later, supported parent objects are
ApplicationFormEvaluation and VettingEvaluation.

For API version 48.0 and later, supported parent objects are Account,
AssetsAndLiabilities, BusinessMilestone, Campaign, Card, Case, Claim, Contact,
Contract, Financial Account, Financial Goal, Financial Holding, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent,
ResidentialLoanApplication, and Visit as well as custom objects with activities
enabled.

For API version 47.0 and later, supported parent objects are Account,
BusinessMilestone, Campaign, Case, Claim, Contact, Contract, InsurancePolicy,
InsurancePolicyCoverage, Lead, Opportunity, PersonLifeEvent, and Visit as well
as custom objects with activities enabled.

For API version 46.0 and later, supported parent objects are Account, Campaign,
Case, Contact, Contract, Lead, and Opportunity as well as custom objects with
activities enabled.

For API version 45.0 and earlier, the only supported parent object is Account.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[ActionPlanOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.financial_services_cloud_object_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ActionPlanShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.financial_services_cloud_object_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


-----
