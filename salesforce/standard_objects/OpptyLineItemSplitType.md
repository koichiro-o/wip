#### OpptyLineItemSplitType

Represents an opportunity product split type. This object is available in API version 58.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
Description

```

**Type**
textarea

**Properties**
Filter, Group, Sort

**Description**
Text description of the opportunity line item split type. Limit: 80 characters.


-----

```
DeveloperName
IsActive
IsTotalValidated
Language
MasterLabel
NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer (API) name of the opportunity line item split type.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the opportunity line item split type is active (true) or not (false). The
value of this field is inherited from the IsActive field of the parent OpportunitySplitType
record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the OpportunityLineItemSplit records associated with the
OpportunityLineItem must have SplitPercent values that aggregate to 100% (true) or not
(false). The value of this field is inherited from the `IsTotalValidated field of the`
parent OpportunitySplitType record.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the opportunity line item split type.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The opportunity line item split type label.

**Type**
string


-----

```
OpportunitySplitTypeId
SplitDataStatus
SplitEntity
SplitField

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent OpportunitySplitType. Every OpptyLineItemSplitType must have a parent
OpportunitySplitType. This field is a relationship field.

**Relationship Name**
OpportunitySplitType

**Relationship Type**
Lookup

**Refers To**
OpportunitySplitType

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the asynchronous job to delete OpportunityLineItemSplit records when the
associated OpptyLineItemSplitType record is deleted. Possible values are:

**•** `DeletionFailed–The job failed the last time it ran.`

**•** `Ready–The job hasn't run or isn't running. OpportunityLineItemSplit records associated`
with the OpptyLineItemSplitType can be interacted with.

**•** `ToBeDeleted–The job is running.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Name or ID of the entity that contains the field being split. In API version 58.0, this value is
always OpportunityLineItem.

**Type**
picklist


-----

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Name or ID of the field on OpportunityLineItem that is being split. If it's a standard field, then
the value is the API name of the field. If it’s a custom field, the value is the custom field
definition ID.

##### Usage

When an OpportunitySplitType has product splits enabled in Setup, then an OpptyLineItemSplitType record is created. For example, if
there is an OpportunitySplitType record with a SplitField of `Amount` and product splits is enabled in Setup, then there is an
OpptyLineItemSplitType record with a SplitField of `TotalPrice` (since the TotalPrice field rolls up to Amount).
