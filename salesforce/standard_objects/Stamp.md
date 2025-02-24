#### Stamp

Represents a User Specialty. This object is available in API version 39.0 and later.

Create User Specialty labels. Specialties can be any term you want, up to 50 characters, including spaces and underscores.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
Description
MasterLabel
ParentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Use this field to describe what the user specialty means and how it applies to a
user. You have a 255 character maximum including spaces and underscores.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The User Specialty label that appears under the user’s profile picture. You can
create any label you want as long as it’s within the 50 character maximum,
including spaces and underscores.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
The id of the org or network.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Organization
