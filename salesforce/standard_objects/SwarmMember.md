#### SwarmMember

Represents a Salesforce member, such as an agent, of a swarm. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object for swarming in Salesforce, enable the Run Flows and Service Cloud User user permissions. For swarming in Slack,
connect Salesforce to Slack and enable the Run Flows and Slack Service User user permissions.

##### Fields

```
AssignedDateTime
CompletedDateTime
HelpNeeded

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the member is added to the swarm.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the member exits the swarm or the swarm closes.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Short description of the problem that the swarm is trying to solve.


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
RelatedRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

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
Name of the swarm or record number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the Salesforce user assigned to a swarm.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


-----

```
Status
SwarmId

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the record the swarm’s problem is related to. The record can be of, for example, a case,
incident, sales opportunity, or change request.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, ChangeRequest, Incident, Opportunity, Problem, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the swarm member or swarm.

Possible values are:

**•** `Closed`

**•** `In Progress`

**•** `New`

The default value is `New.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the swarm the member belongs to.

This field is a relationship field.

**Relationship Name**
Swarm

**Relationship Type**
Lookup

**Refers To**
Swarm


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SwarmMemberFeed on page 54**
Feed tracking is available for the object.

**SwarmMemberHistory on page 62**
History is available for tracked fields of the object.

**SwarmMemberOwnerSharingRule on page 64**
Sharing rules are available for the object.

**SwarmMemberShare on page 66**
Sharing is available for the object.
