#### TenantSecurityPolicySelectedTenant

[Stores the list of tenants selected for a Security Center policy. For more information, see Define and Deploy Security Policies. This object](https://help.salesforce.com/s/articleView?id=sf.security_center_deploy_policies.htm&type=5&language=en_US)
is available to Security Center subscribers in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read/write.

##### Fields

```
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
PolicyIdentifier
Tenant

##### Associated Objects

```

**Description**
The name of the policy for the selected tenant.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the security policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicySelectedTenantChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityPolicySelectedTenantFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityPolicySelectedTenantHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityPolicySelectedTenantOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityPolicySelectedTenantShare on page 66**
Sharing is available for the object.
