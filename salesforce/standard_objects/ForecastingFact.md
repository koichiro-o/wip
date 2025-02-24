#### ForecastingFact

```

**Description**
The order in which product families are displayed on the forecasts page. Each
value is unique to a product family.

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
The product family available to forecast on. Each product family is unique.


This object is read-only and links a ForecastingItem with its opportunities, such as opportunities that share the same owner or forecast
category and have a closing date within the period of the forecasting item. Available in API versions 26 and greater.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

##### Fields

```
ForecastCategoryName
ForecastedObjectId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

A forecast category is the category within the sales cycle to which an opportunity
is assigned based on its opportunity stage. The standard forecast categories are
Pipeline, Best Case, Commit, Omitted (not included in forecasts), and Closed.
Salesforce admins can customize the forecast category names.

**Type**
reference


-----

```
ForecastedSubObjectId
ForecastingItemId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the Split ID of the forecasted OpportunitySplit object if the forecast data
source is opportunity splits or the OpportunityLineItem ID of the forecasted
opportunity if the data source is product families. If the data source is product
families and the opportunity has no line item, this field is null. If the forecast data
source is opportunities, this field is null. This field is available in API version 29
and later. Read-only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Possible values:

**•** If the forecast data source is OpportunityLineItemSplit, and the opportunity
has line items and line item splits, then this field contains the ID of the
forecasted OpportunityLineItemSplit object.

**•** If the forecast data source is OpportunityLineItemSplit, and the opportunity
has line items but no line item splits, this field contains the ID of the forecasted
OpportunitySplit object.

**•** If the forecast data source is OpportunityLineItemSchedule, this field contains
the OpportunityLineItemSchedule ID of the forecasted opportunity.

**•** If the forecast data source is OpportunityLineItemSplit and the opportunity
has no line item, this field is null.

**•** If the forecast data source is OpportunityLineItemSchedule and the
opportunity has no line item, this field is null.

This field is available in API version 58.0 and later. Read-only. This field is a
polymorphic relationship field.

**Relationship Name**
null

**Relationship Type**
Lookup

**Refers To**
OpportunityLineItem, OpportunityLineItemSplit

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
ForecastingTypeId
OpportunityId
OwnerId
PeriodId
TargetValue
Territory2Id

```

**Description**

The ID of the ForecastingItem.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the related ForecastingType.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The opportunity ID.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the opportunity owner.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Period ID for the forecast.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**

Target value of the forecast amount.

**Type**
reference


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the territory to forecast on. Available in API version 43 and later.

##### Usage

Use this object to get information about opportunities linked to forecasting items.

Note: Beginning with API version 30.0, organizations can have more than one forecasting type enabled. The
```
  ForecastingQuota, ForecastingAdjustment, ForecastingOwnerAdjustment, ForecastingItem,

```
and ForecastingFact objects can all have records with different ForecastingTypeId values. Use the ForecastingType
object to determine the ID for each forecast type and then filter `ForecastingQuota,` `ForecastingAdjustment,`
`ForecastingItem, or` `ForecastingFact` records as necessary.

SEE ALSO:

ForecastingAdjustment

ForecastingItem

ForecastingQuota
