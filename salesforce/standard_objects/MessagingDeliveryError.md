#### MessagingDeliveryError

Represents a log of triggered outbound failures to verify when a triggered outbound has failed. This object is available in API version
44.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
CreatedById
CreatedDate
DestinationPhoneNumber

```

**Type**
reference

**Properties**
Defaulted on createFilter, Group, Sort

**Description**
ID of the user who created the error.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date the error was created.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
FailureReason
FlowEntity
FullMessage
Id
IsDeleted
LastModifiedById

```

**Description**
The recipient of the phone call.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The provided reason for why the message failed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The entity that triggered the flow to send the message.

**Type**
textarea

**Description**
Plain error text.

**Type**
id

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**
Identifier of the error.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the error has been deleted.

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The ID of the user who last modified the error log.


-----

```
LastModifiedDate
MessagingChannelId
MessagingEndUserId
MessagingTemplateId

```

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date when the Messaging error log was last modified.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the MessagingChannel on page 3215.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier for the Messaging user.

This is a relationship field.

**Relationship Name**
MessagingEndUser

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Messaging template used.


-----

```
Name
SystemModstamp
Type
