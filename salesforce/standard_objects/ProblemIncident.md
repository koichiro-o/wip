#### ProblemIncident

Represents a junction object that relates a Problem to an Incident. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
IssueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

This field is a polymorphic relationship field.

**Relationship Name**
Issue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem


-----

```
Name
RelatedEntityType
RelatedIssueId
RelationshipType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the incident that's related to the problem.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object type of the related entity.

Possible values are:

**•** `Incident`

**•** `Problem`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedIssue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how the Problem and Incident records relate to each other.

Possible values are:

**•** `Caused By`

**•** `Similar`


-----

The default value is `Caused By.`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProblemIncidentChangeEvent on page 67**
Change events are available for the object.

**ProblemIncidentFeed on page 54**
Feed tracking is available for the object.

**ProblemIncidentHistory on page 62**
History is available for tracked fields of the object.
