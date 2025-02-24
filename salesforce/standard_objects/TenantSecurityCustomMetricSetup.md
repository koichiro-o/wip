#### TenantSecurityCustomMetricSetup

Represents the configuration for a custom metric within Security Center. This object is available in API version 61.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
CustomMetricIdentifier

```

**Type**
string


-----

```
CustomObjectIdentifier
CustomObjectName
DiffFieldIdentifierList
DisplayFieldIdentifierList
Description
MetricDisplayType

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique identifier for the custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the custom object for this custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique name of the custom object for this custom metric.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The list of fields that were selected for `Diff` display.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The list of fields that were selected for display.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the custom metric.

**Type**
string


-----

```
MetricGroup
MetricName
Name

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The display type for this metric. For example, `diff` or `non-diff.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The category of the custom metric. Some category examples include
```
  Authenticationand Configuration.

```
**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom metric. The MetricName and Name fields have the same value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom metric. The MetricName and Name fields have the same value.

