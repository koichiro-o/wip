#### BuyerGroupBuyerCriteria

Associates a buyer group that is enabled for webstores supporting multiple languages and currencies with BuyerCriteria that define
those languages and currencies. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
BuyerCriteriaId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the buyer criteria this record is associated with.

This field is a relationship field.

**Relationship Name**
BuyerCriteria

**Relationship Type**
Lookup


-----

```
BuyerGroupId
CurrencyIsoCode
Name

##### Usage

```

**Refers To**
BuyerCriteria

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the buyer group this record is associated with.

This field is a relationship field.

**Relationship Name**
BuyerGroup

**Relationship Type**
Lookup

**Refers To**
BuyerGroup

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Optional. Three letter ISO currency codes associated with the buyer account record or a
locale. Auto populated if MultiCurrency is enabled in org.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this record.


BuyerGroupBuyerCriteria is related to objects that enable a localized buyer experience. Together, these objects provide buyers with
dynamic access to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and
shop in webstores with localized languages and currencies. The related objects are as follows:

**•** BuyerGroup - stores keys that link member entitlements, price books, promotions, and shipping methods to either a single currency
and language or to multiple currencies and languages.

**•** BuyerCriteria - represents locales (languages and currencies) that are enabled for BuyerGroup members when they shop in webstores
with localized currencies and languages.


-----

**•** BuyerGroupBuyerCriteria - associates a buyer group that is enabled for webstores with multiple languages and currencies with
BuyerCriteria that define those languages and currencies.

**•** BuyerGroupRelatedObject - allows BuyerGroup qualifiers (entitlements, price books, and promotions) to be available in multiple
languages and currencies without duplicating the qualifiers for each language and currency.
