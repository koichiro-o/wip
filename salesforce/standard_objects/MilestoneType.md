#### MilestoneType

Represents a milestone (required step in a customer support process). This object is available in API version 18.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

##### Fields

```
Description
Name
RecurrenceType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
A description of the milestone.

**Type**
string

**Properties**
Create, Filter, idLookup, Update

**Description**
The name of the milestone.

**Type**
picklist

**Properties**
Create,Update


-----

**Description**
The type of recurrence for the milestone.

##### Usage

Use this object to query and manage the milestone type for CaseMilestone records.

SEE ALSO:

CaseMilestone

SlaProcess
