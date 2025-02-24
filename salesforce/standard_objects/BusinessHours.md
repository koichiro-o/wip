#### BusinessHours

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the user who is associated with the alert.

This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


Specifies the business hours of your support organization. Escalation rules are run only during these hours.

Limit a list view to a maximum of 10,000 business hours.

If business hours are associated with any Holiday records, then business hours and escalation rules associated with business hours are
suspended during the dates and times specified as holidays.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), update(), upsert()

 Special Access Rules

```
All users, even those without the “View Setup and Configuration” user permission, can view business hours via the API.

##### Fields

```
BusinessHoursId

```

**Type**
reference

**Properties**
Filter, Group, Nillable,Sort

**Description**
ID of the BusinessHours associated with the SlaProcess.


-----

```
IsActive
Name
IsDefault
LastViewedDate
FridayEndTime
FridayStartTime

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the business hours is active (true) or not active (false).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the business hours.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the business hours are set as the default business hours (true) or not
(false).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the business hours were last viewed.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
MondayEndTime
MondayStartTime
SaturdayEndTime
SaturdayStartTime
SundayEndTime
SundayStartTime

```

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
ThursdayEndTime
ThursdayStartTime
TimeZoneSidKey
TuesdayEndTime
TuesdayStartTime
WednesdayEndTime

```

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The time zone of the business hours.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
 WednesdayStartTime

##### Usage

```

**Description**
Time that business closes.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time that business opens.


Use this object to specify the business hours at which your support team operates. Escalation rules only run during the business hours
with which they are associated. To set business hours to 24-hours a day, set the times from midnight to midnight (00:00:00 ~ 00:00:00)
on each day.

By default, business hours are set from 12:00 AM to 12:00 AM in the default time zone specified in your organization's profile.

SEE ALSO:

Overview of Salesforce Objects and Fields
