#### CollaborationInvitation

Represents an invitation to join Chatter, either directly or through a group. This object is available in API version 21.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

```

-----

##### Special Access Rules

Invitations are available if “Allow Invitations” is enabled for your organization.

Invitations are limited to your allowed domain(s) unless the invite is sent from a private group that allows customers. Allowed domains
are set by the administrator.

Invitations to customers are available if “Allow Customer Invitations” is enabled for your organization. Users must have the “Invite
Customers to Chatter” permission to send invitations to people outside their Chatter domain.

##### Fields

```
InvitedUserEmail
InvitedUserEmailNormalized
InviterId
OptionalMessage
ParentId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The email address for the user invited to join Chatter. Label is `Invited Email.`

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
A normalized version of the InvitedUserEmail entered. Label is Invited Email
```
  (Normalized).

```
**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The person that initiated the invitation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
An optional message from the person sending the invitation to the person receiving it.

**Type**
reference


-----

```
SharedEntityId
Status

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used when the email address on the invitation is different than the one entered when the
invitee accepts the invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group associated with this invitation.

**•** If the invitation is to join Chatter, the `SharedEntityId` is the ID of the User that
created the invitation. The invitee will auto-follow the inviter.

**•** If the invitation is to join a group within Chatter, the `SharedEntityId is the ID of`
the Chatter CollaborationGroup.

**•** To invite a customer, set `SharedEntityId` to the ID of the private
CollaborationGroup with Allow Customers turned on.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the invitation. Possible values are:

**•** `Sent`

**•** `Accepted`

**•** `Canceled`


Use this object to create or delete (cancel) invitations to join Chatter. You can either invite a user to join Chatter directly or as part of a
CollaborationGroup.

Note: To invite someone to join a CollaborationGroup, you must be either the owner or a manager of the group or a Salesforce
system administrator.

The Salesforce system administrator doesn’t need to be a member of the group in order to send invitations using the API.

When the person accepts your CollaborationGroup invitation, they join the CollaborationGroup and Chatter as well.

Note: You can't send invitations to users of the organization the invite was sent from.

Invited users can view profiles, post on their feed, and join groups, but they can't see your Salesforce data or records.


-----

If your organization allows groups with customers, owners and managers of private groups with the “Allow Customers” setting, as well
as system administrators, can use this object to invite customers.

##### Java Samples

The following example shows how to send an invitation to join Chatter:
```
public void invitePeople(String inviterUserId, String invitedEmail) throws Exception {
   CollaborationInvitation invitation = new CollaborationInvitation();
   invitation.setSharedEntityId(inviterUserId);//pass the userId of the inviter
   invitation.setInvitedUserEmail(invitedEmail);//email of the invited user
   insert(invitation);
}

```
The following example shows how to send an invitation to a customer user from a group that allows customers:
```
public void inviteToGroup(String GroupName, String invitedEmail) throws Exception {
   QueryResult qr = query("select id from collaborationgroup where name = '" +
     GroupName); //pass the group name
   String groupId = qr.getRecords()[0].getId();
   CollaborationInvitation invitation = new CollaborationInvitation();
   invitation.setSharedEntityId(groupId);//pass the groupId
   invitation.setInvitedUserEmail(invitedEmail);//email of the invited user
   insert(invitation);
}

##### Apex Samples
String emailAddress = 'bob@external.com';
CollaborationGroup chatterGroup = [SELECT Id
    FROM CollaborationGroup
    WHERE Name='All acme.com'
    LIMIT 1];
CollaborationInvitation inv = New CollaborationInvitation();
inv.SharedEntityId = chatterGroup.id;
inv.InvitedUserEmail = emailAddress;
try {
  Insert inv;
} catch(DMLException e){
  System.debug('There was an error with the invite: '+e);
}
