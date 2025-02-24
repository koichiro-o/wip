#### MessagingLink

Represents the link between a Messaging Channel and where it's shared. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(),
upsert()

```

-----

##### Fields

**Field**
```
 EntityType
 MessagingChannelId
 RecordTypeId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `Account`

**•** `Case`

**•** `Contact`

**•** `CustomEntityDefinition—Custom Object Definition`

**•** `Lead`

**•** `Opportunity`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The channel being shared. This is a relationship field.

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
This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType


-----

```
 ShouldAttemptAutoLink
 ShouldPromptCreate
