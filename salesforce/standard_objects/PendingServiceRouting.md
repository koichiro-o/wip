#### PendingServiceRouting

Represents the routing details of a work item that’s waiting to be routed or assigned. This object is available in API version 40.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

##### Fields

```
BotId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Enhanced Einstein Bot or AI agent that performed the work. This is a relationship
field. This field is available in API version 52.0 and later.

This field is a relationship field.


-----

```
BotType
CapacityPercentage
CapacityWeight
CustomRequestedDateTime

```

**Relationship Name**
Bot

**Relationship Type**
Lookup

**Refers To**
BotDefinition

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of bot. Valid values are:

**•** Bot. Refers to an Einstein bot.

**•** ExternalCopilot. Refers to an AI agent with whom your customers can interact.

The default value is Bot. This field is available in API version 63.0 and later.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Indicates the amount of work that this work item represents as a percentage. Valid values
are from 0 to 100.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Indicates the amount of work that this work item represents as a whole number.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Retains the datetime of this work item’s initial request, so work items are rerouted using the
datetime of the initial work request. When left blank, work items are rerouted using the
datetime when they’re rerouted.


-----

```
DropAdditionalSkillsTimeout
GroupId
IsInterruptible
IsOwnerChangeInitiated
IsPreferredUserRequired

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Time to wait before a skill marked as additional is dropped from Omni-Channel routing. The
case is then routed to the best-matched agent even if they don’t have all the skills.

[If CustomRequestedDateTime is set in the PendingServiceRouting object,](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_pendingservicerouting.htm)
DropAdditionalSkillsTimeout uses CustomRequestedDateTime as the start time. If
CustomRequestedDateTime + DropAdditionalSkillsTimeout has already passed, Omni-Channel
immediately drops the additional skills after the pending service request is created.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Omni-Channel queue.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item consumes interruptible or primary capacity. The default value
is false. Available in version 57.0 and later when the Interruptible Capacity feature is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item owner change triggered the direct assignment of this work
item to the agent. The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this work item stays with the preferred user even when the user isn’t
available. The default value is `false. This field is available in API version 50.0 and later.`


-----

```
IsPushAttempted
IsPushed
IsReadyForRouting
IsStatusChangeInitiated
IsTransfer

```

When a specific agent is required, don’t set PushTimeout. These options aren’t supported
in this case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a push has been attempted. `true` if this work item was pushed to an
agent at least one time and `false` otherwise.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this work item is pushed to an agent.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this work item is ready to be routed to an agent. If `true, you can’t edit`
this PendingServiceRouting record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item status change triggered the direct assignment of this work
item to the agent. The default value is `false. This field is available in API version 50.0 and`
later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this work item routing is a transfer request.


-----

```
LastDeclinedAgentSession
Name
OwnerId
PausedCapacityPercentage
PausedCapacityWeight
PreferredUserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Chat session ID of the agent who last declined this work item.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the PendingServiceRouting record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this PendingServiceRouting record.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of capacity that’s consumed when this work item is paused. The paused
capacity feature is available with status-based capacity only. This field is available in API
version 62.0 and later.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The amount of capacity that’s consumed when this work item is paused. The paused capacity
feature is available with status-based capacity only. This field is available in API version 62.0
and later.

**Type**
reference


-----

```
PushTimeout
QueueId
RoutingModel

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the preferred user to handle the work item.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The time limit set for an agent to respond to an item before it’s rerouted and the agent’s
status is changed accordingly. The time limit is measured in seconds. This field is available
in API version 36.0 and later.

Effective API version 57.0, for inbound Voice calls, this field represents the time limit set for
an agent to respond to a call before it’s declined. The value must be from 0 through 20. The
value is capped at 20, so any number greater than that is treated as 20 seconds. Latency on
the part of the telephony provider can result in agents having less than 20 seconds to answer
a call before it’s rerouted. When an agent attempts to answer a call within 20 seconds and
finds that the call was rerouted, the agent’s status remains unchanged. This scenario applies
to these telephony models.

**•** Service Cloud Voice with Amazon Connect

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

Note: When IsPreferredUserRequired is set to true, don’t set this option.
When a specific agent is required, this option isn’t supported.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Omni-Channel queue. Due to API changes, QueueId is no longer recommended.
Use `GroupId` instead.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of routing model.

Possible values are:

**•** `ExternalRouting`


-----

```
RoutingPriority
RoutingType
SecondaryRoutingPriority
Serial
ServiceChannelId

```


**•** `LeastActive`

**•** `MostAvailable`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Order in which work items are routed to agents. This field is considered with skills-based
routing only. Queue-based routing sets a work item's priority from the routing configuration.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Indicates whether the work item is routed by queue or by skills-based routing.

Possible values are:

**•** `QueueBased`

**•** `SkillsBased`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the secondary routing priority.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Serial number of the PendingServiceRouting record. The serial number is automatically
incremented each time the PendingServiceRouting record is modified.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
TransferRequesterId
WorkItemId

##### Usage

```

**Description**
ID of the service channel.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID of the rep who reassigned the work using the Reassign action. This field is
populated in reassigned AgentWork records only, not the original AgentWork record. This
is a relationship field. This field is available in API version 63.0 and later.

**Relationship Name**
TransferRequester

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the work item.

**Refers To**
Custom objects and these standard objects: Account, Activity, Case, Claim, ClaimCoverage,
ClaimRecovery, Contact, ContactRequest, CustomEntityData, Incident, Lead,
LiveChatTranscript, MessagingSession, Opportunity, Orchestration Work Items, Order, Order,
PaymentRequest, PersonTraining, Referral, SocialPost, SwarmMember, and VoiceCall.
WorkOrder is available in version 58.0 and later.


When you use the PendingServiceRouting object for queue-based routing, the object doesn’t invoke triggers before or after insert, or
any action (trigger, workflow rule, validation) that could interfere with the creation of the record.

##### Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**PendingServiceRoutingChangeEvent (API version 62.0)**
Change events are available for the object.


-----

**PendingServiceRoutingOwnerSharingRule**

Sharing rules are available for the object.

**PendingServiceRoutingShare**

Sharing is available for the object.

##### Limits

You can view the number of Pending Service Routing records that are currently in use in your org, as well as the current hourly use rate.
From Setup, enter Omni-Channel in the Quick Find box and select Limits. The Limits page also displays the current Pending Service
Routing record usage percentage and the Pending Service Routing record limits for your org.
