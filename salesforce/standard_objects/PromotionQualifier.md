#### PromotionQualifier

Represents the product, product category, or order that you want to target with your promotion qualifier in a B2B or D2C store. This
object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The PromotionQualifier object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.


-----

```
ExternalQualifier
LastReferencedDate
LastViewedDate
MinimumAmount
MinimumQuantity
Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A qualifying product or product category stored outside of Salesforce. This field is available
in API version 56.0 and later.

Note: This field is available through the API only.

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
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum dollar amount that a buyer must purchase to qualify for the promotion.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum quantity that a buyer must purchase to qualify for the promotion.

**Type**
string


-----

```
PromotionId
PromotionTierId
QualifierId

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the promotion qualifier.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the promotion that you want to associate with your promotion qualifier.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the promotion tier associated with the qualifier. Only used with tiered promotions.

This is a relationship field.

This field is available in API version 57.0 and later.

**Relationship Name**
PromotionTier

**Relationship Type**
Lookup

**Refers To**
PromotionTier

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the qualifier.


-----

```
QualifierOperator
QualifierProductCategoryName
QualifierProductName
QualifierProductSku

```

This is a polymorphic relationship field.

**Relationship Name**
Qualifier

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Possible values are:

**•** `EQUAL_TO`

**•** `NONE`

**•** `NOT_EQUAL_TO`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product category referenced in the qualifier. This field is available in API
version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the product referenced in the qualifier. This field is available in API version 55.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock keeping unit of the product referenced in the qualifier. This field is available in API
version 55.0 and later.


-----

```
QualifierRuleCriteriaType
QualifierType

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of qualifier rule criteria.

Possible values are:

**•** `All`

**•** `Any`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of qualifier that you want to add to the promotion. Product applies the qualifier
to a single product, `ProductCategory` to a predetermined group of products, and
`TransactionTotal` to the entire order.

Possible values are:

**•** `Product`

**•** `ProductCategory`

**•** `TransactionTotal`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PromotionQualifierFeed on page 54**
Feed tracking is available for the object.


-----

**PromotionQualifierHistory on page 62**
History is available for tracked fields of the object.

SEE ALSO:

Promotion

PromotionMarketSegment

PromotionQualifier

PromotionSegment

PromotionSegmentBuyerGroup

PromotionSegmentSalesStore

PromotionTarget

PromotionTier
