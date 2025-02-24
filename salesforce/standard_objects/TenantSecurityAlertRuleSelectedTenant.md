#### TenantSecurityAlertRuleSelectedTenant

Stores information about a Security Center alert rule for tenants. This object is available for Security Center subscribers in API version
55.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read-only.

##### Fields

```
Name
NotificationRuleIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the corresponding TenantSecurityNotificationRule.


-----

```
Tenant

##### Associated Objects

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant (org) that this record is for.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TenantSecurityAlertRuleSelectedTenantChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityAlertRuleSelectedTenantFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityAlertRuleSelectedTenantHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityAlertRuleSelectedTenantOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityAlertRuleSelectedTenantShare on page 66**
Sharing is available for the object.
