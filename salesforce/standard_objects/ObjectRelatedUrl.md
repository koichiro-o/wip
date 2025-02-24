#### ObjectRelatedUrl

Represents a URL slug for a Product or Category page on a B2B Commerce or D2C Commerce LWR site, or a custom object, account, or
contact page on an enhanced LWR Experience Cloud site. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), undelete(),
update(), upsert()

 Special Access Rules

```
Your org must have B2B Commerce or D2C Commerce license enabled for commerce use cases. ObjectRelatedUrl is available for Product2
and ProductCategory records in Commerce, and on custom object, account and contact record pages in enhanced LWR sites.

##### Fields

```
LanguageCode

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The combined language and locale ISO code, which controls the language of the
object-related URL. The maximum length is 8 characters.


-----

```
Name
ParentId
Scope
UniqueIndex

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the object-related URL. This field isn’t editable.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the parent record that the `UrlName` refers to. `ParentId` can point
only to Product2, ProductCategory, and custom object, account, and contact record pages.

This field is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory, account, contact, and custom objects

Availability in API versions:

**•** Product2 and ProductCategory in LWR Commerce stores (available in API version 58.0 and
later)

**•** Custom object pages on enhanced LWR sites (available in API version 60.0 and later)

**•** Account and contact pages on enhanced LWR sites (available in API version 61.0 and later)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Helps ensure uniqueness of the UrlName field across all records with the same
Scope and LanguageCode values. The maximum length is 18 characters.

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort


-----

```
UrlName

```

**Description**
Ensures uniqueness for each record within your org and creates an index for lookup. This
field isn’t editable.

This field is a calculated field.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The URL slug for the record.


Note: When creating a query, for example, SELECT UrlName From ObjectRelatedUrl WHERE Scope='01t',
the WHERE condition must use `Id,` `UniqueIndex,` `Scope, or` `ParentId.`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ObjectRelatedUrlChangeEvent on page 67 (API version 62.0)**
Change events are available for the object.
