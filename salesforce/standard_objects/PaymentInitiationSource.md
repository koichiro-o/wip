#### PaymentInitiationSource

Represents the originating source of a payment. This information helps other Salesforce products integrate with Salesforce Payments.
This object is available in API version 63.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Special Access Rules

```
To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

##### Fields

```
AccountId

```

**Type**
reference


-----

```
Application
Channel
CollectionPlanId

```

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The account record that initiated this payment.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Salesforce application initiating the payment.

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
Filter, Group, Nillable, Sort, Update

**Description**
The origin of the submitted payment. For example, D2C, virtual terminal, or merchant MOTO
(mail order or phone order).

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update


-----

```
ContactId
CurrencyIsoCode
LastReferencedDate

```

**Description**
The collection plan record that submitted payment. This field is available only for
merchant-initiated payment collections. For example, a merchant collects an outstanding
balance using a Pay Now payment link or over the phone.

This field is a relationship field.

**Relationship Name**
CollectionPlan

**Refers To**
CollectionPlan

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The contact record of the contact that made the payment.

This field is a relationship field.

**Relationship Name**
Contact

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. This field contains
the ISO code for any currency allowed by the organization.

Possible values are:

**•** `AUD—Australian Dollar`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
OpportunityId
OrderSummaryId

```

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view (LastReferencedDate),
but not viewed it.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the payment initiation source record. For example,
d9e01178-b6878-2f4b-a14d-b0132b7ret67

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The opportunity record that made the payment.

This field is a relationship field.

**Relationship Name**
Opportunity

**Refers To**
Opportunity

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order summary record that initiated the payment. This field is available with Salesforce
Order Management and Commerce applications.

This field is a relationship field.


-----

```
PaymentScheduleItemId
Process
QuoteId
ServiceAppointmentId

```

**Relationship Name**
OrderSummary

**Refers To**
OrderSummary

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The payment schedule item record that initiated the payment. This field is available only
with the Scheduler application.

This field is a relationship field.

**Relationship Name**
PaymentScheduleItem

**Refers To**
PaymentSchedleItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Component within the application that’s initiating the payment. Maximum length of the
string is 255 characters. For example, managed or custom checkout, product description
page (PDP).

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The quote record that initiated the payment.

This field is a relationship field.

**Relationship Name**
Quote

**Refers To**
Quote

**Type**
reference


-----

```
SiteId
WebCartId
WebStoreId

```

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The service appointment record that initiated the payment. This field is available only with
the Field Service application.

This field is a relationship field.

**Relationship Name**
ServiceAppointment

**Refers To**
Appointment

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The site record that initiated the payment. This field is for applications that don't have a web
store, but created a digital experience site to accept payments

This field is a relationship field.

**Relationship Name**
Site

**Refers To**
Site

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The web cart record that submitted the payment.

This field is a relationship field.

**Relationship Name**
WebCart

**Refers To**
WebCart

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update


-----

```
WorkOrderId
WorkOrderLineItemId
