#### CaseRelatedIssue

This object acts as a junction between a customer issue (Case) and the Incident or Problem that represents an associated service failure.
This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A relationship field that represents the case you're linking a Problem or Incident to.

**Relationship Name**
Case


-----

```
Name
RelatedEntityType
RelatedIssueId
RelationshipType

```

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A brief description of the related case.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows what type of object the related entity is.

Possible values are:

**•** `Incident`

**•** `Problem`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

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
Shows how two records relate to each other.


-----

```
UniqueKeyIndex

##### Associated Objects

```

Possible values are:

**•** `Root Cause`

**•** `Similar`

The default value is 'Root Cause'.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
This field is unique within your organization.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseRelatedIssueChangeEvent on page 67 (API version 59.0)**
Change events are available for the object.

**CaseRelatedIssueFeed on page 54**
Feed tracking is available for the object.

**CaseRelatedIssueHistory on page 62**
History is available for tracked fields of the object.
