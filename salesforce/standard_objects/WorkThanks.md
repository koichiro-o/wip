#### WorkThanks

Represents the source and message of a thanks post.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Additional Considerations and Related Objects

WorkBadge is a lookup to WorkThanks. Each WorkBadge record must derive a SourceId from WorkThanks.

##### Fields

```
FeedItemId
GiverId
Message

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the FeedItem related to the thanks badge.

This is a relationship field.

**Relationship Name**
FeedItem

**Relationship Type**
Lookup

**Refers To**
FeedItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Salesforce user ID for the giver of the Thanks record.

This is a relationship field.

**Relationship Name**
Giver

**Relationship Type**
Lookup

**Refers To**
User

**Type**
textarea

**Properties**
Create

**Description**
Required. Message associated with the Thanks record.


-----

```
NetworkId
OwnerId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the community that this WorkThanks is associated with. This field is
available only if digital experiences is enabled in your org.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce user ID for the owner of the badge record (typically the same user as
the giver of the record).

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkThanksChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkThanksOwnerSharingRule**

Sharing rules are available for the object.

**WorkThanksShare**

Sharing is available for the object.
