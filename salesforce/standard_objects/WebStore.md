#### WebStore

Represents a B2B or D2C store. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(),describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
You must:

**•** Have CRUD read permission to access this object


-----

**•** Be a Salesforce admin with CRUD create permission to create a new record in this object

##### Fields

```
CheckoutTimeToLive
CheckoutValidAfterDate
Country
CurrencyIsoCode
DefaultLanguage

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Amount of time in minutes that a B2B checkout stays active and doesn’t expire. If you use a
`Null` value, your checkout never expires. If you use a `0` value, checkout is disabled. This
field is available in API version 50.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A timestamp in the default server timezone (GMT). All B2B checkouts that start before this
date are considered expired. A `Null value means that all checkouts are valid. Example`
format: 2020-07-14T14:27:00.000Z. This field is available in API version 50.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Two-digit ISO code of the store's country. Purchases can be shipped only to the country
assigned to the store. This field is available in API version 55.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The default value is `USD. Possible values are:`

**•** `USD—U.S. Dollar`

**Type**
picklist


-----

```
DefaultTaxLocaleType
DefaultTaxPolicyId

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The primary supported language for your store.

Possible values include:

**•** `da— Danish`

**•** `de— German`

**•** `en_US— English`

**•** `es— Spanish`

**•** `en_MX— Spanish (Mexico)`

**•** `fi— Finnish`

**•** `fr— French`

**•** `it— Italian`

**•** `ja— Japanese`

**•** `ko— Korean`

**•** `nl_NL— Dutch`

**•** `no— Norwegian`

**•** `pt_BR— Portuguese (Brazil)`

**•** `ru— Russian`

**•** `sv— Swedish`

**•** `th— Thai`

**•** `zh_CN— Chinese (Simplified)`

**•** `zh_TW— Chinese (Traditional)`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Tax type of the store. This field is available in API version 55.0 and later.

Possible values include:

**•** `Gross— Prices include tax`

**•** `Net— Prices don't include tax`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Description
ExternalReference
GuestBuyerProfileId
GuestCartTimeToLive

```

**Description**
The default tax policy for the store. This field is a relationship field. This field is available in
API version 56.0 and later.

**Relationship Name**
DefaultTaxPolicy

**Relationship Type**
Lookup

**Refers To**
TaxPolicy

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the store.

**Type**
textarea

**Properties**
Nillable

**Description**
Identifies the instance of B2C Commerce. Format is <<SiteId>>@<<InstanceId>>.
This field is available in API version 54.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the GuestBuyerProfile associated with the store. GuestBuyerProfile determines what
buyer groups are part of the profile. The guest buyer groups then determine the entitlements
and pricing of products for the guest buyer.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The time that a guest cart is to remain valid before it expires. The default value is 168 hours
(7 days), and the maximum value is 720 hours (30 days). This field is available in API version
52.0 and later.


-----

```
LastReferencedDate
LastViewedDate
LocationId
MaxValuesPerFacet
Name
OptionsAutoFacetingEnabled

```

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
record might only have been referenced and not viewed directly.

**Type**
reference

**Properties**
Filter, Group, Nillible, Sort

**Description**
The location associated with the address.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of values that can be added to a facet.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the catalog.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
OptionsCartAsyncProcessingEnabled
OptionsCartCalculateEnabled
OptionsCartToOrderAutoCustomFieldMapping
OptionsDuplicateCartItemsEnabled

```

**Description**
If enabled (True), the most relevant search facets are automatically returned, in addition to
the configured search facets, in the product search results. If disabled (False), only the
[configured search facets are returned. The default is False.See Add Product Search Filters](https://help.salesforce.com/s/articleView?id=sf.comm_search_add_filters.htm&language=en_US)
[(Facets).for more information. This field is available in API version 50.0 or later.](https://help.salesforce.com/s/articleView?id=sf.comm_search_add_filters.htm&language=en_US)

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether add-to-cart requests are processed asynchronously (True) or not (False).
The default value is `True. This field is available in API version 59.0 or later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the cart calculate extension is enabled (True) or not (False). The default
value is `False.`

This field is available in API version 59.0 or later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether custom field mapping for cart and order objects is enabled (True) or not
(False). The default value is `True.`

This field is available in API version 57.0 or later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether a cart can include multiple items with the same product ID (True) or not
(False). The default value is `False.`

This field is available in API version 59.0 or later.


-----

```
OptionsGuestBrowsingEnabled
OptionsGuestCartEnabled
OptionsGuestCheckoutEnabled
OptionsPreserveGuestCartEnabled
OptionsSkipAdditionalEntitlementCheckForSearch

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether guest browsing is enabled for this store. Set the option to True to allow
guest buyers access to products in the store.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether guest cart access is enabled for a store created with an LWR template. Set
the option to True to allow guest buyers access to products in the store.

This field is available in API version 58.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether guest checkout access is enabled for a store created with an LWR template.
Set the option to True to allow guest buyers access to products in the store.

This field is available in API version 58.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether cart contents are preserved when a guest logs in to the store. Set the
option to `True to preserve guest carts.`

This field is available in API version 60.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
OrderActivationStatus
OrderLifeCycleType
OwnerId

```

**Description**
By default, user entitlement checks are run as part of a search index rebuild and again when
product search results are returned. Skips the second check to promote faster search
performance. Set the option to `True` to skip additional entitlement checks on a search.
This field is available in API version 52.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Status of the order. This field is available in API version 55.0 and later.

Possible values are:

**•** `Activated`

**•** `Draft`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether order summaries are processed with Order Management features:

**•** `Managed—`

**•** `Unmanaged—`

This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates the owner of the store. This field is available in API 53.0 or later.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
PaginationSize
PricingStrategy
ProductGrouping
SortByPriceBookId

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Dimensions of the page.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `LowestPrice— Best Price`

**•** `Priority— Priority Price.`

The default value is `LowestPrice.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether product variations are listed individually in search results or are
represented by the parent product, which links to its children. Possible values are:

**•** `NoGrouping—Variations are listed individually in search results.`

**•** `VariationParent—The parent product is returned in search results with a link to`
its children.

The default value is `VariationParent.`

This field is available in API version 52.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the price book used for the sorting rule. This field is available in API version 55.0
and later.

This is a relationship field.

**Relationship Name**
SortByPriceBook


-----

```
StrikethroughPricebookId
SupportedCurrencies
SupportedLanguages
Type

```

**Relationship Type**
Lookup

**Refers To**
Pricebook2

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the strikethrough price book.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**
Currencies supported in the store.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**
Languages supported in the store.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Type of store that can be created.

Possible values are:

**•** `B2B`

**•** `B2C`

**•** `B2CE`

**•** `OMS`

The default value is `B2B.`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WebStoreEvent (API version 55.0)**
Change events are available for the object.

SEE ALSO:

WebStoreNetwork
