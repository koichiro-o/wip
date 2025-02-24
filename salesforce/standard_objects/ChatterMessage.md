#### ChatterMessage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the `ChatterExtension.`

This is a relationship field.

**Relationship Name**
ChatterExtension

**Relationship Type**
Lookup

**Refers To**
ChatterExtension

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Experience Cloud site where the `ChatterExtension` is deployed.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The position of the `ChatterExtension` icon in the Chatter publisher.


Represents a message sent as part of a private conversation in Chatter. This object is available in API version 23.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve(), update()

```

-----

##### Fields

**Field Name**
```
Body
ConversationId
SenderId
SenderNetworkId
SentDate

```

**Type**
textarea

**Properties**
Update

**Description**
Text of the message.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the conversation that the message is associated with.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the sender.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site from which the message was sent. This field is
available only if digital experiences is enabled in your org.

This field is available in API version 32.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date the message was sent.


-----

##### Usage

Use this object to view and delete messages sent or received via private conversations in Chatter. Users can access this object if they
have the Manage Chatter Messages and Direct Messages permission. Users with the Moderate Experiences Chatter Messages permission
can access this object in Experience Cloud sites they’re a member of, only if the message has been flagged as inappropriate. This object
is provided to allow administrators to view and delete users’ Chatter messages, for example, for compliance purposes.

Messages are hard deleted. That is, they’re removed completely without a trip to the Recycle Bin.

Deleting a message that resulted from sharing a file with someone doesn’t also delete the file.

SEE ALSO:

ChatterConversation

ChatterConversationMember
