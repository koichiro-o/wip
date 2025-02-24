#### OrgMetricScanSummary

Represents the results summary for a specific feature in a Salesforce Optimizer evaluation. This object is available in API version 47.0 and
later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

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
ErrorMessage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
FeatureLimit
ImplementationEffort
ItemCount
Name

```

**Description**
The message returned if an error occurred during the most recent Optimizer evaluation.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The numerical limit of a feature.

**Example**
For the Custom Field Limits feature, `FeatureLimit` is `500` for Developer Edition orgs.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The estimated time needed to complete the recommended actions for the feature.

Possible values are:

**•** `1 - 2 hours`

**•** `30 - 60 minutes`

**•** `< 30 minutes`

**•** `> 2 hours`

The default value is `30 minutes.`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of issues found for the feature. Corresponds to the number of
```
  OrgMetricScanResult objects generated for the feature in an Optimizer evaluation.

```
**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A number that identifies the feature’s results summary.


-----

```
OrgMetricId
PercentUsage
ScanDate
Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The OrgMetric ID that represents the feature analyzed in the Optimizer evaluation.

This field is a relationship field.

**Relationship Name**
OrgMetric

**Relationship Type**
Master-detail

**Refers To**

OrgMetric on page 3703 (the master object)

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A percentage associated with a feature.

**Example**
For the Incomplete Chatter Profiles feature, the `PercentUsage` value is `100` if 100% of
users have complete Chatter profiles.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the report for the Optimizer evaluation was generated.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The recommended action for the feature.

Possible values are:

**•** `Action Required`

**•** `Immediate Action Required`


-----

```
Unit

```
SEE ALSO:



**•** `No Action Required`

**•** `Not Currently Enabled`

**•** `Review Required`

**•** `Unable to Analyze`

The default value is `No Action Required.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unit of measurement used in the feature’s results summary.

**Example**
For the Data Storage feature, the `Unit` is `MB.`


_[Salesforce Help: Improve Your Implementation with Salesforce Optimizer](https://help.salesforce.com/s/articleView?id=sf.optimizer_introduction.htm&language=en_US&type=5)_
