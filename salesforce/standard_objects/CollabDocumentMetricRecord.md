#### CollabDocumentMetricRecord

Represents an association between a CollabDocumentMetric and a Salesforce record.It tracks which Salesforce record, such as an Account
or Contact, is linked to a Quip thread for which metrics were gathered using CollabDocumentMetric. CollabDocumentMetricRecord is
available in API version 50.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
ParentRecord
QuipDocumentMetric

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
MetricDate
MetricDateOnly
EntityType

```

**Description**
The ID of the CollabDocumentMetric record.

**Type**
dateTime

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
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

