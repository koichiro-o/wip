#### MsgChannelLanguageKeyword

Represents the consent configuration for a Messaging channel. This object is available in API version 48.0 and later.


-----

##### Supported Calls
```
describeSObjects(), delete(), query(), retrieve(), search()

 Fields

```
```
CustomKeywords
CustomResponse
DoubleOptInKeywords
HelpKeywords
HelpResponse

```

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to receive the Custom Response.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user sends a Custom Keyword.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to doubly opt in to receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to request help during a Messaging session.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user requests help.


-----

```
MasterLanguage
MessagingChannelId
MessagingChannelUsageId
OptInConfirmation

```

**Type**
textarea

**Properties**

**Description**
The language used for this consent configuration.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Messaging channel.

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
Filter, Group, Sort

**Description**
The ID of the associated Messaging channel usage record, which is in turn associated with
a messaging channel.

This is a relationship field.

**Relationship Name**
MessagingChannelUsage

**Relationship Type**
Lookup

**Refers To**
MessagingChannelUsage

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user opts in to receiving messages.


-----

```
OptInKeywords
OptOutConfirmation
OptOutKeywords

```

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to explicitly opt in to receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user opts out of receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to opt out of receiving messages.

