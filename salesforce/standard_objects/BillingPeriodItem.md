#### BillingPeriodItem

Represents one payment period for a subscription. The billing period item is used to pass billing information to an invoice line item in
Subscription Management. This object is available in API version 55.0 and later.

When a billing schedule is invoiced, Subscription Management creates a billing period item to store the billing and payment information
that’s passed to an invoice line. Subscription Management next creates an invoice line for billing period items that match the invoice's
target date. One billing period item is created for each billing period in the billing schedule. For example, a one-year subscription that's
billed quarterly creates a billing schedule with four billing period items.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

##### Fields

```
Amount
BillingPeriodEndDate
BillingPeriodItemNumber

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Price for the billing period item. Used to calculate the invoice line's Amount field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used to calculate the invoice line's end date.

**Type**
string


-----

```
BillingPeriodStartDate
BillingScheduleId
CurrencyIsoCode
InvoiceBatchRunId

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined number that refers to the billing period item.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used to calculate the invoice line's start date.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Parent billing schedule of the billing period item.

This field is a relationship field.

**Relationship Name**
BillingSchedule

**Relationship Type**
Lookup

**Refers To**
BillingSchedule

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the org. Available only for orgs with the
multicurrency feature enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Parent invoice batch run of the billing period item.

This field is a relationship field.


-----

```
InvoiceLineId
InvoiceStatus

```

**Relationship Name**
InvoiceBatchRun

**Relationship Type**
Lookup

**Refers To**
InvoiceBatchRun

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field looks up to the invoice line that's generated from the billing period item. This field
is populated only when a billing period item is generated via an invoice batch run. Otherwise,
this field is empty.

This field is a relationship field.

**Relationship Name**
InvoiceLine

**Relationship Type**
Lookup

**Refers To**
InvoiceLine

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the invoice that contains the invoice line created from the billing period item.

Valid values are:

**•** `Canceled—The invoice for this billing period item was canceled.`

**•** `Draft—The invoice has been created but hasn’t been posted. Available in API version`
60.0 and later.

**•** `DraftInProgress—The invoice hasn’t been created yet. When the invoice is`
created, the `InvoiceStatus` field value is changed to `Draft. If the invoice`
generation process fails, the `InvoiceStatus` field value shows
```
   DraftInProgress. Available in API version 60.0 and later.

```
**•** `Error—The invoice for this billing period item was generated in error.`

**•** `Pending—The invoice for this billing period item is being generated.`

**•** `Posted—An invoice line based on this billing period has been created and added`
successfully to the invoice.


-----

```
Status
