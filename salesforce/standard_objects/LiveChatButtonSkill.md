#### LiveChatButtonSkill

Represents all the skills available to a LiveChatButton except the one currently assigned. To retrieve the skill currently assigned, query
LiveChatButton. This object is available in API version 25.0 and later.

##### Supported Calls
```
create(), delete(), update(), query()

 Fields

```
```
ButtonID
SkillID

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record ID of the button.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the skill.


-----

##### Usage

Use this object to assign a specific skill to a specific button for multi-skill routing. For example:
```
String myButtonId = "button_Id";
String myButtonDevName = "button_DeveloperName";
List<String> skillIds = new List<String>();
//Get one skill ID from button
for(LiveChatButton lcb : [SELECT SkillId FROM LiveChatButton WHERE DeveloperName =:
myButtonDevName]) {
   skillIds.add(lcb.SkillId);
}
//Get remaining skills from LiveChatButtonSkill join object
for(LiveChatButtonSkill lcbs : [SELECT SkillID FROM LiveChatButtonSkill WHERE ButtonId =:
myButtonId]) {
   skillIds.add(lcbs.SkillId);
}
//Retrieve all skills into a single list
List<Skill> skills = [SELECT Id, DeveloperName FROM Skill WHERE Id IN :SkillIds];
