#### ProfileSkill

Represents a profile skill, which describes a user’s professional knowledge. This is a global record for the organization, and users are
associated through the ProfileSkillUser object.

Note: For information about Live Agent skills, see the Skill topic.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Description
LastReferencedDate
LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the profile skill.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp indicating when the current user last viewed a record related to
this profile skill. Available in API version 29.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId
UserCount

##### Usage

```

**Description**
The timestamp indicating when the current user last viewed this profile skill.
Available in API version 29.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the profile skill.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the profile skill.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of users with the profile skill.


Use the ProfileSkill object to look up the attributes of a skill that can be assigned to a user. This is a global object and is not owned by
any specific user.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


-----

**ProfileSkillFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillHistory**

History is available for tracked fields of the object.

**ProfileSkillOwnerSharingRule**

Sharing rules are available for the object.

**ProfileSkillShare**

Sharing is available for the object.
