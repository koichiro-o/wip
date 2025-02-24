#### FiscalYearSettings

```

Possible values are:

**•** `DAY`

**•** `MONTH`

**•** `YEAR`

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date of the search.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language filter that’s applied to the user’s search.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The first 100 characters of the search term that was used to search published files.


Settings to define a custom or standard fiscal year for your organization. This object has a parent-child relationship with the Period object.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only partner users and standard users can access this object.


-----

##### Fields

**Field**
```
Description
EndDate
IsStandardYear
Name
PeriodId
PeriodLabelScheme

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the setting.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
End date of the fiscal year.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the fiscal year is a standard calendar year (true) or a custom fiscal year
(false).

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A name for the fiscal year. Limit: 80 characters.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the associated fiscal period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
PeriodPrefix
QuarterLabelScheme
QuarterPrefix
StartDate
WeekLabelScheme
WeekStartDay

```

**Description**
The numbering scheme used for fiscal periods.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The prefix of fiscal periods. For example, if `p is the prefix, then the first period is “P1.”`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The numbering scheme used for fiscal quarters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The prefix of fiscal quarters. For example, if “Q” is the prefix, then the fourth quarter would
be “Q4.”

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**

Start date of the fiscal year.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The numbering scheme used for weeks.

**Type**
int


-----

```
YearType

```
SEE ALSO:

Period


**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the day that starts the week, for example `Monday` or `Sunday`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates one of two types of fiscal years, Standard or Custom. Standard denotes the standard
Gregorian calendar, while Custom means a fiscal year with a custom structure.


Overview of Salesforce Objects and Fields
