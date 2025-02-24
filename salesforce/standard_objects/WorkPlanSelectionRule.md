#### WorkPlanSelectionRule

Represents a rule that selects a work plan for a work order or work order line item. This object is available in API version 52.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
AssetId
Description
IsActive
LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the asset.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the selection rule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether this selection rule is active (true) or not (false). Default is `false.`
Label is Active.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.


-----

```
LastViewedDate
LocationId
OwnerId
Product2Id
ServiceTerritoryId
WorkPlanSelectionRuleNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view (LastReferencedDate),
but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the location.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product. Label is Product.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service territory.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
WorkPlanTemplateId
WorkTypeId

##### Associated Objects

```

**Description**
The auto-generated number of the work plan selection rule, for example, WPSR-0001.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the work plan template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work type.


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**WorkPlanSelectionRuleChangeEvent**

Change events are available for the object.

**WorkPlanSelectionRuleFeed**

Feed tracking is available for the object.

**WorkPlanSelectionRuleHistory**

History is available for tracked fields of the object.

**WorkPlanSelectionRuleOwnerSharingRule**

Sharing rules are available for the object.

**WorkPlanSelectionRuleShare**

Sharing is available for the object.
