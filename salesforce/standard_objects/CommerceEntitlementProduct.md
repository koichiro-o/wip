#### CommerceEntitlementProduct

Represents the entitlement policy for a product. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete()

 Special Access Rules

```
The CommerceEntitlementProduct object is available when you meet these requirements. The B2B Commerce license is enabled. The
Commerce Buyer and Entitlements Integrator permission is granted.

##### Fields

```
CurrencyIsoCode

```

**Type**
picklist


-----

```
Name
PolicyId
ProductId

##### Associated Objects

```

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The product entitlement policy name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the product entitlement policy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the product referenced in the entitlement policy.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommerceEntitlementProductChangeEvent on page 67**
Change events are available for the object.
