#### TenantSecurityCustomMetricDetail

Stores TenantSecurityCustomMetricStat drill down details. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.


-----

##### Fields

**Field**
```
Action
ActionBy
ActionDate
CustomObjectIdentifier
DiffFieldValueListHash
FieldValueListHash

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Whether the metric detail record was added, updated, or removed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user who performs the action.

**Type**
dateTime

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
When this change was made.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A virtual foreign key reference to a Custom Object in which the metric details are stored.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The hash of custom metric `diff fields value.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
MetricStatIdentifier
Name

```

**Description**
The hash of custom metric fields value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A virtual foreign key reference to TenantSecurityCustomMetricStat.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The Custom Object Api Name associates to the custom metric.

