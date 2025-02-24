#### DataKitDeploymentLog

Represents the log details of a data kit component deployment. This object is available in API version 61.0 or later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
undelete(), update(), upsert()

 Special Access Rules

```
Users that have access to Data Cloud.

##### Fields

```
BundleName
ComponentName
ComponentTemplateId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data stream bundle if a data stream is deployed from a data kit.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the component that’s deployed from a data kit.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data kit template from which the component is deployed. This field is a polymorphic
relationship field.


-----

```
ComponentType
DataKitName
DataSpaceName
DeployJob
DeploymentError

```

**Relationship Name**
ComponentTemplate

**Refers To**
DataSourceBundle

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the component for which the deployment is tracked in the log details.

Possible values are:

**•** `MktCalculatedInsight`

**•** `MktDataLakeObject`

**•** `MktDataModelObject`

**•** `MktDataStream`

**•** `MktDataTransform`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data kit being deployed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data space the components are deployed to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The deployment job ID.

**Type**
textarea


-----

```
DeploymentStatus
FlowInterviewIdentifier
LastReferencedDate
LastViewedDate
Name

```

**Properties**
Create, Nillable, Update

**Description**
Contains the error details if the data kit deployment fails.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Deployment status of the data kit components.

Possible values are:

**•** `Failed`

**•** `Started`

**•** `Successful`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of the flow interview if the deployment was triggered using a flow.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed the deployment log file.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this deployment log.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


-----

```
OwnerId
PublisherOrgComponentId
SubscriberOrgComponentId

```

**Description**
The name of the deployment log.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user that owns the deployment.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the component in the publisher org.

This field is a polymorphic relationship field.

**Relationship Name**
PublisherOrgComponent

**Refers To**
MktCalculatedInsight, MktDataTransform

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the component in the subscriber org in which the components of a data kit are
deployed.

This field is a polymorphic relationship field.

**Relationship Name**
SubscriberOrgComponent

**Refers To**
DataGraph, DataStream, ExtDataShare, MktCalculatedInsight, MktDataTransform


-----

```
TemplateVersion

##### Usage

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of the template from which the deployment was done.


Use the DataKitDeploymentLog object to track the deployment of a data kit component.
