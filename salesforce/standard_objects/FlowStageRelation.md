#### FlowStageRelation

```

**Properties**
Filter, Nillable, Sort

**Description**
The ID of the flow definition associated with the flow test view.

This is a relationship field.

**Relationship Name**
FlowDefinitionView

**Relationship Type**
Lookup

**Refers To**
FlowDefinitionView

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the flow test associated with the flow test view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label of the flow test associated with the flow test view.


Represents a relationship between a paused flow interview and its stages. When a flow interview is paused, Salesforce creates a
FlowStageRelation record for each stage that’s set to the `$Flow.CurrentStage` or `$Flow.ActiveStages` global variable.
Available in API version 43.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), undelete()

```

-----

##### Fields

**Field**
```
 Name
 ParentId
 StageLabel
 StageOrder

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of this relation.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The flow interview that the record is related to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
FlowInterview

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Label for the stage. If the stage is translated, the label respects the language of the user who
is querying the label.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The order of this stage when the flow interview was paused. This order may differ from the
order in the stage definition.

**•** If the type is Active, the order corresponds to the order of the stage in
```
   $Flow.ActiveStages.

```

-----

```
 StageType

##### Usage

```


**•** If the type is Current and corresponds to an active stage, the order matches the order of
the active stage.

**•** If the type is Current and doesn't correspond to an active stage, the order is 0.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of stage. The valid values are:

**•** Current: Identifies that the stage is set to `$Flow.CurrentStage.`

**•** Active: Identifies that the stage is set to `$Flow.ActiveStages.`


You can use the FlowStageRelation records to represent the paused interview and its active and current stages visually.

For example, an Online Purchasing flow interview starts with several stages in $Flow.ActiveStages. If the interview is paused, Salesforce
creates a FlowStageRelation record for each stage in `$Flow.ActiveStages` or `$Flow.CurrentStage.`

**StageLabel** **StageType** **StageOrder**

Review Cart Active 0

Shipping Details Active 1

Billing Details Active 2

Payment Details Active 3

Order Confirmation Active 4

Shipping Details Current 1
