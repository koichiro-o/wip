#### PaymentIntentEvent

Represents a payment intent platform event. Subscribe to these events so you can listen and respond to them when they’re published.
For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0
and later.

[For more information about platform events, see the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/platform_events_intro.htm)

##### Supported Calls
```
describeSObjects()

 Special Access Rules

```
To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.

##### Fields

```
ChangeType

```

**Type**
picklist

**Properties**
Restricted picklist


-----

```
PaymentInitiationSourceApplication
PaymentInitiationSourceChannel

```

**Description**
Type of payment intent event that triggers an event notification. You can write code to
operate conditionally on the value of this field. For example, you can ignore an authorization
but get notified of captures.

Possible values are:

**•** `Authorize–Payment is authorized.`

**•** `AuthorizeFailure–There’s an error preventing the payment authorization`

**•** `Capture–Payment is captured.`

**•** `CaptureFailure– An error prevented the payment capture.`

**•** `Refund–Payment is refunded.`

**•** `RefundFailure–An error prevented the payment refund.`

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
Salesforce application initiating the payment. This field is available in API version 63.0 and
later.

Possible values are:

**•** `Collections`

**•** `Commerce`

**•** `Custom`

**•** `FieldService`

**•** `OrderManagement`

**•** `Payments`

**•** `Revenue`

**•** `Sales`

**•** `Scheduler`

**•** `Service`

**Type**
string

**Properties**
Nillable

**Description**
Identifies the channel in the Payment Initiation Source record for which the event occurs.
This field is available in API version 63.0 and later.


-----

```
PaymentInitiationSource
PaymentInitiationSourceProcess
PaymentIntentGuid
PaymentIntent

```

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the Payment Initiation Source record for which the event occurs. This field is available
in API version 63.0 and later.

This field is a relationship field.

**Relationship Name**
PaymentInitiationSource

**Refers To**
PaymentInitiationSource

**Type**
string

**Properties**
Nillable

**Description**
Identifies the process in the Payment Initiation Source record for which the event occurs.

**Type**
string

**Properties**
Nillable

**Description**
Identifies the GUID in the Payment Initiation Source record for which the event occurs. This
field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the PaymentIntent record for which the event occurs. This field is available in API
version 63.0 and later.

This field is a relationship field.

**Relationship Name**
PaymentIntent

**Relationship Type**
Lookup


-----

```
PaymentLink
