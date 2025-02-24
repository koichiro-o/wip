#### AgentWork

Represents a work assignment that’s been routed to an agent. If the work is transferred to another agent, a new AgentWork record is
created. This object is available in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)


-----

##### Fields

**Field**
```
AcceptDateTime
ActiveTime
AcwExtensionCount
AcwExtensionDuration
AfterConversationActualTime

```

**TypedateTime**

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was accepted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time an agent is actively working on a work item in their console. Active time
is tracked only for tasks routed using the tab-based capacity model. It's tracked only when
the work tab is open and in focus. If the agent switches tabs, the time spent on the other
tabs isn't counted. Active time stops when the agent closes the work item or the after
conversation work time ends, whichever happens first.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times that an agent extended the After Conversation Work (ACW) timer. This
field is available in API version 55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of time (in seconds) that the After Conversation Work (ACW) timer was extended
each time that the agent extended the timer. This field is available in API version 55.0 and
later.

To find the total extension duration, multiply this field by AcwExtensionCount or use
```
  AfterConversationActualTime.

```
**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
AgentCapacityWhenDeclined
AssignedDateTime
BotId
BotType

```

**Description**
The number of seconds an agent spent on After Conversation Work (ACW) after customer
contact ended. This field is available in API version 52.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The agent’s capacity when declining work, either explicitly or through push timeout.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was assigned to an agent. This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Enhanced Einstein Bot or AI agent that performed the work. This is a relationship
field. This field is available in API version 52.0 and later.

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


-----

```
CancelDateTime
CapacityModel
CapacityPercentage
CapacityWeight
CloseDateTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work item was canceled.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the capacity model used to determine agent capacity. Valid values are
`StatusBased` and `TabBased. This field is available in API version 50.0 and later.`

A work item consumes agent capacity only if it was first assigned to the agent by Omni-Channel
using queues or skills.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort

**Description**
The percentage of an agent’s capacity that’s consumed when this work item is in progress.
Valid values are from 0 to 100.

The agent can receive a new work item only if they have enough available capacity for the
item. For example, if you give phone calls a capacity percentage of 100, an agent on a call
doesn’t receive new work items until the call ends.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The amount of an agent’s capacity that’s consumed when this work item is in progress.

For example, if cases are assigned a capacity weight of 2, an agent with a capacity of 6 can
accept up to 3 cases before the agent is at capacity and can’t receive new work items.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
DeclineDateTime
DeclineReason
HandleTime
IsInterruptible
IsOwnerChangeInitiated

```

**Description**
Indicates when the work item was closed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the agent declined this record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The provided reason for why an agent declined the work request.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time an agent had the work item open, calculated by `CloseDateTime`
– AcceptedDateTime. Handle time stops when the agent closes the work item or the
after conversation work time ends, whichever happens first.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item consumes interruptible or primary capacity. The default value
is false. Available in API version 57.0 and later when the Interruptible Capacity feature is
enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
IsPreferredUserRequired
IsStatusChangeInitiated
Name
OriginalGroupId

```

**Description**
Indicates whether a work item owner change triggered the direct assignment of the work
item to the agent. The default value is false. Status-Based Capacity Model has to be turned
on to use this field. This field is available in API version 50.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item stays with the preferred user even when the user isn’t available.
The default value is false. This field is available in API version 50.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a work item status change triggered the direct assignment of the work
item to the agent. The default value is false. Status-Based Capacity Model has to be turned
on to use this field. This field is available in API version 50.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID number that identifies the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the queue that the work assignment was originally routed to. This field is a
relationship field.

**Relationship Name**
OriginalGroup

**Relationship Type**
Lookup

**Refers To**
Group


-----

```
OriginalQueueId
OwnerId
PausedCapacityPercentage
PausedCapacityWeight
PendingServiceRoutingId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the queue that the work assignment was originally routed to. Due to API changes,
`OriginalQueueId` is no longer recommended. Use `OriginalGroupId` instead.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the AgentWork. This field is a polymorphic relationship field. This field
is available in API version 50.0 and later.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of an agent’s capacity that’s consumed when this work item is paused. The
paused capacity feature is available with status-based capacity only. This field is available in
API version 62.0 and later.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The amount of an agent’s capacity that’s consumed when this work item is paused. The
paused capacity feature is available with status-based capacity only. This field is available in
API version 62.0 and later.

**Type**
reference


-----

```
PreferredUserId
PushTimeout

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the PendingServiceRouting on page 3883 from which the AgentWork was created.
This field is a relationship field. This field is available in API version 50.0 and later.

