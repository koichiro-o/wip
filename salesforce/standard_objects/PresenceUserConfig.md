#### PresenceUserConfig

Represents a configuration that determines a presence user’s settings. This object is available in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), update(), query(), retrieve()

```

-----

##### Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
AcwExtensionDuration
AfterConvoWorkMaxTime
Capacity
CustomSoundId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent can spend on After Conversation
Work (ACW) each time they extend the timer. You must set this field if
`HasAcwExtensionEnabled` is set to `true. Specify a value from 10 through 3600.`

This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent has to complete After
Conversation Work (ACW). You must set this field if `HasAfterConvoWorkTimer` is
set to `true. Specify a value from 10 through 3600.`

This field is available in API version 56.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The maximum number of work units an agent can be assigned at one time.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Relationship Name**
```
  CustomSound

```

-----

```
DeveloperName
HasAcwExtensionEnabled
HasAfterConvoWorkTimer

```

**Relationship Type**
Lookup

**Refers To**
```
  StaticResource

```
**Description**
The ID of the static resource for the custom sound selected to play for the
```
 PresenceUserConfig object.

```
**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance may slow while Salesforce
generates one for each record.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true, agents can extend their After Conversation Work (ACW) time. Available only`
if `HasAfterConvoWorkTimer` is set to `true. If set to` `true, you must also set the`
`AcwExtensionDuration` and MaxExtensions fields. The default value is true.

This field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
Language
MasterLabel
MaxExtensions
OptionsIsAllowAnyDestinationQueueForTransferEnabled
OptionsIsAllowAnyDestinationFlowForTransferEnabled

```

**Description**
If set to `true, After Conversation Work (ACW) time can be configured for the channel. If`
set to true, you must also set the AfterConvoWorkMaxTime field. The default value
is `false.`

This field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the presence configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The label of the presence configuration.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The maximum number of times an agent can extend their After Work Conversation (ACW)
time. Specify a value from 1 through 10. You must set this field if
`HasAcwExtensionEnabled` is set to `true.`

This field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
queue (true) or only the selected queues (false).

This field is available in API version 61.0 and later.

**Type**
boolean


-----

```
OptionsIsAllowAnyDestinationProfileForTransferEnabled
OptionsIsAutoAcceptEnabled
OptionsIsDeclineEnabled
OptionsIsDeclineReasonEnabled

```

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
flow (true) or only the selected flows (false).

This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Indicates that a rep can transfer a message from an enhanced Messaging channel to any
profile (true) or only the selected profiles (false).

This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether work items that are routed to agents are automatically accepted (true)
or not (false). Available only if `OptionsIsDeclineEnabled` is set to `false.`

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether agents can decline work items that are routed to them (true) or not
(false). Available only if `OptionsIsAutoAcceptEnabled` is set to `false.`

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether agents can select a reason for declining work requests (true) or not
(false). This can be selected only if decline reasons are enabled.


-----

```
OptionsIsDisconnectSoundEnabled
OptionsIsRequestSoundEnabled
PresenceStatusOnDeclineId
PresenceStatusOnPushTimeoutId
SoundLength

```

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether a sound is played when agents are disconnected from Omni-Channel
(true) or not (false).

**Type**
boolean

**Properties**
Create, Filter

**Description**
Indicates whether a sound plays with incoming work requests (true) or not (false). Set
to `true` by default.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s automatically assigned to the agent when the agent
declines a work item. Available only if `OptionsIsDeclineEnabled` is set to `true.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s automatically assigned to the agent when the agent
doesn’t respond to a work item before push timeout occurs. Available in API version 36.0
and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The length of time that a sound plays when new work is assigned to an agent.


-----
