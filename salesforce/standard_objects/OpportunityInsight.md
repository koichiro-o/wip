#### OpportunityInsight

Represents an individual insight (deal prediction, follow-up reminder, or key moment) related to an opportunity record.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), query(), retrieve()

 Special Access Rules

```
To see an insight related to a specific opportunity, users need a Sales Cloud Einstein license and access to the opportunity record. As of
the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

##### Fields

```
ActualHeardWithinDays

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
CloseDate
CompetitorName
ContactName
ContactTitle
CurrencyIsoCode

```

**Description**
The number of days it has been since a prospect has responded for insights of
type Prospect has not responded and No communication.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The close date of the related opportunity for insights of type `Opportunity`
`is overdue` and `Opportunity is unlikely to close in`
```
  time.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field has been deprecated as of API version 45.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use as of API version 46.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use as of API version 46.0.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.


-----

```
Division
ExpectedHeardWithinDays
LastHeard
LastReferencedDate
LastViewedDate
OpportunityId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the related record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The expected number of days it takes to hear back from a prospect for insights
of type Prospect has not responded and No communication.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the related prospect was last heard from for insights of type
```
  Prospect has not responded.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
reference


-----

```
Rationale
Reason
TaskDue
Title
TrendType

```

**Properties**
Filter, Group, Sort

**Description**
The ID of the related opportunity record.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The explanation for an insight, providing more background information and
details that are specific to the org.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason why a specific insight type is appearing. Relevant to the following
insights:

**•** Opportunity is unlikely to close in time

**•** Opportunity slowing

**•** Opportunity boosting

**•** Time-consuming opportunity

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that a task associated with the related opportunity record is due.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The title of the insight.

**Type**
picklist


-----

```
Type

##### Usage

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The trend type of the insight. Possible values include:

**•** Negative

**•** Positive

**•** Informational

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of insight. Possible values include:

**•** Opportunity is unlikely to close in time

**•** Prospect has not responded

**•** Opportunity slowing

**•** Opportunity boosting

**•** Time-consuming opportunity

**•** No communication

**•** Re-engaged opportunity

**•** Opportunity has an overdue task

**•** Opportunity is overdue

**•** Opportunity has no open activity

**•** Unusual opportunity amount


This object is read-only and isn’t supported in workflows, triggers, or process builder.
