#### BuyerGroupRelatedObject

Used to associate currencies and supported ship-to countries with a buyer group and its price books, promotions, and entitlements.
Supports buyer experience when buyer group members shop in stores enabled for multiple locales. This object is available in API version
58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
BuyerGroupRelatedObject is availble only if the org is Market Enabled (Commerce.orgHasCommerceMarketEnabled).

##### Fields

```
BuyerGroupId

```

**Type**
reference


-----

```
LastReferencedDate
LastViewedDate
Name
ObjectType

```

**Properties**
Create, Filter, Group, Sort, Update

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

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate is not null, the user accessed this record or list view indirectly..

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
ObjectValues

##### Usage

```

**Description**
Required. The names displayed in the picklist showing the ObjectValues - currency and
ship-to countries.

Possible values are:

**•** `DefaultCurrency`  - Default Currency

**•** `SupportedShipToCountries`  - Supported Ship-to Countries

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Optional. Values for ObjectType. The actual currency and supported ship-to countries. Possible
values are:

**•** Three-letter ISO currency code associated with the buyer account or a supported locale.

**•** ISO country code for supported ship-to countries.


BuyerGroupRelatedObject is related to objects that enable a localized buyer experience. Together, these objects provide buyers with
dynamic access to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and
shop in webstores with localized languages and currencies. The related objects are as follows:

**•** BuyerGroup - stores keys that link member entitlements, price books, promotions, and shipping methods to either a single currency
and language or to multiple currencies and languages.

**•** BuyerCriteria - represents locales (languages and currencies) that are enabled for BuyerGroup members when they shop in webstores
with localized currencies and languages.

**•** BuyerGroupBuyerCriteria - associates a buyer group that is enabled for webstores with multiple languages and currencies with
BuyerCriteria that define those languages and currencies.

**•** BuyerGroupRelatedObject - allows BuyerGroup qualifiers (entitlements, price books, and promotions) to be available in multiple
languages and currencies without duplicating the qualifiers for each language and currency.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BuyerGroupRelatedObjectChangeEvent on page 67**
Change events are available for the object.

**BuyerGroupRelatedObjectFeed on page 54**
Feed tracking is available for the object.

**BuyerGroupRelatedObjectHistory on page 62**
History is available for tracked fields of the object.


-----
