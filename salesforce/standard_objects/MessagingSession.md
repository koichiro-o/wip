#### MessagingSession

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
No longer in use. Indicated that an incoming messaging session was auto-linked to a
Salesforce contact or account based on information such as a phone number.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
No longer in use. Indicated that a contact or account was created for the messaging user if
none existed.


Represents a session on a Messaging channel. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AcceptTime
AgentMessageCount

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when an agent accepts an incoming Messaging session.

**Type**
int

**Properties**
Nillable


-----

```
AgentType
CaseId
ChannelEndUserFormula
ChannelGroup
ChannelIntent

```

**Description**
The number of messages sent by the agent during the session.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of agent that is assigned to the Messaging session. Possible values are:

**•** `Agent`

**•** `Bot`

**•** `BotToAgent—Bot & Agent`

**•** `System—Used for triggered outbound messages`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case associated with this Messaging session.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A concatenation of the Messaging channel and Messaging user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The group of the associated Messaging channel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The intent of the associated Messaging channel.


-----

```
ChannelKey
ChannelLocale
ChannelName
ChannelType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier for the associated Messaging channel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The locale of the associated Messaging channel.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated Messaging channel.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated Messaging channel. Possible values are:

**•** `Alexa`

**•** `AppleBusinessChat—Represents Apple Messages for Business.`

**•** `EmbeddedMessaging—Available in API version 55.0 and later.`

**•** `Facebook`

**•** `GoogleHome`

**•** `Line`

**•** `Omega`

**•** `Phone`

**•** `Text`

**•** `Voice`

**•** `WeChat`

**•** `WebChat`

**•** `WhatsApp`


-----

```
ConversationId
EndedByType
EndTime
EndUserAccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related conversation. Available in API version 55.0 and later.

This field is a relationship field.

**Relationship Name**
Conversation

**Relationship Type**
Lookup

**Refers To**
Conversation

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Who or what ended the enhanced messaging session. Possible values are:

**•** `Agent`

**•** `Bot`

**•** `EndUser`

**•** `System:`

**–** The session is inactive for a while, so the session ends.

**–** An automation ends the session.

**–** The session ended because of an error.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The time when the Messaging session ended.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
EndUserContactId
EndUserLanguage
EndUserMessageCount
LastReferencedDate

```

**Description**
The ID of the end user's account record.

This is a relationship field.

**Relationship Name**
EndUserAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the end user's contact record.

This is a relationship field.

**Relationship Name**
EndUserContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The preferred language of the messaging user who participated in the messaging session.

**Type**
int

**Properties**
Nillable

**Description**
The number of messages sent by the Messaging end user.

**Type**
dateTime


-----

```
LastViewedDate
LeadId
MessagingChannelId
MessagingEndUserId

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Lead associated with this Messaging session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Messaging channel associated with this Messaging session.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Messaging end user associated with this Messaging session.

This is a relationship field.


-----

```
Name
OpportunityId
Origin
OwnerId

```

**Relationship Name**
MessagingEndUser

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of this Messaging session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the opportunity record associated with this Messaging session.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The origin of this Messaging session. Possible values are:

**•** `AgentInitiated`

**•** `ConversationClose—Messaging user deleted the conversation in Apple Messages`

**•** `ConversationControlLost—Third-party bot resumes control from Salesforce`
bot or agent

**•** `Help`

**•** `InboundInitiated`

**•** `OptIn—Opt In Status Change`

**•** `OptOut—Opt Out Status Change`

**•** `TriggeredOutbound`

Messaging sessions can’t be created using Apex code. They can be created only through
customer initiation or by using Process Builder, flows, or the Start Conversation action.

**Type**
reference


-----

```
PreviewDetails
SessionKey
StartTime
Status

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner associated with this Messaging session.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Nillable

**Description**
The preview shown to an agent for this Messaging session.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier for the Messaging session.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The time when the Messaging session started.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the Messaging session. Possible values are:

**•** `New` (standard channels only)

**•** `Active`


-----

```
 TargetUserId

##### Usage

```


**•** `Consent` (enhanced channels only)

**•** `Waiting`

**•** `Paused` (enhanced channels only)

**•** `Inactive` (enhanced channels only)

**•** `Ended`

**•** `Error` (enhanced channels only)

[To learn more about these statuses, see Lifecycle of a Messaging Session in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.messaging_life_cycle.htm&language=en_US)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the target user associated with this Messaging session.

This is a relationship field.

**Relationship Name**
TargetUser

**Relationship Type**
Lookup

**Refers To**
User


To monitor messaging session activity, report on the MessagingSession and MessagingSessionMetrics on page 3247 objects.
[MessagingSessionMetrics captures metrics about a messaging session, such as agent and end user response time. See Report on](https://help.salesforce.com/s/articleView?id=sf.messaging_reporting.htm&language=en_US)
[Messaging Activity in Service Cloud.](https://help.salesforce.com/s/articleView?id=sf.messaging_reporting.htm&language=en_US)

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**MessagingSessionChangeEvent (API version 62.0)**
Change events are available for the object.

**MessagingSessionFeed**

Feed tracking is available for the object.

**MessagingSessionHistory**

History is available for tracked fields of the object.

**MessagingSessionOwnerSharingRule**

Sharing rules are available for the object.


-----

**MessagingSessionShare**

Sharing is available for the object.
