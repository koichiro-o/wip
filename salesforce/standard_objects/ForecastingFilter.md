#### ForecastingFilter

Represents the custom filter for including or excluding data from opportunity forecasts. This object is available in API version 54.0 and
later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only standard users with the View All Forecasts permission OR Allow Forecasting permission OR delegated
forecast manager status can access this object.


-----

##### Fields

**Field Name**
```
DeveloperName
FilterLogic
ForecastingTypeId
ForecastingTypeSourceId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The developer name of the forecast filter.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The logic that controls the evaluation of conditions. Only `AND` is supported. For
example, `1 AND 2 AND 3.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the forecast type. Can be linked only to forecast types created in Summer
’21 and later. This is a relationship field.

**Relationship Name**

ForecastingType

**Relationship Type**

Lookup

**Refers To**

ForecastingType

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the forecast type source. Can be linked only to forecast type sources
created in Summer ’21 or later and with a forecast source definition with source
object of 'Opportunity.' This is a relationship field.


-----

```
Language
MasterLabel
