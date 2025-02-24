#### TaxRate

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the tax policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
To calculate tax for order products, products must have an active tax policy. Tax policies are
created with a Draft status before being assigned to a product or order product. After
activating a tax policy, you can't edit certain policy fields.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how Subscription Management chooses a tax treatment to assign to order products
related to this tax policy. In API version 55.0, only `Default` is supported.

Possible values are:

**•** `Default—The order product receives the tax treatment defined in the tax policy's`
`DefaultTreatmentId` field.

**•** `LegalEntity—Assigns a tax treatment based on matching legal entities between`
the order product and tax treatment.

**•** `Manual—Order products don't receive tax treatments based on the tax policy; users`
must provide the treatment on their own instead.


Represents a tax rate for a tax code and country. This object is available in API version 56.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The TaxRate object is available if B2B Commerce or D2C Commerce is enabled.

##### Fields

```
GeoCountryId
LastReferencedDate
LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the GeoCountry for which the tax rate applies. You can define only one tax rate per
GeoCountry and tax code combination.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't viewed it directly.


-----

```
Name
OwnerId
Priority
Rate
TaxCode

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique ID of the tax rate.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The TaxRate record owner. By default, the record owner is the user who created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The tax percentage rate that will be applied to orders.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The code used to calculate the tax rate for the invoice line.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TaxRateChangeEvent on page 67**
Change events are available for the object.

**TaxRateFeed on page 54**
Feed tracking is available for the object.

**TaxRateHistory on page 62**
History is available for tracked fields of the object.

**TaxRateOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TaxRateShare on page 66**
Sharing is available for the object.
