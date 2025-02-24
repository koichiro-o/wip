#### BroadcastTopicGroup

Represents a junction object that relates a group to an alert type broadcast topic. The broadcast sends the alert to this group. This object
is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
Enable Customer Service Incident Management and Broadcast Alert. To create a BroadcastTopicGroup record, set the BroadcastReason
field of the associated BroadcastTopic to Incident Communication.

##### Fields

```
BroadcastTopicId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast topic.

This field is a relationship field.

**Relationship Name**
BroadcastTopic

**Relationship Type**
Lookup

**Refers To**
BroadcastTopic


-----

```
GroupId
Name

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group where the alert of the associated BroadcastTopic record with an `Alert`
`BroadcastType` is sent to.

This field is a relationship field.

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Name of the broadcast topic group.

This field is optional.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastTopicGroupChangeEvent on page 67**
Change events are available for the object.

Available in API version 58.0
