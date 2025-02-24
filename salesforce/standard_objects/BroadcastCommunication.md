#### BroadcastCommunication

Represents a broadcast communication related to an incident. This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete()

 Special Access Rules

```
To access this object with Service Cloud, enable Incident Management in setup and set up Broadcast Communications.

##### Fields

```
Body

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**

**•** If `BroadcastType` is `Alert, this field contains the alert message.`

**•** If `BroadcastType` is `Email, this field contains the email body text.`

**•** If `BroadcastType` is `ExperienceSiteBanner, this field is empty.`

**•** If `BroadcastType` is `Slack, this field contains the Slack message.`


-----

```
BroadcastCommunicationNumber
BroadcastType
CustomNotificationTypeId
LastReferencedDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number for every BroadcastCommunication record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Medium used to distribute the message.

Possible values are:

**•** `Alert`

**•** `Email`

**•** `ExperienceSiteBanner`

**•** `Slack`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the custom notification template used to frame the Slack message. Only applies if
`BroadcastType` is `Slack.`

Available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
CustomNotificationType

**Relationship Type**
Lookup

**Refers To**
CustomNotificationType

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
OwnerId
RelatedRecordId

```

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
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the incident associated with the broadcast communication.

This field is a relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Incident


-----

```
Subject

##### Associated Objects

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**

**•** If `BroadcastType` is `Alert, this field is the alert message in the format “Incident`
Alert | <Incident subject> | <Incident Number>.”

**•** If `BroadcastType` is `Email, this field is the subject of the email sent.`

**•** If `BroadcastType` is `ExperienceSiteBanner, this field is empty.`

**•** If `BroadcastType` is `Slack, this field is in the format “Incident Alert | <Incident`
Subject>."


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BroadcastCommunicationChangeEvent on page 67**
Change events are available for the object.

**BroadcastCommunicationFeed on page 54**
Feed tracking is available for the object.

**BroadcastCommunicationHistory on page 62**
History is available for tracked fields of the object.

**BroadcastCommunicationOwnerSharingRule on page 64**
Sharing rules are available for the object.

**BroadcastCommunicationShare on page 66**
Sharing is available for the object.
