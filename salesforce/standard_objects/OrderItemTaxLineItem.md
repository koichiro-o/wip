#### OrderItemTaxLineItem

The tax amount that has been applied to an order item. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

```

-----

##### Special Access Rules

To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.

##### Fields

```
Amount
CalculationReferenceNumber
Description
Name
OrderId

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The total amount of the tax line. The value is rounded to the nearest possible amount
associated with the currency of the order item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Reference number provided by the tax provider, such as Stripe, in the tax calculation API
response.

This field is available in API version 62.0.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Users can add a custom description to the record to provide additional detail.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the tax line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
OrderItemAdjustmentLineItemId
OrderItemId
Rate
ReferenceNumber
RelatedTaxLineItemId

```

**Description**
ID of the parent order for the order item related to the tax line

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order item adjustment line item that the tax line applies to.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The order item that the tax line applies to.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage value of the tax. Null if the tax is a flat amount.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Reference number provided by the tax provider (like Stripe) for each line item in the tax
calculation API call. Use this unique ID to revert taxes during cancellation or return of an
order.

This field is available in API version 62.0.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The original order item tax line. Useful for reference in change order scenarios.


-----

```
TaxEffectiveDate
Type

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date used to calculate the effective tax rate. This field may require an update to
accommodate different buyer time zones.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows whether the amount on the tax line is an estimate or the final calculated amount.
Doesn’t set a value by default. Users can define automation to set and change the value as
needed.

Possible values are:

**•** `Actual`

**•** `Estimated`

