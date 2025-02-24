#### PurchaseQuantityRule

Represents a rule that restricts the quantity of a product that can be purchased. The rule can be an increment, minimum, or maximum
rule. This object is available in API version 52.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The PurchaseQuantityRule object is available only if the B2B Commerce license is enabled.

##### Fields

```
CurrencyIsoCode
Increment
LastReferencedDate
LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD.`

Possible values are:

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Quantity of product that can be added with each increase.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Maximum
Minimum
Name
OwnerId

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate is not null, the user accessed this record or list view indirectly.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Maximum quantity that can be purchased.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Minimum quantity that can be purchased.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the purchase quantity rule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of this object.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----
