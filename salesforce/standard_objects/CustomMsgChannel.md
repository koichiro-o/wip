#### CustomMsgChannel

Represents a custom conversation channel and stores event-driven Messaging settings. Custom conversation channels are implemented
for Bring Your Own Channel and Bring Your Own Channel for CCaaS Messaging channels. This object is available in API version 63.0 and
later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Access to standard objects requires Salesforce admin privileges or the Customize Application permission.

##### Fields

```
ChannelDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
HasInboundReceipts
HasTypingIndicator
MessagingChannelId

```

**Description**
Specifies the ConversationChannelDefinition for the custom channel.

This field is a relationship field.

**Relationship Name**
ChannelDefinition

**Refers To**
ConversationChannelDefinition

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner supports read receipts and delivery receipts for inbound
messages (true) or whether the partner doesn’t support these inbound acknowledgements
and the functionality is hidden from the Salesforce admin in the Messaging settings (false).
The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner doesn’t support typing indicators for outbound messages and
the functionality is hidden from the Salesforce admin in the Messaging settings (true) or
whether outbound typing indicators are supported by the partner (false). The default
value is `false, meaning the outbound typing indicator feature is supported by default.`
To disable the outbound typing indicator feature, set this value to `true.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the Messaging Channel ID for the custom channel. This field is unique within your
organization.

This field is a relationship field.

**Relationship Name**
MessagingChannel

**Refers To**
MessagingChannel


-----
