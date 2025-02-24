#### ContextParamMap

Represents optional context data for a Conversation or a ConversationParticipant. This object is available in API version 57.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ContextEntityId
MapKey
MapValue

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Conversation or ConversationParticipant record.

This field is a polymorphic relationship field.

**Relationship Type**
Lookup

**Refers To**
Conversation, ConversationParticipant

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key for the context data.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The value for the context data.


-----
