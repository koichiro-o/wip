#### MobileSecurityUserMetric

Represents the metrics for users who have Enhanced Mobile Security policies enforced. This object is available in API version 51.0 and
later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

##### Fields

```
MetricsDate
UserCount

##### Usage

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date the metrics were collected.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of users who have mobile security policies enforced.


A user with the Manage Enhanced Mobile App Security permission can run this SOQL query.


-----
