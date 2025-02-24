#### ProfileSkillUser

Represents a detail relationship of User. The object connects profile skills with users.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
EndorsementCount
Name
ProfileSkillId
UserId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of endorsements.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the skill user.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ProfileSkill.

This is a relationship field.

**Relationship Name**
ProfileSkill

**Relationship Type**
Lookup

**Refers To**
ProfileSkill

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the user. This field can’t be changed once it is created.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


-----

**Refers To**
User

##### Usage

Use this object to assign specific skills to specific users. ProfileSkillUser appears on the Overview tab on the Chatter profile page. Users
can only create a skill mapping for themselves, they can’t create skill mappings for others unless they are administrators with the “Modify
All Data” permission. Additionally, users can only edit this object if they are the context user and are not editing the `UserId` field.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProfileSkillUserFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillUserHistory**

History is available for tracked fields of the object.
