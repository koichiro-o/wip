#### ListViewChartInstance

Retrieves metadata for all standard and custom charts for a given entity in context of a given list view. This object is available in API
versions 34.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
AggregateField
AggregateType
ChartType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The field that’s used for calculating data on each group. `AggregateField`
can’t be the same as `GroupingField.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of calculations to run on each group. The supported AggregateType
values are Count, `Sum, and` `Avg.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of chart to create. The supported chart types are horizontal bar chart,
vertical bar chart, and donut chart.


-----

```
DataQuery
DataQueryWithoutUserFilters
DeveloperName
ExternalId
GroupingField

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The SOQL query that can be executed to fetch the data for drawing a chart.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The SOQL query that can be executed to fetch the data for drawing a chart,
without user filters.

Available in API v43.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
API name of the chart. This name can contain only underscores and alphanumeric
characters, and must be unique in your org. It must begin with a letter, not include
spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a
managed package and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no DeveloperName is specified,
performance slows down while Salesforce generates one for each record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
string

**Properties**
Filter, Group, Sort


-----

```
IsDeletable
IsEditable
IsLastViewed
Label
ListViewChartId

```

**Description**
The field that’s used to divide the data into collections. The field has to be
supported by SOQL GROUP BY functionality. GroupingField can’t be the
same as `AggregateField.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the chart can be deleted.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the chart can be edited. Standard charts are not editable.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if a chart is the last viewed by a user.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The display name of the chart.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the chart created by a user. For standard charts, this is null.

This is a relationship field.


-----

```
ListViewContextId
SourceEntity

##### Usage

```

**Relationship Name**
ListViewChart

**Relationship Type**
Lookup

**Refers To**
ListViewChart

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the list view in context of which the chart is generated. Required to query
```
  ListViewChartInstance.

```
This is a relationship field.

**Relationship Name**
ListViewContext

**Relationship Type**
Lookup

**Refers To**
ListView

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
API name of the entity to which the chart is related. Required to query
```
  ListViewChartInstance.

```

**Example 1. Retrieve all custom and standard charts for Account entity for All Accounts list view**
```
  SELECT AggregateField, AggregateType, ChartType, DataQuery, DeveloperName, ExternalId,
   GroupingField, Id, IsDeletable, IsEditable, IsLastViewed, Label, ListViewChartId,
  ListViewContextId, SourceEntity FROM ListViewChartInstance WHERE SourceEntity=’Account’
   and ListViewContextId=’00BR0000000U8Hr’

```
**Example 2. Retrieve metadata for a specific custom chart by ID for Account entity and All Accounts list view**


-----

**Example 3. Retrieve metadata for a specific standard chart by its developer name for Account entity and All Accounts list**
**view**
```
  SELECT AggregateField, AggregateType, ChartType, DataQuery, DeveloperName, ExternalId,
   GroupingField, Id, IsDeletable, IsEditable, IsLastViewed, Label, ListViewChartId,
  ListViewContextId, SourceEntity FROM ListViewChartInstance WHERE SourceEntity=’Account’
   and ListViewContextID=’00BR0000000U8Hr’ and DeveloperName=’AccountsByIndustry’
