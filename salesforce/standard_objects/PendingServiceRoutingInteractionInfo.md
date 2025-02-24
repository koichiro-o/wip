#### PendingServiceRoutingInteractionInfo

Represents PendingServiceRouting interaction information that’s used when work is routed to an agent. For a screen pop, it specifies
which records to open when work is routed to an agent from a specific channel. PendingServiceRoutingInteractionInfo is read-only. This
object is available in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled. To view this object, you must have the “Manage Flow” user permission.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

##### Fields

```
IsFocused
Name

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this record shows on the agent’s screen when multiple records open at
the same time.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the PendingServiceRoutingInteractionInfo.


-----

```
PendingServiceRoutingId
PrimaryRecordId
TargetFlowName
TargetObjectId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the PendingServiceRouting on page 3883 from which the AgentWork on page 541
is created.

This is a relationship field.

**Relationship Name**
PendingServiceRouting

**Relationship Type**
Lookup

**Refers To**
PendingServiceRouting

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the object that’s routed to the agent through Omni-Channel.

**Relationship Name**
PrimaryRecord

**Relationship Type**
Lookup

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name and namespace prefix, if any, of the screen flow to open when work is routed
to the agent. This field and the TargetFlowId field can't be populated at the same time.
Available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
The record to open when work is routed to the agent. This field is required in API version
56.0 and earlier. In API version 57.0 and later, this field is optional and can’t be populated at
the same time as the `TargetFlowName` field.

**Relationship Name**
TargetObject

**Relationship Type**
Lookup
