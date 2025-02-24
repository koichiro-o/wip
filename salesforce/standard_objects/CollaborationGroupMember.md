#### CollaborationGroupMember

Represents a member of a Chatter group. This object is available in API version 19.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), describeLayout(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Fields

```
```
CollaborationGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated CollaborationGroup.

This is a relationship field.

**Relationship Name**
CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
CollaborationGroup


-----

```
CollaborationRole
LastFeedAccessDate
MemberId
NotificationFrequency

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The role of a group member. Group owners and managers can change roles for members
of their groups. The valid values are:

**•** `Standard—Indicates that a user is a group member. Members can post and comment`
in the group.

**•** `Admin—Indicates that a user is a group manager. Managers can post and comment,`
change member roles, edit group settings, add and remove members, delete posts and
comments, and edit the group information field.

Note: To change the group owner, use the `OwnerId` field on the
CollaborationGroup object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when a group member last accessed the group’s feed. The value is only
updated when a member explicitly consumes the group’s feed, not when the member sees
group posts in other feeds, like the profile feed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group member.

This is a relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist


-----

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The frequency at which Salesforce sends Chatter group email digests to this
member. Can only be set by the member or users with the “Modify All Data” permission.
The valid values are:

**•** `D—Daily`

**•** `W—Weekly`

**•** `N—Never`

**•** `P—On every post`

The default value is specified by the member in their Chatter email settings. In communities,
the `Email on every post` option is disabled once more than 10,000 members
choose this setting for the group. All members who had this option selected are automatically
switched to `Daily digests.`

##### Usage

Use this object to view, create, and delete Chatter group members. You must be a group owner or manager to create members for
private Chatter groups.

SEE ALSO:

CollaborationGroup

CollaborationGroupMemberRequest
