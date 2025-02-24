#### ThreatDetectionFeedback

Represents feedback provided by a user about a Threat Detection event that occurred in your org. The feedback specifies whether the
event was malicious, suspicious, not a threat, or unknown. Each ThreatDetectionFeedback object is associated with one of these Threat
Detection storage events: ApiAnomalyEventStore, CredentialStuffingEventStore, ReportAnomalyEventStore, or SessionHijackingEventStore.
This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), update(),
upsert()

 Fields

```
```
LastReferencedDate
LastViewedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.


-----

```
Response
ThreatDetectionEventId
ThreatDetectionFeedbackNumber

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the severity of the threat.

Possible values are:

**•** `Malicious`

**•** `Not a Threat`

**•** `Suspicious`

**•** `Unknown`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the unique ID of one of these associated Threat Detection storage events:

**•** [ApiAnomalyEventStore](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/sforce_api_objects_apianomalyeventstore.htm)

**•** [CredentialStuffingEventStore](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/sforce_api_objects_credentialstuffingeventstore.htm)

**•** [ReportAnomalyEventStore](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/sforce_api_objects_reportanomalyeventstore.htm)

**•** [SessionHijackingEventStore](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/sforce_api_objects_sessionhijackingeventstore.htm)

For example, `0fjRM000000005p.`

This is a polymorphic relationship field.

**Relationship Name**
ThreatDetectionEvent

**Relationship Type**
Lookup

**Refers To**
ApiAnomalyEventStore, CredentialStuffingEventStore, ReportAnomalyEventStore,
SessionHijackingEventStore

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number used as the unique name for this object.


-----

```
UserId
Username

##### Associated Object

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin user’s unique ID. For example, `005000000000123.`

This is a polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin username in the format of `user@company.com` at the time the object was
created.


This object has the following associated object. It’s available in the same API version as this object.

**ThreatDetectionFeedbackFeed**

Feed tracking is available for the object.

SEE ALSO:

_[Salesforce Help: Threat Detection](https://help.salesforce.com/articleView?id=real_time_em_threat_detection.htm&type=5&language=en_US)_
