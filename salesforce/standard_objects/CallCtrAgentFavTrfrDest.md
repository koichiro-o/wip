#### CallCtrAgentFavTrfrDest

Represents a transfer destination that has been marked (starred) as a favorite in the Omni-Channel softphone by a contact center agent
for voice call transfers. This object is available in API version 55.0 and later.

To see a list of transfer destinations that have been marked as favorites in the Omni-Channel softphone, add a participant to the call,
click the Phone tab, and select Favorite from the Filter dropdown menu. Examples of transfer destination types include agents, contacts,
directories, flows, and queues.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AgentId
CallCenterId
Name
OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the contact center agent who marked the transfer destination as a favorite.

This field is a relationship field.

**Relationship Name**
Agent

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the contact center from where the agent starred the transfer destination
as a favorite.

This field is a relationship field.

**Relationship Name**
CallCenter

**Relationship Type**
Lookup

**Refers To**
CallCenter

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the transfer destination record that’s marked as a favorite.

**Type**
reference


-----

```
TransferDestination

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID of the user who owns this object.

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
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the transfer destination that’s marked as a favorite. This is an external ID.

