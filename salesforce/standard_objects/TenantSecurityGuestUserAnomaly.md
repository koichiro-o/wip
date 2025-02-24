#### TenantSecurityGuestUserAnomaly

Represents metric details for guest user anomaly events detected by Threat Detection. This object is available in API version 60.0 and
later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read-only.

##### Fields

```
DetailIdentifier
EventDate

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique identifier for this detail record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
EventIdentifier
EventName
MetricIdentifier
MetricsType
Name
RequestedObjects

```

**Description**
The time when the anomaly was reported. For example, 2020-01-20T19:12:26.965Z. The
most granular setting is milliseconds.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique ID of the event, which is shared with the corresponding storage object.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the event.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of data collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

**Type**
textarea


-----

```
Score
SoqlCommands
Summary
Tenant
TenantName

```

**Properties**
Create, Nillable, Update

**Description**
The objects requested by the customers.

**Type**
double

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
Specifies how significantly the guest user behavior deviates from the other guest users. It is
formatted as a number between 0 and 1.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
SOQL commands run by the guest user.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text summary of the anomaly that caused this event.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant that was targeted in the event.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the tenant that was targeted in the event.


-----

```
TotalControllerEvents
UserAgent
UserIdentifier
UserType
Username

##### Associated Objects

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of times controllers were triggered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User Agent for this event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin user’s unique ID.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of user of this event. For example, a guest user.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The origin username in the format of `user@company.com` at the time the event was
created.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**TenantSecurityGuestUserAnomalyChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityGuestUserAnomalyFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityGuestUserAnomalyHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityGuestUserAnomalyOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityGuestUserAnomalyShare on page 66**
Sharing is available for the object.
