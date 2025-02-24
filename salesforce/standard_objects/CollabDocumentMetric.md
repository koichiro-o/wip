#### CollabDocumentMetric

Represents the engagement metrics for a Quip thread (document or spreadsheet) that’s linked to a Salesforce record. This object is
available in API version 50.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Document
Site
SourceTemplate
DocumentTitle
MetricDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The Quip thread ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site in which the thread is located.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the template (if any) on which a Quip thread is based.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The title of the thread.

**Type**
dateTime


-----

```
MetricDateOnly
LastUpdatedDate
LastUpdatedDateOnly
ViewerCount
UpdateCount

```

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in UTC. Available in API version
55.0 and later.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of thread views by user for the specified MetricDate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of edits made on the thread on a given day.


-----

```
EditorCount
CommenterCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
For the specified MetricDate, the number of users who edited the Quip thread.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
For the specified MetricDate, the number of users who commented on the Quip thread.

