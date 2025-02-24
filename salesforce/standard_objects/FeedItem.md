#### FeedItem

FeedItem represents an entry in the feed, such as changes in a record feed, including text posts, link posts, and content posts. This object
is available in API version 21.0 and later. This object replaces FeedPost.

##### Supported Calls
```
create(), delete(), describeSObjects(), describeLayout(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
**•** You can delete all feed items you created. To delete feed items you didn’t create, you must have one of these permissions:

**–** Modify All Data

**–** Modify All Records on the feed item’s parent object, for example, Account for a feed item on an account feed

**–** Moderate Chatter

Note: Users with the Moderate Chatter permission can delete only the feed items and comments that they can see.


-----

Only users with this permission can delete items in unlisted groups.

**•** Guest users can’t insert system field values for Chatter feeds. Even if you try to assign the CanInsertFeedSystemFields permission to
a Guest User, the permission isn’t granted.

Only users with the Modify All Data permission can delete a feed item of `Type TrackedChange.`

If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s author
and creation date. The fields can’t be updated after migration.

##### Fields

```
BestCommentId
Body
CommentCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the comment marked as best answer on a question post.

This is a relationship field.

**Relationship Name**
BestComment

**Relationship Type**
Lookup

**Refers To**
FeedComment

**Type**
textarea

**Properties**
Create, Nillable, Sort, Update

**Description**
The body of the feed item. Required when `Type` is `TextPost` or
`AdvancedTextPost. Optional when` `Type` is `ContentPost` or
```
  LinkPost.

```
Although a value for `Body` isn’t required for the `ContentPost` type, an
attachment is required. If an attachment isn’t present, the type changes to
`TextPost` or `AdvancedTextPost, depending on the API version.`
`TextPost and` `AdvancedTextPost` do require a value for `Body.`

Tip: See the IsRichText field for a list of HTML tags supported in the
body of rich text posts.

**Type**
int


-----

```
ConnectionId
ContentData
ContentDescription

```

**Properties**
Filter, Group, Sort

**Description**
The number of comments associated with this feed item.

Tip: In a feed that supports pre-moderation, CommentCount isn’t updated
until a comment is published. For example, say that you comment on a post
that already has one published comment and your comment triggers
moderation. Now there are two comments on the post, but the count says
there's only one. In a moderated feed, comments aren’t counted until approved
by an admin or someone with Can Approve Feed Post and Comment or Modify
All Data.

Feed moderation has implications on how you retrieve feed comments. In a
moderated feed, rather than retrieving comments by looping through
```
  CommentCount, go through pagination until the end of comments is

```
returned.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When a PartnerNetworkConnection modifies a record that is tracked, the
`CreatedBy` field contains the ID of the system administrator. The
`ConnectionId` contains the ID of the PartnerNetworkConnection. Available
if Salesforce to Salesforce is enabled for your org.

**Type**
base64

**Properties**
Create, Nillable

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is required if `Type` is `ContentPost.`
Encoded file data in any format, and can’t be 0 bytes. Setting this field
automatically sets `Type` to `ContentPost.`

**Type**
textarea

**Properties**
Create, Nillable, Sort


-----

```
ContentFileName
ContentSize
ContentType
FeedPostId

```

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. The description of the file specified in
```
  ContentData.

```
**Type**
string

**Properties**
Create, Group, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. The name of the file uploaded to the feed. Setting
`ContentFileName` automatically sets `Type` to `ContentPost.`

**Type**
int

**Properties**
Group, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is the size of the file (in bytes) uploaded
to the feed. This field is read-only and is automatically determined during insert.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
This field was removed in API version 35.0, and is available in earlier versions for
backward compatibility only. This field is the MIME type of the file uploaded to
the feed. This field is read-only and is automatically determined during insert.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field was removed in API version 22.0, and is available in earlier versions for
backward compatibility only.

ID of the associated FeedPost. A FeedPost represents the following types of
changes in a feed item: changes to tracked fields, text posts, link posts, and
content posts.


-----

```
HasContent
HasFeedEntity
HasLink
HasVerifiedComment
InsertedById

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has content.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has a feed entity, for example, a post, as an
attachment. Available in API version 39 and later when sharing a feed entity in
Lightning Experience.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item has a link attached.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Determines whether a question has an answer that is marked as Company Verified.

This field is available in API version 41.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who added this item to the feed. For example, if an application
migrates posts and comments from another application into a feed, the
`InsertedBy` value is set to the ID of the context user.

This is a polymorphic relationship field.


-----

```
IsClosed
IsDeleted
IsRichText

