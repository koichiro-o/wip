#### AccountUserTerritory2View

Represents the view of the Users in Assigned Territories related list in Lightning Experience for Sales Territories. Available in API version
42.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Standard and partner users can access this object.


-----

##### Fields

**Field Name**
```
AccountId
RoleInTerritory2
Territory2Id
UserId

##### Usage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for the account associated with the Users in Assigned Territories
related list.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of each user in the Users in Assigned Territories related list.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for each territory in the Users in Assigned Territories related list.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier for each user in the Users in Assigned Territories related list.


Use this object to show the users who are assigned to the territories assigned to an account.

A filter criterion with one `AccountId` is required when you execute a SOQL query on this object.
