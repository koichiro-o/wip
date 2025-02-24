#### ForecastingFilterCondition

```

**Relationship Name**

ForecastingTypeSource

**Relationship Type**

Lookup

**Refers To**

ForecastingTypeSource

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The language of the forecast filter.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label for this object, which displays in Setup. The label is in the default
language locale for the organization. If there’s no default language locale, the
label is in en_US.


Represents the custom filter condition logic for including or excluding data from opportunity forecasts. This object is available in API
version 54.0 and later.

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
FieldName
ForecastingFilterId
Language
MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The developer name of the forecast filter condition.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The name of the opportunity field to be filtered.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the forecast filter. This is a relationship field.

**Relationship Name**

ForecastingFilter

**Relationship Type**

Lookup

**Refers To**

ForecastingFilter

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The language of the forecast filter condition.

**Type**
string


-----

```
Operation
SortOrder
Value

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The label for this object, which displays in Setup. The label is in the default
language locale for the organization. If there’s no default language locale, the
label is in en_US.

**Type**
string

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The operator in the filter condition. Possible values are:

**•** equals

**•** greaterOrEqual – greater than or equal to

**•** greaterThan

**•** lessOrEqual – less than or equal to

**•** lessThan

**•** notEqual

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**

The index value for the condition. This value represents the condition in the
FilterLogic field in the ForecastingFilter object. For example, 1.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The value of the filter condition. If multiple values are specified, they must be
separated by a comma delimiter.

Note: If you have multiple currencies enabled, and add a custom filter
on a currency field as part of your forecast type definition, the corporate
currency at the time the filter was created is used. If you have a single
currency enabled, the absolute value is used in your filter condition.


-----

##### Usage

A forecast type can contain up to three filter conditions.
