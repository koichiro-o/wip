#### OrderSummaryRoutingSchedule

Represents an attempt to route an order summary to one or more inventory locations for fulfillment. You can use it to schedule future
attempts and to record completed attempts. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

##### Fields

```
LastReferencedDate
LastViewedDate
Name
OrderSummaryId
OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the order summary routing schedule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Master-Detail) The order summary associated with the routing schedule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who currently owns this order summary routing schedule. Default value is the
User logged in to the API to perform the create.


-----

```
Reason
ScheduleStatus
ScheduledDatetime

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reason for the routing attempt. You can customize this list.

The list has one default value:

**•** `Unknown`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Identifies whether this routing attempt has already run or is scheduled to run.

Possible values are:

**•** ABANDONED

**•** COMPLETED

**•** SCHEDULED

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Identifies when this routing attempt was run or is scheduled to run. If the
`ScheduleStatus` is ABANDONED or COMPLETED, then you can’t modify this value.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**OrderSummaryRoutingScheduleOwnerSharingRule**

Sharing rules are available for the object.

**OrderSummaryRoutingScheduleShare**

Sharing is available for the object.

SEE ALSO:

OrderSummary


-----
