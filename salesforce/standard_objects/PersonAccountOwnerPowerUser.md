#### PersonAccountOwnerPowerUser

Represents a user who can own more than 50,000 customer or partner portal accounts. Person account owner power users can own a
large number of either customer or partner users. Their role can’t be changed and they must be at the root of the role hierarchy. Person
account owner power user objects can't be created if deferred sharing is turned on for your org. Person account owner power user
objects can be created while deferred sharing is turned off for an org. Deferred sharing can be turned back on after person account
owner power user objects have been created. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Create a PersonAccountOwnerPowerUser object. Enter the user ID of the power user and the type of users that they can own, Customer
`Portal` or `Partner.`

Note: Only users at the highest level of a hierarchy can be added to the PersonAccountOwnerPowerUser object.

##### Fields

```
DeveloperName
Language
MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language that the user’s account is set to. The user is specified using the UserId field.

See Salesforce Help for a full list of languages.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label entered when the person account owner power user is created.


-----

```
PortalType
UserId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of portal user account that the person account owner power user can own.

A possible value is:

**•** `CustomerPortal—Customer Portal`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID associated with the person account owner power user.

This field is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

