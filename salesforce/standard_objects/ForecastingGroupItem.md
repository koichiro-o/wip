#### ForecastingGroupItem

Represents the value within the picklist that is specified as the forecasting group for a forecast type. For example, if you have a forecasting
group that identifies the industry an opportunity is part of, this object represents the value in the the industry picklist that’s chosen to
be part of the group. This object is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
DisplayPosition
ForecastingGroupId
SourceValueApiName

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Indicates the order in which the value displays among other values in the group on the
forecasts page.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
This field is a relationship field.

**Relationship Name**
ForecastingGroup

**Relationship Type**
Lookup

**Refers To**
ForecastingGroup

**Type**
string

**Properties**
Create, Filter, Nillable, Sort


-----

```
SourceValueLabel
SourceValueTranslatedLabel

##### Usage

```

**Description**
The API name that’s derived from the group value.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The label that’s derived from the group value.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
If one exists, the translated version of the group value.


New forecast types based on opportunities or opportunity products can include a forecasting group. This group is based on a custom,
single-selection picklist that’s defined on the Opportunity, OpportunityLineItem, or Product2 objects. The picklist that’s chosen for the
group can contain more values than are needed for the type.
