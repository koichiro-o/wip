#### Scorecard

Use scorecards to measure partner performance and establish benchmarks for channel programs within Experience Cloud. Display any
report summary results that your channel account manager or executive team wants to see. This object is available in API version 40.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
Description
LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the scorecard.

**Type**
dateTime


-----

```
LastViewedDate
Name
OwnerId

##### Usage

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the scorecard visible to end users.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the scorecard.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


The Scorecard object is used in tandem with the ScorecardMetric and ScorecardAssociation objects.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ScorecardOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ScorecardShare on page 66**
Sharing is available for the object.
