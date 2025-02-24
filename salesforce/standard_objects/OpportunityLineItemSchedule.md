#### OpportunityLineItemSchedule

Represents information about the quantity, revenue distribution, and delivery dates for a particular OpportunityLineItem.

In API version 38.0 and later, when an OpportunityLineItem record is created for a product with a previously established schedule, an
OpportunityLineItemSchedule record is also created.


-----

In API version 46.0 and later, this object supports custom fields, validation rules, and Apex triggers. Deleting a schedule now also invokes
delete triggers. If customizable product schedules are enabled, you can use custom fields in default schedules and customize their layout.
But if you’ve applied validation rules or Apex triggers, they’re bypassed when they’re first inserted.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Fields

```
```
CurrencyIsoCode
Description
OpportunityLineItemId
Quantity

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Restricted picklist, Update

**Description**
Available only for organizations with the multicurrency feature enabled.
Contains the ISO code for any currency allowed by the organization. This field
is available in version 10.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the opportunity line item schedule. Limit: 80 characters.
Label is Comments.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the associated `OpportunityLineItem.`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. The total number of units to be scheduled in a quantity schedule.


-----

```
Revenue
ScheduleDate
Type

##### Allowed Type Field Values

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The revenue that should be recognized, or the quantity that should be
shipped, or both - depending upon the value of `Type.`

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The date the associated `OpportunityLineItem` is to be
scheduled for an event: delivery, shipping, or any other date you wish to track.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the schedule. Required when inserting an
OpportunityLineItemSchedule. Valid values include Quantity, Revenue,
or Both.


The allowed `Type` values for an `OpportunityLineItemSchedule` depend on the product-level schedule preferences and
whether the line item has any existing schedules. The following criteria must be met:

**•** The Product2 on which the OpportunityLineItem is based must have the appropriate CanUseRevenueSchedule or
`CanUseQuantitySchedule` fields (or both) set to `true.`

**•** When you create a schedule for a line item that does not have any existing schedules, you can specify any valid value.

**•** If you create a schedule for a line item that already has existing schedules, the new schedule must be consistent with the existing
schedules. The following matrix outlines the allowable values:

**Value of HasRevenueSchedule** **Value of HasQuantitySchedule** **Allowable Type Values**
**on line item** **on line item**

false false `Revenue,` `Quantity, both`

false true `Quantity`

true false `Revenue`


-----

true true both

##### Allowed Quantity and Revenue Field Values

The allowable `Quantity` and `Revenue` field values depend on the value of the `Type` field:

**Type Value** **Allowable Quantity Value** **Allowable Revenue Value**

`Revenue` Null Non-null

`Quantity` Non-null Null

both Non-null Non-null

The `Quantity` and `Revenue` fields have the following restrictions when this object is updated:

**•** For a schedule of `Type Quantity, you can’t update a null Revenue` value to non-null. Likewise for a schedule of `Type`
`Revenue, you can’t update a null Quantity` value to non-null.

**•** You can’t null out the `Quantity` field for a schedule of `Type Quantity. Likewise you can’t null out the` `Revenue` field for
a schedule of `Type Revenue.`

**•** You can’t null out either the `Revenue` or `Quantity` fields for a schedule of type `Both.`

##### Usage

`OpportunityLineItemSchedule` supports two types of schedules:

**•** `Quantity` schedules

**•** `Revenue` schedules

The user must have edit access rights on the Opportunity in order to create or update line item schedules on that opportunity.

##### Products and Schedules Must Be Enabled

The `OpportunityLineItemSchedule` object is defined only for those organizations that have the products and schedules
features enabled. If the organization does not have the products and schedules features, the OpportunityLineItemSchedule
object is not returned in a describe, and you can't describe or query OpportunityLineItemSchedule records.

##### Effects on Opportunities and Opportunity Line Items

`OpportunityLineItemSchedule` records affect opportunities and opportunity line items in the following ways:

**•** Inserting an `OpportunityLineItemSchedule` of `Type` “Revenue” or “Quantity” increments the `TotalPrice` field on
the `OpportunityLineItem` by the OpportunityLineItemSchedule Revenue amount. Inserting an
`OpportunityLineItemSchedule` of Type Quantity or `Both` increments the `Quantity` field on the
`OpportunityLineItem` by the OpportunityLineItemSchedule Quantity amount.

**•** Creating an OpportunityLineItemSchedule record affects the original opportunity:


-----

**1.** The Opportunity Amount is incremented the by OpportunityLineItemSchedule revenue amount

**2. The Opportunity ExpectedRevenue** is incremented by the line item schedule amount multiplied by the Opportunity
```
   Probability

```
**•** Deleting an `OpportunityLineItemSchedule` has a similar effect on the related `OpportunityLineItemand`
Opportunity. Deleting an OpportunityLineItemSchedule decrements the OpportunityLineItemTotalPrice
by the deleted `OpportunityLineItemSchedule Quantity` or `Revenue` amount. The Opportunity Amount is also
decremented by the `OpportunityLineItemSchedule Quantity` or `Revenue` amount, and the Opportunity
`ExpectedRevenue` is reduced by `OpportunityLineItemSchedule Quantity` or `Revenue` amount multiplied
by the Opportunity Probability.

##### Deleting an Opportunity Line Item Schedule

Deleting the last remaining schedule will set the corresponding HasQuantitySchedule or HasRevenueSchedule flags (or
both) to `false` on the parent line item.

SEE ALSO:

OpportunityLineItem

Product2
