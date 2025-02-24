#### DashboardComponent

Represents a dashboard component, which can be a chart, metric, table, or gauge on a dashboard. Access is read-only. This object is
available in API version 21.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
CustomReportId
DashboardId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Requires the user permission "Manage All Private Reports and Dashboards." The ID of the
report that provides data for the dashboard component. See Report.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the dashboard that contains the dashboard component. See Dashboard.

This is a relationship field.


-----

```
Name

##### Usage

```

**Relationship Name**
Dashboard

**Relationship Type**
Lookup

**Refers To**
Dashboard

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the dashboard component.


Provides read only access to the current values in dashboard component fields.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DashboardComponentFeed**

Feed tracking is available for the object.
