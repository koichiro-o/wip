#### EventRelayConfig

```
Represents the configuration of an event relay, which relays platform events and change data capture events from Salesforce to Amazon
EventBridge. This object is available in API version 56.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
**•** To retrieve or query this object, you must have the View Setup and Configuration permission.

**•** [This object is read-only. To configure an event relay, use EventRelayConfig in Tooling API or EventRelayConfig in Metadata API.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_tooling.meta/api_tooling/tooling_api_objects_eventrelayconfig.htm)


-----

##### Fields

**Field**
```
DestinationResourceName
DeveloperName
EventChannel
Language

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name of the named credential, which stores the AWS account information.
The destinationResourceName value contains the callout: prefix. For example:
```
  callout:MyRelayNamedCredential

```
**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is Record Type Name. This field is
automatically generated, but you can supply your own value if you create the record using
the API.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The full name of the event channel used in the event relay. For example:
```
  MyRelayChannel__chn

```
**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the EventRelayConfig.

Possible values are:

**•** `da—Danish`

**•** `de—German`


-----

```
MasterLabel
NamespacePrefix

```


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

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label for the EventRelayConfig. In the UI, this field is Event Relay Config.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
`namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values:

**•** In Developer Edition organizations, the namespace prefix is set to the namespace prefix
of the organization for all objects that support it. There is an exception if an object is in
an installed managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the Developer
Edition organization of the package developer.


-----

```
RelayOption
State
UsageType

```


**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

**Type**
textarea

**Properties**
Nillable

**Description**
A JSON-encoded string that contains an option for resuming an event relay after the system
recovers from an error. This option is used if the event relay can't resume after the last relayed
event. The options available are:

**•** `"{\"ReplayRecovery\":\"LATEST\"}"—(Default) Start relaying events`
from new events received in the event bus. Use this option if you aren’t interested in
missed events while the relay was down.

**•** `"{\"ReplayRecovery\":\"EARLIEST\"}"—Resend all events stored in`
the event bus and relay new events thereafter. The event bus stores events for up to
three days. Use this option if you want to reprocess all stored events and catch up on
missed events.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The execution state of the event relay. Possible values are:

**•** `RUN—The event relay is running and actively relaying event messages from Salesforce`
to Amazon EventBridge.

**•** `PAUSE—An administrator paused the event relay. No events are relayed to Amazon`
EventBridge during this status. All current state information is saved.

**•** `STOP—(Default) The event relay is stopped and no events are relayed to Amazon`
EventBridge. All current state information is deleted.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reserved for future use.


-----
