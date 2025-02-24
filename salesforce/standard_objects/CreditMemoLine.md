#### CreditMemoLine

Represents product, service, adjustment, or tax line items that were included in a credit memo. This object is available in API version 48.0
and later.


-----

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
BillingAddressId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Amount of this credit memo line item if its type is Adjustment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the adjustment amount and the adjustment tax amount.

This field is available in API version 49.0 and later. This field is available when Subscription
Management is enabled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the tax related to the adjustment amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the billing address related to this credit memo line.


-----

```
ChargeAmount
ChargeAmountWithTax
ChargeTaxAmount
CreditMemoId

```

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Relationship Name**
BillingAddress

**Relationship Type**
Lookup

**Refers To**
CreditMemoAddressGroup

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Amount of this credit memo line item if its type is Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the adjustment amount and the adjustment tax amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the tax related to the charge amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the parent credit memo.

This field is a relationship field.


-----

```
CurrencyIsoCode
Description
EndDate
LineAmount
Name

```

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo line.

The default value is USD.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit memo line.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
For credit memos made from a time-based service, the end date of the line item being
credited.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the credit memo line.

This field is a calculated field. This field is available in API version 49.0 and later.

**Type**
string


-----

```
Product2Id
ReferenceEntityItemId
ReferenceEntityItemType

```

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the credit memo line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The product or service being credited in the credit memo line.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order product or invoice line corresponding to this credit memo line.

This field is a polymorphic relationship field. This field is available in API version 53.0 and
later.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItemSummary, OrderProduct, InvoiceLine

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of transaction that generated the credit memo line.

Possible values are:


-----

```
ReferenceEntityItemTypeCode
RelatedLineId
ShippingAddressId

```


**•** `DeliveryCharge`

**•** `OrderProduct`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of object that generated the credit memo line.

Possible values are:

**•** `Charge`

**•** `Product`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The credit memo line related to this line item.

This field is a relationship field.

**Relationship Name**
RelatedLine

**Relationship Type**
Lookup

**Refers To**
CreditMemoLine

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the shipping address.

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Relationship Name**
ShippingAddress

**Relationship Type**
Lookup


-----

```
StartDate
Status
TaxAmount
TaxCode
TaxDocumentNumber

```

**Refers To**
CreditMemoAddressGroup

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
For credit memo lines generated from a time-based service, the first date of the billing for
the service.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
State of the credit memo line. Inherited from the credit memo.

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Total tax for the credit memo.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The code used to calculate the tax rate for the invoice line.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The document number that tracks taxes calculated for this credit memo line.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.


-----

```
TaxEffectiveDate
TaxName
TaxRate
TotalAmount
TotalAmountWithTax
TaxStatus

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The date used to calculate the credit memo line’s `TaxAmount.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
User-defined name for applied tax.

**Type**
percent

**Properties**
Filter, Nillable, Sort, Update

**Description**
Percentage value used for calculating tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of the credit memo line before any applicable tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of tax for this credit memo line, with tax included. Sum of TotalAmount and
TaxAmount.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort


-----

```
TaxTransactionNumber
TaxTreatmentId
Type

```

**Description**
Tracks whether the taxes were calculated for this credit memo line.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `None`

The default value is None. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Tracks the transaction number of the tax calculated for this credit memo line. This field is
available in API version 55.0 and later. This field is available when Subscription Management
is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the tax treatment for the credit memo line.

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

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
The type of transaction for the invoice line.

Possible values are:


-----

**•** `Adjustment`

**•** `Charge`

**•** `Tax`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoLineFeed on page 54**
Feed tracking is available for the object.

**CreditMemoLineHistory on page 62**
History is available for tracked fields of the object.
