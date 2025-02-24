#### CartDeliveryGroupMethod

Represents the selected delivery method for a cart delivery group used in Lightning B2B Commerce checkout. This object is available in
API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The CartDeliveryGroupMethod object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AdjustedShippingFee
Carrier
CartCheckoutSessionId
CartDeliveryGroupId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shipping fee, including `TotalAdjustmentAmount, for the delivery method.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The carrier that the buyer chose for their delivery method. Values are defined based on the
user’s shipping service. This field is available in API version 59.0 or later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID used to identify your cart checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
ClassOfService
CurrencyIsoCode
DeliveryMethodId
ExternalProvider
IsActive

```

**Description**
The ID of the cart delivery group associated with the checkout session.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The carrier class of service that the buyer chose for their delivery method. Values are defined
based on the user’s shipping service. This field is available in API version 59.0 or later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency used for your shipping fee. Default value is `USD.`

Possible values are:

**•** `USD—U.S. Dollar`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the selected order delivery method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the external shipping method provider. Optional field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Assign new delivery groups to active delivery methods. The default value is `False. This`
field is available in API version 59.0 or later.


-----

```
Name
ProcessTime
ProcessTimeUnit
ProductId
ReferenceNumber

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the delivery method.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Merchant-specified process time for the delivery method. Process time includes the time
between when an order is placed and when the shipment is given to the shipping carrier.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time used to define `ProcessTime.`

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. This product represents a delivery charge order product for a delivery using this
delivery method. For example, you could create a product that represents an overnight
express charge and assign it to an overnight express delivery method. If your store uses
[Salesforce Native Shipping, the ProductId](https://help.salesforce.com/s/articleView?id=sf.comm_set_up_native_shipping.htm&language=en_US) is selected from a non-variation product with
`Shipping` in its name. The term `Shipping` in a product name isn’t localized. If no
matching product is found, a random non-variation product is used. This field is available in
API version 59.0 or later.

**Type**
string


-----

```
ShippingFee
TotalAdjustmentAmount
TransitTimeMax
TransitTimeMin
TransitTimeUnit

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference number for an external delivery method. This field is available in API version 59.0
or later.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Shipping fee associated with the delivery method. Required field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The adjustment amount of a promotion applicable to the delivery method.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum estimate of transit time for the delivery method. Transit time includes the time
between when a shipping carrier receives a shipment and when the shipment arrives at the
delivery address.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum estimate of transit time for the delivery method. Transit time includes the time
between when a shipping carrier receives a shipment and when the shipment arrives at the
delivery address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
WebCartId

##### Usage

```

**Description**
Unit of time used to define `TransitTimeMax` and `TransitTimeMin.`

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the WebCart associated with the cart delivery group method. Required field.


Use the CartDeliveryGroupMethod object to give commerce buyers the ability to choose a delivery method for a cart delivery group.
Shipping integrations populate the delivery options that are available for a cart delivery group.
