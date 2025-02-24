#### CollaborationGroup

Represents a Chatter group. This object is available in API version 19.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), search(), update(),
upsert()

 Special Access Rules

```
The visibility of information in groups depends on the type of group and the user’s permissions.

**•** **Members: Any user with the Create and Own New Chatter Groups permission can create public, private, and unlisted groups,**
including in any Experience Cloud sites they belong to.

**•** **Owners and managers: Users can modify group details for any group they own or manage. Owners can also delete groups they**
own.


-----

**•** **Nonmembers: These user permissions allow group access regardless of group membership.**

**–** View All Data—Allows users to view all public and private groups across their org and its Experience Cloud sites. Users with this
permission can’t view unlisted group information, unless they have the Modify Unlisted Groups permission as well.

**–** Modify All Data—Allows users to view, modify, and delete all public and private groups across their org and its Experience Cloud
sites. Users with this permission can’t view or modify unlisted group information, unless they have the Manage Unlisted Groups
permission as well.

**–** Create and Set Up Experiences—Allows users to view, modify, and delete all public and private groups in Experience Cloud sites.

**–** Manage Unlisted Groups—Allows users to search for, access, and modify any unlisted group in an org and its Experience Cloud
sites.

**–** Data Export—Allows users to export any data from Salesforce, including private and unlisted group data from an org and its
Experience Cloud sites.

**•** **Apex and Visualforce: Apex code runs in system mode, which means that the permissions of the current user aren’t taken into**
account.

**–** Visualforce pages that display groups might expose unlisted or private group data to users who aren’t members.

**–** Because system mode disregards the user’s permissions, all users who are accessing a Visualforce page that’s showing a group
can act as an owner of that group.

**–** AppExchange apps that are written in Apex and that access all groups will expose unlisted groups to users who aren’t members.

To limit and manage access to the unlisted and private groups in your org:

**•** Explicitly filter out unlisted and private group information from SOQL queries in all Apex code.

**•** Use permission sets, profile-level permissions, and sharing checks in your code to further limit group access.

**•** Use Apex triggers on the CollaborationGroup object to monitor and manage the creation of groups. In Setup, enter `Group`
`Triggers` in the Quick Find box, then select Group Triggers to add triggers.

##### Fields

```
AnnouncementId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the ID of the Announcement last associated with the group. This field is available
in API version 30.0 and later.

This is a relationship field.

**Relationship Name**
Announcement

**Relationship Type**
Lookup

**Refers To**
Announcement


-----

```
BannerPhotoUrl
CanHaveGuests
CollaborationType

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the group's banner photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 36.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to true, indicates that a group allows customers. Chatter customers are people outside
your company's email domains. Customers can see only the groups they're invited to. They
can interact only with members of those groups. Customers can’t see any Salesforce
information.

This field is available starting in API version 23.0, but groups that allow customers are
accessible from earlier API versions. However, when accessed from earlier API versions, groups
that allow customers aren't distinguishable from private groups. We strongly recommend
that you upgrade to the latest API version. If you must use an earlier version, name groups
that allow customers to indicate that they include customers.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of Chatter group. Available values are:

**•** `Public—Anyone can see and post updates. Anyone can join a public group.`

**•** `Private—Only members can see the group feed and post updates. Non-members`
can only see the group name and a few other details in list views, search, and on the
group page. The group's owner or managers must add members who request to join
the group.

**•** `Unlisted—Only members and users with the Manage Unlisted Groups permission`
can see the group and post updates. Other users can’t access the group or see it in lists,
search, and feeds.


-----

```
Description
FullPhotoUrl
GroupEmail
HasPrivateFieldsAccess
InformationBody

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the group.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the group's profile photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

**Type**
email

**Properties**
Nillable, Sort

**Description**
The email address for posting to the group. For private groups, only visible to members and
users with Modify All Data or View All Data permissions.

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If set to `true, indicates that a user can see the InformationBody` and
`InformationTitle` fields in a private group. This field is set to `true` for members of
a private group and users with Modify All Data or View All Data permissions.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
InformationTitle
IsArchived
IsAutoArchiveDisabled
IsBroadcast
LastFeedModifiedDate

```

**Description**
The text of the Information section. For private groups, only visible to members and users
with Modify All Data or View All Data permissions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the Information section. For private groups, only visible to members and users
with Modify All Data or View All Data permissions.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the group is archived (true) or not (false).

This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether automatic archiving is disabled for the group (true) or not (false).

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the group is a broadcast group (true) or not (false).

This field is available in API version 36.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort


-----

```
LastReferencedDate
LastViewedDate
MediumPhotoUrl
MemberCount
Name
NetworkId

```

**Description**
The date of the last post or comment on the group.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the larger, cropped photo size.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of members in the group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the group. Group names must be unique across public and private groups. Unlisted
groups don’t require unique names.

**Type**
reference


-----

```
OwnerId
SmallPhotoUrl

##### Usage

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this group is part of. This field is available only if digital
experiences is enabled in your org.

You can only add a NetworkId when creating a group. You can’t change or add a
`NetworkId` for an existing group. This field is available in API version 26.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the group. Only the current group owner or people with the Modify All
Data permission can update the `OwnerId.`

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the group's profile photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.


Use this object to create, edit, or delete groups in an org or Experience Cloud site. Deleting a group permanently deletes all posts and
comments to the group. It also deletes all files and links posted to the group and removes the files from other locations where they were
shared.

As a Chatter group member, you can post to the group using the CollaborationGroupFeed object. As a Chatter group owner or manager,
you can add or remove group members using the CollaborationGroupMember object, post announcements to the group using the


-----

Announcement object, and accept or decline requests to join private groups using the CollaborationGroupMemberRequest object.
Additionally, the group owner, manager, or your Salesforce system administrator can invite people to join the group using the
CollaborationInvitation object.

The Salesforce system administrator doesn’t need to be a member of the group in order to send invitations using the API.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CollaborationGroupFeed**

Feed tracking is available for the object.

SEE ALSO:

CollaborationGroupMember

CollaborationGroupMemberRequest
