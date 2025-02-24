#### SurveyInvitation

Represents the invitation sent to a participant to complete the survey.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
CommunityId
ContactId
EmailBrandingId
InvitationLink

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site that you want to send the survey to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact who received the invitation. This field is available in API v49.0
and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the survey email branding object that’s associated with this invitation.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL to the survey that is sent to participants. To query on this field, you need
access to the associated Survey record.


-----

```
InviteExpiryDateTime
IsDefault
LastReferencedDate
LastViewedDate
LeadId
Name

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the survey invitation expires.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether this is the default survey invitation to use when the survey
is sent to participants.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
survey invitation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this survey invitation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the lead who received the invitation. This field is available in API v49.0 and
later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
OptionsAllowGuestUserResponse
OptionsAllowParticipantAccessTheirResponse
OptionsCollectAnonymousResponse
OwnerId
ParticipantId
ResponseStatus

```

**Description**
The name of the survey invitation that appears in the UI.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants who don’t have a Salesforce account can
complete the survey.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants can access a copy of their responses after they
complete the survey.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants can complete the survey anonymously.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the survey invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the participant if the participant is a Salesforce contact, user, or lead.

**Type**
picklist


-----

```
SurveyId
UUID

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of a participant’s response to the survey that’s associated with the
survey invitation. Possible values include:

**•** `NotStarted — For an invitation with a` `ParticipantID, it means`
that the recipient hasn’t opened the survey. For an invitation without the
```
   ParticipantID, it means that none of the recipients have opened the

```
survey.

**•** `Started — For an invitation with a` `ParticipantID, it means that`
the recipient opened the survey. For an invitation without the
```
   ParticipantID, it means that the survey has been opened by at least

```
one recipient.

**•** `Paused — For an invitation with a` `ParticipantID, it means that the`
recipient has paused the survey. For an invitation without the
```
   ParticipantID, it means that the survey has been paused by any one

```
of the recipients. Paused isn't available for invitations in which either
```
   OptionsAllowParticipantAccessTheirResponse or

```
`OptionsCollectAnonymousResponse` is true.

**•** `PartiallyCompleted— For an invitation with a ParticipantID`
field, it means that the recipient has partially completed the survey. For an
invitation without the `ParticipantID` field, it means that at least one
recipient has partially completed the survey. Available in API version 63.0
and later.

**•** `Completed — For an invitation with a ParticipantID, it means that`
the recipient has submitted the survey. For an invitation without the
```
   ParticipantID, it means that the invitation has been submitted by at

```
least one recipient.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the survey that’s sent in the invitation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique user ID that's added to a survey invitation generated for a contact,
lead,or user.


-----

```
UserId

##### Associated Objects

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user who received the invitation. This field is available in API v49.0 and
later.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyInvitationChangeEvent (API version 62.0)**
Change events are available for the object.

**SurveyInvitationOwnerSharingRule**

Sharing rules are available for the object.

**SurveyInvitationShare**

Sharing is available for the object.
