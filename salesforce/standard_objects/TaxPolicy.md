#### TaxPolicy

A tax policy contains a group of tax treatments, where each treatment represents parameters to determine how a particular product is
taxed for a transaction line item. Tax policies are related to products, which pass the policy on to the resulting order items. When you
activate an order, Subscription Management assigns a tax treatment to each order item based on the tax policy's DefaultTaxTreatmentId,
then uses the tax treatment to calculate tax. This object is available in API version 55.0 and later.

Each tax policy requires at least one tax treatment. We recommend determining the taxation needs for each of your products and creating
policies and treatments for each product accordingly. You can then assign your tax policies to the relevant products on your own or
through automation.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available when Subscription Management is enabled in your org.


-----

##### Fields

**Field**
```
DefaultTaxTreatmentId
Description
LastReferencedDate
LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When you order a product, the order product receives this tax treatment.

This field is a relationship field.

**Relationship Name**
DefaultTaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description for providing more information about the tax policy.

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
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.


-----

```
Name
Status
TreatmentSelection
