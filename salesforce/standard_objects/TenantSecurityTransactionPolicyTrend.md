#### TenantSecurityTransactionPolicyTrend

Stores changes to the count of Transaction Security Policies for a connected tenant within Security Center. This object is available for
Security Center subscribers in API version 55.0 and later.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read-only.

##### Fields

```
Action
ActionBy
ActionConfig
ActionDate

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Stores information on a change to the policy. Available options include:

**•** `ADDED`

**•** `REMOVED`

**•** `UPDATED`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the person who made this change.

**Type**
textarea

**Properties**
Nillable

**Description**
Contains a JSON description for how a user is alerted to an action on the policy. For example:

**•** `In-app`

**•** `Email`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
DetailIdentifier
EventName
MetricIdentifier
MetricsType
Name
Tenant

```

**Description**
When this change was made.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Unique identifier for this detail record.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the event of the corresponding Transaction Security Policy.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding TenantSecurityMonitorMetric.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The type of metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


-----

```
TenantName
TransactionPolicyState
TransactionPolicyType

##### Associated Objects

```

**Description**
The ID of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the tenant (org) that this record is for.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The state of the transaction security policy. The possible states are ENABLED or DISABLED.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The type of policy configured. The available types are standard policy or a custom Apex
policy.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicyChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityPolicyFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityPolicyHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityPolicyOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityPolicyShare on page 66**
Sharing is available for the object.


-----
