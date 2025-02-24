#### WorkOrder

```

**Properties**
Create, Filter, Group, Sort

**Description**
The foreign key to the Workload object.

This is a relationship field.

**Relationship Name**
Workload

**Relationship Type**
Lookup

**Refers To**
Workload

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The derived field from Workload.WorkloadType to indicate the type of workload, for example,
a history or forecast workload.

Possible values are:

**•** `F—Forecasted`

**•** `H—Historical`

The default value is 'H'.


Represents field service work to be performed for a customer. This object is available in API version 36.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
**•** Work orders or Field Service must be enabled.

**•** The following fields can’t be edited, regardless of your field-level security settings:

**–** Discount

**–** GrandTotal


-----

**–** IsGeneratedFromMaintenancePlan

**–** RootWorkOrderId

##### Fields

**Field Name**
```
AccountId
Address
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the work order.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address where the work order is completed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the work order.

This is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset


-----

```
AssetWarrantyId
BusinessHoursId
CaseId
City

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset warranty term associated with the work order. This field is available in
API version 50.0 and above.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The business hours associated with the work order.

This is a relationship field.

**Relationship Name**
BusinessHours

**Relationship Type**
Lookup

**Refers To**
BusinessHours

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The case associated with the work order.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ContactId
Country
CurrencyIsoCode
Description

```

**Description**
The city where the work order is completed. Maximum length is 40 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact associated with the work order.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the work order is completed. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization. The label in the user interface
is Currency ISO Code.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work order. Try to include the steps needed to change the
work order’s status to Completed.


-----

```
Discount
Duration
DurationInMinutes
DurationType
EndDate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The weighted average of the discounts on all line items in the work
order. It can be any positive number up to 100.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated time required to complete the work order. Specify the duration
unit in the `Duration Type` field. If the Duration field on a Work Order
is null, it adopts the duration value from the Work Type object when the work
type is updated or inserted.

Note: Work order duration and work order line item duration are
independent of each other. If you want work order duration to
automatically show the sum of the work order line items’ duration, replace
the Duration field on work orders with a custom roll-up summary field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The estimated duration in minutes. For internal use only.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of the duration: Minutes or Hours.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
EntitlementId
GeocodeAccuracy
GrandTotal
IsClosed
IsGeneratedFromMaintenancePlan

```

**Description**
The date when the work order is completed. This field is blank unless you set up
an Apex trigger or quick action to populate it. For example, you can create a quick
action that sets the `EndDate` to 365 days after the `StartDate.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The entitlement associated with the work order.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address. See Compound Field
Considerations and Limitations for details on geolocation compound fields.

Note:
conref="sforce_api_objects_workorderlineitem.xml#sforce_api_objects_workorderlineitem/api_only"

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The total price of the work order with tax added.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the work order is closed (true) or open (false).

Tip: Use this field to report on closed versus open work orders.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
IsStopped
LastReferencedDate
LastViewedDate
Latitude

```

**Description**
(Read Only) Indicates that the work order was generated from a maintenance
plan (true), rather than manually created (false).

Note: This option is deselected for work orders that were generated from
maintenance plans before Summer ’18.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a milestone is paused (true) or counting down (false).
This field is available only if Enable stopped time and actual elapsed time is
selected on the Entitlement Settings page.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work order was last modified. Its label in the user interface is
```
  Last Modified Date.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the work order was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
work order is completed. Acceptable values are numbers between –90 and 90
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.


-----

```
LineItemCount
LocationId
Longitude
MaintenancePlanId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of work order line items in the work order. Its label in the user
interface is `Line Items.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location associated with the work order. For example, a work site.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
work order is completed. Acceptable values are numbers between –180 and 180
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance plan associated with the work order. When the work order is
auto-generated from a maintenance plan, this field automatically lists the related
plan.


-----

```
MaintenanceWorkRuleId
MilestoneStatus
MinimumCrewSize
OwnerId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the maintenance work rule that generated this work order. This field is
available in API version 50.0 and above.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Indicates the status of a milestone. This field is visible if an entitlement process
is applied to a work order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum crew size allowed for a crew assigned to the work order.

If you’re not using the Field Service managed package, this field serves as a
suggestion rather than a rule. If you are using the managed package, the
scheduling optimizer counts the number of service crew members on a service
crew to determine whether it fits a work order’s minimum crew size requirement.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The work order’s assigned owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
ParentWorkOrderId

```
PostWorkSummary
```
PostalCode

```
PreWorkBriefPromptTemplate
```
Pricebook2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order’s parent work order, if it has one.

Tip: Create a custom report to view a work order’s child work orders.

This is a relationship field.

