#### CollabTemplateMetricRecord

Represents an association between a CollabTemplateMetric and a Salesforce record.It tracks which Salesforce record, such as an Account
or Contact, is linked to a Quip template for which metrics were gathered using CollabTemplateMetric. CollabTemplateMetricRecord is
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


-----

```
MetricDate
MetricDateOnly
EntityType

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabTemplateMetric record.

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

