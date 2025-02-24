#### TenantUsageEntitlement

Represents a data structure that contains information about the features or functionalities that a Salesforce org has access to. This object
is available in API version 28.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

 Fields

```
```
AmountUsed

```

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
CurrentAmountAllowed
EndDate
Frequency
HasRollover

```

**Description**
The quantity of an entitlement that has been used.

**Type**
double

**Properties**
Filter, Sort

**Description**
The amount of an entitlement that a tenant is allowed to use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The end date of the setting, based on license end dates that entitle the org to that setting.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How often the tenant's entitlement data is automatically reviewed to see how much of the
entitlement has been used.

Possible values are:

**•** `Daily`

**•** `Fortnightly`

**•** `Monthly`

**•** `Once`

**•** `Quarterly`

**•** `Weekly`

**•** `Yearly`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that a certain amount of a customer's unused entitlements from a set time period
can be added to the next set time period. This field is reserved for future use.

The default value is `false.`


-----

```
IsPersistentResource
MasterLabel
OverageGrace
ResourceGroupKey
Setting

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the data that will be saved and available for future use even after closing a
session.

The default value is `false.`

**Type**
string

**Properties**
Group, Nillable

**Description**
The overarching name of an element in your organization. A MasterLabel is visible to
customers.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the Allowed Amount that a customer can use without incurring an
additional charge. The default value is 100% (no overage grace). This field is reserved for
future use.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Tracks resource usage across different segments for the same setting. For example, a Messages
entitlement that tracks email messages and SMS messages separately could have one
ResourceGroupKey of SMS and another ResourceGroupKey of Email. In most cases though,
TenantUsageEntitlements are configured for the org and not by segment.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A rule or attribute that can be used to configure the appearance or actions in an organization.


-----

```
StartDate
UsageDate

##### Associated Objects

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
This date is the earliest start date of any license contributing to the provisioning aggregation
output.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date an event occurred that deducted from the tenant's entitlement.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantUsageEntitlementChangeEvent on page 67**
Change events are available for the object.

**TenantUsageEntitlementFeed on page 54**
Feed tracking is available for the object.

**TenantUsageEntitlementHistory on page 62**
History is available for tracked fields of the object.

**TenantUsageEntitlementOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantUsageEntitlementShare on page 66**
Sharing is available for the object.