```

**Relationship Name**
InsertedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
As of API version 43, a read-only field that indicates whether the feed item is
open or closed to new actions. A value of true places restrictions on the actions
a user can take on a feed item and its comments. For more information, see the
Usage section.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Standard system field. Indicates whether the record has been moved to the
Recycle Bin (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the feed item `Body contains rich text. If you post a rich text`
feed comment using SOAP API, set IsRichText to true and escape HTML
entities from the body. Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:

**•** `<p>`

Tip: Though the `<br>` tag isn’t supported, you can use
`<p>&nbsp;</p>` to create lines.

**•** `<a>`

**•** `<b>`

**•** `<code>`

**•** `<i>`


-----

```
LastEditById
LastEditDate
LikeCount
LinkUrl

```


**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files
in Salesforce similar to this example: `<img`
```
   src="sfdc://069B0000000omjh"></img>

```
Note: In API version 35.0 and later, the system replaces special characters
in rich text with escaped HTML. In API version 34.0 and prior, all rich text
appears as a plain-text representation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the user who last edited the feed item.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date the feed item was last edited.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of likes associated with this feed item.

**Type**
url

**Properties**
Create, Nillable, Sort

**Description**
The URL of a `LinkPost.`


-----

```
NetworkScope
ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether this feed item is available in the default Experience Cloud site,
a specific Experience Cloud site, or all sites. This field is available in API version
26.0 and later, if digital experiences is enabled for your org.

`NetworkScope` can have the following values:

**•** `NetworkId—The ID of the Experience Cloud site in which the FeedItem`
is available. If left empty, the feed item is only available in the default
Experience Cloud site.

**•** `AllNetworks—The feed item is available in all Experience Cloud sites.`

Note the following exceptions for `NetworkScope:`

**•** Only feed items with a Group or User parent can set a `NetworkId` or a
null value for `NetworkScope.`

**•** For feed items with a record parent, users can set `NetworkScope` only
to `AllNetworks.`

**•** You can’t filter a feed item on the `NetworkScope` field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the object type to which the feed item is related. For example, set this field
to a `UserId` to post to someone’s profile feed, or an `AccountId` to post to
a specific account.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant, CareBarrierType,
CareDeterminant, CareDeterminantType, CareDiagnosis, CareInterventionType,
CareMetricTarget, CareObservation, CareObservationComponent,


-----

```
RelatedRecordId

```

CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareProviderSearchableField, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CollaborationGroup,
CommSubscription, CommSubscriptionChannelType, CommSubscriptionConsent,
CommSubscriptionTiming, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContentDocument, Contract, CoverageBenefit,
CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EngagementChannelType,
EnhancedLetterhead, EnrollmentEligibilityCriteria, Event, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, Identifier, Image, IndividualApplication, Invoice,
InvoiceLine, Lead, Location, MarketSegment, MarketSegmentActivation,
MemberPlan, MessagingSession, MktCalculatedInsight, OperatingHours,
Opportunity, Order, OrderItem, OtherComponentTask, PartyConsent,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, ProviderSearchSyncLog, PurchaserPlan, PurchaserPlanAssn,
ReceivedDocument, Report, ReportAnomalyEventStore, ResourceAbsence,
ResourcePreference, ReturnOrder, ReturnOrderLineItem, ServiceAppointment,
ServiceResource, ServiceResourceSkill, ServiceTerritory, ServiceTerritoryMember,
ServiceTerritoryWorkType, SessionHijackingEventStore, Shift, Shipment,
ShipmentItem, Site, SkillRequirement, SocialPost, Solution, Task,
ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall,
VolunteerProject, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem,
WorkType, WorkTypeGroup, WorkTypeGroupMember

**Type**
reference

**Properties**
Create, Group, Nillable, Sort

**Description**
ID of the ContentVersion record associated with a `ContentPost. For WDC`
thanks posts, it’s the ID of the WorkThanks object associated with a
```
  RypplePost. This field is typically null for all posts except ContentPost

```
and `RypplePost.`

For example, set this field to an existing ContentVersion ID and post it to a feed
with `Type` set to `ContentPost.`


-----

```
Revision
Status
Title

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The revision number of the feed item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed item is published and visible to all who can access
the feed. This field is available in API version 37.0 and later.

Possible values are:

**•** `Published—The item’s visible to all with access to the feed.`

**•** `PendingReview—The item’s visible to its author and users who see the`
item and have View All Data or Can Approve Feed Post and Comment
permission. Some people can delete and edit the item. They include the
author and users who see the item and have Can Approve Feed Post and
Comment or Modify All Data permission.

Note: These permissions don’t apply when you retrieve feed items
using SOQL. To filter out Pending Review feed items you must add an
explicit clause.

Some actions are blocked when a feed item is pending review:

**–** Comment

**–** Like and unlike

**–** Bookmark

**–** Share

**•** `Isolated—The item is visible only to admins. After an item is isolated,`
the author no longer has view or edit access. The admin user can edit, view,
and delete isolated feed items.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the feed item. When the `Type` is `LinkPost, the` `LinkUrl` is
the URL and this field is the link name. The Title field can be updated on posts
of `Type QuestionPost.`


-----

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of feed item. Except for `ContentPost,` `LinkPost,`
```
  QuestionPost, and TextPost, all the FeedItem types listed here are

