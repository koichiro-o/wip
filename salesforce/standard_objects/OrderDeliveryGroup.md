#### OrderDeliveryGroup

A group of order items that share a delivery method and address. The delivery method and address are used during the fulfillment
process, such as shipping as a gift, downloading, picking up in store, or shipping to a standard address This object is available in API
version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.


-----

##### Fields

**Field**
```
DeliverToAddress
DeliverToCity
DeliverToCompanyName
DeliverToCountry
DeliverToFullFirstName
DeliverToFullLastName

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The delivery group’s order items are delivered to this address. Created based on the values
of the other DeliverTo fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City address value. Sent to DeliverToAddress.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country address value. Sent to DeliverToAddress

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**


-----

```
DeliverToFullName
DeliverToFullSalutation
DeliverToGeocodeAccuracy
DeliverToLatitude
DeliverToLongitude

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Possible values are:

**•** `Dr.`

**•** `Mr.`

**•** `Mrs.`

**•** `Ms.`

**•** `Prof.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Geocode accuracy address value. Sent to DeliverToAddress.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude address value. Sent to DeliverToAddress.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Longitude address value. Sent to DeliverToAddress.


-----

```
DeliverToName
DeliverToPostalCode
DeliverToState
DeliverToStreet
DeliveryInstructions
Description

```

**Type**
string

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Name of the delivery recipient. Sent to DeliverToAddress.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code address value. Sent to DeliverToAddress.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State address value. Sent to DeliverToAddress.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address value. Sent to DeliverToAddress.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text field for users to add other delivery instructions.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
User-defined description for this delivery group.


-----

```
DesiredDeliveryDate
EmailAddress
GiftMessage
GrandTotalAmount
IsGift
OrderDeliveryGroupNumber

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The buyer’s target delivery date for the order items included in the delivery group.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The buyer’s email address.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An optional gift message that the buyer can define if they’re sending the order items as a
gift to another recipient. Applies to all order items in the delivery group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the group’s total delivery amount and total tax amount.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
All items in the delivery group are gifts.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
OrderDeliveryMethodId
OrderId
PhoneNumber
PromisedDeliveryDate
RelatedDeliveryGroupId
TotalAdjustmentAmount

```

**Description**
Unique number used for referencing this order delivery group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the order delivery method related to this order delivery group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent order for this order delivery group. An order can have multiple order delivery
groups.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the buyer.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Merchant-defined date that the items in this group will be delivered to the customer. Usually
defined based on an estimated date from the shipping provider.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The original delivery group. Used for reference in change order scenarios.

**Type**
currency


-----

```
TotalAdjustmentAmtWithTax
TotalAdjustmentTaxAmount
TotalAmount
TotalLineAmount

```

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all adjustments (of type Delivery Charge) made to order items in the order delivery
group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all adjustments (of type Delivery Charge) made to order items in the order delivery
group, including tax.

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order Management
license. Commerce Orders fields are available only in Lightning Experience.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all adjustments (of type Delivery Charge) made to tax lines for order items in the
order delivery group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all Total Amount fields (of type Delivery Charge) on order items within this delivery
group. On an order item, the total amount equals the quantity multiplied by the unit price,
including adjustments and tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of order items (of the type Delivery Charge). On an order item, the total line amount
equals the quantity multiplied by the unit price, before adjustments or tax.


-----

```
TotalLineAmtWithTax
TotalLineTaxAmount
TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all `TotalLineAmtWithTax fields (of type Delivery Charge) on order items`
within this delivery group. On an order item, the total line amount with tax equals the quantity
multiplied by the unit price, plus tax, before adjustments.

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order Management
license. Commerce Orders fields are available only in Lightning Experience.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all Total Line Tax Amount fields (of type Delivery Charge) on order items within
this delivery group. On an order item, the total line tax amount equals the total tax for that
line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all Total Tax Amount fields (of type Delivery Charge) on order items within this
order delivery group.

