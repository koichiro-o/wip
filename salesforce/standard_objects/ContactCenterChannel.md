#### ContactCenterChannel

Represents a junction object that relates a Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging channel to a
CallCenter object for Bring Your Own Channel for CCaaS. This object also represents the routing details for a voicemail configuration.
This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, Service Cloud Voice with Amazon Connect, Service Cloud Voice with Partner Telephony, Service Cloud Voice with
Partner Telephony from Amazon Connect, or Bring Your Own Channel for Contact Center as a Service (CCaaS) must be enabled.To access
this object, you must be a SysAdmin user or have ViewSetup user permissions.

##### Fields

```
ChannelId
ContactCenterId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
For Bring Your Own Channel for CCaaS, this field represents the unique ID of the Bring Your
Own Channel messaging channel (MessagingChannel) that’s associated with the contact
center (CallCenterId). Available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
Channel

**Refers To**
MessagingChannel

**Type**
reference


-----

```
UserId
VoicemailFallbackQueueId
VoicemailHandler

```

**Properties**
Create, Filter, Group, Sort

**Description**
This field is a relationship field. For Bring Your Own Channel for CCaaS, this field represents
the unique ID of the contact center (CallCenterId) that’s associated with the Bring Your Own
Channel messaging channel (MessagingChannel). Available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
ContactCenter

**Relationship Type**
Master-detail

**Refers To**
CallCenter (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For internal use only.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If voicemail routing is configured for the contact center, this field represents the unique ID
of the fallback queue to use if voicemail routing fails. Don't change the value in this field.
Instead, configure voicemail routing in Lightning Experience.

This field is a relationship field.

**Relationship Name**
VoicemailFallbackQueue

**Refers To**
Group

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

**Description**
If voicemail routing is configured for the contact center, this field represents the unique ID
of the flow used to route voicemails. Don't change the value in this field. Instead, configure
voicemail routing in Lightning Experience.
