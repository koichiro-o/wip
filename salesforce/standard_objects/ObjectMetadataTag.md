#### ObjectMetadataTag

Represents a meta tag for a store page. Meta tags in HTML documents provide structured data used by search engines for ranking and
to show content in search results. This object is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), undelete(),
update(), upsert()

 Special Access Rules

```
This object is available only if the B2B Commerce or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
CurrencyIsoCode
Language
Name
RecordId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The language of the page meta tag.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the page meta tag.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product or product category with which this record is associated.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory

Availability in API versions:

**•** Product2 is available in API versions 60.0 and later


-----

```
TagType
Value
