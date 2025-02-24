#### ListViewChart

Represents a graphical chart that’s displayed on Salesforce for Android, iOS, and mobile web list views. The chart aggregates data that
is filtered based on the list view that’s currently displayed. This object is available in API version 33.0 and later and is accessible by portal
users.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
AggregateField
AggregateType
ChartType
DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Query, Restricted picklist, Retrieve, Sort, Update

**Description**
The field that’s used for calculating data on each group. `AggregateField` can’t be the
same as `GroupingField.`

**Type**
picklist

**Properties**
Create, Filter, Group, Query, Restricted picklist, Retrieve, Sort, Update

**Description**
The type of calculations to run on each group. The supported `AggregateType` values are
```
  Count, Sum, and Avg.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Query, Restricted picklist,Retrieve, Sort, Update

**Description**
The type of chart to create. The supported chart types are horizontal bar chart, vertical bar chart,
and donut chart.

**Type**
string

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The fully qualified developer name of the chart.


-----

```
GroupingField
Language
MasterLabel
OwnerId
SobjectType

```

Note: Only users with View DeveloperName OR View Setup and Configuration permission
can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Query, Restricted picklist, Retrieve, Sort, Update

**Description**
The field that’s used to divide the data into collections. The field must be supported by SOQL
`GROUP BY` functionality. `GroupingField` can’t be the same as `AggregateField.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the `MasterLabel.`

**Type**
string

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The label for the chart.

**Type**
reference

**Properties**
Create, Filter, Group, Query, Retrieve, Sort, Update

**Description**
The ID of the user who owns the chart.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist


-----

**Properties**
Create, Filter, Group, Query, Restricted picklist, Retrieve, Sort

**Description**
The API name of the sObject for the chart.
