#### EngagementChannelType

Represents a channel through which a customer can be reached for communication. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
 ContactPointType
 LastReferencedDate
 LastViewedDate
 Name
 OwnerId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact point type of the channel.

Possible values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

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

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the communication subscription consent record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

**Description**
The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EngagementChannelTypeChangeEvent (API version 61.0)**
Change events are available for the object.

**EngagementChannelTypeFeed**

Feed tracking is available for the object.

**EngagementChannelTypeHistory**

History is available for tracked fields of the object.

**EngagementChannelTypeOwnerSharingRule**

Sharing rules are available for the object.

**EngagementChannelTypeShare**

Sharing is available for the object.
