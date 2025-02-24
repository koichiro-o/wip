#### VisualforceAccessMetrics

Represents summary statistics for Visualforce pages.

```
SELECT City, CountryIso, Latitude,
Longitude, PostalCode FROM LoginGeo WHERE
LoginGeoId = '0LE###############'

```

-----

##### Supported Calls
```
count(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, to access VisualforceAccessMetrics, users must have the Customize Application permission.

##### Fields

```
ApexPageId
ProfileId
DailyPageViewCount

```

**Type**
reference

**Properties**
Aggregate, Filter, Group, Sort

**Description**
The ID of the Visualforce page.

This is a relationship field.

**Relationship Name**
ApexPage

**Relationship Type**
Lookup

**Refers To**
ApexPage

**Type**
reference

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The ID of the use who viewed the Visualforce page.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

**Type**
int


-----

```
MetricsDate
LogDate

##### Usage

```

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of views received by the specified Visualforce page.

**Type**
date

**Properties**
Aggregate, Filter, Group, Sort

**Description**
The date the metrics are queried.

**Type**
date

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The most recent page access date.


Use this object to query information on the Visualforce pages in your org.
```
SELECT ApexPageId, DailyPageViewCount, Id, ProfileId, MetricsDate, LogDate FROM
VisualforceAccessMetrics
