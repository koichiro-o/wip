#### UserLocationAssignment

Represents the assignment between a location and a user. This object is available in API version 57.0 and later.

##### Supported Calls:

create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(), undelete(), update(),
upsert()

##### Special Access Rules:

This object is only available in Salesforce Order Management orgs.

##### Fields

```
UserLocationAssignmentNumber

```

**Type**
text


-----

```
AssignedTo
Location
Username
IsActive

##### Usage:

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated number for the association

**Type**
foreignkey (user)

**Properties**
Create, Filter, Group, Sort, Update

**Description**
User being associated with the location

**Type**
foreignkey (location)

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Location being associated to the User

**Type**
string (derived)

**Properties**
Filter, Sort

**Description**
Username of the User that is associated to the Location

**Type**
boolean

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Whether the location is active or not


The UserLocationAssignment object associates a user to specified work locations. To assign a user to multiple locations, create Multiple
UserLocationAssignment objects. Use the isActive field to indicates the user's current active location.


-----
