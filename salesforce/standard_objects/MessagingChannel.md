#### MessagingChannel

```


**•** `Create–Merchant account is created.`

**•** `Disable–The account is deactivated. For example, the payment provider or the`
merchant disables an account due to fraudulent activity.

**•** `PaymentEnable–The account is active and ready to receive payments.`

**•** `PayoutEnable–The account is ready to receive payouts.`

**•** `Update–Merchant account property change occurs.`

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the merchant account for which the event occurs.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount


Represents a communication channel that an end user can use to send a message to an agent. A communication channel can be an
SMS number, a Facebook page, or another supported messaging channel. This object is available in API version 40.0 and later.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), query(), retrieve(), search(), update(), upsert()

 Fields

```
```
BusinessHoursId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ChannelAddressIdentifier
ChannelDefinitionId
ConsentType

```

**Description**
The operating hours for your business, when agents are available. Available only
in orgs that use Einstein Bots.

This is a relationship field.

**Relationship Name**
BusinessHours

**Relationship Type**
Lookup

**Refers To**
BusinessHours

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A UUID that identifies a deployed messaging channel. This identifier is unique
across orgs, so a channel with the same MessagingPlatformKey in a sandbox and
production will have a different ChannelAddressIdentifier for each. Available in
API version 59.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated conversation channel definition, which is used only in Bring Your
Own Channel. Available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
ChannelDefinition

**Refers To**
ConversationChannelDefinition

**Type**
picklist

**Properties**
Create, defaultedOnCreate, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of consent, or opt-in, that is required to message users on this channel.
This field is available in API version 48.0 and later. Possible values are:


-----

```
ConversationEndResponse
CriticalWaitTime
Description
DeveloperName
DoubleOptInPrompt
EngagedResponse

```


**•** `DoubleOptIn`

**•** `ExplicitOptIn`

**•** `ImplicitOptIn` (default value)

The property `defaultedOnCreate` has been removed in API version 51.0
and later. Now the consent type is defaulted to `ImplicitOptIn` when the
consent type isn’t set on create only for channels that support consents.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Automated response to the customer when the agent ends the conversation.
(Optional)

**Description**
Reserved for future use. This field has been deprecated as of API version 52.0.

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name for the messaging channel. This value is a concatenation
of the messaging platform key and the message type.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Automated response to the end user to prompt them to doubly opt in to receiving
messages. Available in API version 48.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
InitialResponse
IsActive
IsAuthenticated
IsoCountryCode
IsRequireDoubleOptIn

```

**Description**
Automated response to the customer when the conversation is accepted by the
agent. (Optional)

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
First automated response to the customer for a new conversation. (Optional)

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a channel is active and can receive messages.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a user is authenticated to a voice assistant. The org permission
Live Message Voice is required to access and update this field. Available in API
version 44.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Two-letter ISO 3166-1 alpha-2 code for the country that the phone number is
associated with. For example, the code for United States is `US. Available in API`
version 44.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
IsRestrictedToBusinessHours
IsUserMatchByExternalIdOnly
Language
MasterLabel
MessageType

```

**Description**
Indicates whether double opt-in is required (true) or not (false) for this
Messaging channel. Available in API version 48.0 and later.

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to restrict matching on customer by external ID only (and not
use the full name). This field has been deprecated as of API version 52.0.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Unique name for the `MessagingChannel.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of message. Possible values are:

**•** `AppleBusinessChat—Represents Apple Messages for Business.`

**•** `Custom—Represents Bring Your Own Channel. Available in API version`
58.0 and later.

**•** `EmbeddedMessaging—Represents Messaging for In-App and Web.`
Available in API version 50.0 and later.

**•** `Facebook`


-----

```
MessagingPlatformKey
OfflineAgentsResponse
OptInPrompt
OptInResponse
OptOutResponse

```


**•** `Phone`

**•** `Text`

**•** `Voice`

**•** `WhatsApp`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Unique key for a channel that the end user can message.

**Description**
Reserved for future use.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Automated response to the end user to prompt them to explicitly opt in to
receiving messages. Available in API version 49.0 and earlier.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**

Automated response to the end user when they opt in to messaging. Available
in API versions 48.0 and 49.0. Use the `OptInConfirmation field of the`
MsgChannelLanguageKeyword on page 3295 object instead.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**

Automated response to the end user when they opt out of messaging. Available
in API version 48.0 only. Use the `OptOutConfirmation field of the`
MsgChannelLanguageKeyword object instead.


-----

```
OutsideBusinessHoursResponse
PlatformType
RoutingConfigurationId
RoutingType
SessionHandler

```

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the channel is `Standard` or `Enhanced.`

When a standard SMS or Facebook Messenger channel is upgraded, the
PlatformType changes from `Standard` to `Enhanced. When a standard`
WhatsApp channel is upgraded, the original channel’s PlatformType remains
`Standard` and a new channel is created with a PlatformType of Enhanced.

Messaging for In-App and Web channels have a PlatformType of `Enhanced.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Specifies which Omni-Channel routing configuration to use. This field is required
when `RoutingType` [is OmniSkills. To learn more, see Create Routing](https://help.salesforce.com/articleView?id=service_presence_create_routing_configuration.htm&language=en_US)
[Configurations.](https://help.salesforce.com/articleView?id=service_presence_create_routing_configuration.htm&language=en_US)

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type used to support Omni-Channel’s different routing methods.

**•** `OmniQueue (queue-based routing)`

**•** `OmniSkills (skills-based routing)`

When this value isn’t set, `OmniQueue` is used.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The queue or Omni-Channel flow that the channel's messaging sessions are
routed to. Available in API version 51.0 and later.


-----

```
TargetQueueId
TargetUserId

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Queue in which incoming conversations are placed while waiting for an agent
to accept.

This is a relationship field.

**Relationship Name**
TargetQueue

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Messaging User or agent for the conversation. Available in API version 50.0 and
earlier.


While third-party messaging channels can be created via Apex, we recommend creating channels via the Messaging Settings page in
Setup. Channels created via Apex may not work and can't be deleted.

In enhanced WhatsApp, Facebook Messenger, Apple Messages for Business, and LINE channels, the flow of a channel's messaging traffic
is controlled by an associated MessagingChannelUsage record. The MessagingChannelUsage determines whether the channel is active
or deactivated.
