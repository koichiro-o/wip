#### InvoiceLine

Represents the amount that a buyer must pay for a product, service, or fee. Invoice lines are created based on the amount of an order
line. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update()

 Special Access Rules

```
This object is available when Order Management or Subscription Management is enabled.

##### Fields

```
AdjustmentAmount
AdjustmentAmountWithTax
AdjustmentTaxAmount
Balance

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of adjustments made to the invoice line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of adjustment amounts, including associated taxes related to the invoice line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of tax adjustments to the invoice line.

This field is available in API version 55.0 and later.

**Type**
currency


-----

```
BillingAddressId
BillingScheduleGroupId
BillingScheduleId

```

**Properties**
Filter, Nillable, Sort

**Description**
The outstanding balance for an invoice line. This is equal to the invoice’s total amount with
tax after deducting the payments made.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup field to an InvoiceAddressGroup containing the billing address for the invoice line.
Assign one InvoiceAddressGroup to the invoiceLine's BillingAddressID, and another
InvoiceAddressGroup to the invoiceLine's ShippingAddressId.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
BillingAddress

**Relationship Type**
Lookup

**Refers To**
InvoiceAddressGroup

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
BillingScheduleGroup

**Refers To**
BillingScheduleGroup

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the billing schedule for the invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.


-----

```
ChargeAmount
ChargeAmountWithTax
ChargeTaxAmount
ConvertedNegAmount
Description

```

**Relationship Name**
BillingSchedule

**Relationship Type**
Lookup

**Refers To**
BillingSchedule

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Sum of charges made to the invoice line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount on a charge invoice line, including tax.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax to be applied on a charge invoice line.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount from an invoice line that is converted to credit.

This field is available in API version 56.0 and later.

**Type**
string


-----

```
GroupReferenceEntityItemId
HasMultipleItems
InvoiceId

```

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the invoice line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Grouping field for adjustment line items.

This field is a polymorphic relationship field.

**Relationship Name**
GroupReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, OrderItemAdjustmentLineItem

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this field merges items from the same billing period.

The default value is `false.`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The invoice that contains this invoice line.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice


-----

```
InvoiceLineEndDate
InvoiceLineStartDate
InvoiceStatus
LegalEntityAccountingPeriodId
LegalEntityId

```

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
For invoice lines made from a time-based service, the end date of the billing for the service.

**Type**
date

**Properties**
Filter, Group, Sort, Update

**Description**
For invoice lines made from a time-based service, the first date of the billing for the service.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
State of the invoice line. Inherited from the invoice’s status.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
LegalEntityAccountingPeriod

**Refers To**
LegalEntyAccountingPeriod

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

**Relationship Name**
LegalEntity


-----

```
LineAmount
Name
NetCreditsApplied
NetPaymentsApplied
Product2Id

```

**Refers To**
LegalEntity

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of the invoice line.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the invoice line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total credit memo line amount applied to the invoice line. This amount is calculated by
subtracting the unapplied credit memo line amount from the applied credit memo line
amount.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total payment applied to the invoice line. This amount is calculated by subtracting the
unapplied payment amount from the applied payment amount.

This field is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update


-----

```
Quantity
ReferenceEntityItemId
ReferenceEntityItemType

```

**Description**
The product that was charged or ordered to create the invoice line.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
double

**Properties**
Filter, Nillable, Sort, Update

**Description**
Number of units of the order product that created the invoice line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order item or adjustment item that created the invoice line.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItem, OrderItemAdjustmentLineItem

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of transaction that created the invoice line.

Possible values are:

**•** `DeliveryCharge—Charge`

**•** `Fee—Charge. This value is available in API version 56.0 and later.`


-----

```
ReferenceEntityItemTypeCode
RelatedLineId
ShippingAddressId

```


**•** `OrderProduct—Product`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of object that created the invoice line.

Possible values are:

**•** `Charge`

**•** `Product`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The original invoice line that was adjusted or taxed.

This field is a relationship field.

**Relationship Name**
RelatedLine

**Relationship Type**
Lookup

**Refers To**
InvoiceLine

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the shipping address associated with the invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
ShippingAddress

**Relationship Type**
Lookup

**Refers To**
InvoiceAddressGroup


-----

```
TaxAmount
TaxCode
TaxDocumentNumber
TaxEffectiveDate
TaxName
TaxRate

```

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Total tax for the invoice line.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The code used to calculate tax rate for the invoice line.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the latest record in the external tax engine in which this invoice line item is
included.

This field is available in API version 55.0 and later.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The date used to calculate the invoice line’s `TaxAmount.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
User-defined name for the applied tax.

**Type**
percent

**Properties**
Filter, Nillable, Sort, Update


-----

```
TaxTransactionNumber
TaxTreatmentId
Type
UnitPrice

```

**Description**
Percentage value used for calculating tax.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the transaction in the external tax engine in which the taxes for the line were
calculated for the invoice line.

This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tax treatment used on this invoice line.

This field is a relationship field. This field is available in API version 55.0 and later.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows the type of transaction for the invoice line.

Possible values are:

**•** `Adjustment`

**•** `Charge`

**•** `Tax`

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update


-----

**Description**
Price for one unit of the item on the invoice line.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceLineFeed on page 54**
Feed tracking is available for the object.

**InvoiceLineHistory on page 62**
History is available for tracked fields of the object.

**InvoiceLineOwnerSharingRule on page 64**
Sharing rules are available for the object.

**InvoiceLineShare on page 66**
Sharing is available for the object.
