#### LiveChatTranscriptEvent

Captures specific events that occur over the lifetime of a chat. This object is available in API version 24.0 and later.

##### Supported Calls
```
create(), delete(), getDeleted(), getUpdated(), query(), retrieve(), undelete(), update(),
upsert()

 Fields

```
```
AgentId
Detail

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the agent associated with the event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
LastReferencedDate
LastViewedDate
LiveChatTranscriptId
Name
Time

```

**Description**
Details associated with the event.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
(LastReferencedDate) but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the live chat transcript associated with the event.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the event.

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The time at which the event happened.


-----

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The kind of event that occurred.

**•** `Accept—Accepted`

**•** `AgentBlocked—Blocked by Agent`

**•** `AlertCriticalWaitChat—Critical Wait Alert Time Reached`

**•** `CancelBlocked—Cancel (Blocked)`

**•** `CancelNoAgent—Cancel (No Agent)`

**•** `CancelNoQueue—Cancel (No Queue)`

**•** `CancelVisitor—Canceled by Visitor`

**•** `ChasitorIdleTimeout—Visitor Idle Time-Out`

**•** `ChasitorIdleTimeoutWarningCleared—Visitor Idle Time-Out`
Warning Cleared

**•** `ChasitorIdleTimeoutWarningTriggered—Visitor Idle Time-Out`
Warning Appeared

**•** `ChatRequest—Chat Requested`

**•** `ChatResumedAfterTransfer—Chat resumed`

**•** `ChatbotEndChat—Chatbot end chat`

**•** `ChatbotEndedChatByAction—Conversation ended by automated`
action

**•** `ChatbotEstablished—Accepted by Chatbot`

**•** `ChatbotNotEstablished—Chatbot Request Failed`

**•** `ChoiceRoute—Routed (Choice)`

**•** `ClearCriticalWaitChat—Critical Wait Alert Cleared`

**•** `ConferenceRequest—Chat Conference Requested`

**•** `ConferenceRequestCanceled—Chat Conference Canceled`

**•** `ConferenceRequestDeclined—Chat Conference Declined`

**•** `ConnectionTimeout—Visitor connection timed out. Available in API`
version 38.0 and later.

**•** `ConnectionWarning—Warning that visitor hasn't been connected for`
some time and that the connection times out soon. Available in API version
38.0 and later.

**•** `DeclineManual—Decline (Manual)`

**•** `DeclineTimeout—Decline (Timeout)`

**•** `EndAgent—Ended by Agent`

**•** `EndVisitor—Ended by Visitor`


-----

**•** `Enqueue—Queued`

**•** `FileCanceledAgent—File Transfer Canceled by Agent`

**•** `FileCanceledChasitor—File Transfer Canceled by Visitor`

**•** `FileTransferFailure—File Transfer Failure`

**•** `FileTransferRequested—File Transfer Requested by Agent`

**•** `FileTransferSuccess—File Transfer Success`

**•** `FileTransferToChasitor—File Transfer Initiated by Agent`

**•** `FlagLoweredAgent—Flag Lowered by Agent`

**•** `FlagLoweredSupervisor—Flag Lowered by Supervisor`

**•** `FlagRaised—Flag Raised`

**•** `LeaveAgent—Agent Left`

**•** `LeaveVisitor—Visitor Left`

**•** `OperatorJoinedConference—Agent Joined Conference`

**•** `OperatorLeftConference—Agent Left Conference`

**•** `Other`

**•** `PushAssignment—Routed (Push)`

**•** `SensitiveDataAgent—Sensitive data blocked (Agent)`

**•** `SensitiveDataSupervisor—Sensitive data blocked (Supervisor)`

**•** `SensitiveDataVisitor—Sensitive data blocked (Visitor)`

**•** `Transfer—Transfer Accepted`

**•** `TransferCancelled—Transfer Request Canceled`

**•** `TransferDeclined—Transfer Request Declined`

**•** `TransferRequest—Transfer Requested`

**•** `TransferToBotFailed—Transfer to bot failed`

**•** `TransferToButtonFailed—Transfer to button failed`

**•** `TransferToQueueFailed—Transfer to queue failed`

**•** `TransferredToBot—Transferred to bot`

**•** `TransferredToButton—Transferred to button`

**•** `TransferredToQueue—Transferred to queue`

**•** `TransferredToSbrSkill—Transferred to skill`

**•** `TransferredToSbrSkillFailed—Transfer to skill failed`

**•** `Unassigned`

##### Usage

Use this object to query and manage live chat transcript events.


-----

Note: LiveChatTranscriptEvent records are inserted after the chat is closed and the LiveTranscript record updated). However, the
trigger on the LiveChatTranscriptEvent sObject fires separately on each LiveChatTranscriptEvent record within the same transaction.

All the LiveChatTranscriptEvent records are inserted in a single transaction but one by one. For example, the trigger is executed
for each individual record.
```
   trigger LCTE on LiveChatTranscriptEvent (before insert) {
      // Trigger.New will have only 1 record at a time and trigger will execute for
   individual record
      for(LiveChatTranscriptEvent l : Trigger.New)
      system.debug(l.Type + '>>' +l.Detail);
      }

```
To avoid hitting any governors and limits, design your functionality considering this behavior. You can execute the logic by filtering
the records based on the `Type` field of LiveChatTranscriptEvent.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatTranscriptChangeEvent (API version 62.0)**
Change events are available for the object.
