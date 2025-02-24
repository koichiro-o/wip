#### ReturnOrderLineItem

Represents a specific product that is returned or repaired as part of a return order in Field service, or a specific order item that is returned
as part of a return order in Order Management. This object is available in API version 42.0 and later.

Return orders are available in Lightning Experience, Salesforce Classic, the Salesforce mobile app, the Field Service mobile app for Android
and iOS, and communities built using Salesforce Tabs + Visualforce.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

Field Service or Order Management must be enabled.

##### Fields

```
AssetId
ChangeOrderItemId
CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the return order line item. One or more of the following
fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId, and
ProductRequestLineItemId.

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
Create, Filter, Group, Nillable, Sort

**Description**
ID of the change order item associated with the return order line item.

This field is available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
ChangeOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
Description
DestinationLocationId
GrossUnitPrice

```

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for the currency of the original Order associated with the
ReturnOrderLineItem.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes or context about the return order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location where the items are being returned to. For example, if the return
order tracks the return of products from a technician’s van to a warehouse, the
warehouse is the destination location.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
LastReferencedDate
LastViewedDate
OrderItemId
OrderItemSummaryId

```

**Description**
Unit price, including tax, of the product represented by the associated order item
summary.

This field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order line item was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the return order line item was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order product associated with the return order line item. One or more of the
following fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId,
and ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
OrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
ProcessingPlan
Product2Id
ProductItemId

```

**Description**
ID of the order item summary associated with the return order line item.

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the preferred fate of the items following their return. Available values
are:

**•** `Repair—Repair the items and return them to the owner`

**•** `Discard—Discard the items`

**•** `Salvage—Salvage the items’ working parts`

**•** `Restock—Return the items to your inventory`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product associated with the return order line item. One or more of the
following fields must be filled out: AssetId, OrderItemId, Product2Id, ProductItemId,
and ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product item representing the location of the product at the start of the
return. One or more of the following fields must be filled out: AssetId, OrderItemId,
Product2Id, ProductItemId, and ProductRequestLineItemId.

This is a relationship field.


-----

```
ProductRequestLineItemId
ProductServiceCampaignId
ProductServiceCampaignItemId
QuantityExpected

```

**Relationship Name**
ProductItem

**Relationship Type**
Lookup

**Refers To**
ProductItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product request line item associated with the return order line item. One or
more of the following fields must be filled out: AssetId, OrderItemId, Product2Id,
ProductItemId, and ProductRequestLineItemId.

This is a relationship field.

**Relationship Name**
ProductRequestLineItem

**Relationship Type**
Lookup

**Refers To**
ProductRequestLineItem

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product service campaign associated with the return order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product service campaign item associated with the return order line item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
QuantityReceived
QuantityRejected
QuantityReturned
QuantityUnitOfMeasure
ReasonForRejection

```

**Description**
The quantity of items expected to be returned.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual quantity of items received for return.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The quantity of items rejected for return.

This field is available in API version 50.0 and later.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The quantity of items being returned. If multiple types of products are being
returned, track each product in a different return order line item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the returned items; for example, kilograms or liters. Quantity Unit of
Measure picklist values are inherited from the Quantity Unit of Measure field on
products.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


-----

```
ReasonForReturn
ReasonForChangeText
RepaymentMethod

```

**Description**
Reason for rejecting returned items on this return order line item.

Possible values are:

**•** `Damaged Item`

**•** `Expired Warranty`

**•** `Missing Item or Part`

**•** `Wrong Item`

The default value is `Missing Item or Part.`

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the items are being returned. Available values are:

**•** `Damaged`

**•** `Defective`

**•** `Duplicate Order`

**•** `Wrong Item`

**•** `Wrong Quantity`

**•** `Not Satisfied`

**•** `Outdated`

**•** `Other`

The default value is `Damaged.`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Details about the reason for return change

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


-----

```
ReturnOrderId
ReturnOrderLineItemNumber
SourceLocationId

```

**Description**
The method by which the customer or owner will be reimbursed for the items
being returned. Available values are:

**•** `Replace—The items will be replaced`

**•** `Refund—The items will be returned and the owner will be refunded`

**•** `Credit—The items will be returned and the owner will receive credit for`
them

**•** `Return—The items will be returned to the owner (for example, following`
their repair)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The return order that the return order line item belongs to.

This is a relationship field.

**Relationship Name**
ReturnOrder

**Relationship Type**
Lookup

**Refers To**
ReturnOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) Auto-generated number that identifies the return order line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The items’ location at the start of the return or repair. For example, if the return
order tracks the return of products from a technician’s service vehicle to a
warehouse, the service vehicle is the source location.

This is a relationship field.


-----

```
TotalAdjustmentAmount
TotalAdjustmentAmountWithTax
TotalAdjustmentTaxAmount
TotalAmount

```

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of all price adjustments applied to the return order line item.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the return order line item,
inclusive of tax. This amount is equal to TotalAdjustmentAmount +
TotalAdjustmentTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalLineAmount
TotalLineAmountWithTax
TotalLineTaxAmount
TotalPrice

```

**Description**
Total, including adjustments and tax, of the return order line item.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Total, not including adjustments or tax, of the return order line item.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the return order line item, inclusive of tax. This amount is equal to
TotalLineAmount + TotalLineTaxAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments but not tax, of the return order line item. Equal to
UnitPrice times Quantity.

This is a calculated field.


-----

```
TotalTaxAmount
Type
TypeCode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

This is a calculated field.

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of the return order line item. Matches the type of the associated order item
summary. Delivery Charge indicates that the return order line item represents a
delivery charge. Fee indicates that it represents another type of fee, such as a
return fee. Order Product indicates that it represents any other type of product,
service, or charge. Each type corresponds to one type code, shown here in
parentheses.

Possible values are:

**•** `Delivery Charge (Charge)`

**•** `Fee (Charge)` This value is available in API v56.0 and later.

**•** `Order Product (Product)`

This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type code of the return order line item. Matches the type code of the associated
order item summary. Processing depends on this value. Charge indicates that
the return order line item represents a delivery charge. Product indicates that it
represents an other type of product, service, or charge. Each type category
corresponds to one or more types.

Possible values are:

**•** `Charge`

**•** `Product`

This field is available in API version 50.0 and later.


-----

```
UnitPrice

##### Associated Objects

```

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Unit price of the return order line item.

This field is available in API version 50.0 and later.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ReturnOrderLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ReturnOrderLineItemFeed**

Feed tracking is available for the object.

**ReturnOrderLineItemHistory**

History is available for tracked fields of the object.