**Relationship Name**
PendingServiceRouting

**Relationship Type**
Lookup

**Refers To**
PendingServiceRouting

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the preferred user to handle the work. This field is a relationship field. This field is
available in API v46.0 and later.

**Relationship Name**
PreferredUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time limit set for an agent to respond to an item before it’s pushed to another agent.
The time limit is measured in seconds. This field is available in API version 36.0 and later.

Effective API version 57.0, for inbound Voice calls, this field represents the time limit set for
an agent to respond to a call before it’s declined. The value must be between 0 and 20. The
value is capped at 20, so any number greater than that is treated as 20 seconds. This applies
to the following telephony models:

**•** Service Cloud Voice with Amazon Connect

**•** Service Cloud Voice with Partner Telephony from Amazon Connect


-----

```
PushTimeoutDateTime
RequestDateTime
RoutingModel
RoutingPriority
RoutingType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the push timeout event occurred. This field is available in
API version 36.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the work was requested.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determines how incoming work items are routed to agents assigned to a service channel.
Possible values are:

**•** `ExternalRouting`

**•** `LeastActive`

**•** `MostAvailable`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which work items from the queue that are associated with the routing
configuration are routed to agents.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of Omni-Channel routing. Possible values are:

**•** `QueueBased`


-----

```
SecondaryRoutingPriority
ServiceChannelId
ShouldSkipCapacityCheck
SpeedToAnswer

```


**•** `SkillsBased`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the secondary routing priority.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel that’s associated with the work assignment. This field is a
relationship field.

**Relationship Name**
ServiceChannel

**Relationship Type**
Lookup

**Refers To**
ServiceChannel

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to skip checking an agent’s available capacity (true) or not (false)
when an externally routed work item is created. This field is used when agents can
simultaneously handle work from both Omni-Channel queues and queues using external
routing.

When `true, the receiving agent can exceed their set capacity to accept the item, but they`
don’t receive more Omni-Channel routed work. When `false, the receiving agent can’t`
exceed their set capacity and must have enough open capacity to accept the item.

The default value is `false.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
Status
TransferRequesterId
UserId

```

**Description**
The amount of time between when the work was requested and when an agent accepted
it.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The working status of the work item. Valid values are:

**•** `Assigned – The item is assigned to the agent but hasn’t been opened.`

**•** `Canceled – The item no longer needs to be routed. For example: a chat visitor cancels`
their Omni-Channel routed chat request before it reaches an agent.

**•** `Closed – The item is closed.`

**•** `Declined – The item was assigned to the agent but the agent explicitly declined it.`

**•** `DeclinedOnPushTimeout` – The item was declined because push time-out is
enabled and the item request timed out with the agent.

**•** `Opened – The agent opened the item.`

**•** `Transferred–The item was transferred from an agent to another agent, queue, or`
skill.

**•** `Unavailable – The item was assigned to the agent but the agent became unavailable`
(went offline or lost connection).

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


-----

```
WorkItemId

##### Usage

```

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user that the work item was assigned to. This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the object that’s routed to the agent through Omni-Channel.

This field is a polymorphic relationship field.

**Relationship Name**
WorkItem

**Relationship Type**
Lookup

**Refers To**
Custom objects and these standard objects: Account, Activity, Case, Claim, ClaimCoverage,
ClaimRecovery, Contact, ContactRequest, CustomEntityData, Incident, Lead,
LiveChatTranscript, MessagingSession, Opportunity, Orchestration Work Items, Order,
PaymentRequest, PersonTraining,Referral, SocialPost, SwarmMember, and VoiceCall.
WorkOrder is available in version 58.0 and later.


`AgentWork` records can only be deleted if they have the status Closed, Declined, or Unavailable. They can’t be deleted if their status
is Assigned or Opened because they’re active in Omni-Channel.

When `AgentWork` records are created, they have the status Assigned. After a record is created, it’s automatically pushed to the
assigned agent.

While the metadata for `AgentWork` indicates support for `upsert()` and `update(), these calls aren’t used with` `AgentWork`
because none of its fields can be updated.

Apex triggers are supported with `AgentWork.`


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**AgentWorkChangeEvent (API version 63.0)**
Change events are available for the object.

**AgentWorkOwnerSharingRule**

Sharing rules are available for the object.

**AgentWorkShare**

Sharing is available for the object.

SEE ALSO:

_[Salesforce Help: Understand the Details of the Routing Lifecycle](https://help.salesforce.com/s/articleView?id=sf.omnichannel_psr_lifecycle.htm&language=en_US)_
