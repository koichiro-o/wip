#### WebstoreBuyerGroup

Associates a webstore with a buyer group. Supports dynamically changing locales when buyers shop in orgs that are enabled for multiple
languages and currencies. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
BuyerGroupId
LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the buyer group this record references.

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


-----

```
LastViewedDate
Name
WebStoreId

##### Usage

```

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate isn’t null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the webstore.

This field is a relationship field.

**Relationship Name**
WebStore

**Relationship Type**
Lookup

**Refers To**
WebStore


This object can support a localized buyer experience by associating a Market-enabled webstore with a buyer group, allowing shoppers
to view their group entitlements, price books, and promotions in localized languages and currencies.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WebstoreBuyerGroupChangeEvent on page 67**
Change events are available for the object.

**WebstoreBuyerGroupFeed on page 54**
Feed tracking is available for the object.

**WebstoreBuyerGroupHistory on page 62**
History is available for tracked fields of the object.

**WebstoreBuyerGroupOwnerSharingRule on page 64**
Sharing rules are available for the object.

**WebstoreBuyerGroupShare on page 66**
Sharing is available for the object.
