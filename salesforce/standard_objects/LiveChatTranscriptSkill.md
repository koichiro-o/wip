#### LiveChatTranscriptSkill

Represents a join between LiveChatTranscript and Skill. This object is available in API version 25.0 and later.

##### Supported Calls
```
create(), delete(), getDeleted(), getUpdated(), query(), retrieve(), undelete(), update()

 Fields

```
```
Name
SkillId
TranscriptId

##### Usage

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the transcript.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the skill.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the transcript.


Use this object to assign a specific skill to a specific transcript for multi-skill routing.


-----
