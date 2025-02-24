#### Period

Represents a fiscal period defined in FiscalYearSettings.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only Chatter Free users and standard users can access this object.

##### Fields

```
EndDate
FiscalYearSettingsId

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The last date of the fiscal period.

**Type**
reference

**Properties**
Filter, Nillable, Group, Sort

**Description**
The parent record for this period.

This is a relationship field.


-----

```
FullyQualifiedLabel
IsForecastPeriod
Number
PeriodLabel
QuarterLabel

```

**Relationship Name**
FiscalYearSettings

**Relationship Type**
Lookup

**Refers To**
FiscalYearSettings

**Type**
string

**Properties**
Group, Nillable

**Description**
Represents the period’s complete name in the UI. For example, “September FY 2016”.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the period is associated with Salesforce Forecasting (true) or not (false).

**Type**
int

**Properties**
Filter, Nillable, Group, Sort

**Description**
If the labeling scheme of your fiscal year's quarters or months is numbered, this field indicates
the relative number of the row.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the months in your fiscal year use custom names, then this field contains the appropriate
name for rows of type Month.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


-----

```
 StartDate
 Type

##### Usage

```

**Description**
If the quarters in your fiscal year use custom names, then this field contains the appropriate
name for rows of type Quarter.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The first date of the fiscal period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the period is of type Month, Quarter, Week, or Year. Label is the field value.


In API version 36.0 and earlier, querying the Period object yields no results. In API version 37.0 and later, a query returns period records.

SEE ALSO:

FiscalYearSettings
