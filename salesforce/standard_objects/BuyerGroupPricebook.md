#### BuyerGroupPricebook

Represents a buyer group price book used in Lightning B2B Commerce. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The BuyerGroupPricebook object is available only if the B2B Commerce license is enabled.


-----

##### Fields

**Field**
```
BuyerGroupId
IsActive
LastReferencedDate
LastViewedDate
Name
Pricebook2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the buyer group that the price book record is assigned to.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the BuyerGroupPricebook is active (true) or not (false). Default
value is `false.`

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

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Buyer Group Price Book record.

**Type**
reference


-----

```
Priority

##### Usage

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the price book assigned to the buyer group.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The sequential priority used to determine the price of a product. This field is only available
for web stores that use the Priority pricing strategy.


Use the BuyerGroupPricebook object to assign a price book to a set of buyer users. Assigning a price book to a buyer group allows buyers
within that buyer group to retrieve product prices from the price book. When a buyer has multiple price book assignments, including
multiple prices for the same product, the store Pricing Strategy determines the price.
