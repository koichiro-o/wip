#### ForecastingType

```

**Refers To**
ForecastingSubmission (the master object)

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only. The ID of this record.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
For forecasting types that use Quantity as the measure, the quantity for the forecast category.
Quantities must be provided in the corporate currency.


Used to identify the forecast type associated with `ForecastingAdjustment,` `ForecastingOwnerAdjustment,`
`ForecastingQuota,` `ForecastingFact, and` `ForecastingItem` objects. Available in API version 30.0 and greater.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(). delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

##### Fields

```
CanDisplayQuotas

```

**Type**
boolean


-----

```
DateType
DeveloperName

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a forecast type can show quota information. The default value
is `false. Available in API version 38.0 and later.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The date type that forecast amounts are based on. These values are available for
forecast types that were available before Summer ’21.

**•** `OpportunityCloseDate: Base forecasts on opportunity close dates.`

**•** `ProductDate: Base forecasts on opportunity product line item dates, if`
available.

**•** `ScheduleDate: Base forecasts on opportunity product schedule dates,`
if available.

These values are available in API version 52.0 and later in Performance Edition
and in Unlimited Edition with the Sales Cloud.

**•** `OLIMeasureCloseDateOnly: Base forecasts on opportunity close`
dates.

**•** `ProductDateOnly: Base forecasts on opportunity product line item`
dates, if available.

**•** `ScheduleDateOnly: Base forecasts on opportunity product schedule`
dates, if available.

These values to create forecasts on custom date fields are available in API version
57.0 and later in Performance, Professional, Enterprise, and Unlimited Edition
with the Sales Cloud.

**•** `OLIMeasureOppCustomDateOnly: Base forecasts on custom`
opportunity dates, if available.

**•** `OpportunityCustomDate: Base forecasts on custom opportunity`
dates.

The custom date field used must be on the opportunity object and based on the
date type.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
ForecastingGroupID
HasAdjustments
HasOwnerAdjustments
HasProductFamily

```

**Description**
The name of the forecasting type. The DeveloperName is called name in
the Metadata API and Forecasting Type in custom reports.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a group assignment, and if so, the
name of the group. This field is a relationship field. Available in API version 60.0
and later.

**Relationship Name**
ForecastingGroup

**Relationship Type**
Lookup

**Refers To**
ForecastingGroup

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether forecast managers can adjust forecasts of their immediate
subordinates and child territories. The default value is `false. Available in API`
version 60.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether all forecast users can adjust their own forecasts, including the
territory forecasts that they own. The default value is `false. Available in API`
version 60.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group


-----

```
IsActive
IsAmount
IsPlatformType
IsQuantity
Language

```

**Description**
Indicates whether a forecasts view includes product families. The default value
is `false. Available in API version 40.0 and later.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the forecasting type is enabled. The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecasting type is based on the revenue measure. The
default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a legacy forecast type that wasn’t available before Summer ’21. The
default value is `false. Available in API version 52.0 and later.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the forecasting type is based on the quantity measure. The
default value is `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the forecasting type.


-----

```
LastActivatedDate
MasterLabel
OpportunitySplitTypeId
OpptyLineItemSplitTypeId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date when a forecast type was activated. Read only. Available in API version
53.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Controlling label for this forecasting type value. This display value is the internal
label that doesn’t get translated.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a split type, and if so, the name of the
split type. This field is a relationship field. Available in API version 41.0 and later.

**Relationship Name**
OpportunitySplitType

**Relationship Type**
Lookup

**Refers To**
OpportunitySplitType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a product split type, and if so, the
name of the product split type. This field is a relationship field. Available in API
version 58.0 and later.

**Relationship Name**
OpptyLineItemSplitType

**Relationship Type**
Lookup


-----

```
RoleType
Territory2ModelId
