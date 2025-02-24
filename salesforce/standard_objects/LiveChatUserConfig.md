#### LiveChatUserConfig

Represents a setting that controls the console settings for Chat users. This object is available in API version 24.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update()

 Special Access Rules

```
As of Summer ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
AutoGreeting
Capacity
CriticalWaitTime
CustomAgentName

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The text that is automatically sent from an agent to a visitor when a chat session
starts.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Limits the amount of active chat sessions an agent can engage in.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The amount of time before a chat flashes to alert an agent to answer it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
DeveloperName
HasLogoutSound
HasNotifications
HasRequestSound

```

**Description**
The custom name of the agent associated with the Live Agent configuration.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin
with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a sound plays when an agent logs out of the console.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether desktop notifications are enabled for the configuration.
Available in API version 25.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


-----

```
HasSneakPeek
HasTransferConferenceGreeting
IsAutoAwayOnDecline
Language
MasterLabel

```

**Description**
Determines whether a sound plays when a chat request comes in.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether an agent sees a real-time preview of the messages typed
by a visitor.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether to enable sending an autogreeting when you transfer to
another agent or invite an agent to a conference chat.

The default value is `false. Available in API version 53.0 and later.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Determines whether agents’ status is automatically changed to Away when they
decline a chat request. Available in API version 26.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the configuration.


-----

```
OptionsHasAgentFileTransfer
OptionsHasAgentSneakPeek
OptionsHasAssistanceFlag
OptionsHasChatConferencing
OptionsHasChatMonitoring
OptionsHasChatTransferToAgent

```

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether agents can initiate a file transfer from a chat customer.
Available in API version 31.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether Sneak Peek is enabled for agents. Available in API version
29.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether assistance flags are enabled for agents. Available in API
version 29.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether agents can invite other agents into a customer chat. Available
in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether supervisors can view agents’ ongoing chats. Available in
API version 29.0 and later.

**Type**
boolean


-----

```
OptionsHasChatTransferToButton
OptionsHasChatTransferToSkill
OptionsHasTransferConferenceGreeting
OptionsHasVisitorBlocking
OptionsHasWhisperMessage

```

**Properties**
Create, Filter

**Description**
Specifies whether an agent can transfer a chat directly to another agent. Available
in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Specifies whether an agent can transfer a chat to an agent assigned to a particular
chat button. Available in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Specifies whether an agent can transfer a chat to agents assigned to a particular
skill. Available in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether an agent can transfer a chat to an autogreeting or conference
greeting. Available in API version 53.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether an agent can block IP addresses of troublesome visitors.
Available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter


-----

```
OptionsIsAutoAwayOnPushTimeout
SupervisorDefaultAgentStatus
SupervisorDefaultButtonId
SupervisorDefaultSkillId

##### Usage

```

**Description**
Determines whether supervisors can send private messages to agents within an
agent’s chat with a customer. Available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether an agent’s status automatically changes to Away if the agent
doesn’t respond to a chat request within the specified push time-out limit.
Available in API version 34.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The default agent status by which to filter agents in the Agent Status list in the
supervisor panel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The default button ID by which to filter agents in the Agent Status list in the
supervisor panel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The default skill ID by which to filter agents in the Agent Status list in the
supervisor panel.


Use this object to query and manage agent configurations in Chat.


-----
