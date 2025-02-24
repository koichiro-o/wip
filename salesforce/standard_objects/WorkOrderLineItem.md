#### WorkOrderLineItem

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the work order being tracked. The history is displayed on the detail page
for this record.

This is a relationship field.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder


Represents a subtask on a work order in field service. This object is available in API version 36.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

Work orders or Field Service must be enabled.

##### Fields

**Field Name**
```
Address
AssetId
AssetWarrantyId
City

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address where the line item is completed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the work order line item. The asset is not automatically
inherited from the parent work order.

This is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset warranty term associated with the work order line item. This field is
available in API version 50.0 and above.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Country
CurrencyIsoCode
Description
Discount
Duration

```

**Description**
The city where the line item is completed. Maximum length is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the line item is completed. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization. The label in the user interface
is Currency ISO Code.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the work order line item. Try to describe the steps needed to
mark the line item Completed.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percent discount to apply to the line item. You can enter a number with or
without the percent symbol, and you can use up to two decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated time required to complete the line item. Specify the duration unit
in the Duration Type field. If the Duration field on a Work Order is null,


-----

```
DurationInMinutes
DurationType
EndDate
GeocodeAccuracy

```

it adopts the duration value from the Work Type object when the work type is
updated or inserted.

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

**Description**
The date on which the line item is completed. This field is blank unless you set
up an Apex trigger or quick action to populate it. For example, you can create a
quick action that sets the EndDate to 365 days after the StartDate.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

Possible values are:

**•** `Address`


-----

```
IsClosed
IsGeneratedFromMaintenancePlan
LastReferencedDate
LastViewedDate

```


**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the line item has been closed. Changing the line item’s status
to Closed causes this checkbox to be selected in the user interface (sets
`IsClosed` to true).

Tip: Use this field to report on closed versus open work order line items.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Identifies whether the work order line item is generated from a maintenance
plan.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last modified. Its label in the user interface is
```
  Last Modified Date.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Latitude
LineItemNumber
ListPrice
LocationId

```

**Description**
The date when the line item was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where
the line item is completed. Acceptable values are numbers between –90 and 90
with up to 15 decimal places.

Note: This field is available in the API only.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number that identifies the work order line item. Each work
order’s line items start at 1.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**

The price of the line item (product) as listed in its corresponding price book entry.
If a price book entry isn’t specified, the list price defaults to zero.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

A location associated with the work order line item. For example, a work site.

This is a relationship field.

**Relationship Name**
Location

**Relationship Type**
Lookup


-----

```
Longitude
MaintenancePlanId
MaintenanceWorkRuleId
MinimumCrewSize
OrderId

```

**Refers To**
Location

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address where
the line item is completed. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.

Note: This field is available in the API only.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance plan associated with the work order line item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the maintenance work rule that generated this line item. This field is available
in API version 50.0 and above.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum crew size allowed for a crew assigned to the line item.

If you’re not using the Field Service managed package, this field serves as a
suggestion rather than a rule. If you are using the managed package, the
scheduling optimizer counts the number of service crew members on a service
crew to determine whether it fits a work order line item’s minimum crew size
requirement.

**Type**
reference


-----

```
ParentWorkOrderLineItemId
PostalCode
PricebookEntryId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order associated with the line item. For example, you may need to order
replacement parts before you can complete the line item.

This is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The line item’s parent work order line item, if it has one.

Tip: Create a custom report to view a line item’s child line items.

This is a relationship field.

**Relationship Name**
ParentWorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the line item is completed. Maximum length is 20
characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Priority
Product2Id

```

**Description**
The price book entry (product) associated with the line item. The label in the user
interface is Product. This field’s lookup search only returns products that are
included in the work order’s price book.

This is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the line item. The picklist includes the following values, which can
be customized:

**•** `Low`

**•** `Medium`

**•** `High`

**•** `Critical`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
(Read only) The product associated with the price book entry. This field is not
available in the user interface. For best results, use the PricebookEntryId
field in any custom code or layouts.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2


-----

```
ProductServiceCampaignId
ProductServiceCampaignItemId
Quantity
RecommendedCrewSize
ReturnOrderId
ReturnOrderLineItemId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product service campaign associated with the work order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the work order line item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Number of units of the line item included in the associated work order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended number of people on the service crew assigned to the line
item. For example, you might have a Minimum Crew Size of 2 and a
Recommended Crew Size of 3.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The return order associated with the work order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
RootWorkOrderLineItemId
ServiceAppointmentCount
ServiceDocumentTemplate
ServiceReportTemplateId

```

**Description**
The return order line item associated with the work order line item.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level line item in a work order line item hierarchy. Depending
on where a line item lies in the hierarchy, its root could be the same as its parent.

Note: View a line item’s child line items in the Child Work Order Line
Items related list.

This is a relationship field.

**Relationship Name**
RootWorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of service appointments on the work order line item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The template ID which sets the template for each service document for the
Document Builder feature.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ServiceTerritoryId
StartDate
State
Status

```

**Description**
The service report template that the line item uses. If you don’t specify a service
report template on a work order line item, it uses the service report template
listed on its work type. If the work type doesn’t list a template or no work type is
specified, the line item uses the default service report template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service territory where the line item is completed.

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
Create, Filter, Nillable, Sort, Update

**Description**
The date on which the line item goes into effect. This field is blank unless you
set up an Apex trigger or quick action to populate it. For example, you can create
a quick action that sets the StartDate to the date when the Status changes to In
Progress.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the line item is completed. Maximum length is 80 characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


-----

```
StatusCategory
Street
Subject
Subtotal

```

**Description**
The status of the line item. The picklist includes the following values, which can
be customized:

**•** `New—Line item was created, but there hasn’t yet been any activity.`

**•** `In Progress—Work has begun.`

**•** `On Hold—Work is paused.`

**•** `Completed—Work is complete.`

**•** `Cannot Complete—Work could not be completed.`

**•** `Closed—All work and associated activity is complete.`

**•** `Canceled—Work is canceled, typically before any work began.`

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
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name where the line item is completed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A word or phrase describing the line item.

**Type**
currency


-----

```
SuggestedMaintenanceDate
TotalPrice
UnitPrice
WorkOrderId

```

**Properties**
Filter, Nillable, Sort

**Description**

(Read only) The line item’s unit price multiplied by the quantity.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when maintenance work is planned.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The line item’s subtotal with discounts applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Initially, the unit price for a work order line item is the line item’s list price from
the price book, but you can change it.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The line item’s parent work order. Because work order line items must be
associated with a work order, this is a required field.

This is a relationship field.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder


-----

```
WorkTypeId

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the line item. When a work type is selected, the
line item automatically inherits the work type’s Duration, Duration Type,
and required skills. If the `Duration` field for the work type is null, enter the
duration value.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType


A work order line item is a child record of a work order. It represents a specific subtask on a work order.

For example, suppose a customer purchased a truck from you. The truck is represented as an asset in your Salesforce org. After some
time, the truck needs both headlight bulbs replaced. Here’s one way that you can use work orders and work order line items to track
the repair.

**1. Create a work order named “Replace Headlight Bulbs” from the asset record detail page.**

**2. Add three work order line items to the work order: “Replace Left Headlight Bulb,” “Replace Right Headlight Bulb,” and “Test Headlights.”**

**3. Assign the work order to a technician via a queue.**

**4. As the technician completes each line item, he or she marks the item Completed.**

**5. When all the line items are complete, the technician marks the work order Completed.**

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkOrderLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**WorkOrderLineItemFeed**

Feed tracking is available for the object.

**WorkOrderLineItemHistory**

History is available for tracked fields of the object.


-----
