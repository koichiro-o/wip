#### WorkCapacityLimit

Represents the capacity limit in a specific service territory for a workstream or for the whole service territory in a given period. This object
is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
CapacityLimitRelaxation
Description
Description
EndDate
IsActive

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the relaxation behavior that determines the limit override policy for this limit if the
limit override policy is set per limit in Field Service Settings. If the limit override policy isn’t
set per limit, this value is ignored. Valid strings are:

**•** Empty value - no limit override

**•** 0 - limit override starts at midnight on the day of service

**•** Positive integer - limit override starts this number of hours after midnight. the maximum
value is 23.

**•** Negative integer - limit override starts this number of hours before midnight. The
maximum value is 336.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the work capacity limit.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the work capacity limit.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
End date of the work capacity limit. If no EndDate is set this work capacity limit is without
an expiration date.

**Type**
boolean


-----

```
IsFriday
IsMonday
IsSaturday
IsSunday
IsSvcTerrOnlyLimit

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the work capacity limit is active or inactive. When creating a record, save
the record, and then activate it. You can't update fields in an active record.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Fridays.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Mondays.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Saturdays.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Sundays.

The default value is `false.`

**Type**
boolean


-----

```
IsThursday
IsTuesday
IsWednesday
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Apply this work capacity limit to the entire service territory.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Thursdays.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Tuesdays.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the limitation is applied on Wednesdays.

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime


-----

```
LimitationUnits
LimitationValue
OwnerId

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate isn’t null, the user accessed this record or list view indirectly.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Unit of the `LimitationValue.`

Possible values are:

**•** `Hours`

**•** `Percentage`

The default value is `Hours.`

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
If the `LimitationUnits` is `Hours,` `LimitationValue` is the threshold that
represents how many hours of total work capacity can be scheduled for a specific workstream
in a service territory. Enter the number of hours for the daily limitation as a whole number.

If the `LimitationUnits` is `Percentage` this threshold represents the percentage
of the total work capacity that can be scheduled for a specific workstream in a service territory.
Enter the percentage for the daily limitation as a whole number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of the work capacity limit.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


-----

```
ServiceTerritoryId
StartDate
SvcApptField

```

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the service territory of the work capacity workstream for which the limit is defined.

This field is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The start date of the Work Capacity Limit.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Work-specific criteria used to define the capacity limit for the workstream. The service
appointment field is set for the organization when the first work capacity limit instance is
created.

Possible values are:

**•** `ServiceAppointment.AccountId`

**•** `ServiceAppointment.ActualDuration—Actual duration (in minutes)`

**•** `ServiceAppointment.Duration—Duration`

**•** `ServiceAppointment.DurationInMinutes`

**•** `ServiceAppointment.FSL__Appointment_Grade__ce`

**•** `ServiceAppointment.FSL__Auto_Schedule__c`

**•** `ServiceAppointment.FSL__Duration_In_Minutes__c—Scheduled`
duration


-----

```
SvcApptFieldValDplyNm
SvcApptFieldValue

```


**•** `ServiceAppointment.FSL__Emergency__c`

**•** `ServiceAppointment.FSL__GanttColor__c`

**•** `ServiceAppointment.FSL__GanttLabel__c`

**•** `ServiceAppointment.FSL__InJeopardyReason__c`

**•** `ServiceAppointment.FSL__InJeopardy__c`

**•** `ServiceAppointment.FSL__IsFillInCandidate__c`

**•** `ServiceAppointment.FSL__IsMultiDay__c`

**•** `ServiceAppointment.FSL__Last_Updated_Epoch__c`

**•** `ServiceAppointment.FSL__MDS_Calculated_length__c—Multiday`
work calculated length

**•** `ServiceAppointment.FSL__Pinned__c`

**•** `ServiceAppointment.FSL__Prevent_Geocoding_For_Chatter_Actions__c`

**•** `ServiceAppointment.FSL__Related_Service__c`

**•** `ServiceAppointment.FSL__Same_Day__c`

**•** `ServiceAppointment.FSL__Same_Resource__c`

**•** `ServiceAppointment.FSL__Schedule_Mode__c`

**•** `ServiceAppointment.FSL__Schedule_over_lower_priority_appointment__c`

**•** `ServiceAppointment.FSL__Scheduling_Policy_Used__c`

**•** `ServiceAppointment.FSL__Time_Dependency__c`

**•** `ServiceAppointment.FSL__UpdatedByOptimization__c`

**•** `ServiceAppointment.FSL__Use_Async_Logic__c`

**•** `ServiceAppointment.FSL__Virtual_Service_For_Chatter_Action__c`

**•** `ServiceAppointment.IsOffsiteAppointment`

**•** `ServiceAppointment.Subject`

**•** `ServiceAppointment.WorkTypeId—Work Type ID`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The workstream display name of SvcApptFieldValue. If SvcApptField is a lookup
to a service appointment, SvcApptFieldValue is an ID and the display name describes
the value for the user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
TimePeriod
WorkCapacityLimitNumber

##### Associated Objects

```

**Description**
The value of `SvcApptField, the work-specific criteria of the capacity limit.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Duration for defining the capacity limitation on the workstream in the service territory.

Possible values are:

**•** `Day`

The default value is `Day.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Auto populated, unique identifying number.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkCapacityLimitChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkCapacityLimitFeed on page 54**
Feed tracking is available for the object.

**WorkCapacityLimitHistory on page 62**
History is available for tracked fields of the object.

**WorkCapacityLimitShare on page 66**
Sharing is available for the object.
