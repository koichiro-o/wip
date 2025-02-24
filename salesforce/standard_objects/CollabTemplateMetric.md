#### CollabTemplateMetric

Represents the engagement metrics for a Quip template.This object is available in API version 50.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Template

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


-----

```
TemplateTitle
Site
MetricDate
MetricDateOnly
LastUpdatedDate
LastUpdatedDateOnly

```

**Description**
The ID of the template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site on which the template is available.

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
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort


-----

```
TotalDocumentCount

##### Associated Objects

```

**Description**
The date that the thread was created, last edited, or last shared in UTC. Available in API version
55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of documents created based on the template.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CollabTemplateMetricChangeEvent (API version 62.0)**
Change events are available for the object.
