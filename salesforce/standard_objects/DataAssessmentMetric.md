#### DataAssessmentMetric

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that contain blank fields.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that have a different value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that have the same value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unmatched records that contain blank fields.


Represents a summary of statistics for fields matched and unmatched in your account records with Data.com account records. This
object is available in API version 37.0 and later.


-----

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Name
NumDuplicates
NumMatched
NumMatchedDifferent

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of duplicate records.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records in your org matched with a Data.com record that have
different fields.


-----

```
NumProcessed
NumTotal
NumUnmatched

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records processed in the data assessment.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records available for data assessment processing.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records not matched.

