#### ChangeRequestRelatedIssue

Represents a junction object that relates a ChangeRequest to an Incident or Problem due to a service failure. This object is available in
API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
ChangeRequestId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ChangeRequest ID that's linked to the Problem or Incident.


-----

```
Name
RelatedEntityType
RelatedIssueId
RelationshipType

```

**Relationship Name**
ChangeRequest

**Relationship Type**
Lookup

**Refers To**
ChangeRequest

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A description of the change request as it relates to the problem or incident.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the related object type.

Possible values are:

**•** `Incident`

**•** `Problem`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents the related Problem or Incident.

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


-----

**Description**
Shows how the ChangeRequest and Incident or Problem records relate to each other.

Possible values are:

**•** `Caused By`

**•** `Fixed By`

The default value is 'Caused By'.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestRelatedIssueChangeEvent on page 67**
Change events are available for the object.

**ChangeRequestRelatedIssueFeed on page 54**
Feed tracking is available for the object.

**ChangeRequestRelatedIssueHistory on page 62**
History is available for tracked fields of the object.
