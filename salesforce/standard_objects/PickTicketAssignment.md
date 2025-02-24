#### PickTicketAssignment

Represents the association of a FulfillmentOrder with a PickTicket. A PickTicket has one PickTicketAssignment for each FulfillmentOrder
containing products to be picked as part of that PickTicket. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is available with an Order Management Growth license.

##### Fields

```
AttachedToId
PickTicketAssignmentNumber
PickTicketId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the FulfillmentOrder to associate with a PickTicket.

This field is a relationship field.

**Relationship Name**
AttachedTo

**Relationship Type**
Lookup

**Refers To**
FulfillmentOrder

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PickTicketAssignment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the PickTicket to associate with a FulfillmentOrder.

This field is a relationship field.

**Relationship Name**
PickTicket

**Relationship Type**
Lookup


-----

**Refers To**
PickTicket

SEE ALSO:

PickTicket

FulfillmentOrder

PickTicketProduct
