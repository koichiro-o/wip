#### ServiceChannel

Represents a channel of work items that are received from your organization—for example, cases, chats, or leads. This object is available
in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
AcwExtensionDuration
AfterConvoWorkMaxTime

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum length of time, measured in seconds, an agent can spend on After Conversation
Work (ACW) each time they extend the timer. You must set this field if
`HasAcwExtensionEnabled` is set to `true. Specify a value from 10 through 3600.`
Available only for service channels of type Messaging or Voice.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
CapacityModel
CustomSoundId
DeveloperName

```

**Description**
The maximum length of time, measured in seconds, an agent has to complete After
Conversation Work (ACW). You must set this field if HasAfterConvoWorkTimer is set
to `true. Specify a value from 10 through 3600. Available only for service channels of type`
Messaging or Voice.

For service channels of type Voice, this field is available in API version 52.0 and later. For
service channels of type Messaging, this field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, RestrictedPicklist, Sort, Update

**Description**
The method that determines when an agent's capacity for a work item is released. With the
Status-Based capacity routing model, work remains assigned and applied to an agent’s
capacity until the work is completed or reassigned to a different agent. In contrast, the
tab-based capacity model releases an agent’s capacity when a work tab is closed in the
service console. Possible values are StatusBased and TabBased.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Relationship Name**
```
  CustomSound

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
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With


-----

```
DoesCheckCapOnOwnerChange
DoesCheckCapOnStatusChange
DoesMinimizeWidgetOnAccept
DoesOverridePresenceAudio
HasAcwExtensionEnabled

```

this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
In the Status-Based capacity routing model, when work is reassigned to a specific agent, you
can choose to override the capacity check and keep the work assigned to the agent. The
default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
In the Status-Based capacity routing model, when work is reopened, you can choose to
override the capacity check keep the work assigned to a specific agent. The default value is
```
  false.

```
**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Automatically minimizes the Omni-Channel widget when an agent accepts work. The default
value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Service channel settings override the audio settings for each agent’s presence configuration.
The default value is `false.`

**Type**
boolean


-----

```
HasAfterConvoWorkTimer
HasAutoAcceptEnabled
Language
MasterLabel

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true, agents can extend their After Conversation Work (ACW) time. Available only`
if HasAfterConvoWorkTimer is set to `true. If set to true, you must also set the`
`AcwExtensionDuration and MaxExtensions` fields. The default value is false.
Available only for service channels of type Messaging or Voice.

This field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true, After Conversation Work (ACW) time can be configured for the channel. If`
set to true, you must also set the AfterConvoWorkMaxTime field. The default value
is `false. Available only for service channels of type Messaging or Voice.`

For service channels of type Voice, this field is available in API version 52.0 and later. For
service channels of type messaging, this field is available in API version 56.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Work items in a service channel open automatically in the agent’s workspace so that the
agent doesn’t have to manually accept them. The default value is `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the service channel.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the service channel.


-----

```
MaxExtensions
RelatedEntity
SecRoutingPriorityField
SoundLength
StatusField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The maximum number of times an agent can extend their After Work Conversation (ACW)
time. Specify a value from 1 through 10. You must set this field if
`HasAcwExtensionEnabled` is set to `true. Available only for service channels of`
type Messaging or Voice.

This field is available in API version 56.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of object that’s associated with this service channel. This field is unique within your
organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The name of the standard field or the id of the custom field that is used for secondary routing
priority. This field is unique within your organization.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The length of time that a sound plays when new work is assigned to an agent.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The picklist field that you use to track work status in the Status-Based capacity routing model.
Use ServiceChannelStatusField to specify the values that indicate completed and in-progress
work-item status.


-----
