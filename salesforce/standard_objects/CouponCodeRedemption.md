#### CouponCodeRedemption

Tracks each coupon code redemption. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available through the B2B Commerce license. To access this object, the Promotions Coupon Redemption Limit user
permission must be assigned.

##### Fields

```
Buyer

```

**Type**
string

**Properties**
Create, Filter, Group, Sort


-----

```
CouponId
Name
OwnerId
Transaction

```

**Description**
Information about the buyer. Can be any buyer-specific information.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the redeemed coupon.

This field is a relationship field.

**Relationship Name**
Coupon

**Relationship Type**
Lookup

**Refers To**
Coupon

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Salesforce generated coupon code, such as CCR-000000002. Can’t be edited.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the coupon code redemption.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string


-----

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
ID of the transaction where the coupon code was redeemed. Must be a valid cart ID.
