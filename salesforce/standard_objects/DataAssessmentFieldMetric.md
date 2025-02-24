#### DataAssessmentFieldMetric

Represents summary statistics for matched, blank, and differing fields in account records of an org compared to records in Data.com.
This object is available in API version 37.0 and later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
**Child Relationships**
DataAssessmentFieldMetric is a child object of DataAssessmentMetric object.

##### Fields

```
DataAssessmentMetricId
FieldName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
A unique number that identifies the parent DataAssessmentMetric record.

This is a relationship field.

**Relationship Name**
DataAssessmentMetric

**Relationship Type**
Lookup

**Refers To**
DataAssessmentMetric

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the assessed field.


-----

```
Name
NumMatchedBlanks
NumMatchedDifferent
NumMatchedInSync
NumUnmatchedBlanks
