#### DataKitDeployEvent

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the name of the data service record matched to the Salesforce record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Indicates the ID of a user to whom purchase credits are assigned.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the number of purchase credits assigned to a user.


Represents a data kit deployment event that notifies subscribers of the status of the data kit component deployment. This object is
available in API version 61.0 or later.

##### Supported Calls
```
create(), describeSObjects()

```

-----

##### Special Access Rules

Users that have access to Data Cloud.

##### Fields

**Field**
```
DataKitName
DataspaceName
DeployStartTime
ErrorDetails
EventCreationDate

```

**Type**
string

**Properties**
Create, Nillable

**Description**
Name of the data kit from which a component is deployed.

**Type**
string

**Properties**
Create, Nillable

**Description**
Name of the data space into which a component is deployed.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time the deployment starts.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
Explanation of the error.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time the data kit deploy creation event was created.


-----

```
EventPublishDate
EventUuid
IsDataKitDeployStatusSuccess
JobIdentifier
ReplayId
TemplateName

```

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time of the data kit deploy publish event.

**Type**
string

**Properties**
Nillable

**Description**
The unique ID of the event.

**Type**
string

**Properties**
Create, Nillable

**Description**
Status of the data kit component deployment. Possible values are:

**•** `Active`

**•** `Failure`

**Type**
string

**Properties**
Create, Nillable

**Description**
Data kit component deployment job identifier.

**Type**
string

**Properties**
Nillable

**Description**
The ID of the data kit deploy event replay.

**Type**
string

**Properties**
Create, Nillable


-----

**Description**
The template name from which the data kit deploy event is created.
