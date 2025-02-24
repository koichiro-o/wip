#### Pricebook2

Represents a price book that contains the list of products that your org sells.

Note: Price books are represented by Pricebook2 objects. As of API version 8.0, the Pricebook object is no longer available. Requests
containing Pricebook are refused, and responses don’t contain the Pricebook object.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Description
IsActive
IsArchived

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the price book.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the price book is active (true) or not (false). Inactive price books are
hidden in many areas in the user interface. You can change this field’s value as often as
necessary. Label is Active.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the price book has been archived (true) or not (false). This field is read
only.


-----

```
IsDeleted
IsStandard
LastReferencedDate
LastViewedDate
Name
ValidFrom

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the price book has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the price book is the standard price book for the org (true) or not
(false). Every org has one standard price book—all other price books are custom price
books.

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this object. This field is read-only for the standard price book. Label is
**Price Book Name.**

**Type**
dateTime


-----

```
ValidTo

##### Usage

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a Commerce price book is initially valid. If this field is `null, the`
price book is valid immediately when active. Available in API version 48.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a Commerce price book is valid to. If this field is `null, the price`
book is valid until it’s deactivated. Available in API version 48.0 and later.


A price book is a list of products that your org sells.

**•** Each org has one standard price book that defines the standard or generic list price for each product or service that it sells.

**•** An org can have multiple custom price books to use for specialized purposes, such as for discounts, different channels or markets,
or select accounts or opportunities. While your client application can create, delete, and update custom price books, your client
application can only update the standard price book.

**•** For some orgs, the standard price book is the only price needed. If you set up other price books, you can reference the standard
price book when setting up list prices in custom price books.

Use this object to query standard and custom price books that have been configured for your org. A common use of this object is to
allow your client application to obtain valid Pricebook2 object IDs for use when configuring PricebookEntry records via the API.

Your client application can perform the following tasks on PricebookEntry objects:

**•** Query

**•** Create for the standard price book or custom price books.

**•** Update

**•** Delete

**•** Change the `IsActive` field when creating or updating records

##### PriceBook2, Product2, and PricebookEntry Relationships

In the API:

**•** Price books are represented by Pricebook2 records (as of version 8.0, the Pricebook object is no longer available).

**•** Products are represented by Product2 records (as of version 8.0, the Product object is no longer available).

**•** Each price book contains zero or more entries (represented by PricebookEntry records) that specify the products that are associated
with the price book. A price book entry defines the price for which you sell a product at a particular currency.


-----

These objects are defined only for those orgs that have products enabled as a feature. If the org doesn’t have the products feature
enabled, the Pricebook2 object doesn’t appear in the `describeGlobal()` call, and you can’t access it via the API.

If you delete a Pricebook2 while a line item references PricebookEntry in the price book, the line item is unaffected, but the Pricebook2
is archived and unavailable from the API.

For a visual diagram of the relationships between Pricebook2 and other objects, see Product and Schedule Objects.

##### Price Book Setup

The process of setting up a price book via the API usually means:

**1. Load product data into Product2 records (creating one Product2 record for each product that you want to add).**

**2. For each Product2 record, create a PricebookEntry that links the Product2 record to the standard Pricebook2. Define a standard price**
for a product at a given currency (if you have multicurrency enabled) before defining a price for that product in the same currency
in a custom price book.

**3. Create a Pricebook2 record to represent a custom price book.**

**4. For each Pricebook2 record, creating a PricebookEntry for every Product2 that you want to add, specifying unique properties for**
each PricebookEntry (such as the `UnitPrice` and `CurrencyIsoCode) as needed.`

##### Code Sample—Java


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**Pricebook2ChangeEvent (API version 48.0)**
Change events are available for the object.

**Pricebook2History**

History is available for tracked fields of the object.
