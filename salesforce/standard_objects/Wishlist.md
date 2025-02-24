#### Wishlist

```

**Type**

**reference**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the User. This field can’t be updated.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Refers To**
Group, User


Represents a buyer-created list of WishlistItems in a store that’s built with B2B Commerce on Lightning. Available in API version
49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The Wishlist object is available only if the B2B Commerce license is enabled.

##### Fields

```
AccountId
CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the account that owns the `Wishlist.`

**Type**
picklist


-----

```
Name
OwnerId
WebStoreId
WishlistProductCount

##### Associated Objects

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD.`
Possible values are:

**•** `USD—U.S. Dollar`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `Wishlist` record. `Name` can be up to 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user or group that owns the `Wishlist.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the `WebStore` related to this `Wishlist.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The count of `WishlistItems on this` `Wishlist.` `WishlistProductCount` is a
calculated field.


This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**WishlistOwnerSharingRule on page 64**
Sharing rules are available for the object.


-----

**WishlistShare on page 66**
Sharing is available for the object.

##### Usage Notes

**•** Wishlists aren’t included in any searches.

SEE ALSO:

WishlistItem
