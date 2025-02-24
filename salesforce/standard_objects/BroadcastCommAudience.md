#### BroadcastCommAudience

Represents the audience that the broadcast communication is sent to. This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object with Service Cloud, enable Incident Management in Setup and set up Broadcast Communications.

##### Fields

```
AudienceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast communication audience.

**•** If `BroadcastType` is `Alert, this value is the ID of the Group record where the`
message is sent to.

**•** If `BroadcastType` is `Email, this value is the ID of the ListEmail record where the`
email is sent to.

**•** If `BroadcastType` is `ExperienceSiteBanner, this value is the ID of the`
Network record where the banner is displayed at.

**•** If `BroadcastType` is `Slack, this value is the ID of the CollaborationRoom record`
where the message is sent to.

This field is a polymorphic relationship field.

**Relationship Name**
Audience


-----

```
BroadcastCommAudienceNumber
BroadcastCommunicationId
BroadcastFailureReason
BroadcastType

```

**Relationship Type**
Lookup

**Refers To**
CollaborationRoom, Group, ListEmail, Network

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number for the BroadcastCommAudience record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the broadcast communication record.

This field is a relationship field.

**Relationship Name**
BroadcastCommunication

**Relationship Type**
Lookup

**Refers To**
BroadcastCommunication

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason the broadcast communication failed to send.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Medium used to distribute the message.

Possible values are:

**•** `Alert`


-----

```
LastReferencedDate
LastViewedDate
MessageTimeStamp
OwnerId

```


**•** `Email`

**•** `ExperienceSiteBanner`

**•** `Slack`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate is not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If `BroacastType` is `Slack, this value is the timestamp when the broadcast Slack`
message was sent.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
SiteBannerText
SiteBannerVisibility
Status

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**
If BroadcastType is ExperienceSiteBanner, this field contains the banner text
displayed on the associated site.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If `BroadcastType` is `ExperienceSiteBanner, this field contains information`
about who can view the banner.

Possible values are:

**•** `AuthenticatedUsers`

**•** `GuestUsers`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the broadcast communication.

Possible values are:

**•** `Active—The site banner is visible on the site. Only applies if` `BroadcastType` is
```
   ExperienceSiteBanner.

```
**•** `Deleted—The message is successfully deleted and isn’t visible anymore. Only applies`
if `BroadcastType` is `Slack.`

**•** `DeleteFailed—The message failed to delete but is still visible. Only applies if`
`BroadcastType` is `Slack.`

**•** `Failed—The message failed to send. Applies to any` `BroadcastType.`

**•** `Inactive—The site banner isn’t visible on the site. Only applies if BroadcastType`
is `ExperienceSiteBanner.`

**•** `Sent—The message is sent successfully. Only applies if the` `BroadcastType` is
`Email` or `Slack.`

**•** `Updated—The message is successfully edited. Only applies if the BroadcastType`
is `Slack.`

**•** `UpdateFailed—The message failed to edit and the update isn’t visible. Only applies`
if the `BroadcastType` is `Slack.`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastCommAudienceChangeEvent on page 67**
Change events are available for the object.

**BroadcastCommAudienceFeed on page 54**
Feed tracking is available for the object.

**BroadcastCommAudienceHistory on page 62**
History is available for tracked fields of the object.

**BroadcastCommAudienceOwnerSharingRule on page 64**
Sharing rules are available for the object.

**BroadcastCommAudienceShare on page 66**
Sharing is available for the object.
