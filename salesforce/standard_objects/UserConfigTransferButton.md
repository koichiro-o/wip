#### UserConfigTransferButton

Represents the association between a Chat configuration and a live chat button. This association allows users associated with a specific
configuration to transfer chats to a button queue.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Summer ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
LiveChatButtonId
LiveChatUserConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the live chat button that agents can transfer chats to.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

**Description**

The ID of the Chat configuration; agents associated with this configuration can
transfer chats to the chat button indicated by the `LiveChatButtonId.`
