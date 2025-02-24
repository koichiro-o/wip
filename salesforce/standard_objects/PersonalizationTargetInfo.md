#### PersonalizationTargetInfo

Represents a target for an audience. This object is available in API version 47.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ContainerId

```

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
DraftRowId
GroupName
PublishStatus
TargetType

```

**Description**
ID of the Experience Cloud site or org that contains the target.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the draft PersonalizationTargetInfo.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Group name of the target. Groups bundle related targets.You can have up to 2,000 groups
and 500 targets per group.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Publish status of the target.

Possible values are:

**•** `Draft`

**•** `Live`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the target.

Possible values are:

**•** `ExperienceVariation`

**•** `NavigationLinkSet`

**•** `Topic`

**•** `CollaborationGroup`

**•** `KnowledgeArticle`


-----

```
TargetValue
