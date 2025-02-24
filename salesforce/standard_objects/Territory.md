#### Territory

Represents a flexible collection of accounts and users where the users have at least read access to the accounts, regardless of who owns
the accounts. Available if Sales Territories has been enabled.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

```

-----

##### Special Access Rules

Standard and partner users can access this object. Users assigned to the Manage Territories permission set can edit this object.

##### Fields

```
AccountAccessLevel
CaseAccessLevel
ContactAccessLevel
Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Account access level granted to users assigned to this territory.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Case access level granted to users assigned to this territory.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
A value that represents the type of access granted to the target Group, UserRole, or
User for any associated contacts. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

Note: When DefaultContactAccess is set to “Controlled by Parent,”
you can’t create or update this field.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the territory that is 1,000 characters or less.


-----

```
DeveloperName
ForecastUserId
MayForecastManagerShare
Name
OpportunityAccessLevel

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to Territory Name in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Forecast Manager, who is the user to whom forecasts from this territory’s
child territories roll up.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the forecast manager can manually share their own forecast.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A name for the territory. Limit is 80 characters. Corresponds to Label on the user
interface.

**Type**
picklist


-----

```
ParentTerritoryID
RestrictOppTransfer

##### Usage

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Opportunity access level granted to users assigned to this territory.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Territory immediately above this territory in the territory hierarchy. Label is Parent
**Territory ID.**

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the opportunities associated with this territory are kept within the
bounds of this territory and this territory’s children when account assignment rules
are run (true), or if opportunities associated with this territory can be assigned to
other nodes of the territory hierarchy when account assignment rules are run (false).
Label is Confine Opportunity Assignment.


Use the Territory object to query your organization’s territory hierarchy. Use it to obtain valid territory IDs when querying or modifying
records associated with territories.

SEE ALSO:

AccountTerritoryAssignmentRule

AccountTerritoryAssignmentRuleItem

UserTerritory
