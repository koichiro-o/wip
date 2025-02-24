#### TaxTreatment

A tax treatment contains details about how Salesforce and external engines calculate taxes, and the tax engine to use for tax calculation.
The IsTaxable field determines whether tax is calculated for the product in the transaction. The tax code, tax engine, and product code
are sent via API to the external tax calculation service. When you invoice an order item that has a tax treatment, the invoice line inherits
the tax treatment from the order item’s related billing schedule. The invoice line’s TaxCode field is populated based on the code that
the tax engine used for calculation. This object is available in API version 55.0 and later.

Each product requires a tax policy to determine whether to apply tax. The tax treatments determine how taxable products are taxed.
Each tax policy requires at least one tax treatment. We recommend determining the taxation needs for each of your products and creating
policies and treatments for each product accordingly. You can then assign your tax policies to the relevant products on your own or
through automation.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available when Subscription Management, B2B Commerce, or D2C Commerce is enabled in your org.

##### Fields

```
Description

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
IsTaxable
LastReferencedDate
LastViewedDate
Name
ProductCode

```

**Description**
Optional user-defined description for providing more information about the tax treatment.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether Subscription Management calculates tax for order items covered by
the tax treatment. When this value is True, Subscription Management calls the CalculateTax
API for the order item during order item creation.

The default value is 'False'.

This field is available when Subscription Management is enabled.

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

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the tax treatment.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


-----

```
Status
TaxCode
TaxEngineId

```

**Description**
Code of the product that the tax treatment applies to.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the tax treatment.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference code used when tax is calculated in an external tax engine.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The tax engine for the tax treatment. A tax engine represents both an instance of a tax engine
provider as well as the merchant credentials for that specific instance. When Subscription
Management begins the tax calculation process for an order item, it uses the tax engine
from the order item’s tax treatment.

If the tax treatment’s `IsTaxable` value is True, the treatment requires a tax engine.

This field is a relationship field.

This field is available when Subscription Management is enabled.

**Relationship Name**
TaxEngine

**Relationship Type**
Lookup

**Refers To**
TaxEngine


-----

```
TaxPolicyId
