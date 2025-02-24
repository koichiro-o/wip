#### PipelineInspMetricConfigLocalization

Represents the translated label of a Pipeline Inspection metric. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

```

-----

##### Fields

**Field**
```
Language
NamespacePrefix
ParentId
Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language of the Pipeline Inspection metric.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix of the Pipeline Inspection metric language.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related Pipeline Inspection metric.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PipelineInspMetricConfig

**Type**
textarea

**Properties**
Create, Filter, Sort, Update

**Description**
The value of the Pipeline Inspection metric.


-----
