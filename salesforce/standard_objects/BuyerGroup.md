#### BuyerGroup

Associates group qualifiers (entitlements, price books, promotions, and shipping methods) with buyer members based on buyer account
ID or on the localized language and currency of the market browsed in a webstore. This object is available in API version 57.0; amended
to support Market in version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Description

```

**Type**
string


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Buyer group details.

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
and LastReferenceDate is not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the buyer group.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
RecordTypeId
Role

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record type of the version

This field is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines a fixed or dynamic relationship to the language and currency that products,
promotions, and entitlements are displayed in.

Possible values are:

**•** `AccountBased`

**•** `Market`

**•** `DataCloudSegments`

The default value is AccountBased. When set to Market, and when the org has multiple
locales, the currency and language for qualifiers (price books, promotions, entitlements)
dynamically change as the buyer views different locale-based markets.


BuyerGroup is related to objects that enable a localized buyer experience. Together, these objects provide buyers with dynamic access
to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and shop in webstores
with localized languages and currencies. The related objects are as follows:

**•** BuyerGroup - stores keys that link member entitlements, price books, promotions, and shipping methods to either a single currency
and language or to multiple currencies and languages.

**•** BuyerCriteria - represents locales (languages and currencies) that are enabled for BuyerGroup members when they shop in webstores
with localized currencies and languages.

**•** BuyerGroupBuyerCriteria - associates a buyer group that is enabled for webstores with multiple languages and currencies with
BuyerCriteria that define those languages and currencies.


-----

**•** BuyerGroupRelatedObject - allows BuyerGroup qualifiers (entitlements, price books, and promotions) to be available in multiple
languages and currencies without duplicating the qualifiers for each language and currency.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BuyerGroupChangeEvent on page 67**
Change events are available for the object.

**BuyerGroupFeed on page 54**
Feed tracking is available for the object.

**BuyerGroupHistory on page 62**
History is available for tracked fields of the object.

**BuyerGroupOwnerSharingRule on page 64**
Sharing rules are available for the object.

**BuyerGroupShare on page 66**
Sharing is available for the object.
