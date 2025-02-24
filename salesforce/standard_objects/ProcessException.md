#### ProcessException

Represents a business exception, such as a processing failure on an order summary. A separate process is required to resolve the failure
that caused the process exception before processing can continue. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AttachedToId

```

**Type**
reference


-----

```
CaseId
Category

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the object associated with the ProcessException.

This field is a polymorphic relationship field.

**Relationship Name**
AttachedTo

**Relationship Type**
Lookup

**Refers To**
CreditMemo, FulfillmentOrder, Invoice, Order, OrderItem, OrderItemSummary,
OrderPaymentSummary, OrderSummary, Payment, PaymentAuthorization, Refund,
ReturnOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the case associated with the ProcessException.

This field is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ProcessingException type. You can customize the category picklist to represent your business
processes.

Possible values are:

**•** `Fulfillment`

**•** `Invoicing`

**•** `Order Activation`

**•** `Order Approval`


-----

```
CurrencyIsoCode
Description
ExternalReference
FlowOrchestrationInstRelaObj

```


**•** `Payment`

The default value is `Order Activation.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
the currency of the OrderSummary associated with the ProcessException.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Detailed description of the ProcessException.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of external entities associated with the ProcessException.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The flow orchestration instance related object associated with this record.

This field is a relationship field.

**Relationship Name**
FlowOrchInstRelaObj


-----

```
LastReferencedDate
LastViewedDate
Message
OrderSummaryId

```

**Relationship Type**
Lookup

**Refers To**
FlowOrchestrationInstRelaObj

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last viewed this record. A null value can mean that this
record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Short description of the ProcessException

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the OrderSummary associated with the ProcessException. The ProcessException
component is displayed on this OrderSummary.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary


-----

```
OwnerId
Priority
ProcessExceptionNumber
Severity

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who currently owns this ProcessException. Default value is the User who
created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Resolution priority for the ProcessException. You can customize the priority picklist to
represent your business processes.

Possible values are:

**•** `High`

**•** `Low`

The default value is `Low.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the ProcessException, formatted as PE-(00000000).

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


-----

```
SeverityCategory
Status

```

**Description**
Severity of the ProcessException. Each severity value corresponds to one severity category.
You can customize the severity picklist to represent your business processes. If you customize
the severity picklist, include at least one severity value for each severity category.

Possible values are:

**•** `High`

**•** `Low`

The default value is `High.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Severity category of the ProcessException. Each severity category corresponds to one or
more severity values. The severity category is used to show the severity icon in the
ProcessException list view.

Possible values are:

**•** `HIGH`

**•** `LOW`

**•** `MEDIUM`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the ProcessException. Each status corresponds to one status category, shown here
in parentheses. You can customize the status picklist to represent your business processes.
If you customize the status picklist, include at least one status value for each status category.

Possible values are:

**•** `Ignored` (Inactive)

**•** `New` (Active)

**•** `Paused` (Inactive)

**•** `Resolved` (Resolved)

**•** `Triaged` (Active)

**•** `Voided` (Inactive)

The default value is `New.`


-----

```
StatusCategory

##### Associated Objects

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status category of the ProcessException. Each status category corresponds to one or more
statuses.

Possible values are:

**•** `ACTIVE`

**•** `INACTIVE`

**•** `RESOLVED`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProcessExceptionChangeEvent (API version 62.0)**
Change events are available for the object.

**ProcessExceptionOwnerSharingRule**

Sharing rules are available for the object.

**ProcessExceptionOwnerSharingRule**

Sharing rules are available for the object.
