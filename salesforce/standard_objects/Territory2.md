#### Territory2

```


**•** `Lead`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the supported object.


Represents a sales territory. Available if Sales Territories has been enabled.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or `Archived).`

##### Fields

```
AccountAccessLevel
CaseAccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default account record access levels for users that are assigned
to the territory. Values are:

**•** `Read Only`

**•** `Read/Write`

**•** `Owner`

**Type**
picklist


-----

```
ContactAccessLevel
Description
DeveloperName

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default case record access levels for users that are assigned to
the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents the default contact record access levels for users that are assigned to
the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the territory. The field label in the user interface is Territory
```
  Description.

```
**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Territory Name.`

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is


-----

```
ForecastUserId
Name
OpportunityAccessLevel
ParentTerritory2Id
Territory2ModelId

```

specified, performance slows down while Salesforce generates one for
each record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier of a territory’s forecast manager. To select a
```
  ForecastUserId, select someone in the list of users assigned to the territory.

```
**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the territory. The field label in the user interface is `Territory`
```
  Label.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Represents the default opportunity record access levels for users that are assigned
to the territory. Values are:

**•** `Private`

**•** `Read Only`

**•** `Read/Write`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the territory’s parent territory (if any). If the territory has no parent
territory, this value is `null.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Territory2TypeId
