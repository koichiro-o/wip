#### WebStoreSearchProdSettings

Search settings for a WebStore product search. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
You must have a B2B Commerce or D2C Commerce commerce license to create a web store.

##### Fields

```
CurrencyIsoCode
IsExcludedFromSearch
Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code for the store’s currency.

The default value is `USD. Possible values are:`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the product is excluded from searches.

The default value is `false.`

**Type**
string


-----

```
ProductId
WebStoreId

##### Associated Objects

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the search settings for the WebStore product search.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product to search.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Webstore to search.

This field is a relationship field.

**Relationship Name**
WebStore

**Relationship Type**
Lookup

**Refers To**
WebStore


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WebStoreSearchProdSettingsChangeEvent on page 67**
Change events are available for the object.


-----
