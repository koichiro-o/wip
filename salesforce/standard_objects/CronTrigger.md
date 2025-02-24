#### CronTrigger

Contains schedule information for a scheduled job. CronTrigger is similar to a cron job on UNIX systems. This object is available in API
version 17.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field**
```
CronExpression
CronJobDetailId
EndTime
NextFireTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The cron expression used to initiate the schedule.

Syntax:
```
  Seconds Minutes Hours Day_of_month Month Day_of_week
  Optional_year

```
[See schedule(jobName, cronExpression, schedulableClass) in the](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexref/apex_methods_system_system.htm)
_Apex Reference Guide._

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CronJobDetail record containing more details about this scheduled job.

This is a relationship field.

**Relationship Name**
CronJobDetail

**Relationship Type**
Lookup

**Refers To**
CronJobDetail

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the job either finished or will finish.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
OwnerId
PreviousFireTime
StartTime
State

```

**Description**
The next date and time the job is scheduled to run. `null` if the job is not scheduled to run
again.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Owner of the job.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date and time the job ran. null if the job has not run before current local
time.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the most recent iteration of the scheduled job started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The current state of the job. The job state is managed by the system. Possible values are:

**•** `WAITING—The job is waiting for execution.`

**•** `ACQUIRED—The job has been picked up by the system and is about to execute.`

**•** `EXECUTING—The job is executing.`

**•** `COMPLETE—The trigger has fired and is not scheduled to fire again.`

**•** `ERROR—The trigger definition has an error.`

**•** `DELETED—The job has been deleted.`

**•** `PAUSED—A job can have this state during patch and major releases. After the release`
has finished, the job state is automatically set to `WAITING` or another state.


-----

```
TimesTriggered
TimeZoneSidKey

##### Usage

```


**•** `BLOCKED—Execution of a second instance of the job is attempted while one instance`
is running. This state lasts until the first job instance is completed.

**•** `PAUSED_BLOCKED—A job has this state due to a release occurring. When the release`
has finished and no other instance of the job is running, the job’s status is set to another
state.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this job has been triggered.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the timezone ID. For example, `America/Los_Angeles.`


Use this object to query scheduled jobs in your organization.
