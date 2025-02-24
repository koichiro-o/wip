#### PipelineInspectionSumField

Use this object to learn which field from the opportunity object is used to aggregate Pipeline Inspection metrics on a pipeline view. This
object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To use PipelineInspectionSumField, enable Pipeline Inspection. Users with a Pipeline Inspection user permission, the Customize Application
permission or the Modify All Data permission can access this object. To create and modify records, users must have either the Customize
Application permission or the Modify All Data permission.

##### Fields

```
SobjectType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object that stores the summary fields.

Possible values are:


-----

```
SummaryField

```


**•** `Opportunity`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The field used to summarize Pipeline Inspection metrics. Possible values are standard field
names or custom field IDs for custom currency and number fields.

**•** `Amount`

**•** `ExpectedRevenue`

**•** `TotalOpportunityQuantity`

**•** custom_field_ID

