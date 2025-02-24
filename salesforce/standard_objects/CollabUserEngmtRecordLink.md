#### CollabUserEngmtRecordLink

Represents an association between a CollabUserEngagementMetric and a Salesforce record. It tracks which Salesforce record, such as
an Account or Contact, is associated with the user engagement metric. This object is available in API version 50.0 and later.

Note: The CollabUserEngmtRecordLink object is now deprecated. You can still access user engagement metrics for metric dates
before August 12, 2021. To obtain user engagement metric for dates starting from August 12, 2021, follow the instructions in the
[Quip Engagement Metrics documentation.](https://help.salesforce.com/articleView?id=sf.quip_template_metrics.htm&type=5&language=en_US)

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
MetricDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date of the gathered metric.


-----

```
Name
ObjectType
ParentRecordId
UserEngagementMetricId
