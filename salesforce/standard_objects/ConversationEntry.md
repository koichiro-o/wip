#### ConversationEntry

Represents a message or event in a voice call or a standard or enhanced messaging session. This object is available in API version 43.0
and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To use the ConversationEntry object, enable the Access Conversation Entries user permission, which is available in API version 50.0 and
later. Earlier versions do not require permissions.

##### Fields

```
ActorId
ActorName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the author. The possible values can be `null` or any ID in the following domain
set:

**•** `BotDefinition`

**•** `LiveChatVisitor`

**•** `MessagingEndUser`

**•** `User`

This is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser, User

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The name of the author sending the message or event.


-----

```
ActorType
ClientDuration
ClientTimestamp
ConversationId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The author of this entry in the chat history. The valid values include:

**•** `Agent`

**•** `Bot`

**•** `EndUser`

**•** `Supervisor`

**•** `System`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The length in milliseconds for the entry. This field is used with voice messages and other
applicable use cases. This value may be 0 if not set by the client. This field is available in API
version 51.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The timestamp sent by the client when it generated the entry. This field is available in API
version 51.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The MessagingSession ID this entry belongs to.

This is a polymorphic relationship field.

**Relationship Name**
Conversation

**Relationship Type**
Lookup


-----

```
EntryEndTime
EntryTime
EntryTimeMilliSecs
EntryType

```

**Refers To**
MessagingSession, VoiceCall

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The timestamp that this entry ended in the chat history. This field is available in API version
48.0 and later.

**Type**
datetime

**Properties**
Create, Filter, Sort

**Description**
The timestamp of this entry in the chat history.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The milliseconds value for the time when an entry was received by the server. Note that the
related `EntryTime field does not provide millisecond accuracy. This field is available in`
API version 51.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of entry in the chat history. Can be a message (text) or an event. The possible
values include:

**•** `Text`

**•** `AdminOptedIn`

**•** `AdminOptedOut`

**•** `BotEscalated`

**•** `ChatbotClosedIdleSession`

**•** `ChatbotEndedChatByAction—Conversation ended by automated action`


-----

```
HasAttachments
Message
MessageDeliverTime
MessageIdentifier
MessageReadTime

```


**•** `ChatbotEndedTransferNotConfigured—Conversation ended because`
transfer fail is not configured

**•** `ChatbotEstablished`

**•** `ChatbotNotEstablished`

**•** `EndUserOptedIn`

**•** `EndUserOptedOut`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a message has attachments associated with it (true) or not (false).

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The message or event sent by the author. In ConversationEntry records for enhanced
Messaging channels or Messaging for In-App and Web, the Message field is blank due to
data storage differences from standard channels.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Unused field reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique ID for the message. Maximum size is 36 characters.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort


-----

```
MessageSendTime
MessageStatus
MessageStatusCode
Seq
ServerReceivedTimestamp

```

**Description**
Unused field reserved for future use.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Unused field reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the message sent by the author. The valid values include:

**•** `Delivered`

**•** `Error`

**•** `Pending`

**•** `Read`

**•** `Sent`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The code associated with a message status. `MessageStatusCode` is only populated
when a message is undeliverable

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The sequence position of this entry in the chat history.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort


-----

**Description**
The timestamp recorded when the server received the entry. This is a unique value and is
used for ordering. This value can also be referred to as the “transcripted timestamp.” This
field is available in API version 51.0 and later.

##### Usage

In standard SMS, WhatsApp, and Facebook Messenger channels, a ConversationEntry record is created for each message sent by a
messaging end user or an agent, bot, or automation. Each ConversationEntry record is associated with a MessagingSession record, which
represents the interaction between the messaging end user and the business. Access and work with ConversationEntry records like any
standard object. You can report on messaging activity and track the conversation workflow end to end. You can also download or delete
transcripts, redact sensitive text, and customize your workflows with solutions built on the ConversationEntry object.

In enhanced Messaging channels, Messaging for In-App and Web, and Service Cloud Voice ("enhanced channels"), inbound and outbound
messages are processed in one of two ways depending on your location.

**•** A ConversationEntry record is created but the `Message` field is blank, or

**•** No ConversationEntry record is created.

To get the fullest picture of conversations in enhanced channels, use Data Cloud, the Connect REST API, or the Conversation Transcript
[Export tool to access transcripts. See Accessing Messaging and Voice Conversation Data.](https://help.salesforce.com/s/articleView?id=sf.conversation_transcript_access.htm&language=en_US)

Note: ConversationEntry records aren’t created until the messaging session ends and the agent closes the session tab. One
exception is for the first message in any standard messaging session, whose ConversationEntry record is created immediately.
