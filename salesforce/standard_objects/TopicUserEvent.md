#### TopicUserEvent

Represents an action (such as comment, post, like, or share) made by a user on a topic. This object is available in API version 42.0 and
later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
Only users with the Modify All Data permission can view and delete these data.

##### Fields

```
ActionEnum
NetworkId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The action taken by a user on a topic. The possible values are:

**•** LIKE

**•** COMMENT

**•** POST

**•** ASSIGN

**•** SHARE

**•** FAVORITE

**•** UNFAVORITE

**•** AT_MENTION

**•** BANG_MENTION

**•** COMMENT_LIKE

**•** USER_ENDORSEMENT

**•** SKILL_PEER_ENDORSEMENT

**•** SKILL_SELF_ENDORSEMENT

**•** BEST_ANSWER

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
 TopicId
UserId

##### Usage

```

**Description**
ID of the Experience Cloud site where the action was performed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Identifier of the topic.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique Salesforce user ID.


Use the TopicUserEvent object to delete topic-related activities by Experience Cloud site users who would like all their topic-related
activities to be removed from a site.
