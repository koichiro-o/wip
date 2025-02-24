#### WishlistItem

Represents an item on a `Wishlist` in a store built with B2B Commerce for Lightning. Available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The WishListItem object is available only if the B2B Commerce for Lightning license is enabled.

##### Fields

```
CurrencyIsoCode
Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is
```
  USD.Possible values are:

```
**•** `USD—U.S. Dollar`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `WishlistItem` record. `Name` can be up to 255 characters.


-----

```
Product2Id
WishlistId

```
SEE ALSO:

Wishlist
