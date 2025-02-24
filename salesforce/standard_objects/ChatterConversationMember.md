#### ChatterConversationMember

Represents a member of a private conversation in Chatter. A member has either sent messages to or received messages from other
conversation participants. This object is available in API version 23.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ConversationId
MemberId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated ChatterConversation.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
ID of the conversation member.

##### Usage

Use this object to view members of private conversations in Chatter. Users can access this object if they have the Manage Chatter
Messages and Direct Messages permission. This object is read-only via the API and is provided only to allow administrators to view users'
Chatter messages; for example, for compliance purposes.

SEE ALSO:

ChatterConversation

ChatterMessage