```
system-generated. In most situations, we recommend that you don't create
system-generated fields using Apex or our APIs. One exception is during Chatter
data migrations, which can require admins to migrate system-generated post
types.

**•** `ActivityEvent—indirectly generated event when a user or the API`
adds a Task associated with a feed-enabled parent record (excluding email
tasks on cases). Also occurs when a user or the API adds or updates a Task or
Event associated with a case record (excluding email and call logging).

For a recurring Task with CaseFeed disabled, one event is generated for the
series only. For a recurring Task with CaseFeed enabled, events are generated
for the series and each occurrence.

**•** `AdvancedTextPost—created when a user posts a group announcement`
and, in Lightning Experience as of API version 39.0 and later, when a user
shares a post.

**•** `AnnouncementPost—Not used.`

**•** `ApprovalPost—generated when a user submits an approval.`

**•** `BasicTemplateFeedItem—Not used.`

**•** `CanvasPost—a post made by a canvas app posted on a feed.`

**•** `CollaborationGroupCreated—generated when a user creates a`
public group.

**•** `CollaborationGroupUnarchived—Not used.`

**•** `ContentPost—a post with an attached file.`

**•** `CreatedRecordEvent—generated when a user creates a record from`
the publisher.

**•** `DashboardComponentAlert—generated when a dashboard metric`
or gauge exceeds a user-defined threshold.

**•** `DashboardComponentSnapshot—created when a user posts a`
dashboard snapshot on a feed.

**•** `LinkPost—a post with an attached URL.`

**•** `PollPost—a poll posted on a feed.`

**•** `ProfileSkillPost—generated when a skill is added to a user’s Chatter`
profile.

**•** `QuestionPost—generated when a user posts a question.`

**•** `ReplyPost—generated when Chatter Answers posts a reply.`


-----

```
Visibility

```


**•** `RypplePost—generated when a user creates a Thanks badge in WDC.`

**•** `TextPost—a direct text entry on a feed.`

**•** `TrackedChange—a change or group of changes to a tracked field.`

**•** `UserStatus—automatically generated when a user adds a post.`
Deprecated.

The following values appear in the `Type` picklist for all feed objects but apply
only to CaseFeed:

**•** `AttachArticleEvent—generated event when a user attaches an`
article to a case.

**•** `CallLogPost—generated event when a user logs a call for a case through`
the user interface. CTI calls also generate this event.

**•** `CaseCommentPost—generated event when a user adds a case comment`
for a case object.

**•** `ChangeStatusPost—generated event when a user changes the status`
of a case.

**•** `ChatTranscriptPost—generated event when Chat transcript is saved`
to a case.

**•** `EmailMessageEvent—generated event when an email related to a`
case object is sent or received.

**•** `FacebookPost—generated when a Facebook post is created from a`
case. Deprecated.

**•** `MilestoneEvent—generated when a case milestone is completed or`
reaches violation status.

**•** `SocialPost—generated when a social post is created from a case.`

Note: If you set Type to ContentPost, also specify ContentData
and `ContentFileName.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether this feed item is available to all users or internal users only. This
field is available in API version 26.0 and later, if digital experiences is enabled for
your org.

`Visibility` can have the following values:

**•** `AllUsers—The feed item is available to all users who have permission`
to see the feed item.

**•** `InternalUsers—The feed item is available to internal users only.`

Note the following exceptions for `Visibility:`


-----

**•** For record posts, Visibility is set to InternalUsers for all internal
users by default.

**•** External users can set `Visibility` only to `AllUsers.`

**•** `Visibility` can be updated on record posts.

**•** The `Update` property is supported only for feed items posted on records.

##### Usage

**•** When a feed item’s `IsClosed` field is set to true, some actions are blocked and others are blocked to most users. This table sets
out the actions that are blocked when a feed item is closed.

