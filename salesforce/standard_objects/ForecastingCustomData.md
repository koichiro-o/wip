#### ForecastingCustomData

Represents forecast data from external sources to display in the forecasts page. For example, risk or last year’s revenue. This object is
available in API version 58.0 and later.

This object doesn’t support forecast rollups or adjustments. Number and currency columns are supported only.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
Available in Enterprise Edition and above, and in Professional Edition with an add-on license. Access to this object requires the Manage
Forecasts Custom Data user permission.

##### Fields

```
ForecastOwnerId
ForecastingGroupItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast owner. This field is a relationship field.

**Relationship Name**
ForecastOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If a forecast group is assigned to the forecast type, the ID of the group value that the custom
data belongs to. This field is a relationship field. Available in API version 60.0 and later.

**Relationship Name**
ForecastingGroupItem


-----

```
ForecastingTypeId
PeriodId
ProductFamily

```

**Relationship Type**
Lookup

**Refers To**
ForecastingGroupItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast type. This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup

**Refers To**
ForecastingType

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Period ID for the custom data. This field is a relationship field.

**Relationship Name**
Period

**Relationship Type**
Lookup

**Refers To**
Period

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The user-defined product family available to forecast on. Each product family is unique.
Possible values are:

**•** `[user-defined]–For example,` `Electronics` or `Appliances.`

**•** `None`


-----

```
StartDate
Territory2Id

##### Usage

```

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
The start of the custom data, expressed as month and year. The date can include any day in
a given month. Stored using the first date of the month.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the territory to forecast on.


Each record displays as a custom column on the forecasts summary page.
