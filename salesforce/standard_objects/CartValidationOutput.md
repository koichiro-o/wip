#### CartValidationOutput

Associate errors to cart entities, such as cart line items, delivery groups, and the like, in a store built with B2B Commerce or D2C Commerce.
An example error is “Out of stock.” Available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The CartValidationOutput object is available only if the B2B Commerce or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
BackgroundOperationId
CartId
CurrencyIsoCode
IsDismissed
Level

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the background operation that ran the validation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related `WebCart.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is
```
  USD.Possible values are:

```
**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the validation process is finished. Default value is `false.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the type of output resulting from the validation process. Possible values are:

**•** 0 (Info)

**•** 1 (Error)


-----

```
Message
Name
RelatedEntityId
RelatedEntityPrefix
Type

```


**•** 2 (Warning)

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the message to show in the log when validation is complete. Message can be up to
255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this CartValidationOutput record. Name can be up to 255 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Foreign key to `WebCart,` `CartItem, and` `CartDeliveryGroup.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Three-character prefix for the related entity.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The `CartValidationOutput` type. Possible values are:

**•** `Entitlement`

**•** `Inventory`

**•** `Other`

**•** `Pricing`


-----

**•** `Promotions`

**•** `Shipping`

**•** `ShippingPromotions`

**•** `SystemError`

**•** `Taxes`

##### Associated Objects

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartValidationOutputChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

WebCart

CartItem

CartDeliveryGroup
