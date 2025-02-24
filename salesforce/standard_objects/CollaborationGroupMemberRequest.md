#### CollaborationGroupMemberRequest

Represents a request to join a private Chatter group. This object is available in API version 21.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
CollaborationGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
RequesterId
ResponseMessage
Status

```

**Description**
ID of the private Chatter group.

This is a relationship field.

**Relationship Name**
CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
CollaborationGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user requesting to join the group; must be the ID of the context user.

This is a relationship field.

**Relationship Name**
Requester

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Optional message to be included in the notification email when `Status` is `Declined.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the request. Available values are:

**•** `Accepted`

**•** `Declined`

**•** `Pending`


-----

##### Usage

This object represents a request to join a private Chatter group, and can be used to accept or decline requests to join private groups you
own or manage. On create, an email is sent to the owner and managers of the private group to be accepted or declined. When the
`Status` is `Accepted` or `Declined, an email is sent to notify the requester. When the` `Status` is `Declined, a`
`ResponseMessage` is optionally included to provide additional details.

Note the following when working with requests:

**•** Users with the “Modify All Data” or “View All Data” permission can view records for all groups, regardless of membership.

**•** A user can be a member of 300 groups. Requests to join groups count against this limit.

**•** `Status` can't be specified on create.

**•** You can only update a request when the `Status` is `Pending.`

**•** You can't delete or update a request with a `Status` of `Accepted` or `Declined.`

SEE ALSO:

CollaborationGroup

CollaborationGroupMember
