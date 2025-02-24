#### SOSDeployment

Represents the general settings for deploying SOS video call capability in a native mobile application. This object is available in API
version 34.0 and later.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the


-----

```
Language
MasterLabel
OptionsIsBackwardFacingCameraEnabled
OptionsIsEnabled
OptionsIsVoiceOnlyMode

```

object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the deployment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the deployment.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether customers can use the backwards-facing camera on their
mobile devices to talk to SOS agents.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether the deployment is enabled for customers to request new
SOS video calls.

**Type**
boolean


-----

```
QueueId

##### Usage

```

**Properties**
Create, Filter, Update

**Description**
Determines whether video functionality is disabled for customers, making it so
customers can only talk to SOS agents using only audio.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the queue that’s associated with the SOS deployment.


Use this object to query and manage SOS deployments.
