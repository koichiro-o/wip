#### WebCartAdjustmentBasis

Coupons that trigger promotions for the cart. When a customer tries to add a coupon to the cart, the store looks for promotions associated
with the coupon. If a promotion results in a price adjustment, a WebCartAdjusmentBasis record is created. This object is available in API
version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AdjustmentBasisDetail

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Coupon code for the coupon associated with the promotion.


-----

```
AdjustmentBasisReferenceId
CurrencyIsoCode
Name
WebCartId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Foreign key reference to the coupon.

This field is a relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency ISO code of the cart.

Possible values are:

**•** `EUR`

**•** `USD`

The default value is `USD.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the WebCartAdjustmentBasis record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the cart.

This field is a relationship field.


-----

**Relationship Name**
WebCart

**Relationship Type**
Lookup

**Refers To**
WebCart

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WebCartAdjustmentBasisChangeEvent on page 67**
Change events are available for the object.
