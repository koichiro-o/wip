#### ConversationChannelDefinition

Represents a configurable definition of a conversation channel that’s implemented for Interaction Service for Bring Your Own Channel
and Bring Your Own Channel for CCaaS messaging channels. This object is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, interaction service must be configured. Access to standard objects requires Salesforce admin privileges or the
Customize Application permission.

##### Fields

```
CapabilitiesSupportsCustomChannelParameters
CapabilitiesSupportsDoubleOptInConsent

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether admins can configure custom parameters and parameter mappings for
messaging channels. Custom parameters and parameter mappings are used to pass additional
information at runtime to Omni-Channel flows. The default value is false. Available in API
version 61.0.

**Type**
boolean


-----

```
CapabilitiesSupportsExplicitConsent
CapabilitiesSupportsImplicitConsent
CapabilitiesSupportsIsoCountryCode
CapabilitiesSupportsKeywords
ConnectedAppOauthLink

```

**Properties**
Filter

**Description**
Indicates whether the channel supports (true) the Double Opt-In consent level. The default
value is `false. If set to true, then` `capabilitiesSupportsExplicitConsent`
must also be set to true. This field is optional and isn’t supported for Bring Your Own Channel.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports (true) the Explicit Opt-In consent level. This field
is optional.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports (true) the Implicit Opt-In consent level. This value
is required and must always be set to true. The default value is false.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports (true) ISO country codes. The default value is false.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports (true) keywords. The default value is false.

**Type**
string

**Properties**
Filter, Group, Sort


-----

```
ConnectedAppType
ConsentOwner
ConversationVendorInfoId

```

**Description**
DO NOT SET OR CHANGE THIS VALUE. This value is automatically generated. This field
represents the OAuth link for the connected app if the ConnectedAppType is `Partner.`
This is a string identifier to the connected app containing the partner Org ID and the consumer
ID minus the key prefixes.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The owner of the connected app used to manage authentication between Salesforce
Interaction Service and the Messaging or CCaaS partner’s system.

Possible values are:

**•** `Partner`

**•** `Customer`

The default value is `Partner.`

If set to Partner, the partner creates the connected app and includes it in their managed
package. If set to `Customer, the admin creates the connected app.`

Available in API version 62.0.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system the customer uses to manage consent levels.

Possible values are:

**•** `Partner`

**•** `Salesforce`

The default value is `Salesforce.`

For example, if set to Salesforce, consent levels are managed by the Salesforce system.
If set to `Partner, consent levels are managed by the partner’s telephony system.`

For Bring Your Own Channel, this value must be set to `Salesforce.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
customEventChnlAddrIdField
CustomEventPayloadField
customEventRecipientField

```

**Description**
The `ConversationChannelDefinition.ConversationVendorInfoId`
value used to link this record to the ConversationVendorInfo record. For example,
0m8000000000000123.

This field is a relationship field.

**Relationship Name**
ConversationVendorInfo

**Relationship Type**
Lookup

**Refers To**
ConversationVendorInfo

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the
`ChannelAddressIdentifier` field.

This field is deprecated in API version 60.0 and will be removed in API version 61.0. Use a
combination of `customEventTypeField` and `customEventPayloadField`
instead.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the `Payload` field in
the format `<orgNamespace>__<CustomFieldName>__c. This is the API name of`
the custom Payload field in the custom platform event. For example, devorg__Payload__c.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the Recipient field.

This field is deprecated in API version 60.0 and will be removed in API version 61.0. Use a
combination of `customEventTypeField` and `customEventPayloadField`
instead.


-----

```
CustomEventTypeField
CustomIconId
CustomPlatformEvent
CustomerConnectedAppOauthLink

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the Platform event type
(EventType) field, in the format <orgNamespace>__<CustomFieldName>__c. This
is the API name of the custom EventType field in the custom platform event. For example,
devorg__EventType__c.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For Bring Your Own Channel and Bring Your Own Channel for CCaaS, this field represents
the name of the status resource image used to identify the channel integration, such as a
channel logo. For the best results, set the image size to 50px x 50px and save the image in
SVG file format. This field is optional. Available in API version 61.0 and later.

This field is a relationship field.

**Relationship Name**
CustomIcon

**Relationship Type**
Lookup

**Refers To**
StaticResource

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The API name of the custom platform event created for the Interaction Service API in the
format `<orgNamespace>__<CustomPlatformEventName>__e. For example,`
devorg__TestEvent__e.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
DeveloperName
IsInboundReceiptsEnabled
IsTypingIndicatorDisabled
MasterLabel

```

**Description**
DO NOT SET OR CHANGE THIS VALUE. This value is automatically generated. This field
represents the OAuth link for the connected app created by an admin if the
ConnectedAppType is `Customer.` Available in API version 62.0.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the custom metadata type object in the API in the format
`<Prefix>_<ConversationChannelDefinition>, where` `Prefix` matches
the prefix you gave to the name of the interaction service connected app. For example,
Partner1_ChannelDefinition1, where Partner1 is the prefix and ChannelDefinition1 is the
given name.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner supports read receipts and delivery receipts for inbound
messages (true) or whether the partner doesn’t support these inbound acknowledgements
and the functionality is hidden from the Salesforce admin in the Messaging settings (false).
The default value is `false.`

This field is available in API version 63.0 and later.

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

This field is vailable in API version 63.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort


-----

```
NamespacePrefix
RoutingOwner

```

**Description**
The UI label name for the custom metadata type object in the API. This name appears in
several places in the UI, so include the partner channel name for easy identification. For
example, Channel Definition 1.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation. The namespace prefix can have

```
one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

`NamespacePrefix` is null if the publisher is Salesforce.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system the customer uses to manage routing for Bring Your Own Channel or Bring Your
Own Channel for CCaaS.

Possible values are:

**•** `Partner`

**•** `Salesforce`

The default value is `Salesforce.`

For example, if set to `Salesforce, routing is managed by the Salesforce system. If set to`
```
  Partner, routing is managed by the partner’s system.

```
For Bring Your Own Channel, this value must be set to `Salesforce.`


-----
