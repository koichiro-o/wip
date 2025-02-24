#### BillingScheduleGroup

Represents a consolidated view of all billing schedules related to the order items generated from one asset, including new orders and
amendment orders. This object is available in API version 55.0 and later.

When an order is created, a billing schedule is generated for each order item. The billing schedule group summarizes fields from each
billing schedule. For example, it summarizes financial fields such as Total Billed Amount and Total Pending Amount and billing fields
such as Billing Day of Month and Billing Term.

The billing schedule group includes schedules generated from a new order item and schedules generated from amendment order items.
The billing schedule group shows users the summarized financial data that includes any changes, such as new orders or amendments,
made to the asset.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update()

 Special Access Rules

```
This object is available if Subscription Management or Commerce Subscriptions is enabled. If your org has both Subscription Management
and Commerce Subscriptions enabled, then Subscription Management takes precedence.

##### Fields

```
BillDayOfMonth
BillToContactId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Billing Day of Month for the billing schedules that comprise the billing schedule group.

Subscription Management uses the order item's billing day of month to calculate the order
item’s next billing date, which the billing schedule then inherits. For example, an order item
can be billed on the first day of the month.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The contact related to the billing schedule group.

This field can’t be modified when related billing schedules are in processing.

This field is a relationship field.


-----

```
BillingAccountId
BillingAddress
BillingCity
BillingCountry

```

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The Salesforce account for the billing schedule group.

This field is a relationship field.

**Relationship Name**
BillingAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
[The compound form of the billing address. Read-only. See Address Compound Fields for](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_address.htm)
details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
BillingGeocodeAccuracy
BillingLatitude
BillingLongitude
BillingMethod
BillingPostalCode

```

**Description**
Details for the billing address of this billing schedule group. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
[Accuracy level of the geocode for the billing address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with BillingLongitude to specify the precise geolocation of a billing address. Acceptable
[values are numbers between –90 and 90 with up to 15 decimal places. See Compound Field](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with BillingLatitude to specify the precise geolocation of a billing address. Acceptable
[values are numbers between –180 and 180 with up to 15 decimal places. See Compound](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows the type of billing used for the source item.

Possible values are:

**•** `Evergreen`

**•** `OrderAmount`

**Type**
string


-----

```
BillingScheduleGroupNumber
BillingStartMonth
BillingState
BillingStreet
BillingTerm

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 20 characters.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated reference number for the billing schedule group.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only field used with annual billing. The field shows the numbers from 1 to 12, which
indicate the month when billing begins for an annual subscription. For example, if billing
starts in January, the value is 1; if billing starts in June, the value is 6. This field is available in
API version 58.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of this billing schedule group. Maximum size is 80 characters.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address of this billing schedule group.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
BillingTermUnit
BillingType

```

**Description**
Used with `BillingTermUnit` to define a billing cycle. For example, bill every 20 days
or every two months. In this example, the `BillingTerm` is `20` and the
`BillingTermUnit` is `days`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The frequency with which the billing schedule is invoiced.

Possible values are:

**•** `Day`

**•** `Month`

**•** `OneTime`

**•** `Quarter`

**•** `Semi-Annual`

**•** `Year`

Used with `BillingTermUnit` to define a billing cycle.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Inherited from the shared value of each billing schedule in the billing schedule group. Defines
when Subscription Management bills a product or service relative to when it’s provided to
the customer. Advance billing invoices a product or service before you provide it, while
arrears billing invoices a product or service after you provide it. Subscription Management
evaluates the billing type when it calculates an order's next billing date.

Possible values are:

**•** `Advance` – If the billing schedule is billed in advance, Subscription Management
evaluates the order’s billing day of month to choose the nearest date on or before the
order product’s start date. For example, if a monthly order product’s start date is January
1, and the order’s billing day of month is 15, the next billing date is December 15.

**•** `Arrears` – If the billing schedule is billed in arrears, Subscription Management evaluates
the order’s billing day of month to choose the nearest date after the order product’s start
date. For example, if a monthly order product’s start date is January 1 and the order’s
billing day of month is 15, the order product’s next billing date is January 15.


-----

```
CancellationDate
Controller
CurrentBillingPeriodAmount
CurrentQuantity
EffectiveNextBillingDate

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that a cancellation was made against the billing schedule. Subscription Management
doesn't invoice billing schedules past their cancellation date.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
During the invoicing process, this field determines which date is used when the billing
schedule group and billing schedule have a related field with conflicting values.

For example, when `Controller` has a value of `BillingScheduleGroup, if the`
billing schedule's billing day of month is 5 while the billing schedule group's billing day of
month is 10, the invoice is sent on the 10th day of the month.

Possible values are:

**•** `BillingScheduleGroup—The date on the billing schedule group controls.`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
This field was removed in Subscription Management API version 55.0.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
This field was removed in Subscription Management API version 55.0.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


-----

```
EndDate
LastReferencedDate
LastViewedDate
OwnerId

```

**Description**
The earliest NextBillingDate from all billing schedules in the billing schedule group.
This field is a reference field that isn't used for any features or calculations.

This field is a calculated field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The latest end date from all billing schedules in the billing schedule group.

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
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The Salesforce user who owns the billing schedule group.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


-----

```
PaymentTermId
PeriodBoundary
Product2Id

```

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the payment term used in this billing schedule group.

This field can’t be modified when related billing schedules are in processing.

This field is a relationship field.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Inherited from the order item's parent quote line item or sales transaction item. The period
boundary helps determine the start and end date of the billing periods.

Possible values are:

**•** `AlignToCalendar—the period starts on the first day of the term unit; for example,`
the first day of the month.

**•** `Anniversary—The start date determines the boundary. For example, if a monthly`
subscription starts on September 13, the subscription starts on the 13th day of each
month.

**•** `DayOfPeriod—the period starts on the day indicated by PeriodBoundaryDay.`

**•** `EndOfPeriod—the period starts on the last day of the pricing term unit.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the product for the order item represented by each billing schedule in the billing
schedule group.


-----

```
ProductName
ProrationPolicyId
ReferenceEntityId

```

This field is a relationship field.

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
The name of the product for the order item represented by each billing schedule in the
billing schedule group.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Refers to the proration policy that applies to this billing schedule group. The proration policy
defines how time periods are calculated for subscription orders. For example, whether partial
periods are allowed.

Inherited from the shared proration policy for each billing schedule in the billing schedule
group.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The asset used to create the billing schedules in the billing schedule group.

This field is a relationship field.


-----

```
ShippingAddress
ShippingCity
ShippingCountry
ShippingGeocodeAccuracy
ShippingLatitude

```

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
address

**Properties**
Filter, Nillable

**Description**
[The compound form of the shipping address. Read-only. See Address Compound Fields for](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_address.htm)
details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. City maximum size is 40
characters

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. Country maximum size is 80
characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
[Accuracy level of the geocode for the shipping address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double


-----

```
ShippingLongitude
ShippingPostalCode
ShippingState
ShippingStreet
StartDate

```

**Properties**
Filter, Nillable, Sort

**Description**
Used with ShippingLongitude to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with ShippingLatitude to specify the precise geolocation of an address. Acceptable
[values are numbers between –180 and 180 with up to 15 decimal places. See Compound](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. Postal code maximum size
is 20 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the shipping address for this billing schedule group. State maximum size is 80
characters.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street address of the shipping address for this billing schedule group. Maximum of 255
characters.

**Type**
date


-----

```
TotalBilledAmount
TotalPendingAmount
