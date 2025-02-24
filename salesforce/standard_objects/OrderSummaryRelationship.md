#### OrderSummaryRelationship

Junction object used to track how an original order summary (created before any exchanges have occurred) relates to other order
summary objects in a chain of exchange orders. This object is available in API version 60.0 and later.

An exchange order is an OrderSummary object whose SourceProcess property is set to Exchange. An original order summary can
have an exchange order, which in turn can have yet another exchange order, and so on. The OrderSummaryRelationship object maintains
this relationship between OrderSummary objects.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs or if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
AssociatedOrderSummaryId
AssociatedOrderSummaryStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated OrderSummary.

This field is a relationship field.

**Relationship Name**
AssociatedOrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Status of the associated OrderSummary.

Possible values are:

**•** `Activated`

**•** `Approved`

**•** `Canceled`

**•** `Created`

**•** `Fulfilled`

**•** `Returned`

**•** `Waiting to Fulfill`

The default value is `Created.`


-----

```
AssociatedRelationshipType
CurrencyIsoCode
MainAttachedToId
MainOrderSummaryId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Relationship type of the associated OrderSummary.

Possible values are:

**•** `Exchange`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

Possible values are:

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of an Order (Change Order) or a ReturnOrder that belongs to the parent OrderSummary
(whose ID is stored in the `MainOrderSummaryId` field).

This field is a polymorphic relationship field.

**Relationship Name**
MainAttachedTo

**Relationship Type**
Lookup

**Refers To**
Order, ReturnOrder

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Name
RootOrderSummaryId

```

**Description**
ID of the associated OrderSummary’s parent.

This field is a relationship field.

**Relationship Name**
MainOrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the OrderSummaryRelationship.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the original OrderSummary that existed before any exchange orders were created.

This field is a relationship field.

**Relationship Name**
RootOrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary

