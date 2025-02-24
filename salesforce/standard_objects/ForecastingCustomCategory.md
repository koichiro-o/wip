#### ForecastingCustomCategory

Represents a custom forecasting category used for forecast rollups. This object is available in API version 62.0 and later.

In API version 62.0, this object is available for rollup of Manager Judgments only.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
Description
DeveloperName
DisplayPosition

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A user-defined description of the custom category.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name of the custom category.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
ForecastingSourceDefinitionId
ForecastingTypeId
IsAdjustable
IsOwnerAdjustable

```

**Description**
Indicates the placement of the custom category column among the other columns on the
forecasts page.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the forecasting source definition.

This field is a relationship field.

**Relationship Name**
ForecastingSourceDefinition

**Refers To**
ForecastingSourceDefinition

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related ForecastingType.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether forecast managers can adjust forecasts in the custom category. The default
value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
Language
MasterLabel
MeasureFieldOverride

```

**Description**
Indicates whether all forecast users can adjust their own forecasts in the custom category,
including the territory forecasts that they own. The default value is `false.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the custom category.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for this column. The label is in the default language locale for the organization. If
there’s no default language locale, the label is in en_US.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The measure that this custom category supports.

Possible values are:

**•** `Opportunity.Amount`

**•** `Opportunity.AmountCustom__c`

**•** `Opportunity.AmountRSF__c`

**•** `Opportunity.TotalOpportunityQuantity`

**•** `OpportunityLineItem.Quantity`

**•** `OpportunityLineItem.TotalPrice`

**•** `OpportunityLineItem.oliCustomAmount__c`

**•** `OpportunityLineItemSplit.SplitAmount`

**•** `OpportunitySplit.SplitAmount`

**•** `OpportunitySplit.customAmount__c`


-----
