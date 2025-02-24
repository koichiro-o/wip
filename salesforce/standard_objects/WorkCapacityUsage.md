#### WorkCapacityUsage

Represents the capacity limit in a specific service territory for a workstream or for the whole service territory in a given period. This object
is available in API version 59.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AvailCapacityHours
CapacityLimitRelaxation
ConsumptionToLimitRatio

```

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
This value is copied from the AvailCapacityHours of the WorkCapacityAvailability
object for the service territory on the same date.

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
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
(Time consumed in hours / Limit in hours) * 100

Note the following exceptions.

**•** If a limit isn’t defined (-1) the ratio is -1 (even if consumption is 0 or higher).

**•** If consumption is 0, and the limit is a number greater than 0, then the ration is 0.

**•** If consumption is 0 and the limit is 0, the ration is 100% hard-coded.


-----

```
EndDate
IsSvcTerrOnlyLimit
LastReferencedDate
LastViewedDate
LimitationPercentage

```


**•** If consumption is greater than 0 and the limit is 0, the ration is calculated as if the limit
= 0.99 in order to get a result that’s higher than 100%.

**Type**
date

**Properties**
Create, Filter, Group, Sort

**Description**
End date of the time period for which the capacity usage is accumulated.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Applies this work capacity limit to the entire service territory.

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

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate isn’t null, the user accessed this record or list view indirectly.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort

**Description**
If the `LimitationUnits` is `Percentage` this value is copied from the
```
  LimitationValue field of the WorkCapacityLimit object.

```

-----

```
LimitationUnits
LimitationValue
OriginalLimit
OwnerId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether the limitation for the workstream in the service territory is in hours or as a
percentage of all the available hours for all the workstreams for which limitations exist in the
service territory on a specific day.

Possible values are:

**•** `Hours`

**•** `Percentage`

The default value is `Hours.`

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
The `LimitationValue` depends on the LimitationUnit. If the LimitationUnit is
Hours the value is copied from LimitationValue in the WorkCapacityLimit object. If
the LimitationUnit is Percentage, the percentage is calculated relative to the availability
in the WorkCapacityAvailability object.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
If the limit value is changed after the work capacity usage was created, this parameter is the
original value.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner


-----

```
ServiceTerritoryId
StartDate
SvcApptField

```

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the service territory of the work capacity workstream for which usage is accumulated.

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
Create, Filter, Group, Sort

**Description**
Start date of the time period for which the capacity usage is accumulated.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Work-specific criteria used to define the capacity limit for the workstream.

Possible values are:

**•** `ServiceAppointment.AccountId`

**•** `ServiceAppointment.ActualDuration—Actual duration (in minutes)`

**•** `ServiceAppointment.Duration—Duration`

**•** `ServiceAppointment.DurationInMinutes`

**•** `ServiceAppointment.FSL__Appointment_Grade__ce`

**•** `ServiceAppointment.FSL__Auto_Schedule__c`


-----

```
SvcApptFieldValDplyNm
SvcApptFieldValue

```


**•** `ServiceAppointment.FSL__Duration_In_Minutes__c—Scheduled`
duration

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
Workstream display name of SvcApptFieldValue.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
TimeConsumedInHours
TimeConsumedInMinutes
TimePeriod
WcuUniqueField1
WcuUniqueField2

```

**Description**
Value of `SvcApptField, the work-specific criteria of the capacity limit.`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
Time consumed in hours by the workstream in the service territory for the defined period.
This value is calculated by dividing TimeConsumedInMinutes by 60.

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
Time consumed in minutes by the workstream in the service territory for the defined period.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Duration for defining the capacity limitation on the workstream in the service territory.

Possible values are:

**•** `Day`

The default value is `Day.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Read-only. Auto populated, unique identifying number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Read-only. Auto populated, unique identifying number.


-----

```
WorkCapacityUsageNumber

##### Associated Objects

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Auto populated, unique identifying number.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkCapacityUsageFeed on page 54**
Feed tracking is available for the object.

**WorkCapacityUsageShare on page 66**
Sharing is available for the object.
