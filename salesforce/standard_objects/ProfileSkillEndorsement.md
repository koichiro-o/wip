#### ProfileSkillEndorsement

Represents a detail relationship of ProfileSkillUser. An endorsement of a profile skill shows approval and support of another user’s publicly
declared skill.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Name
ProfileSkillUserId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the profile skill being endorsed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ProfileSkillUser record that is being endorsed.

This is a relationship field.

**Relationship Name**
ProfileSkillUser

**Relationship Type**
Lookup

**Refers To**
ProfileSkillUser


-----

```
UserId

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID of the person giving the endorsement.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


Use the ProfileSkillEndorsement object to query about a single endorsement given to a user about a specific skill. Users can’t endorse
themselves, they can only be endorsed by others unless they are administrators with the “Modify All Data” permission.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ProfileSkillEndorsementChangeEvent (API version 62.0)**
Change events are available for the object.

**ProfileSkillEndorsementFeed (API version 34.0)**
Feed tracking is available for the object.

**ProfileSkillEndorsementHistory**

History is available for tracked fields of the object.
