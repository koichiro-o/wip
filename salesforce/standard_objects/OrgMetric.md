#### OrgMetric

Represents a feature or metric that Salesforce Optimizer evaluates. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in orgs where Salesforce Optimizer is enabled. Requires the Modify All Data and Customize Application user
permissions.

##### Fields

```
Category

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The category of the feature evaluated.

Possible values are:

**•** `Custom Code`

**•** `Custom Layouts`

**•** `Fields`

**•** `Improve Org Security`

**•** `Improve User Experience`


-----

```
FeatureType
LatestOrgMetricScanSummaryId
Name

```
SEE ALSO:



**•** `Increase User Adoption`

**•** `Object Limits`

**•** `Org Limits`

**•** `Reports And Dashboards`

**•** `Usage`

**•** `User Management`

**•** `Workflow`

The default value is `Org Limits.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
[The feature evaluated. For a full list, see Features Evaluated in Salesforce Optimizer.](https://help.salesforce.com/s/articleView?id=sf.optimizer_included_features.htm&type=5&language=en_US)

The default value is `Unassigned Page Layouts.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The feature’s OrgMetricScanSummaryID from the most recent Optimizer evaluation.

This field is a relationship field.

**Relationship Name**
LatestOrgMetricScanSummary

**Refers To**

OrgMetricScanSummary on page 3708

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A unique number that identifies the feature.


_[Salesforce Help: Improve Your Implementation with Salesforce Optimizer](https://help.salesforce.com/s/articleView?id=sf.optimizer_introduction.htm&language=en_US&type=5)_


-----
