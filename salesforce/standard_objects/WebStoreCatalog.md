#### WebStoreCatalog

Represents the collection of products associated with a store. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
You must have the B2B Commerce license and a CMS workspace to access product media.

##### Fields

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `GBP— British Pound`

**•** `USD— U.S. Dollar`

The default value is `USD.`


-----

```
LastReferencedDate
LastViewedDate
Name
ProductCatalogId
SalesStoreId

##### Associated Objects

```
**WebStoreCatalogHistory**


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
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the catalog.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the catalog, containing products.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the store that the catalog is associated with. This field is unique within your org.


History is available for tracked fields of the object.


-----
