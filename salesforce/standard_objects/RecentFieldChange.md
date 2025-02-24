#### RecentFieldChange

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The quote work source associated with the quote line item.

This field is a relationship field.

**Relationship Name**
QuoteLineWorkSource

**Refers To**
QuoteLineWorkSource


Use this virtual object to see how an opportunity has changed in the past seven days. Learn the previous value of a field, who made the
change, and when the change was made. This object is available in API version 52.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To use RecentFieldChange, set up historical trend reporting for opportunities in your org. You must also have the Pipeline Inspection
user permission and the Pipeline Inspection setting enabled.

##### Fields

```
ChangeDate
CurrencyIsoCode

```

**Type**
dateTime

**Properties**

**Description**
The date and time that the specified field was changed.

**Type**
picklist


-----

```
FieldName
ParentId
PreviousCurrencyValue

```

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The ISO code for the currency value. Must be one of the valid alphabetic, three-letter currency
ISO codes defined by the ISO 4217 standard, such as USD, GBP, or JPY.

The default value is 'USD'.

**Type**
string

**Properties**
Filter, Group

**Description**
The name of the opportunity field that you want the previous value of. Possible values are:

**•** `Amount`

**•** `CloseDate`

**•** `StageName`

**•** `ForecastCategory`

**•** `NextStep`

**Type**
reference

**Properties**
Filter, Group

**Description**
The ID of the opportunity that you want the change history for.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
currency

**Properties**
Nillable

**Description**
The previous value of a currency field on an opportunity.


-----

```
PreviousDateOnlyValue
PreviousTextValue
ValueChangedById

##### Usage

```

**Type**
date

**Properties**
Group, Nillable

**Description**
The previous value of a date field on an opportunity.

**Type**
string

**Properties**
Group, Nillable

**Description**
The previous value of a text field on an opportunity.

**Type**
reference

**Properties**
Group

**Description**
The ID of the user who changed the specified field's value during the specified time period.

This is a relationship field.

**Relationship Name**
ValueChangedBy

**Relationship Type**
Lookup

**Refers To**
User


One recentFieldChange record is returned for each field that was changed in the past seven days. The supported fields are Amount,
Close Date, Forecast Category, Next Step, and Stage Name. Only the most recent previous value is returned.

Example: To see the most recent previous amount for an opportunity, use the following query. Replace 006R0000XXXXXXXXXX
with the ID of the opportunity.
```
   select PreviousTextValue from RecentFieldChange where ParentId = '006R0000003JkHBIA0'
   and FieldName = 'StageName'

```
If the sales rep didn't change the opportunity stage name in the past seven days, no values are returned. If the sales rep changed
the opportunity amount several times in the past seven days, only the most recent previous value is returned.


-----

Example: To see the most recent previous amount, close date, forecast category, next step, and stage name for an opportunity,
use the following query. Replace `006R0000XXXXXXXXXX` with the ID of the opportunity.
```
   select PreviousTextValue, PreviousCurrencyValue, PreviousDateOnlyValue from
   RecentFieldChange where ParentId = '006R0000XXXXXXXXXX' and FieldName IN ('StageName',
   'Amount', 'CloseDate')

```
If the opportunity amount, close date, forecast category, next step, and stage name didn’t change in the past seven days, no values
are returned.
