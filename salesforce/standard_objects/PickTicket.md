#### PickTicket

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A set of bits where each bit indicates a controlling value for which this picklist value is valid.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the picklist value.


A PickTicket represents quantities of one or more products to be picked for fulfillment at a location. It can include products belonging
to one or more fulfillment orders. This object is available in API version 57.0 and later.

A PickTicket is associated with one or more PickTicketAssignments and one or more PickTicketProducts. Each PickTicketAssignment
represents the relationship between the PickTicket and a FulfillmentOrder. Each PickTicketProduct represents the quantity of a product
to be picked as part of the PickTicket. If multiple FulfillmentOrders associated with the PickTicket include the same product, one
PickTicketProduct can represent the total quantity of that product to be picked for all of those FulfillmentOrders.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with an Order Management Growth license.


-----

##### Fields

**Field**
```
AssignedToId
LastReferencedDate
LastViewedDate
LocationId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user assigned to pick the items associated with the PickTicket.

This field is a relationship field.

**Relationship Name**
AssignedTo

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed data in this record, a record related to
this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't view it directly.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location fulfilling the items to be picked.

This field is a relationship field.

**Relationship Name**
Location


-----

```
OwnerId
PickTicketNumber
Status

```

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the PickTicket record. By default, the asset owner is the user who created the
record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicket.

**Type**
picklist

**Properties**
Create, Filter, Group, Printed, Sort, Update

**Description**
Status of the PickTicket. Each status corresponds to one status category, shown here in
parentheses. You can customize the status picklist to represent your business processes, but
the status category picklist is fixed because processing is based on those values. If you
customize the status picklist, include at least one status value for each status category.

Default values are:

**•** `Assigned` (Active)

**•** `Canceled (Canceled)`

**•** `Completed (Completed)`

**•** `Created` (Active)


-----

```
StatusCategory

##### Associated Objects

```


**•** `Draft` (Draft)

**•** `Picked` (Active)

**•** `Picking` (Active)

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status category of the PickTicket. Processing of the PickTicket depends on this value. Each
status category corresponds to one or more status values.

Possible values are:

**•** `ACTIVE`

**•** `CANCELED`

**•** `COMPLETED`

**•** `DRAFT`

The default value is `DRAFT.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PickTicketFeed on page 54**
Feed tracking is available for the object.

**PickTicketShare on page 66**
Sharing is available for the object.

SEE ALSO:

PickTicketAssignment

PickTicketProduct
