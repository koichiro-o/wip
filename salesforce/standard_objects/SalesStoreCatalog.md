#### SalesStoreCatalog

Represents the catalog associated with a store. This object is available in API version 49.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
You must have the B2B Commerce license and a CMS workspace to access a store.

##### Fields

```
CurrencyIsoCode
ImplementorType
ProductCatalogId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The default value is `USD. Possible values are:`

**•** `USD—U.S. Dollar`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of implementor. WebStoreCatalog is the only available implementor type for
SalesStoreCatalog.

**Type**
reference


-----

```
SalesStoreId

```

**Properties**
Filter, Group, Sort

**Description**
The ID that references the product catalog.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID that references the store.

