#### WorkBadgeDefinition

Represents the attributes of a badge including the badge name, description, and image. Each WorkBadge record must have a lookup
to a WorkBadgeDefinition since badge attributes (like badge name) are derived from the WorkBadgeDefinition object.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Additional Considerations and Related Objects

```
WorkBadgeDefinition has a field called `ImageUrl` that references a DocumentID. This is a required field for creating a Badge.

To grant “giver” access to a WorkBadgeDefinition, you must also create the WorkAccess (and the related WorkAccessShare records.

Each WorkBadgeDefinition has an `ImageUrl` field that must be populated with a DocumentID of the Document record containing
the badge image.

##### Fields

```
Description
GivenBadgeCount

```

**Type**
textarea

**Properties**
Create, Update

**Description**
Required. Limit: 4000 characters. The description of the badge and what it means
to receive this badge.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of badges given per user or across all users.


-----

```
ImageUrl
IsActive
IsCompanyWide
IsLimitPerUser
IsRewardBadge

```

Note: This field can’t be added in a list view or referenced in a formula
field.

**Type**
url

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. This is the badge image that will be displayed in the UI. Use DocumentID
or ImageURL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents whether a WorkBadgeDefinition is active and available in the UI and
API.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents a special class of badges known as Company Badges. Company
badges are visible to the entire company and visible in specific list view filters.

Note: If this field is selected, everyone within the user’s network will be
able to give the badge automatically. If this field is not selected, people
with sharing must be added to the badge’s access list in order to give the
badge.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the badge limit is per user (true) or across all users (false).
The default value is `false.`

**Type**
boolean


-----

```
LastReferencedDate
LastViewedDate
LimitNumber
LimitStartDate
Name

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the badge is a reward badge (true) or not (false).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed a record that is
related to this WorkBadgeDefinition.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this
WorkBadgeDefinition. If this value is null, this record might have been only
referenced (LastReferencedDate) and not viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The badge limit per user or across all users.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the badge limit. The date can be reset to the current date.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the Badge. Label: Badge Title.


-----

```
NetworkId
OwnerId
RewardFundId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the community that this WorkBadgeDefinition is associated with. This
field is available only if digital experiences is enabled in your org.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce User ID for User who is the Owner of the WorkBadgeDefinition record
(usually the creator of the record)

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce unique ID for the WorkRewardFund that is associated with this
WorkBadgeDefinition. WorkBadgeDefinition records with a RewardFundID indicate
a Reward Badge.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkBadgeDefinitionChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkBadgeDefinitionFeed**

Feed tracking is available for the object.

**WorkBadgeDefinitionHistory**

History is available for tracked fields of the object.


-----

**WorkBadgeDefinitionOwnerSharingRule**

Sharing rules are available for the object.

**WorkBadgeDefinitionShare**

Sharing is available for the object.
