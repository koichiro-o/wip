#### Skill

Represents a category or group of Chat users or service resources in Field Service or Workforce Engagement. This object is available in
API version 24.0 and later.

Note: For information about WDC skills on a user's profile, see the ProfileSkill topic.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
Description
DeveloperName
Language

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the skill.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
LastViewedDate
MasterLabel
TypeId

##### Usage

```

**Description**

The language of the skill.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the skill.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the skill.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The skill type associated with the skill.

This field is a relationship field.

This field is available in API version 58.0 and later.

**Relationship Name**
Type

**Refers To**
SkillType


**Chat**
Use this object to assign Chat users to groups based on their abilities. The skills associated with a LiveChatButton determine which
agents receive chat requests that come in through that button.

**Field Service**
Use this object to track certifications and areas of expertise in your workforce. After you create a skill, you can:

**•** Assign it to a service resource via the Skills related list on the resource’s detail page. When you assign a skill to a service resource,
you can specify their skill level and the duration of the skill.


-----

**•** Add it as a required skill via the Skill Requirements related list on any work type, work order, or work order line item. When you
add a required skill to a work record, you can specify the skill level.

**Workforce Engagement**
Use this object to specify areas of expertise in your workforce. After you create a skill, you can:

**•** Assign it to a service resource via the Skills related list on the resource’s detail page.

**•** Add it as a required skill via the Skill Requirements related list on a job profile.
