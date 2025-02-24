#### BroadcastTopic

Represents a definition of a broadcast topic. A broadcast topic is associated with a list of Experience Cloud network sites for Service Cloud
and collaboration rooms for Sales Cloud. The topic is created for a specific user role. Collaboration rooms are linked to Slack channels.
This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object with Sales Cloud, enable Slack Terms of Service and Sales Cloud for Slack App.


-----

To access this object with Service Cloud, enable Incident Management in Setup and Broadcast Site Banner in the Incident Management
setup.

##### Fields

```
BroadcastReason
Description
IsFeatured
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Reason for the broadcast topic. This field differentiates between Service Cloud and Sales
Cloud use cases.

Possible values are:

**•** `FeedChannels—Used in Sales Cloud and associates the topic with collaboration`
rooms.

**•** `IncidentCommunication—Used in Service Cloud for Customer Service Incident`
Management and associates the topic with networks.

The default value is `FeedChannels.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the broadcast topic.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the broadcast topic is featured (true) or not (false). This field is
applicable only when BroadcastReason is FeedChannels. A featured topic displays the
associated collaboration rooms to new users.

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
OwnerId
TopicType

```

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the broadcast topic.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Owner of the broadcast topic.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Category for the broadcast topic.

Possible values are:


-----

**•** `DealsWon—Feed of won deals to see your team's successes. This value appears when`
the Sales Cloud special access rules are enabled.

**•** `DealsToWatch—Feed of deals that have an amount above a specified value and`
are likely to close. This value appears when the Sales Cloud special access rules are
enabled.

**•** `Incident Communication—This value appears when the Service Cloud special`
access rules are enabled.
