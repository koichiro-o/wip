#### CommSubscriptionChannelType

Represents the engagement channel through which you can reach a customer for a communication subscription. This object is available
in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
 CommunicationSubscriptionId
 EngagementChannelTypeId
 LastReferencedDate
 LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated communication subscription record.

This is a relationship field.

**Relationship Name**
CommunicationSubscription

**Relationship Type**
Lookup

**Refers To**
CommSubscription

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated engagement channel type record.

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
MessagingChannelUsageId
Name
OwnerId

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

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
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the communication subscription channel type record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionChannelTypeChangeEvent (API version 61.0)**
Change events are available for the object.

**CommSubscriptionChannelTypeFeed**

Feed tracking is available for the object.

**CommSubscriptionChannelTypeHistory**

History is available for tracked fields of the object.

**CommSubscriptionChannelTypeOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionChannelTypeShare**

Sharing is available for the object.
