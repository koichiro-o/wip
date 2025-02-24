#### EventRelayFeedback

Represents execution state information about an event relay from Salesforce to Amazon EventBridge for platform events and change
data capture events. Query this object to get information such as the event relay status and any error message. This object is available
in API version 56.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
ErrorCode
ErrorIdentifier
ErrorMessage
ErrorTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code of the last error that occurred during the relay of event messages. For a list
of possible error codes and messages, see Error Codes.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier of an unexpected system error that occurred during the relay of event messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The error message of the last error that occurred during the relay of event messages. For a
list of possible error codes and messages, see Error Codes.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time in the UTC time zone when the last error occurred during the relay of
event messages.


-----

```
EventRelayConfigId
EventRelayNumber
LastRelayedEventTime
RemoteResource
Status

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the event relay configuration that this feedback record is collecting the execution
information of.

This field is a relationship field.

**Relationship Name**
EventRelayConfig

**Relationship Type**
Lookup

**Refers To**
EventRelayConfig

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number that identifies the EventRelayFeedback record. This field is of type Auto Number.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time in the UTC time zone when the last event was relayed to Amazon
EventBridge.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the partner event source associated with the event relay. It is in the format
```
  aws.partner/salesforce.com/orgID/channelID. For example:
  aws.partner/salesforce.com/00DRM000000Fxts2AC/0YLRM0000004Dfg4AE.

```
**Type**
picklist


-----

```
UsageType

##### Error Codes

```

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the event relay.

Possible values are:

**•** `ERROR— The event relay encountered an error while running or during a state change`
that the administrator initiates. During the ERROR state, no events are relayed to Amazon
EventBridge. The system attempts periodically to recover from the error. If it succeeds,
the Status field value changes to RUNNING or to the new state that the administrator
selected. The event relay attempts to resume sending events from the event bus from
where it left off. In rare occasions, if it can't resume after the last relayed event, it uses
the error recovery option in the relayOption field of EventRelayConfig to determine
where to resume from.

**•** `DELETED—Reserved for future use.`

**•** `PAUSED— An administrator paused the event relay. No events are relayed to Amazon`
EventBridge during this status. When an administrator resumes the event relay, events
are relayed from the last position in the event bus, as long as they're within the retention
window.

**•** `RUNNING— The event relay is running and actively relaying events from Salesforce to`
Amazon EventBridge.

**•** `STOPPED—The event relay is stopped and no events are relayed to Amazon`
EventBridge. Some state information stored in EventRelayFeedback fields is deleted, such
as `LastRelayedEventTime and error fields. When the event relay is resumed,`
only new events are relayed.

The default value is `STOPPED.`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.


This table contains the error codes and messages that a query on EventRelayFeedback can return in the `ErrorCode` and
`ErrorMessage` fields.

|Error Code|Error Description|
|---|---|
|sfdc.platform.eventbus.relay.aws.partner.eventsource.invalid|The configured event relay's AWS named credentials are invalid.|


-----

|Error Code|Error Description|
|---|---|
|sfdc.platform.eventbus.relay.aws.partner.eventsource.connect.error|The configured event relay encountered an error while connecting to Amazon EventBridge.|
|sfdc.platform.eventbus.relay.feature.not.supported|The event relay is configured with an unsupported feature, such as event encryption and change data capture event enrichment.|
|sfdc.platform.eventbus.relay.event.delivery.limit.error|You’ve exceeded the event delivery limit for your org.|
|sfdc.platform.eventbus.relay.temporarily.unavailable|The event relay is temporarily unavailable due to an internal error.|

