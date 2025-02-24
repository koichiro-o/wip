#### ProductQuantityRule

Represents the relationship between a quantity rule and a product. This object assigns quantity rules to a product. This object is available
in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The ProductQuantityRule object is available only if the B2B Commerce license or Automotive Cloud license is enabled.

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
The ISO code for the currency that’s specified on the buyer’s account. This field is exposed
in orgs that have multicurrency enabled. Default value is `USD.`

Possible values are:

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the product quantity rule.


-----

```
ProductId
PurchaseQuantityRuleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related purchase quantity rule.

This field is a relationship field.

**Relationship Name**
PurchaseQuantityRule

**Relationship Type**
Lookup

**Refers To**
PurchaseQuantityRule

