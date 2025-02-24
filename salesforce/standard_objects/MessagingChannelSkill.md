#### MessagingChannelSkill

Junction object that represents an association between MessagingChannel and Skill. This object is available in API version 45.0 and later.

For example, when we want to use Omni-Channel skills-based routing in Live message, this object maintains the mapping between the
messaging channel and the skill.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
MessagingChannelId
SkillId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the MessagingChannel on page 3215.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Skill on page 4744.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

