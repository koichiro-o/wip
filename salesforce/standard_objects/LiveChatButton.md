#### LiveChatButton

Represents a button that allows visitors to request chats with Chat users. This object is available in API version 24.0 and later.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
Animation
AutoGreeting

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of animation used when an automated chat invitation appears on-screen.
For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Appear`

**•** `Custom`

**•** `Fade`

**•** `Slide`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The text that is automatically sent from an agent to a visitor when a chat session
starts.

Note: A greeting message in the `AutoGreeting` field of the
LiveChatButton object overrides individual users’ greeting messages in
the `AutoGreeting` field in the LiveChatUserConfig object.


-----

```
ChasitorIdleTimeout
ChasitorIdleTimeoutWarning
ChatPageId
CustomAgentName

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time a customer has to respond to an agent message before the
chat times out.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time a customer has to respond to an agent message before a
warning appears and a timer begins a countdown. This value must be shorter
than the ChasitorIdleTimeout value. We recommend at least 30 seconds
shorter.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page that contains the custom chat
window code.

This field is a relationship field.

**Relationship Name**
ChatPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The custom name of the agent associated with the button. Available in API version
29.0 and later.


-----

```
DeveloperName
HasQueue
InviteEndPosition

```

Note: A custom agent name in the `CustomAgentName` field of the
LiveChatButton object overrides individual users’ custom agent name in
the `CustomAgentName` field in the LiveChatUserConfig object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance may slow while Salesforce generates one for each
record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether or not to allow queing incoming chat requests until an
agent is available.

The default value is `false.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position on screen where an automated chat invitation’s animation ends.

Note: You don’t need to select an end position for your automated chat
invitation if you use a custom animation.

For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Bottom`


-----

```
InviteImageId
InviteStartPosition

```


**•** `BottomLeft`

**•** `BottomRight`

**•** `Center`

**•** `Left`

**•** `Right`

**•** `Top`

**•** `TopLeft`

**•** `TopRight`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the static image resource displayed on your automated chat
invitation. For automated chat invitations only. Available in API version 29.0 and
later.

This field is a relationship field.

**Relationship Name**
InviteImage

**Relationship Type**
Lookup

**Refers To**
StaticResource

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The position on screen where an automated chat invitation’s animation begins.

Note: You don’t need to select a start position for your automated chat
invitation if you use a custom animation.

For automated chat invitations only. Available in API version 29.0 and later.

Possible values are:

**•** `Bottom`

**•** `BottomLeft`

**•** `BottomLeftBottom`

**•** `BottomLeftLeft`

**•** `BottomRight`


-----

```
IsActive
IsRoutingFlowEnabled
Language

```


**•** `BottomRightBottom`

**•** `BottomRightRight`

**•** `Left`

**•** `Top`

**•** `Right`

**•** `TopLeft`

**•** `TopLeftLeft`

**•** `TopLeftTop`

**•** `TopRight—Top Right`

**•** `TopRightRight`

**•** `TopRightTop`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
For automated chat invitations, specifies whether an automated chat invitation
is active or not.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether routing flow is enabled or not.

The default value is `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the chat.

Possible values are:

**•** `da—Danish`

**•** `de—German`

**•** `en_US—English`

**•** `es—Spanish`


-----

```
MasterLabel
NumberOfReroutingAttempts
OfflineImageId

```


**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`

**•** `ja—Japanese`

**•** `ko—Korean`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the chat button.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the number of times a chat request can be rerouted to available agents
if all agents reject the chat request.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the static image resource that is displayed when the button is
offline (inactive).

This field is a relationship field.

**Relationship Name**
OfflineImage


-----

```
OnlineImageId
OptionsHasChasitorIdleTimeout
OptionsHasInviteAfterAccept
OptionsHasInviteAfterReject

```

**Relationship Type**
Lookup

**Refers To**
StaticResource

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the static image resource that is displayed when the button is
online (active).

This field is a relationship field.

**Relationship Name**
OnlineImage

**Relationship Type**
Lookup

**Refers To**
StaticResource

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether Customer Time-Out is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an automated chat invitation can be sent to a customer after
that customer has accepted a prior automated chat invitation (true) or not
(false). For automated chat invitations only. Available in API version 29.0 and
later.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
OptionsHasRerouteDeclinedRequest
OptionsIsAutoAccept
OptionsIsInviteAutoRemove
OverallQueueLength
PerAgentQueueLength

```

**Description**
Specifies whether an automated chat invitation can be sent to a customer after
that customer has rejected a prior automated chat invitation (true) or not
(false). For automated chat invitations only. Available in API version 29.0 and
later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether a chat request that has been rejected by all available agents
should be rerouted to available agents again (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether a chat request should be automatically accepted by the agent
it’s assigned to (true) or not `false). For chat buttons and automated chat`
invitations with `RoutingType` set to `Most Available` or `Least`
```
  Active. Available in API version 30.0 and later.

```
**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an automated chat invitation should be automatically removed
from the screen after a certain amount of time (true) or not (false). For
automated chat invitations only. Available in API version 29.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of chat requests allowed to queue.

**Type**
int


-----

```
PostchatPageId
PostchatUrl
PrechatFormPageId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of chat requests allowed to queue for each agent with
the required skill.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page displayed when the chat ends.

This field is a relationship field.

**Relationship Name**
PostchatPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL the user is directed to after the chat ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the custom VisualForce page displayed before the chat begins.

This field is a relationship field.

**Relationship Name**
PrechatFormPage

**Relationship Type**
Lookup

**Refers To**
ApexPage


-----

```
PrechatFormUrl
PushTimeout
QueueId
RoutingConfigurationId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL the user is directed to before the chat begins.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of seconds an agent has to answer a chat request before it’s routed
to the next available agent.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the queue used for this chat button.

This field is a relationship field.

**Relationship Name**
Queue

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the routing configuration used for this chat button.

This field is a relationship field.

**Relationship Name**
RoutingConfiguration

**Relationship Type**
Lookup


-----

```
RoutingType
SiteId
SkillId

```

**Refers To**
QueueRoutingConfig

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
How chat requests are routed to agents. The values are:

**•** `Choice—Incoming chat requests are added to the queue in Live Agent in`
the Salesforce console and are available to any agent with the required skill.

**•** `Least Active—Incoming chats are routed to the agent with the`
required skill who has the fewest active chats.

**•** `Most Available—Incoming chats are routed to the agent with the`
required skill and the greatest difference between chat capacity and active
chat sessions. For example, if Agent A and Agent B each have a chat capacity
of five, and Agent A has three active chat sessions while Agent B has one,
incoming chats will be routed to Agent B.

**•** `Omni—Incoming chats are routed using Omni-Channel queues.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record ID of the site used for loading static resources and custom VisualForce
pages.

This field is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
TimeToRemoveInvite
Type
WindowLanguage

```

**Description**
The record ID of the skill used to route incoming chat requests. To associate
multiple skills with a chat button, reference one skill in the `SkillId` field and
use LiveChatButtonSkill junction objects for the remaining skills.

This field is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of seconds an automated invitation stays on-screen before it is
automatically removed. For automated chat invitations only. Available in API
version 29.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of element to display to customers.

Possible values are:

**•** `Invite—Automated invitation`

**•** `Standard—Chat button`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for standard chat windows. Custom chat windows use the
language of the user’s browser.

Possible values are:

**•** `da—Danish`

**•** `de—German`


-----

**•** `en_US—English`

**•** `es—Spanish`

**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`

**•** `ja—Japanese`

**•** `ko—Korean`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

##### Usage

Use this object to query and manage chat buttons and automated chat invitations.
