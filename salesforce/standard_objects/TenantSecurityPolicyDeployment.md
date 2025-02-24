#### TenantSecurityPolicyDeployment

[Stores the status of deployments of a Security Center policy on a tenant. For more information, see Define and Deploy Security Policies.](https://help.salesforce.com/s/articleView?id=sf.security_center_deploy_policies.htm&type=5&language=en_US)
This object is available to Security Center subscribers in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read/write.

##### Fields

```
DeploymentDate

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update


-----

```
DeploymentStatus
Description
Name
PolicyIdentifier
StatusDate
Tenant

```

**Description**
The date the deployment was triggered.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The status of the deployment. For example, Not Deployed, Processing, Deployed, or Failed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the deployment status.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the deployment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the TenantSecurityPolicy entity.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date that the status of the deployment was provided.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

**Description**
The ID of the tenant for which the policy was deployed.

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityPolicyDeploymentChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityPolicyDeploymentFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityPolicyDeploymentHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityPolicyDeploymentOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityPolicyDeploymentShare on page 66**
Sharing is available for the object.
