#### ReputationPointsRule

```


**•** Swedish: `sv`

**•** Thai: `th The Salesforce user interface is fully translated to Thai, but Help is`
in English.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the reputation level this translated value applies to.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**

The translated text for the reputation level. Label is Translation Text.


Represents the reputation point rules for an Experience Cloud site. Each rule specifies an action that members can earn points from and
the points associated with those actions in a particular site. This object is available in API version 32.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is available only if digital experiences is enabled in your org. Only users with permissions to create or manage an Experience
Cloud site can view the ReputationPointsRule records.

##### Fields

```
ParentId
Points
Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent Experience Cloud site that the point rule applies to.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**

The reputation points associated with the member action this rule is for. The
maximum value this field can contain is 999,999.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The member action associated with this rule, limited to one of these actions:

**•** Write a post (FeedItemWriteAPost)

**•** Write a comment (FeedItemWriteAComment)

**•** Receive a comment (FeedItemReceiveAComment)

**•** Like something (FeedItemLikeSomething)

**•** Receive a like (FeedItemReceiveALike)

**•** Share a post (FeedItemShareAPost)

**•** Someone shares your post (FeedItemSomeoneSharesYourPost)

**•** Mention someone (FeedItemMentionSomeone)

**•** Receive a mention (FeedItemReceiveAMention)


-----

**•** Ask a question (FeedItemPostQuestion)

**•** Answer a question (FeedItemAnswerAQuestion)

**•** Receive an answer (FeedItemReceiveAnAnswer)

**•** Mark an answer as best (FeedItemMarkAnswerAsBest)

**•** Someone marks your answer as best
(FeedItemYourAnswerMarkedBest)

**•** Endorse someone for knowledge on a topic
(EndorseSomeoneForKnowledgeOnATopic)

**•** Someone endorses you for knowledge on a topic
(EndorsedForKnowledgeOnATopic)

**•** Upload a profile picture (ProfilePhotoUpload) This action is available
in API version 45.0 and later.
