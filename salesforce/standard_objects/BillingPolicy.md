#### BillingPolicy

```


**•** `PostingInProgress—An invoice line based on this billing period has been created`
and is in the process of being added to the invoice. Available in API version 60.0 and
later.

**•** `Voided—An invoice line based on this billing period was voided.`

**•** `VoidInProgress—An invoice line based on this billing period is in the process of`
being voided.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the billing period item. Draft billing period items aren't evaluated for invoice line
creation.

Valid values are:

**•** `Canceled`

**•** `Draft`

**•** `Reviewed`


Represents a group of billing treatments, which define the rules for how to invoice a customer for an order item. This object is available
in API version 55.0 and later.

Billing policies are related to products, which pass the policy on to the resulting order items. When an order is activated, Subscription
Management assigns a billing treatment to each order item based on the values in the `BillingTreatmentSelection` field.
Then Subscription Management uses the billing treatment to create billing schedules.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available when Subscription Management is enabled.


-----

##### Fields

**Field**
```
BillingTreatmentSelection
DefaultBillingTreatmentId
Description
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how Subscription Management assigns billing treatments to order items and to
assets related to the billing policy.

Possible values are:

**•** `Default—The value specified in the DefaultBillingTreatmentId field is automatically`
applied to order items and assets.

**•** `Manual—Users must specify the billing treatment that's applied to the order items`
and assets.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When `BillingTreatmentSelection` has a value of `Default, Subscription`
Management uses the selected billing treatment for all order items and assets related to the
billing policy.

This field is a relationship field.

**Relationship Name**
DefaultBillingTreatment

**Relationship Type**
Lookup

**Refers To**
BillingTreatment

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description that describes the billing policy.

**Type**
dateTime


-----

```
LastViewedDate
Name
Status
