#### CommerceEntitlementPolicy

Represents an entitlement policy, which determines what products and prices a user can see. This object is available in API version 49.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The CommerceEntitlementPolicy object is available only if the B2B Commerce license is enabled.

##### Fields

```
CanViewPrice
CanViewProduct

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a user can view the price of a product (true) or not (false). Default
value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
CurrencyIsoCode
Description
IsActive
LastReferencedDate
LastViewedDate

```

**Description**
Determines whether a user can view the product (true) or not (false). Default value is
```
  false.

```
**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The entitlement policy description.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines if the entitlement policy is active (true) or inactive (false). Default value is
```
  false.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId

##### Associated Objects

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it can
mean that the record was only referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the entitlement policy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID for the entitlement policy owner.


This object has the following associated objects. Except where noted, these objects are available in the same API version as
CommerceEntitlementPolicy.

**CommerceEntitlementPolicyChangeEvent on page 67**
Change events are available for the object.

**CommerceEntitlementPolicyOwnerFeed on page 54**
Feed tracking is available for the object.

**CommerceEntitlementPolicyHistory on page 62**
History is available for tracked fields of the object.

**CommerceEntitlementPolicyOwnerSharingRule**

Sharing rules are available for this object.
