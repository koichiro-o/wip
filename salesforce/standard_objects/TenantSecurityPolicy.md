#### TenantSecurityPolicy

[Stores security policies created and deployed in Security Center. For more information, see Define and Deploy Security Policies. This](https://help.salesforce.com/s/articleView?id=sf.security_center_deploy_policies.htm&type=5&language=en_US)
object is available to Security Center subscribers in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read/write.

##### Fields

```
ApiName
Description
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The API name of the policy.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the policy.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the policy.


-----

```
PolicyData
PolicyIdentifier
PolicyType
SourceRowIdentifier
Status
Version

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The policy details contained in JSON format.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of this policy. Contains a unique virtual key from child to parent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The type of policy. For example, Health Check Baseline.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the policy that is applied to the tenant. This value is specific to the org that owns
this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The status of the policy. For example, the policy is active or inactive.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

**Description**
The version of the policy.

##### Associated Objects

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
