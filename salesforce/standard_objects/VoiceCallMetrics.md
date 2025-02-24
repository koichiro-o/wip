#### VoiceCallMetrics

Represents metrics for a VoiceCall lifecycle event, aggregated daily. This object is available in API version 56.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
AverageSCVCallDuration

```

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
AvgMessagesPerCall
InboundCallsAgentsConnected
MaxMessagesPerCall
MaxSCVCallDuration
MetricsDate
NumACWInitiated

```

**Description**
The average call duration, measured in minutes, for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The average number of transcription messages per call for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls where agents connect with callers for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of transcription messages for the call with the highest number of said messages
for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longest call duration, measured in minutes, for a given day.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date and time (in UTC) when the metric was gathered. For example, daily metrics jobs
run at 12am local instance time (not UTC).

**Type**
int


-----

```
NumCallbackCallsCtrCompleted
NumInboundCallsCtrCompleted
NumInboundIVRAbandonCalls
NumInboundQueueAbandonCalls
NumOutboundCallsCtrCompleted

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls where After Conversation Work (ACW) is initiated for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of callback calls where interactive voice response (IVR) data is fully and completely
captured from a telephony provider for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls where interactive voice response (IVR) data is fully and
completely captured from a telephony provider for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls where callers disconnected while waiting in the interactive
voice response (IVR) system for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls where callers disconnected while waiting in the queue for a
given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
NumRecordedCalls
NumSCVCallbackCalls
NumSCVInboundCalls
NumSCVOutboundCalls
NumSCVTransferCalls
NumTransferCallsCtrCompleted

```

**Description**
The number of outbound calls where interactive voice response (IVR) data is fully and
completely captured from a telephony provider for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls where the conversation between an agent and caller is recorded for a
given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of callback calls for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound calls for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of outbound calls for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of transfer calls for a given day.

**Type**
int


-----

```
OutboundCallsAgentsConnected
TotalACWInboundMinutes
TotalACWOutboundMinutes
TotalAgentInboundMinutes
TotalHoldDurationMinutes

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of transfer calls where interactive voice response (IVR) data is fully and completely
captured from a telephony provider for a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of outbound calls where an agent is connected with a caller for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes agents spent in After Conversation Work (ACW) for inbound
calls for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes agents spent in After Conversation Work (ACW) for outbound
calls for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total number of minutes agents spent talking to callers on inbound calls for a given day.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of minutes callers were put on hold for a given day.


-----

```
TotalIVRInboundMinutes
TotalMessages
TotalOutboundMinutes
TotalQueueInboundMinutes
