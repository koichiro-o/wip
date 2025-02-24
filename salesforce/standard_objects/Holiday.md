#### Holiday

Represents a period of time during which your customer support team is unavailable. Business hours and escalation rules associated
with business hours are suspended during any holidays with which they are affiliated.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
Customer Portal users can’t access this object.

All users, even those without the “View Setup and Configuration” user permission, can view holidays via the API.

##### Fields

```
ActivityDate
Description

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the Holiday `IsAllDay` flag is set to `true` (indicating that it is an all-day holiday), then
the holiday due date information is contained in the `ActivityDate` field. This field is a
date field with a timestamp that is always set to midnight in the Coordinated Universal Time
(UTC) time zone. The timestamp is not relevant, and you should not attempt to alter it to
account for any time zone differences.

**Type**
string


-----

```
EndTimeInMinutes
IsAllDay
IsRecurrence
Name
NextOccurrenceDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the holiday.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end time of the holiday in minutes.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the duration of the holiday is all day (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the holiday is scheduled to repeat itself (true) or only occurs once
(false). This is a read only field on update, but not on create. If this field value is `true,`
then any recurrence fields associated with the given recurrence type must be populated.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the holiday.

**Type**
date

**Properties**
Filter, Group, Nillable


-----

```
RecurrenceDayOfMonth
RecurrenceDayOfWeekMask
RecurrenceEndDateOnly
RecurrenceInstance

```

**Description**

The next date of the holiday. Applies to recurring holidays only. Available in API version 58.0
and later. To access this field, you must have Field Service enabled and the Field Service
Standard permission.

This field isn't sortable. To compare this date to other dates, you must parse the string into
a date value to compare it to other dates.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day of the month on which the holiday repeats.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day or days of the week on which the holiday repeats. This field contains a bitmask. For
each day of the week, the values are as follows:

**•** Sunday = `1`

**•** Monday = `2`

**•** Tuesday = `4`

**•** Wednesday = `8`

**•** Thursday = `16`

**•** Friday = `32`

**•** Saturday = `64`

Multiple days are represented as the sum of their numerical values. For example, Tuesday
and Thursday = 4 + 16 = 20.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date on which the holiday repeats. For multiday recurring events, this is the day on
which the last occurrence starts.

**Type**
picklist


-----

```
RecurrenceInterval
RecurrenceMonthOfYear
RecurrenceStartDate
RecurrenceType
StartTimeInMinutes

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The frequency of the recurring holiday. For example, `2nd` or `3rd.`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The interval between recurring holidays.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The month of the year on which the event repeats.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the recurring holiday begins. Must be a date and time before
```
  RecurrenceEndDateOnly.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how often the holiday repeats. For example, daily, weekly, or every Nth month
(where “Nth” is defined in RecurrenceInstance).

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start time of the holiday in minutes.


-----

##### Usage

Use this object to view and update holidays, which specify dates and times at which associated business hours and escalation rules are
suspended.
