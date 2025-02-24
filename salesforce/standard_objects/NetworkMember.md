#### NetworkMember

Represents a member of an Experience Cloud site. Members can be either users in your company or external users with portal profiles.
This object is available in API version 26.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), update()

 Special Access Rules

```
This object is available only when your org has digital experiences enabled.

##### Fields

```
DefaultGroupNotificationFrequency
DigestFrequency

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The default frequency for sending the member’s group
email notifications when the member joins groups in the Experience
Cloud site. The valid values are:

**•** `P—Email on every post`

**•** `D—Daily digests`

**•** `W—Weekly digests`

**•** `N—Never`

The default value is `W. In sites, the` `Email on every post`
option is disabled once more than 10,000 members choose this setting
for the group. All members who had this option selected are
automatically switched to `Daily digests. However, this field is`
not currently enabled. These values are reserved for future use.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The frequency for sending the member’s personal email
digest for the Experience Cloud site. The valid values are:

**•** `D—Daily`


-----

```
LastChatterActivityDate
MemberId
NetworkId
PreferencesDisableAllFeedsEmail
PreferencesDisableBestAnswerEmail

```


**•** `W—Weekly`

**•** `N—Never`

The default value is `D. However, daily and weekly personal digests`
aren’t currently available in sites. These values are reserved for future
use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last time the member posted or commented in the Experience
Cloud site.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of a person who is a member of an Experience Cloud site.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Experience Cloud site that the member is part of.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member can automatically receive email for`
updates in the Experience Cloud site, based on the types of feed emails
and digests the member has enabled.

**Type**
boolean

**Properties**
Filter, Update


-----

```
PreferencesDisableBookmarkEmail
PreferencesDisableChangeCommentEmail
PreferencesDisableDirectMessageEmail
PreferencesDisableEndorsementEmail
PreferencesDisableFollowersEmail

```

**Description**
When `false, the member automatically receives email when`
someone selects their answer to a post as best. Available in API 46.0
and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone comments on a feed item after the member has bookmarked
it.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone comments on a change the member has made, such as an
update to their profile.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone sends them a direct message in the Experience Cloud site.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone endorses them for a topic.

**Type**
boolean


-----

```
PreferencesDisableItemFlaggedEmail
PreferencesDisableLaterCommentEmail
PreferencesDisableLikeEmail
PreferencesDisableMarketingCloudEmail

```

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone in the Experience Cloud site starts following the member.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the user automatically receives email every time a`
member flags a post or comment. This setting only applies for
community moderators (with the Moderate Experiences Feeds
permission) and group owners or managers.

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone comments on a feed item after the member has commented
on the feed item.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone comments on a feed item after the member has liked the
feed item.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When false, the member automatically receives marketing emails
sent by Journey Builder. Available in API version 41.0 and later.


-----

```
PreferencesDisableMentionsPostEmail
PreferencesDisableMessageEmail
PreferencesDisableProfilePostEmail
PreferencesDisableSharePostEmail
PreferencesDisCommentAfterLikeEmail
PreferencesDisMentionsCommentEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
the member is mentioned in posts.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
the member is sent a Chatter message.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone posts to the member’s profile.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
the member’s post is shared.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone comments on a post the member has liked.

**Type**
boolean


-----

```
PreferencesDisProfPostCommentEmail
ReputationPoints

##### Usage

```

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
the member is mentioned in comments.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false, the member automatically receives email every time`
someone comments on posts on the member’s profile.

**Type**
double

**Properties**
Filter, Sort, Update

**Description**
The number of reputation points the user has accumulated by
performing actions in the Experience Cloud site.


Use this object to query members of a certain Experience Cloud site and to update their email notification settings. If you have Modify
All Data, View All Data, or Create and Set Up Experiences, you can view all members of any Experience Cloud site, regardless of your own
membership. If you have Modify All Data or Create and Set Up Experiences, you can also update any member’s email settings. Users
without these permissions can update their own email settings and can see members of the Experience Cloud sites that they’re also
members of.

Tip: You can directly update reputation points for a member via the Salesforce API. You can also use Apex triggers to send custom
notifications based on changes to reputation points.
