#### MaintenancePlan

Represents a preventive maintenance schedule for one or more assets in field service.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

The Frequency and Frequency Type fields began their phased retirement in Summer ‘22. To prepare for this retirement and take advantage
of updated features, migrate your frequency and frequency type data to maintenance work rules. The retired frequency fields impact
work order generation. Complete migration as soon as possible to avoid being impacted by this change.

```
AccountId
ContactId
Description
DoesAutoGenerateWorkOrders

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated account, which typically represents the customer receiving the
maintenance service.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated contact.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A brief description of the plan.

**Type**
boolean


-----

```
DoesGenerateUponCompletion
EndDate
Frequency
FrequencyType

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Turns on auto-generation of work order batches for a maintenance plan and
prohibits the manual generation of work orders via the Generate Work Orders
action. If this option is selected, a new batch of work orders is generated for the
maintenance plan on the NextSuggestedMaintenanceDate listed on
each maintenance asset, or on the maintenance plan if no assets are included.
If a GenerationHorizon is specified, the date of generation is that many
days earlier.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If both this option and DoesAutoGenerateWorkOrders are set to true,
a new batch of work orders isn’t generated until the last work order generated
from the maintenance plan is completed. A work order is considered completed
when its status falls into one of the following status categories: Cannot Complete,
Canceled, Completed, or Closed.

If a maintenance plan covers multiple assets, work orders are generated per asset.
If a maintenance asset’s final work order is completed late, its work order
generation is delayed, which may cause a staggered generation schedule between
maintenance assets.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last day the maintenance plan is valid.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
(Optional) Amount of time between work orders. The unit is specified in the
```
  FrequencyType field.

```
**Type**
picklist


-----

```
GenerationHorizon
GenerationTimeframe
GenerationTimeframeType

```

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
(Optional) The unit of frequency:

**•** Days

**•** Weeks

**•** Months

**•** Years

For example, to perform monthly maintenance visits you need a work order for
each visit, so enter 1 as the `Frequency` and select Months.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Moves up the timing of batch generation if
`DoesAutoGenerateWorkOrders` is set to true. A generation horizon of
5 means the new batch of work orders is generated 5 days before the
maintenance asset’s (or maintenance plan’s, if there are no assets)
```
  NextSuggestedMaintenanceDate. The generation horizon must be a

```
whole number.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

(Required) How far in advance work orders are generated in each batch. The unit
is specified in the `GenerationTimeframeType field.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
(Required) The generation timeframe unit:

**•** Days

**•** Weeks

**•** Months

**•** Years


-----

```
LastReferencedDate
LastViewedDate
LocationId
MaintenancePlanNumber
MaintenancePlanTitle
MaintenanceWindowEndDays

```

For example, if you need work orders for six months, enter 6 and select Months.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the service takes place.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read Only) An auto-assigned number that identifies the maintenance plan.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A name for the maintenance plan.

**Type**
int


-----

```
MaintenanceWindowStartDays
NextSuggestedMaintenanceDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Days after the suggested service date on the work order that its service
appointment can be scheduled.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Days before the suggested service date on the work order that its service
appointment can be scheduled.

The maintenance window start and end fields affect the Earliest Start Permitted
and Due Date fields on the maintenance plan’s work orders’ service appointments.
For example, if you enter 3 for both the maintenance window start and end, the
Earliest Start Permitted and the Due Date will be 3 days before and 3 days after,
respectively, the Suggested Maintenance Date on each work order. If the
maintenance window fields are left blank, the service appointment date fields
list their work order’s suggested maintenance date.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The suggested date of service for the first work order (not the date the work order
is created). This corresponds to the work order’s
```
  SuggestedMaintenanceDate. You can use this field to enforce a delay

```
before the first maintenance visit (for example, if monthly maintenance should
begin one year after the purchase date). Its label in the user interface is Date of
the first work order in the next batch.

For example, if you want the first maintenance visit to take place on May 1, enter
May 1. When you generate work orders, the earliest work order will list a suggested
maintenance date of May 1, and the dates on the later work orders will be based
on the GenerationTimeframe and Frequency.

Important: Maintenance assets also list a
```
    NextSuggestedMaintenanceDate, which is initially inherited

```
from the maintenance plan. If the plan has maintenance assets, this date
auto-updates on the maintenance assets after each batch is generated,
but doesn’t update on the maintenance plan itself because batch timing
is calculated at the maintenance asset level. If the plan doesn’t have


-----

```
OwnerId
ServiceContractId
StartDate
SvcApptGenerationMethod

```

maintenance assets, this date auto-updates on the maintenance plan after
each batch is generated.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the maintenance plan.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service contract associated with the maintenance plan. The service contract
can’t be updated if any child maintenance asset is associated with a contract line
item from the service contract.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The first day the maintenance plan is valid.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The service appointment generation method.

**•** One service appointment per work order

**•** One service appointment per work order line item

If your existing maintenance plans have work orders or work order line items
associated with them, you can’t change their generation methods. To change
pre-existing maintenance plan generation methods, either delete the work orders
and regenerate them or delete the maintenance plan and recreate it with the
needed generation methods.

If Work Order Generation Method is set to One work order per asset, you can’t
set a Service Appointment Generation Method.


-----

```
WorkOrderGenerationMethod
WorkOrderGenerationStatus
WorkTypeId

```

If Work Order Generation Method is set to One work order line item per asset,
you must select a Service Appointment Generation Method.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The work order generation method.

**•** One work order per asset

**•** One work order line item per asset

If your existing maintenance plans have work orders or work order line items
associated with them, you can’t change their generation methods. To change
pre-existing maintenance plan generation methods, either delete the work orders
and regenerate them or delete the maintenance plan and recreate it with the
needed generation methods.

If Work Order Generation Method is left as None, the generation is defaulted to
one work order per asset.

When One work order line item per asset is set, and all maintenance assets have
the same Next Suggested Maintenance Date on the maintenance plan, they are
grouped in one work order. However, if maintenance assets have different Next
Suggested Maintenance Dates, multiple work orders are created for each date.

If Work Order Generation Method is set to One work order per asset, you can’t
set a Service Appointment Generation Method.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
(Read Only) Indicates the status of work order generation:

**•** NotStarted—the default value, work order generation has not started

**•** InProgress—work order generation is underway

**•** Completed—work order generation is complete

**•** Unsuccessful—it was not possible to generate work orders

You can generate only one batch at a time.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

**Description**
The associated work type. Work orders generated from the maintenance plan
inherit its work type’s duration, required skills and products, and linked articles.
Maintenance assets covered by the plan use the same work type, though you
can update them to use a different one.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MaintenancePlanChangeEvent (API version 48.0)**
Change events are available for the object.

**MaintenancePlanFeed**

Feed tracking is available for the object.

**MaintenancePlanHistory**

History is available for tracked fields of the object.

**MaintenancePlanOwnerSharingRule**

Sharing rules are available for the object.

**MaintenancePlanShare**

Sharing is available for the object.