**Relationship Name**
ParentWorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The summary of a completed work order that’s either entered manually or created
by an AI agent.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the work order is completed. Maximum length is 20
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the activated Pre-Work Brief prompt template.

**Type**
reference


-----

```
Priority
ProductServiceCampaignId
ProductServiceCampaignItemId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The price book associated with the work order. Adding a price book to the work
order lets you assign different price book entries to the work order’s line items.
This is only available if Product2 is enabled.

This is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the work order. The picklist includes the following values, which
can be customized:

**•** `Low`

**•** `Medium`

**•** `High`

**•** `Critical`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign associated with the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the work order.


-----

```
RecommendedCrewSize
ReturnOrderId
ReturnOrderLineItemId
RootWorkOrderId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended number of people on the service crew assigned to the work
order. For example, you might have a Minimum Crew Size of 2 and a
Recommended Crew Size of 3.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The return order line item associated with the work order.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level work order in a work order hierarchy. Depending on
where a work order lies in the hierarchy, its root could be the same as its parent.

Note: View a work order’s child work order in the Child Work Orders
related list.

This is a relationship field.

**Relationship Name**
RootWorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder


-----

```
ServiceAppointmentCount
ServiceContractId
ServiceDocumentTemplate
ServiceReportLanguage
ServiceReportTemplateId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of service appointments on the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service contract associated with the work order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The template ID which sets the template for each service document for the
Document Builder feature.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for all service reports and service report previews created for
the work order, its service appointments, and its work order line items and their
service appointments. If the field is blank, service reports are generated in the
default language in Salesforce of the person creating the report.

To appear as an option in the ServiceReportLanguage field, a language must be
[set up in Translation Workbench or be one of Salesforce’s 18 fully supported](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)
[languages. Rich text fields and service report section names aren’t translated.](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service report template that the work order uses. If you don’t specify a service
report template on a work order, it uses the service report template listed on its


-----

```
ServiceTerritoryId
SlaExitDate
SlaStartDate
StartDate

```

work type. If the work type doesn’t list a template or no work type is specified,
the work order uses the default service report template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service territory where the work order is taking place.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time that the work order exits the entitlement process.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the work order enters the entitlement process. You can update or
reset the time if you have “Edit” permission on work orders.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the work order goes into effect. This field is blank unless you set
up an Apex trigger or quick action to populate it. For example, you can create a
quick action that sets the StartDate to the date when the Status changes to In
Progress.


-----

```
State
Status
StatusCategory
StopStartDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the work order is completed. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the work order. The picklist includes the following values, which
can be customized:

**•** `New—Work order was created, but there hasn’t yet been any activity.`

**•** `In Progress—Work has begun.`

**•** `On Hold—Work is paused.`

**•** `Completed—Work is complete.`

**•** `Cannot Complete—Work could not be completed.`

**•** `Closed—All work and associated activity is complete.`

**•** `Canceled—Work is canceled, typically before any work began.`

Changing a work order’s status does not affect the status of its work order line
items or associated service appointments.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `Status Category`
field has eight default values: seven values which are identical to the default
`Status values, and a` `None` value for statuses without a status category.

If you create custom `Status` values, you must indicate which category it
belongs to. For example, if you create a `Waiting for Response` value,
you may decide that it belongs in the `On Hold category. To learn which`
[processes reference StatusCategory, see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Street
Subject
Subtotal
SuggestedMaintenanceDate
Tax

```

**Description**
Indicates when the milestone was paused. The label in the user interface is
```
  Stopped Since.

```
**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name where the work order is completed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subject of the work order. Try to describe the nature and purpose of the job
to be completed. For example, “Annual On-Site Well Maintenance.” Maximum
length is 255 characters.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The total of the work order line items’ subtotals before discounts and
taxes are applied.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The suggested date that the work order is completed. When the work order is
auto-generated from a maintenance plan, this field is automatically populated
based on the maintenance plan’s settings.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
TotalPrice
WorkOrderNumber
WorkTypeId

##### Associated Objects

```

**Description**
The total tax on the work order. You can enter a number with or without the
currency symbol and use up to two decimal places. For example, in a work order
whose total price is $100, enter $10 to apply a 10% tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The total of the work order line items’ prices. This value has discounts
applied but not tax.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An eight-digit, auto-generated number that identifies the work order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the work order. When a work type is selected, the
work order automatically inherits the work type’s `Duration, Duration`
`Type, and required skills. If the Duration` field for the work type is null, enter
the duration value.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**WorkOrderChangeEvent (API version 48.0)**
Change events are available for the object.

**WorkOrderFeed**

Feed tracking is available for the object.

**WorkOrderHistory**

History is available for tracked fields of the object.

**WorkOrderOwnerSharingRule**

Sharing rules are available for the object.

**WorkOrderShare**

Sharing is available for the object.
