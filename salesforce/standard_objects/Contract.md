#### Contract

Represents a contract (a business agreement) associated with an Account.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AccountId
ActivatedById
ActivatedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort,Update

**Description**
Required. ID of the Account associated with this contract.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort,Update

**Description**
ID of the User who activated this contract.

This field is a relationship field.

**Relationship Name**
ActivatedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime


-----

```
ActivityMetricId
ActivityMetricRollupId
BillingAddress
BillingCity

```

**Properties**
Filter, Nillable, Sort, Update

**Description**
Date and time when this contract was activated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the billing address. Read-only. See Address Compound Fields for
details on compound address fields.

**Type**
string


-----

```
BillingCountry
BillingCountryCode
BillingGeocodeAccuracy
BillingLatitude

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. The maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the contract's billing address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy of the geocode for the billing address.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double


-----

```
BillingLongitude
BillingPostalCode
BillingState
BillingStateCode
BillingStreet

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. The maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the contract's billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for the billing address.


-----

```
CompanySignedDate
CompanySignedId
ContractNumber
ContractTerm
CustomerSignedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date your organization signed the contract.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user who signed the contract.

This field is a relationship field.

**Relationship Name**
CompanySigned

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the contract.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of months that the contract is valid.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the customer signed the contract.


-----

```
CustomerSignedId
CustomerSignedTitle
Description
EndDate
IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Contact who signed this contract.

This field is a relationship field.

**Relationship Name**
CustomerSigned

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the customer who signed the contract.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the contract.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort,

**Description**
Read-only. Calculated end date of the contract. This value is calculated by adding the
`ContractTerm` to the StartDate. If the Auto-calculate Contract End Date setting
is disabled, the contract end date is editable.

**Type**
boolean

**Properties**
Defaulted on create or filter


-----

```
LastActivityDate
LastApprovedDate
LastReferencedDate
LastViewedDate
OwnerExpirationNotice

```

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
The label is Deleted.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is the most recent:

**•** The due date of the most recent event is logged against the record.

**•** The due date of the most recently closed task associated with the record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Last date the contract was approved.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view (LastReferencedDate)
but didn’t view it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
OwnerId
Pricebook2Id
PricingSource
RecordTypeId

```

**Description**
Number of days ahead of the contract end date (15, 30, 45, 60, 90, and 120). Used to notify
the owner in advance that the contract is ending.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the contract.

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the pricebook, if any, associated with this contract.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Source of the pricing for the contract.

Valid values are:

**•** `LastTransaction`

**•** `PriceBookListPrice—Price Book or List Price`

Available in API version 60.0 and later.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update


-----

```
RenewalTerm2
RenewalTermUnit
ShippingAddress
ShippingCity

```

**Description**
ID of the record type assigned to this object.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The default subscription term for renewals. For example, if the Renewal Term Unit is months
and you want a 6-month term, set the Renewal Term to 6. Available in API version 60.0 and
later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of time for a subscription term.

Valid values are:

**•** `Annual—UI label is Years`

**•** `Months`

**•** `Quarterly—Available in API version 61.0 and later.`

**•** `Semi-Annual—Available in API version 61.0 and later.`

Available in API version 60.0 and later.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields for
details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. City maximum size is 40 characters.


-----

```
ShippingCountry
ShippingCountryCode
ShippingGeocodeAccuracy
ShippingLatitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. Country maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the contract's shipping address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy of the geocode for the shipping address.

Valid values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

Available in API version 60.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
ShippingLongitude
ShippingPostalCode
ShippingState
ShippingStateCode
ShippingStreet
SpecialTerms

```

**Description**
Used with ShippingLongitude to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. The postal code maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. The maximum size for the state is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the contract's shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address of the shipping address. The maximum size is 255 characters.

**Type**
textarea


-----

```
StartDate
Status
StatusCode

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Special terms that apply to the contract.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort,Update

**Description**
Start date for this contract. The label is Contract Start Date.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The picklist of values that indicate order status. Each value is within one of two status
categories defined in `StatusCode. For example, the status picklist may contain: Ready`
to Ship, Shipped, Received as values within the Activated `StatusCode.`

Valid values are:

**•** `Activated`

**•** `Draft`

**•** `In Approval Process`

Available in API version 60.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status category for the contract. A contract can be Draft, InApproval, or Activated. Label
is Status Category.

Valid values are:

**•** `Activated`

**•** `Draft`

**•** `InApproval`

Available in API version 60.0 and later.


-----

##### Usage

The Contract object represents a business agreement.

The `Status` field specifies the current state of a contract. Status strings (defined in the ContractStatus object) represent its current
state (Draft, `InApproval, or` `Activated).`

Client applications must initially create a Contract in a non-Activated state. Client applications can subsequently activate a Contract by
updating it and setting the value in its `Status` field to `Activated; however, the` `Status` field is the only field you can update
when activating the Contract.

After a Contract has been activated, your client application can't change its status; however, before activation, your client application
can change the status value from Draft to InApproval via the API. Also, your client application can delete contracts whose status
is `Draft` or `InApproval` but not when a contract status is Activated.

Client applications can use the API to create, update, delete, and query any Attachment associated with a contract.

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 46.0)**
Change events are available for the object.

**ContractFeed (API version 18.0)**
Feed tracking is available for the object.

**ContractHistory**

History is available for tracked fields of the object.

SEE ALSO:

ContractContactRole

ContractStatus
