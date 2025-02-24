#### WorkBadge

```

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
WorkAccess

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is Manual. If no value is specified, the field defaults to Manual.
All other RowCause values are read-only. After the sharing entry is created,
this field can’t be edited.

Values can include:

**•** `Manual—The User or Group has access because a user with “All” access`
manually shared the WorkAccess with them.

**•** `Owner—The User is the owner of the WorkAccess or is in a role above the`
WorkAccess owner in the role hierarchy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
User or Group ID for WorkAccess.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


Represents information about who the badge was given to and which badge was given. A WorkBadge record is created for each recipient
of a WorkBadgeDefinition.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Additional Considerations and Related Objects

```
WorkBadge is a lookup to WorkThanks. Each WorkBadge record must derive a SourceId from WorkThanks. There can be multiple
WorkBadge records tied to a single WorkThanks record.

##### Fields

```
DefinitionId
Description
GiverId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Salesforce unique ID for the given WorkBadgeDefinition record given.

This is a relationship field.

**Relationship Name**
Definition

**Relationship Type**
Lookup

**Refers To**
WorkBadgeDefinition

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the WorkBadgeDefinition.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the badge giver. Can’t be the same as `RecipientId.`

This is a relationship field.


-----

```
ImageUrl
LastReferencedDate
LastViewedDate
Message
NetworkId

```

**Relationship Name**
Giver

**Relationship Type**
Lookup

**Refers To**
User

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the badge image.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkBadge.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this WorkBadge.
If this value is null, this record might have been only referenced
(LastReferencedDate) and not viewed.

**Type**
textarea

**Properties**
Nillable

**Description**
The message accompanying the thanks badge.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
RecipientId
RewardId
SourceId

```

**Description**
The ID of the community that this WorkBadge is associated with. This field is
available only if digital experiences is enabled in your org.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Salesforce unique ID for User who is the Recipient of Badge. Can’t be
the same as `GiverId`

This is a relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce unique ID for Reward given with badge (if Reward Badge)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Salesforce unique ID for Thanks record referenced to this badge.

This is a relationship field.

**Relationship Name**
Source

**Relationship Type**
Lookup

**Refers To**
WorkThanks


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WorkBadgeChangeEvent (API version 62.0)**
Change events are available for the object.
