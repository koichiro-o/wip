#### CronJobDetail

Contains details about the associated scheduled job, such as the job’s name and type. This object is available in API version 29.0 and
later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field**
```
JobType
Name

##### Usage

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated scheduled job. The following are the available job types. Use the
job type value when querying for a specific job type.

**•** `1—Data Export`

**•** `3—Dashboard Refresh`

**•** `4—Reporting Snapshot`

**•** `6—Scheduled Flow`

**•** `7—Scheduled Apex`

**•** `8—Report Run`

**•** `9—Batch Job`

**•** `A—Reporting Notification`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the associated scheduled job.


Use this object to query additional information about a scheduled job, such as the job’s name and type.