|Action|Availability on a Closed Conversation|
|---|---|
|Add a comment|Blocked|
|Answer a question|Blocked|
|Vote on a poll|Blocked|
|Edit a feed item or its comments or answers|Blocked to author; available to admins, moderators, and people with the Close Conversation Threads in Feeds permission Editing is blocked specifically for the feed item title, feed item body, and feed content body fields.|
|Edit a topic|Available|
|Delete a feed item or its comments or answers|Blocked to author; available to admins, moderators, and people with the Close Conversation Threads in Feeds permission|
|Publish a pending review comment (moderation)|Available to admins and moderators|
|Like or unlike; upvote or downvote|Available|
|Select or remove a best answer|Blocked to author; available to admins, moderators, and people with the Close Conversation Threads in Feeds permission|
|Company verify; remove verification|Available only to people with the Verify Answers to Chatter Questions permission|
|Flag|Available|
|Share|Available|
|Bookmark|Available|
|Mute and unmute|Available|
|Escalate to case|Available only to people permitted to escalate a feed item to a case|


-----

**•** This Apex example shows how to add a feed item with an attachment to a lead using API version 36.0 and later. First, post a feed
item.
```
  //create and insert post
  FeedItem post = new FeedItem();
  post.Body = 'HelloThere';
  post.ParentId = 'ID_OF_LEAD_ENTITY';
  post.Title = 'FileName';
  insert post;

```
Then insert the attachment.
```
  //create and associate a content attachment to the post
  FeedAttachment feedAttachment = new FeedAttachment();
  feedAttachment.FeedEntityId = post.Id;
  feedAttachment.RecordId = 'ID_OF_CONTENT_VERSION';
  feedAttachment.Title = 'FileName';
  feedAttachment.Type = 'CONTENT';
  insert feedAttachment;

```
**•** If you’re using API version 23.0 or later and have View All Data permission, you can directly query for a FeedItem. The following
example returns the 20 most recent feed items.
```
  SELECT ID, CreatedDate, CreatedById, CreatedBy.FirstName, CreatedBy.LastName, ParentId,
   Parent.Name, Body,
   (SELECT ID, FieldName, OldValue, NewValue FROM FeedTrackedChanges ORDER BY ID DESC)
  FROM FeedItem
  WHERE CreatedDate > LAST_MONTH
  ORDER BY CreatedDate DESC

```
**•** If you’re using an earlier API version than version 23.0, query FeedItem objects through a feed (such as AccountFeed or
OpportunityFeed). The following example returns all feed items for a given account, ordered by date descending:
```
  SELECT Id, Type, FeedItem.Body
  FROM AccountFeed
  WHERE ParentId = AccountId ORDER BY CreatedDate DESC

```
Note: Provide the `ParentId` for API version 22.0 and earlier.

**•** A feed item of type UserStatus is automatically created when a user adds a post to update the status. You can’t explicitly create
a feed item of type `UserStatus.`

**•** The FeedItem object doesn’t support aggregate functions in queries.

**•** If the context user has the Insert System Field Values for Chatter Feeds user permission, the `create` field property is available on
`CreatedBy` and `CreatedDate` system fields. During migration, the context user can set these fields to the original post’s
author and creation date. The fields can’t be updated after migration.

**•** The size limit for an attachment on a feed is 2 GB.

**•** You can’t use the content fields to update or delete the content.

**•** You can’t filter or update the content fields.

**•** Deleting a feed item via the API also deletes the associated content. Likewise, undeleting a feed item restores associated content.

Note: This object is hard deleted. It isn’t sent to the Recycle Bin.


-----

**•** After uploading to a feed, it’s possible for an attachment or document to be deleted, marked private, or hidden by sharing rules. In
this case, all content fields in a FeedItem object appear as `null` in a SOQL query.

**•** You can’t explicitly create or delete a FeedTrackedChange record.

**•** Imagine that you insert a feed item or feed comment of `Type ContentPost` on a User or Group to create a file. Then the
`NetworkScope` field value of the feed item is passed to the file.

**•** If you use an Apex trigger to modify the Body of a FeedItem object, all mentions hyperlinks are converted to plain text. The mentioned
users don’t get email notifications.

**•** If you insert rich text into the feed item body, make sure that the case of the opening and closing HTML tags matches. For example,
`<b>This is bold text</B>` generates an error.

**•** To check file sharing with Apex triggers, write triggers on ContentDocumentLink instead of FeedItem. For an example, see
ContentDocumentLink.

**•** In API version 36.0 and later, use FeedAttachment to attach one or more content items to a feed item. As a result of support for
multiple attachments through FeedAttachment, all fields related to content attachments have been removed. These fields are:
```
  ContentData, ContentDescription, ContentFileName, ContentSize, and ContentType.

```
**•** For all API versions of FeedItem, you can’t query a FeedItem object using the `System Modstamp` filter.

**•** When you use the FeedItem object to create a record-triggered flow, and the flow tries to update a field on the parent record, the
field may not update in the UI until the page is refreshed.
