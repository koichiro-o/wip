#### ForecastingGroup

Represents groups used to roll up forecast totals on the forecasts page. For example, group forecasts by industry or sales type. This object
is available in API version 60.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Available for forecast types created in Spring ‘24 or later and that are based on the Opportunity and Opportunity Product objects.

You can only add groups to new forecast types.

##### Fields

```
DeveloperName
DisplayPosition
ForecastingTypeId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer (API) name of the forecast group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which forecasting dimensions are displayed on the forecasts page. Each value
is unique to a dimension.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
GroupField
Language
MasterLabel
SourceObject

```

**Description**
The ID of the forecast type associated with the forecasting group.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The field name of the custom picklist used as a group. Possible values include custom,
single-selection picklists available in `SourceObject.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the custom picklist identified as the group.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for this object, which displays in Setup. The label is in the default language locale
for the organization. If there’s no default language locale, the label is in en_US.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The entity the picklist used for the forecast group is on.

Possible values are:

**•** `Opportunity`

**•** `OpportunityLineItem`

**•** `Product2`


-----

##### Usage

Each forecast group can apply to only one forecast type.
