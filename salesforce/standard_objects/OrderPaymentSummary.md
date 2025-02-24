#### OrderPaymentSummary

Represents the current properties and state of payments using a single payment method that are applied to one OrderSummary. This
object is available in API version 48.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Unlike most summary objects, an OrderPaymentSummary isn’t related to a similarly named order payment object. Instead, it combines
values from multiple payment objects that use the same payment method and apply to the same OrderSummary.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AuthorizationAmount
AuthorizationReversal
Amount
AvailableToCaptureAmount
AvailableToRefundAmount
BalanceAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that has been authorized.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the AuthorizationAmount that has been reversed.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s available to be captured. Equal to
AuthorizationAmount minus (CapturedAmount and PendingCaptureAmount and
AuthorizationReversalAmount and PendingReverseAuthAmount). However, if the calculated
amount is a negative number, this value is 0.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s available to be refunded. Equal to
CapturedAmount plus PendingCaptureAmount minus (RefundedAmount and
PendingRefundAmount). However, if the calculated amount is a negative number, this value
is 0.

**Type**
currency


-----

```
CapturedAmount
CurrencyIsoCode
FullName
LastPaymentGatewayLogId

```

**Properties**
Filter, Nillable, Sort

**Description**
Total balance of all payments associated with this summary object.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that has been captured.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
the currency of the OrderSummary associated with the OrderPaymentSummary. Order
Management APIs and actions that create an OrderPaymentSummary for an OrderSummary
set this value. The default value is USD.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The full name of the payment method user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the most recent payment gateway log associated with the OrderPaymentSummary.


-----

```
LastPaymentGateway
Message
LastReferencedDate
LastViewedDate
Method
OrderSummaryId
OwnerId

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The most recent message received from the payment gateway associated with the
OrderPaymentSummary.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed a record related to this record.

This field is available in API version 49.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record. A null value can mean that this
record was only referenced (LastReferencedDate) and not viewed.

This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderPaymentSummary.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the OrderSummary associated with the OrderPaymentSummary.

**Type**
reference


-----

```
PaymentMethodId
PendingAuthorization
Amount
PendingCaptureAmount
PendingRefundAmount
PendingReverseAuth
Amount

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this OrderPaymentSummary. Default value is the user
logged in to the API to perform the create.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the payment method associated with this OrderPaymentSummary.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s pending authorization.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s pending capture.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that’s pending refund.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the AuthorizationAmount that’s pending reversal.


-----

```
 RefundedAmount
ReservedBalanceTotalAmount
 Type

##### Associated Objects

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the OrderPaymentSummary that was refunded.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field that summarizes the ReservedBalanceAmount for all
OrderPaymentSummaryReferences for the OrderPaymentSummary.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The payment method type associated with the OrderPaymentSummary. For example, visa,
```
  mastercard, check, or giftcard.

```

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**OrderPaymentSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

**OrderPaymentSummaryFeed**

Feed tracking is available for the object.

**OrderPaymentSummaryOwnerSharingRule**

Sharing rules are available for the object.

**OrderPaymentSummaryShare**

Sharing is available for the object.

SEE ALSO:

OrderSummary

Payment

PaymentAuthorization

PaymentMethod


-----
