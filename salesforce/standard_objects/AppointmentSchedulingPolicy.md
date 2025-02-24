#### AppointmentSchedulingPolicy

Represents a set of rules for scheduling appointments using Salesforce Scheduler. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field**
```
AppointmentAssignmentPolicyId
AppointmentStartTimeInterval

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name or ID of the appointment assignment policy. This is a relationship field, available
in version 52.0 and later.

**Relationship Name**
AppointmentAssignmentPolicy

**Relationship Type**
Lookup

**Refers To**
AppointmentAssignmentPolicy

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The proposed time interval in minutes between appointment start times. For example, set
the interval to 15. Appointments can then begin at the top of the hour and at 15-minute
intervals thereafter (10:00 AM, 10:15 AM, 10:30 AM, and so on). Possible values are:

**•** `5`

**•** `10`

**•** `15`

**•** `20`

**•** `30`

**•** `45`

**•** `60`

**•** `90`

**•** `120`

**•** `150`

**•** `180`

**•** `240`

**•** `300`

**•** `360`

**•** `420`

**•** `480`


-----

```
DeveloperName
ExtCalEventHandlerId
IsOrgDefault
IsSvcTerrOpHoursWithShiftsUsed
IsSvcTerritoryMemberShiftUsed

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the AppointmentSchedulingPolicy object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the custom Apex class that checks service resources’ external calendar
events and returns the time slots where service resources are already booked. Available in
API version 50.0 and later.

This is a relationship field.

**Relationship Name**
ExtCalEventHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this scheduling policy is the default appointment scheduling policy for
Lightning Scheduler appointments in this org.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this scheduling policy considers the intersection of shifts and service
territory operating hours when determining the availability of service resources for
appointments (true). The default value is false. Available in API version 56.0 and later.

**Type**
boolean


-----

```
Language
MasterLabel

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this scheduling policy considers shifts of service territory members when
determining the availability of service resources for appointments (true). The default value
is false. Available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the appointment scheduling policy.

Possible values are:

**•** `Possible` values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexican)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazilian)

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the appointment scheduling policy.


-----

```
ShouldConsiderCalendarEvents
ShouldEnforceExcludedResource
ShouldEnforceRequiredResource
ShouldMatchSkill
ShouldMatchSkillLevel
ShouldRespectVisitingHours

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this policy checks the Salesforce calendar for resource availability.

The default value is 'false'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy prevents excluded service resources
from being assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
who have certain skills to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only required service resources
who have certain skills and skill levels to be assigned to appointments.

**Type**
boolean


-----

```
ShouldUsePrimaryMembers
ShouldUseSecondaryMembers

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy prevents users from scheduling
appointments outside of an account’s visiting hours.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows only service resources who are
primary members of a service territory to be assigned to appointments.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this appointment scheduling policy allows service resources who are
secondary members of a service territory to be assigned to appointments.

