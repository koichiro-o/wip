#### Coupon

A coupon associated with a promotion. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The Coupon object is available only if the B2B Commerce license is enabled.

##### Fields

```
CouponCode
CurrencyIsoCode
Description

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Coupon code for the coupon. A buyer can use the coupon code to qualify for a promotion.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the coupon.


-----

```
EndDateTime
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end date and time when the coupon is no longer active.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the coupon.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this coupon.

This is a polymorphic relationship field.

**Relationship Name**
Owner


-----

```
PromotionId
RedemptionLimitAllBuyers
RedemptionLimitPerBuyer
StartDateTime

```

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the promotion associated with the coupon.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times this coupon can be used in total. This field is available in API version 61.0
and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times this coupon can be used per customer. This field is available in API version
61.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start date and time when the coupon is active.


-----

```
Status

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the coupon.

Possible values are:

**•** `Active`

**•** `Inactive`

The default value is `Inactive`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CouponChangeEvent on page 67 (API version 62.0)**
Change events are available for the object.
