#### NetworkActivityAudit

Represents an audit trail of moderation actions in Experience Cloud sites. This object is available in API version 30.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is available only when your org has digital experiences enabled.

##### Fields

```
Action

```

**Type**
picklist


-----

```
Description
EntityCreatedById

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The moderation action a member performed on a post, comment, or file in an
Experience Cloud site.

Values are:

**•** Flagged as Inappropriate—A member flagged a post, comment, or file as
inappropriate.

**•** Flagged as Spam - A member flagged a post, comment, or file as spam.

**•** Unflagged—A member removed the flag from a post, comment, or file.

**•** RemovedFlags—A moderator removed all flags from a post, comment, or
file.

**•** DeletedFlaggedItem—A moderator deleted a flagged post, comment,
message, or file.

**•** DeletedPendingReviewItem—A moderator deleted a post or comment with
pending status.

**•** ModerationRuleFlag—A moderation rule flagged member-generated content.

**•** ModerationRuleBlock—A moderation rule blocked member-generated
content.

**•** ModerationRuleReplace—A moderation rule replaced member-generated
content.

**•** ModerationRuleReview—A moderation rule sent member-generated content
to be reviewed and approved by a moderator.

**•** ModerationRuleFreeze—A moderation rule froze a member because they
created content too frequently within a specific time frame.

**•** ModerationRuleNotify—A moderation rule notified moderators because a
member created content too frequently within a specific time frame.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Notes entered by the user.

If the entity being tracked is a file, records the version number of the file when
it was flagged.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
EntityId
EntityType
Name
NetworkId
ParentEntityId
ParentEntityType

```

**Description**
ID of the user that created the entity being tracked.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the entity that is being tracked. The following entities are tracked:
ChatterMessage, ContentDocument, ContentVersion, FeedComment, and
FeedItem.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key prefix of the entity being tracked.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the item being tracked.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Experience Cloud site where the moderation action was performed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent of the entity on which an action was performed.

**Type**
picklist


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key prefix of the parent of the entity being audited.

##### Usage

Use this object to view an audit trail of moderation activity for your Experience Cloud sites. You must have the Modify All Data permission
to access this object.

Users with Moderate Experiences Feeds, Moderate Experiences Files, or View All Data can view the audit trail using reports in the Salesforce
user interface.
