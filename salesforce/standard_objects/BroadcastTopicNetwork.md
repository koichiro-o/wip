#### BroadcastTopicNetwork

Represents a link between a broadcast topic and the Experience Cloud network site for Service Cloud. This object is available in API
version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Special Access Rules

To access this object with Service Cloud, enable Incident Management in Setup and Broadcast Site Banner in the Incident Management
setup.

##### Fields

```
BroadcastTopicId
Name
NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The BroadcastTopic ID that's linked to the Network.

This field is a relationship field.

**Relationship Name**
BroadcastTopic

**Relationship Type**
Lookup

**Refers To**
BroadcastTopic

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the broadcast topic that's assigned to the network.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Network ID that's linked to the BroadcastTopic..

This field is a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastTopicNetworkChangeEvent on page 67**
Change events are available for the object.
