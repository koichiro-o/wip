#### ServiceContract

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For the field that you use to track work status, specifies whether the values are for completed
or in-progress work.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Specifies the values that you use to indicate completed and in-progress work status. Valid
values are `Completed,` `InProgress, and` `Paused.`


Represents a customer support contract (business agreement). This object is available in API version 18.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AccountId

```

**Type**
reference


-----

```
ActivationDate
AdditionalDiscount
ApprovalStatus

```
`BillingAddress` (beta)
```
BillingCity

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the account associated with the service contract.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The initial day the service contract went into effect (whereas StartDate may include
a renewal date).

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Extra discount percentage for the service contract. Available in API version 55.0 and
later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Approval status of the service contract.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the billing address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.


-----

```
BillingCountry
BillingCountryCode
BillingLatitude
BillingLongitude
BillingPostalCode
BillingState

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the service contract’s billing address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with BillingLatitude to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address. Maximum size is 20 characters.

**Type**
string

**Properties**
Group, Sort, Filter, Nillable


-----

```
BillingStateCode
BillingStreet
ContactId
ContractNumber
Description
Discount

```

**Description**
Details for the billing address. Maximum size is 20 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the service contract’s billing address.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Street address for the billing address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the Contact associated with the service contract. Must be a valid ID.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Unique number automatically assigned to the service contract.

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the service contract.

**Type**
percent

**Properties**
Filter, Nillable, Sort


-----

```
EndDate
GrandTotal
IsDeleted
LastReferencedDate
LastViewedDate

```

**Description**

Discount percentage for the service contract.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last day the service contract is in effect.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price of the service contract plus shipping and taxes.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is
null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.


-----

```
LineItemCount
Name
OwnerId
ParentServiceContractId
Pricebook2Id
RootServiceContractId

```

**Type**
int

**Properties**
Filter, Nillable, Group, Sort

**Description**
Number of ContractLineItem records associated with the service contract.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the service contract.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns the service contract.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service contract’s parent service contract, if it has one.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Pricebook2 associated with the service contract. Must be a valid ID.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

`ShippingAddress` (beta)
```
ShippingCity
ShippingCountry
ShippingCountryCode
ShippingLatitude

```

**Description**
(Read only) The top-level service contract in a service contract hierarchy. Depending
on where a service contract lies in the hierarchy, its root could be the same as its parent.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Maximum size is 40 characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details of the shipping address. Country maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the service contract’s shipping address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLongitude` to specify the precise geolocation of a shipping
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.


-----

```
ShippingLongitude
ShippingPostalCode
ShippingState
ShippingStateCode
ShippingStreet
SpecialTerms

```

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
Create, Filter, Nillable, Update

**Description**
Details of the shipping address. Postal code maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
Details of the shipping address. State maximum size is 20 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the service contract’s shipping address.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
The street address of the shipping address. Maximum of 255 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
StartDate
Status
Subtotal
Tax
Term
TotalPrice

```

**Description**
Any terms specifically agreed to and tracked in the service contract.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The first day the service contract is in effect.

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
The status of the service contract, such as Inactive.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Total of the service contract line items (products) before discounts, taxes, and shipping
are applied.

**Type**
currency

**Properties**
Create, Filter, Nillable, Update

**Description**
Total taxes for the service contract.

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
Number of months that the service contract is valid.

**Type**
currency


-----

**Properties**
Filter, Nillable

**Description**
Total of the contract line items (products) after discounts and before taxes and shipping.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceContractChangeEvent (API version 44.0)**
Change events are available for the object.

**ServiceContractFeed (API version 23.0)**
Feed tracking is available for the object.

**ServiceContractHistory**

History is available for tracked fields of the object.

**ServiceContractOwnerSharingRule**

Sharing rules are available for the object.

**ServiceContractShare**

Sharing is available for the object.

SEE ALSO:

ServiceContractOwnerSharingRule
