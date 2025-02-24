#### ChatterConversation

Represents a private conversation in Chatter, consisting of messages that conversation members have sent or received. This object is
available in API version 23.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field Name**
```
Id

##### Usage

```

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the conversation.


Use this object to identify private conversations in Chatter. Users can access this object if they have the Manage Chatter Messages and
Direct Messages permission. This object is read-only via the API and is provided only to allow administrators to view users' Chatter
messages; for example, for compliance purposes.

SEE ALSO:

ChatterConversationMember

ChatterMessage
