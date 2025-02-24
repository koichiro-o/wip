#### LiveChatTranscript

This object is automatically created for each Live Agent chat session and stores information about the session. This object is available in
API version 24.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
Abandoned
AccountId
AverageResponseTimeOperator
AverageResponseTimeVisitor
Body
Browser

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time in seconds an incoming chat request remained unanswered
by an agent before the chat was disconnected by the customer.

**Type**
ID

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with the chat transcript.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The agent’s average response time (in seconds) to chat messages from the visitor.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s average response time (in seconds) to chat messages from the agent.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
BrowserLanguage
CaseID
ChatDuration
ChatKey
ContactID
EndedBy

```

**Description**
The browser the visitor used for the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The language of the visitor’s browser.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case associated with the chat transcript.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total duration of the chat in seconds.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort

**Description**
The session ID of the chat before it is persisted. `ChatKey` can be used with
advanced integrations in the Salesforce console. This field is available in API
version 25.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact associated with the chat transcript.

**Type**
picklist


-----

```
EndTime
IpAddress
IsChatbotSession
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The way the chat was ended: by the operator, the visitor, or the system.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the chat ended.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The auto-populated visitor’s IP address. Do not edit. Create a custom field if you
need an IP address field for your use case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the visitor is chatting with a chatbot (true) or not (false).

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update


-----

```
LeadID
LiveChatButtonID
LiveChatDeploymentID
LiveChatVisitorID
Location

```

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, this record might only have been referenced (LastReferencedDate)
and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the lead associated with the chat transcript.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the LiveChatButton the chat session originated from.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the LiveChatDeployment the chat session originated from.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the visitor associated with the chat transcript.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated best-guess approximation of the visitor’s location. Do not
edit.


-----

```
MaxResponseTimeOperator
MaxResponseTimeVisitor
Name
OperatorMessageCount
OwnerID
Platform

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum time in seconds it took an agent to respond to a chat visitor’s
message.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum time in seconds it took a customer to respond to an agent’s
message.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the transcript.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of messages sent by one or more agents during the chat.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the operator who participated in the chat last; for missed chats, this is
a system user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ReferrerUri
RequestTime
ScreenResolution
SkillId
StartTime
Status

```

**Description**
The visitor’s operating system platform.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated URI where the chat request originated. Do not edit.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the visitor requested the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s screen resolution.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The auto-populated record ID of the primary Skill associated with the
LiveChatButton the chat session originated from. Do not edit. To associate multiple
skills with a LiveChatTranscript, use LiveChatTranscriptSkill junction objects.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time the chat started.

**Type**
picklist


-----

```
SupervisorTranscriptBody
UserAgent
VisitorMessageCount
VisitorNetwork
WaitTime

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The final status of the chat: completed, missed, or blocked.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The text body of the supervisor’s chat transcript.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The visitor’s user agent string.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of messages sent by the visitor during the chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The network or service provider the chat visitor used for the chat.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total amount of time in seconds a chat request was waiting to be accepted
by an agent.


-----

##### Usage

Use this object to query and manage live chat transcripts.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatTranscriptChangeEvent (API version 44.0)**
Change events are available for the object.

**LiveChatTranscriptFeed (API version 47.0)**
Feed tracking is available for the object.

**LiveChatTranscriptHistory**

History is available for tracked fields of the object.

**LiveChatTranscriptOwnerSharingRule (API version 29.0)**
Sharing rules are available for the object.

**LiveChatTranscriptShare**

Sharing is available for the object.
