#### CallCoachConfigModifyEvent

Represents a Conversation Insights configuration change. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), describeSObjects()

```

-----

##### Fields

**Field**
```
ChangeType
OrganizationId
ProviderIdChange
ReplayId

```

**Type**
picklist

**Properties**
Create, Restricted picklist

**Description**
The type of configuration change made.

Possible values are:

**•** `FEATURE`

**•** `OTHER`

**•** `PROVIDER`

**•** `USER`

**Type**
string

**Properties**
Create

**Description**
The ID of the Salesforce org with the related change.

**Type**
string

**Properties**
Create, Nillable

**Description**
The ID of the provider related to the change.

**Type**
string

**Properties**
Nillable

**Description**
The ID of the related event as it is positioned in the event stream.

