#### InvoiceBatchRunRecovery

Provides information about an invoice batch run recovery procedure. This object is available in API version 57.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

##### Fields

```
Comments
CompletionTime
InvoiceBatchRunId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**
Optional user-defined information about the scheduler.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the invoice batch run recovery procedure was completed.

**Type**
reference


-----

```
InvoiceBatchRunRecoveryNumber
LastReferencedDate
LastViewedDate
StartTime

```

**Properties**
Filter, Group, Sort

**Description**
The unique identifier of the invoice batch run related to this recovery run.

This field is a relationship field.

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique identifier of the invoice batch run recovery process.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user indirectly accessed this record (LastReferencedDate), but
did not view it.

**Type**
dateTime

**Properties**
Filter, Sort


-----

```
Status

##### Associated Objects

```

**Description**
The timestamp when the invoice batch run recovery started.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The final state of the invoice batch run recovery process.

Possible values are:

**•** `Completed—The recovery run successfully reset all billing schedules to Ready for`
```
   Invoicing.

```
**•** `CompletedWithErrors—Some, but not all, billing schedules included in the`
recovery run were reset to `Ready for Invoicing. The billing schedules that`
were recovered are included in the next scheduled invoice batch run. The billing schedules
that weren’t successfully recovered must be manually reset to `Ready for`
`Invoicing` so they can be processed.

**•** `Failed—The recovery run was unable to complete the reset process.`

**•** `Started—Indicates that the recovery run reset process began, is ongoing, and has`
not yet produced a result.

The default value is `Started.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceBatchRunRecoveryChangeEvent on page 67**
Change events are available for the object.

**InvoiceBatchRunRecoveryFeed on page 54**
Feed tracking is available for the object.

**InvoiceBatchRunRecoveryHistory on page 62**
History is available for tracked fields of the object.

**InvoiceBatchRunRecoveryOwnerSharingRule on page 64**
Sharing rules are available for the object.

**InvoiceBatchRunRecoveryShare on page 66**
Sharing is available for the object.


-----
