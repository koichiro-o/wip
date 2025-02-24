#### PricebookEntry

Represents a product entry (an association between a Pricebook2 and Product2) in a price book.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Fields

```
Note: Salesforce Object Search Language (SOSL) allows you to search records across standard and custom objects. When filtering
records in the PriceBookEntry object using SOSL, you can only sort by fields related to Product2.

```
ActivePriceAdjustmentQuantity

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The count of active price adjustment schedules associated with the price book entry. This
field is available in API version 49.0 and later.


-----

```
CurrencyIsoCode
IsActive
IsArchived
Name
Pricebook2Id

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this price book entry is active (true) or not (false). Although you can
never delete PricebookEntry records, your client application can set this flag to `false.`
Inactive PricebookEntry records are hidden in many areas in the user interface. You can
change this flag on a PricebookEntry record as often as necessary.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the PricebookEntry has been archived (true) or not (false). This field is set
to true when the Product2 record it’s associated with is archived, or when the Pricebook2
record is archived. This field is read only. Available in API version 45.0 and later. Label is
**Archived.**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of this PricebookEntry record. This read-only field references the value in the Name
field of the Product2 record. Label is Product Name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Product2Id
ProductCode
ProductSellingModelId

```

**Description**
Required. ID of the Pricebook2 record with which this record is associated. This field must
be specified when creating Pricebook2 records. It can’t be changed in an update.

This field is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 record with which this record is associated. This field must be
specified when creating Product2 records. It can’t be changed in an update.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Product code for this record. This read-only field references the value in the ProductCode
field of the associated Product2 record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related product selling model. This field is available in API version 55.0 and later.
This field is available when Subscription Management is enabled.


-----

```
UnitPrice
UseStandardPrice

##### Usage

```

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Required. Unit price for this price book entry. You can specify a value only if
`UseStandardPrice` is set to `false. Label is List Price.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this price book entry uses the standard price defined in the standard
Pricebook2 record (true) or not (false). If set to `true, then the UnitPrice` field is
read-only, and the value is the same as the UnitPrice value in the corresponding
PricebookEntry in the standard price book (that is, the PricebookEntry record whose
`Pricebook2Id` refers to the standard price book and whose `Product2Id` and
`CurrencyIsoCode` are the same as this record). For PricebookEntry records associated
with the standard Pricebook2 record, this field must be set to `true.`


Use this object to define the association between your organization’s products (Product2) and your organization’s standard price book
or to custom price books ( Pricebook2). Create one PricebookEntry record for each standard or custom price and currency combination
for a product in a Pricebook2.

When creating these records, you must specify the IDs of the associated Pricebook2 record and Product2 record. Once these records are
created, your client application can’t update these IDs.

This object is defined only for those organizations that have products enabled as a feature. If the organization doesn’t have the products
feature enabled, then the PricebookEntry object doesn’t appear in the describeGlobal call, and you can’t access it.

If you delete a PriceBookEntry that is referenced by a line item, the line item is unaffected, but the PriceBookEntry is archived and
unavailable from the API. Deleted PriceBookEntry records can’t be recovered.

You must load the standard price for a product before you’re permitted to load its custom prices.


-----

##### Associated Objects

This object has the following associated objects. Unless otherwise noted, they’re available in the same API version as this object.

**PricebookEntryChangeEvent(API version 57.0)**
Change events are available for the object.

**PricebookEntryHistory**

History is available for tracked fields of the object.

SEE ALSO:

Overview of Salesforce Objects and Fields
