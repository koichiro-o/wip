#### ScorecardMetric

```

**Description**
The name of the Scorecard Association.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the scorecard that the association is related to. Several metrics can be tied to a
single scorecard.

This is a relationship field.

**Relationship Name**
Scorecard

**Relationship Type**
Lookup

**Refers To**
Scorecard

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The associated object that a specific scorecard is associated with.

This is a polymorphic relationship field.

**Relationship Name**
TargetEntity

**Relationship Type**
Lookup

**Refers To**
Account, ChannelProgram, ChannelProgramLevel


Stores information about a Salesforce report that is run and summarized to get a single value. The stored value is added as a metric to
the related Scorecard object. This object is available in API version 40.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
Category
Description
Name
ReportId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Groups metrics together. It comes with a predefined set of dropdown list entries and can
be extended to address vendor’s needs each category is user-generated and can be localized
through translation workbench.

Possible values are:

**•** `Adoption`

**•** `Field Enablement`

**•** `Marketing`

**•** `Sales`

**•** `Support`

The default value is 'Sales'.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the metric that appears on a scorecard.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric that appears on a scorecard.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ScorecardId
