#### BillingBatchScheduler

Represents a scheduled processing job that triggers recurring invoice batch runs and payment batch runs in Subscription Management.
This object is available in API version 55.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

##### Fields

```
BillingSchedulerName
Comments
CronExpression
EndDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the scheduler.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional field for comments about the scheduler.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Determines how often the scheduler recurs.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


-----

```
FrequencyCadence
FrequencyOptions
JobType
LastReferencedDate

```

**Description**
The date when the scheduler stops triggering batch processing jobs.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates how often the scheduler triggers the invoice batch run or the payment batch run.

Possible values are:

**•** `Daily—The scheduled job recurs every day.`

**•** `Monthly—The scheduled job recurs every month.`

**•** `Once—The scheduled job occurs one time and doesn’t recur.`

**•** `Weekly—The scheduled job recurs every week.`

**Type**
textarea

**Properties**
Nillable

**Description**
Derived field that stores the scheduler configuration.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the type of batch processing job that the scheduler triggers.

Possible values are:

**•** `Invoice—The scheduler starts a batch invoice run.`

**•** `Payment—The scheduler starts a batch payment run.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


-----

```
LastViewedDate
NextRunTime
OwnerId
RecurringSubType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and timestamp of the next scheduled batch invoice run or batch payment run are
shown in the user's time zone.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who created the scheduler.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the frequency at which the batch processing job recurs when the
`FrequencyCadence` is set to Monthly.

Possible values are:


-----

```
RecurringType
RecursOn
RecursOnDate

```


**•** `Every—The processing job recurs at every instance of the frequency of the value. For`
example, if the `RecurringSubType` is `Every` and the `FrequencyCadence`
is `Weekly, then the batch processing job recurs every week.`

**•** `SpecificDate—The scheduler triggers the batch processing job on the selected`
date. For example, if the selected date is `5, and the` `FrequencyCadence` is
```
   Monthly, then the job recurs on the fifth day of each month.

```
**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the frequency at which the batch processing job is repeated when the
`FrequencyCadence` is set to Weekly.

Possible values are:

**•** `Every`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the interval at which the scheduler triggers a batch processing job.

If the FrequencyCadence is Monthly, you must select either the specific date or the interval
when the schedule triggers the job.

Possible values are:

**•** `First`

**•** `Fourth`

**•** `Last`

**•** `Second`

**•** `Third`

**Example: To tell the scheduler to trigger the job on the first Monday of the month, set the**
following fields:

**•** `FrequencyCadence=Monthly`

**•** `RecursOn=First`

**•** `RecursOnDay=` `Monday`

**Type**
string


-----

```
RecursOnDay
RunCriteriaId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the date on which the scheduler triggers a batch processing job.

**Example: To tell the scheduler to trigger the job on the fifth day of the month, set the**
following fields:

**•** `FrequencyCadence=Monthly`

**•** `RecursOnDate=5`

**Example: To tell the scheduler to trigger the job on the second to last day of the month,**
set the following fields:

**•** `FrequencyCadence=Monthly`

**•** `RecursOnDate=SecondToLast`

If you select Last, SecondToLast, or ThirdToLast, the date of the batch processing
job varies depending on the number of days in the month.

For example, suppose SecondToLast is selected. If the month has 30 days, such as June,
then the batch processing job occurs on the 28th day. If the month has 31 days, such as July,
then the batch processing job occurs on the 29th day.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the day on which the scheduler triggers a batch processing job.

If the `FrequencyCadence` field is set to `Weekly, then you must select the day when`
the scheduler runs. The scheduler recurs every week on the selected day; for example, weekly
on Monday.

Possible values are:

**•** `Sunday`

**•** `Monday`

**•** `Tuesday`

**•** `Wednesday`

**•** `Thursday`

**•** `Friday`

**•** `Saturday`

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
StartDate
StartTime
Status
TimeZone

```

**Description**
The ID of the filter criteria that’s defined for the invoice batch run or the payment batch run.

This field is a polymorphic relationship field.

**Relationship Name**
RunCriteria

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRunCriteria, PaymentBatchRunCriteria

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date when the scheduler triggers its first batch processing job.

**Type**
time

**Properties**
Filter, Sort

**Description**
The time when the scheduler triggers the batch processing job.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the scheduler. Only Active schedulers can trigger batch processing jobs.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `Draft`

**•** `Inactive`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

**Description**
The time zone is either the value selected when the run was configured, or it's the user's
time zone. The time zone is shown in Greenwich Mean Time (GMT).
