#### PaymentLinkEvent

Represents a payment link platform event. Subscribe to these events so you can listen and respond to them when they’re published.
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
PaymentLinkId

```

**Type**
picklist

**Properties**
Restricted picklist

**Description**
Type of payment link event, which triggers and event notification.

Possible values are:

**•** `Create–Payment link created.`

**•** `Delete–Payment link deleted.`

**•** `Update–Payment link property changed.`

**Type**
reference


-----

**Properties**
Nillable

**Description**
Type of payment link event. You can write code to operate conditionally on the value of this
field. For example, you can ignore a create change but get notified of updates.

This field is a relationship field.

**Relationship Name**
PaymentLink

**Relationship Type**
Lookup

**Refers To**
PaymentLink
