#### BuyerCriteria

Represents the buyer context qualifier of locale for any buyer groups of type Market This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
CriteriaKey
CriteriaKeyType
CriteriaValue
CurrencyIsoCode
Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The label displayed to list supported markets with associated languages and
currencies.

Possible values are:

**•** `Locale`

**•** `DataCloudSegment`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Defines the type of key.

Possible values are:

**•** `SessionAttributes Session Attributes`

**•** `DataCloudObjects`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update, Nillable

**Description**
Required. The value of a `Locale. For example,` `fr-FR.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Optional. Three letter ISO currency codes associated with the buyer account record or a
locale. Auto populated if MultiCurrency is enabled in org.

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
The supported criteria in this record.

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the buyer group the criteria apply to.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the member group or Admin/Merchandiser .

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

##### Usage

BuyerCriteria is related to objects that enable a localized buyer experience. Together, these objects provide buyers with dynamic access
to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and shop in webstores
with localized languages and currencies. The related objects are as follows:

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

**BuyerCriteriaFeed on page 54**
Feed tracking is available for the object.

**BuyerCriteriaHistory on page 62**
History is available for tracked fields of the object.

**BuyerCriteriaOwnerSharingRule on page 64**
Sharing rules are available for the object.

**BuyerCriteriaShare on page 66**
Sharing is available for the object.
