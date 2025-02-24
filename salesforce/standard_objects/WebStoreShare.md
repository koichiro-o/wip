#### WebStoreShare

Represents a sharing entry on a B2B or D2C store. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(),, describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Your Salesforce admin can manage this object using standard Salesforce sharing rules and CRUD access for the WebStore.

##### Fields

```
AccessLevel
ParentId

```

**Type**

**picklist**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing allowed.

Possible values are:

**•** `All—Owner`

**•** `Edit—Read/Write`

**•** `Read—Read Only`

**Type**

**reference**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent folder for the record.

This field is a relationship field.

**Relationship Name**
Parent

**Refers To**
WebStore


-----

```
RowCause

```

**Type**

**picklist**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is Manual. If no value is specified, the field defaults to Manual. All other RowCause
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `ALMAssignmentSharing—Actionable List Member Sharing Rule`

**•** `CompliantDataSharing—Compliant Data Sharing`

**•** `GuestParentImplicit—Associated guest user sharing`

**•** `GuestPersonImplicit—Associated Guest User Sharing`

**•** `GuestRule—Guest User Sharing Rule`

**•** `ImplicitChild—Account Sharing`

**•** `ImplicitParent—Associated record owner or sharing`

**•** `ImplicitPerson—Person Contact`

**•** `LearningAssignment—Learning Assignment Share`

**•** `LearningAssignmentImplicit—Learning Assignment Implicit Share`

**•** `LearningItemAssignment—Learning Item Assignment Share`

**•** `Manual—Manual Sharing`

**•** `MfgTargetShare—Manufacturing Target Sharing Rule`

**•** `ObligationAssigneeShare—Obligation Assignee Share`

**•** `Owner`

**•** `Rule—Sharing Rule`

**•** `SharingRecordCollection—Record Collection`

**•** `SurveyShare—Survey Sharing Rule`

**•** `Team—Sales Team`

**•** `Territory—Territory Assignment Rule`

**•** `Territory2AssociationManual—Territory Manual`

**•** `Territory2Forecast—Territory assignment for forecasting and reporting`

**•** `Territory2SplitsForecast—Territory Splits Share`

**•** `TerritoryManual—Territory Manual`

**•** `TerritoryRule—Territory Sharing Rule`


-----

```
UserOrGroupId
