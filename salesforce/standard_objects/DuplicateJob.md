#### DuplicateJob

Represents an instance of a job that identifies duplicates among existing records in the system.

This object is available in API versions 42.0 and later.

A duplicate job is the parent of the DuplicateRecordSet instances that it generates. The duplicate record items in a set generated by a
duplicate job are of one object type.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Special Access Rules

```
As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

##### Fields

```
DuplicateJobDefinitionId
DuplicateJobStatus
EndDateTime

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the corresponding duplicate job definition.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The current status of a duplicate job. Valid values are `Not Started,` `In`
```
  Progress, Completed, Canceled, Failed, Results Deleted.

```
**Type**
dateTime


-----

```
LastReferencedDate
LastViewedDate
Name
NumDuplicateRecordItems
NumDuplicateRecordSets

```

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when a duplicate job was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when a duplicate job was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when a duplicate job was last viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The name of a duplicate job.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The total number of duplicate records identified as a result of invoking a duplicate
job.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of duplicate record sets identified as a result of invoking a duplicate
job.


-----

```
NumRecordsScanned
ResultListViewId
StartDateTime
