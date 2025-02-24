#### ContentVersion

Represents a specific version of a document in Salesforce CRM Content or Salesforce Files. This object is available in versions 17.0 and
later for Salesforce CRM Content documents. This object is available in versions 20.0 and later for Salesforce Files.

The maximum number of versions that can be published in a 24-hour period is 200,000.

Note: Depending on how files are shared, queries on ContentDocument and ContentVersion without specifying an ID don’t
return all files a user has access to. For example, if a user only has access to a file because they have access to a record that the file
is shared with, the file won't be returned in a query such as "SELECT Id FROM ContentDocument."

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), query(), retrieve(), search(), update(), upsert()

 Special Access Rules

```
**•** All users with a content feature license can create versions in their personal library. Customer and Partner Portal users must also
supply the NetworkId of the Experience Cloud site in the request.

**•** By default, users (including users with the “View All Data” permission) can only query files they have access to, including:

**–** Salesforce Files in their personal library and in libraries they're a member of, regardless of library permissions (API version 17.0
and later).

**–** Salesforce Files they own, shared directly with them, posted on their profile, or posted on groups they can see (API version 21.0
and later).

Enable the Query All Files permission to let your View All Data users bypass the restrictions on querying files.

**–** Query All Files returns all files, including files in non-member libraries and files in unlisted groups.

**–** Users can’t edit, upload new versions, or delete files they don’t have access to.

**–** View All Data permission is required to enable Query All Files.

**•** All users can update versions in their personal library.

**•** The owner of a version or document can update the document if they’re a member of the library, regardless of library permissions.

**•** To update a Salesforce CRM Content document, the user must be a member of the library with one of these library privileges enabled:

**–** Add Content

**–** Add Content On Behalf of Others

**–** Manage Library

**•** Customer and Partner Portal users must have the View Content in Portal permission to query content in libraries where they have
access.

**•** Customer and Partner Portal users can only publish, version, or edit documents if they have a Salesforce CRM Content feature license.

**•** `FileType` is defined by either ContentUrl for links or PathOnClient for documents, but not both.


-----

**•** In API version 34.0 and later, any file can be shared with libraries, whether the file originated in Chatter or in Salesforce CRM Content.

**•** [In API version 39.0 and later, custom Apex download handlers can be created that can control access to documents. See the Apex](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_dev_guide.htm)
[Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_dev_guide.htm)

##### Fields

```
Checksum
ContentBodyId
ContentDocumentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
MD5 checksum for the file.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Allows inserting a file version independently of the file blob being uploaded. This field is
available for query and insert only. It can only point to a ContentBody record. This field is
available in API version 40.0 and later.

This is a relationship field.

**Relationship Name**
ContentBody

**Relationship Type**
Lookup

**Refers To**
ContentBody

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup


-----

```
ContentLocation
ContentModifiedById
ContentModifiedDate
ContentSize

```

**Refers To**
ContentDocument

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Origin of the document. Valid values are:

**•** **S—Document is located within Salesforce. Label is Salesforce.**

**•** **E—Document is located outside of Salesforce. Label is External.**

**•** **L—Document is located on a social network and accessed via Social Customer Service.**
Label is Social Customer Service.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user who modified the document.

This is a relationship field.

**Relationship Name**
ContentModifiedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

Date the document was modified.

`ContentModifiedDate` updates when, for example, the document is renamed or a
new document version is uploaded. When uploading the first version of a document,
`ContentModifiedDate` can be set to the current time or any time in the past.

**Type**
int


-----

```
ContentUrl
Description
Division
ExternalDataSourceId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Size of the document in bytes. Always zero for links.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URL for links. This is only set for links. One of the fields that determines the FileType. The
character limit in API versions 33.0 and later is 1,300. The character limit in API versions 32.0
and earlier was 255.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the content version.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the org has the Division permission
enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the external document referenced in the ExternalDataSource object.

This is a relationship field.

**Relationship Name**
ExternalDataSource

**Relationship Type**
Lookup


-----

```
ExternalDocumentInfo1
ExternalDocumentInfo2
FeaturedContentBoost
FeaturedContentDate
FileExtension

```

**Refers To**
ExternalDataSource

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Stores the URL of the file in the external content repository. The integration from the external
source determines the content for this string. After the reference or copy is created, the URL
of the external file is updated when you:

**•** Republish a file reference in Lightning Experience

**•** Open the document

**•** Create a file reference in the Connect REST API with `reuseReference` set to true.

When the file is updated, the shared link is updated to the most current version.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Contains the external file ID. Salesforce determines the content for this string, which is private.
The content can change without notice, depending on the external system. After the file
reference is created, this field isn’t updated, even if the file path changes.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Designates a document as featured.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date the document was featured.

**Type**
string


-----

```
FileType
FirstPublishLocationId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the document.

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Type of content determined by ContentUrl for links or PathOnClient for documents.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

ID of the location where the version was first published. If the version is first published into
a user's personal library or My Files, the field will contain the ID of the user who owns the
personal library or My Files. In Lightning Experience, if the first version is published into a
public library, the field will contain the ID of that library.

Accepts all record IDs supported by ContentDocumentLink (anything a file can be attached
to, like records and groups).

Setting `FirstPublishLocationId allows you to create a file and share it with an`
initial record/group in a single transaction, and have the option to create more links to share
the file with other records or groups later. When a file is created, it’s automatically linked to
the record, and PublishStatus will change to Public from Pending/Personal.

This field is only set the first time a version is published via the API.
`FirstPublishLocationId` can’t be set to another ID when a new content version
is inserted.

Note: Salesforce updates the FirstPublishLocationId updates automatically
when a new OwnerId is added to the ContentVersion. For example, when
you publish a new version with a different OwnerId than the current OwnerId,
the FirstPublishLocationId of all previous versions updates to the previous
```
    OwnerId. The new published version sets the FirstPublishLocationId

```
to the new `OwnerId.`

This is a polymorphic relationship field.

**Relationship Name**
FirstPublishLocation


-----

```
IsAssetEnabled

```

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess, ApiAnomalyEventStore,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CollaborationGroup, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionSchedule, Contact,
ContactEncounter, ContactEncounterParticipant, ContentWorkspace, Contract,
ConversationEntry, CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore,
CreditMemo, CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria, Event,
HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, Image,
IndividualApplication, Invoice, InvoiceLine, Lead, ListEmail, Location, MarketSegment,
MarketSegmentActivation, MemberPlan, MessagingSession, MktCalculatedInsight,
OperatingHours, Opportunity, Order, OrderItem, Organization, OtherComponentTask,
OutgoingEmail, PartyConsent, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report, ReportAnomalyEventStore,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore, Shift,
Shipment, ShipmentItem, Site, SkillRequirement, SocialPost, Solution, Task,
ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall, VolunteerProject,
WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkType, WorkTypeGroup,
WorkTypeGroupMember

**Type**
boolean


-----

```
IsLatest
IsMajorVersion
Language
NegativeRatingCount

```

**Properties**
Create, Group, Defaulted on create

**Description**
Can be specified on insert of ContentVersion to automatically convert a ContentDocument
file into a ContentAsset. This field can be SOQL queried, but it can’t be edited. This field is
available in API version 38.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the latest version of the document (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
`true` if the document is a major version; false if the document is a minor version. Major
versions can’t be replaced.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this document. This field defaults to the org’s default language unless the
multi language setting is enabled.

Specifies the language of the labels returned. The value must be a valid user locale (language
and country), such as `de_DE` or `en_GB. For more information on locales, see the`
```
  Language field on the CategoryNodeLocalization object.

```
**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The number of times different users have given the document a thumbs down.

Rating counts for the latest version are not version-specific. If Version 1 receives 10
thumbs-down votes, and Version 2 receives 2 thumbs-down votes, the


-----

```
NetworkId
Origin
OwnerId

```

`NegativeRatingCount` on Version 2 is 12. However, rating counts are not retroactive
for prior versions. The NegativeRatingCount on Version 1 is 10.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this file originated from. This field is available in API version
26.0 and later, if digital experiences is enabled for your org.

You can add a `NetworkId only when creating a file. You can’t change or add a`
`NetworkId` for an existing file.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The source of the content version. Valid values are:

**•** **C—Content document from the user's personal library. Label is Content. The**
`FirstPublishLocationId` must be the user's ID. If
`FirstPublishLocationId` is left blank, it defaults to the user's ID.

**•** **H—Salesforce file from the user's My Files. Label is Chatter. The**
`FirstPublishLocationId` must be the user's ID. If
`FirstPublishLocationId` is left blank, it defaults to the user's ID. Origin can
only be set to H if Chatter is enabled for your organization.

This field defaults to C. Label is Content Origin.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User


-----

```
PathOnClient
PositiveRatingCount
PublishStatus
RatingCount

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The complete path of the document. One of the fields that determines the FileType.

Note: Specify a complete path including the file extension in order for the document
to be visible in the Preview tab.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The number of times different users have given the document a thumbs up.

Rating counts for the latest version are not version-specific. If Version 1 receives 10 thumbs-up
votes, and Version 2 receives 2 thumbs-up votes, the PositiveRatingCount on Version
2 is 12. However, rating counts are not retroactive for prior versions. The
`PositiveRatingCount` on Version 1 is 10.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates if and how the document is published. Valid values are:

**•** `P—The document is published to a public library and is visible to other users. Label is`
**Public.**

**•** `R—The document is published to a personal library and is not visible to other users.`
Label is Personal Library.

**•** `U—The document is not published because publishing was interrupted. Label is Upload`
**Interrupted.**

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Total number of positive and negative ratings.


-----

```
ReasonForChange
RecordTypeId
SharingOption
SharingPrivacy

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The reason why the document was changed. This field can only be set when inserting a new
version (revising) a document.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type of the version.

Custom fields are restricted in `RecordTypeId. When an administrator creates a custom`
field via the API it must be added to at least one page layout:

**•** If the custom field is added to the page layout associated with the General record type,
the RecordTypeId that corresponds to that record type does not have to be set on
the version record.

**•** If the custom field is added to the page layout associated with a custom record type, the
`RecordTypeId` that corresponds to that record type must be set on the version
record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls whether sharing is frozen for a file. Only administrators and file owners with
Collaborator access to the file can modify this field. Default is Allowed, which means that
new shares are allowed. When set to Restricted, new shares are prevented without
affecting existing shares.

This field is available in API versions 35.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only administrators and file owners with Collaborator access
to the file can modify this field. Default is `Visible to Anyone With Record`


-----

```
TagCsv
TextPreview
Title
VersionData

```
```
  Access. When set to Private on Records, the file is private on records but can be

```
shared selectively with others.

This field is available in API versions 41.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Sort, Update

**Description**
Text used to apply tags to a content version via the API.

**Type**
string

**Properties**
Nillable, Filter,Group, Sort

**Description**
A preview of a document. Available in API version 35.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The title of a document.

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
The content or body of the note, which can include properly formatted HTML or plain text.
When a document is uploaded or downloaded via the API, it should be base64 encoded (for
upload) or decoded (for download). Any special characters within plain text in the Content
field must be escaped. You can escape special characters by calling
```
  content.escapeHtml4().

```
This field can't be set for links.

The maximum file size you can upload via the SOAP API is 50 MB. When a document is
uploaded or downloaded via the API, it is converted to base64 and stored in VersionData.
This conversion increases the document size by approximately 37%. Account for the base64
conversion increase so that the file you plan to upload is less than 50 MB after conversion.


-----

```
VersionDataURL
VersionNumber

##### Usage

```

If a custom Apex download handler is active, this field is accessed from the API, and the
download is not allowed, Salesforce will return a
```
  CONTENT_CUSTOMIZED_DOWNLOAD_EXCEPTION error.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL used to fetch a file from the binary data endpoint. This field is only populated on
direct queries to ContentVersion, and not when queried through a related entity’s foreign
key to ContentVersion.

If available, access preview images of a file by appending a `thumb query parameter to this`
URL. For example:
```
  myContentVersion.VersionDataUrl + '?thumb=THUMB240BY180'

```
Available thumb parameter values are:

**•** `THUMB720BY480` — corresponds to the big-thumbnail preview format

**•** `THUMB240BY180` — corresponds to the thumbnail preview format

**•** `THUMB120BY90` — corresponds to the tiny-thumbnail preview format

[See File Preview in the Connect REST API Developer Guide for additional details about file](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_files_preview_format.htm)
previews.

This field can't be set for links.

This field is available in API versions 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number. The number increments with each version of the document, for example,
1, 2, 3.



**•** Use this object to create, query, retrieve, search, edit, and update a specific version of a Salesforce CRM Content document or Salesforce
file. Use the ContentDocument object to retrieve, query, update, and delete the latest version of a document, but not a content pack,
in a library or a Salesforce file.

**•** Use this object to create, query, retrieve, search, edit, and update a specific version of a Salesforce file. Use the ContentDocument
object to retrieve, query, update, and delete the latest version of a Salesforce file.

**•** To query a file that is shared only with a record, you must specify the content ID of the file.


-----

**•** Not all fields can be set for Salesforce Files.

**•** You can only update a version if it is the latest version and if it is published.

**•** You can't archive versions.

**•** Using API version 32.0 and later, you can update record types on versions.

**•** You can't delete a version via the API.

**•** The maximum file size you can upload via the SOAP API is 50 MB. When a document is uploaded or downloaded via the API, it is
converted to base64 and stored in `VersionData. This conversion increases the document size by approximately 37%. Account`
for the base64 conversion increase so that the file you plan to upload is less than 50 MB after conversion.

**•** To download a document via the API, you must export the VersionData of the document. This does not increase the download
count.

**•** When you upload a document from your local drive using the Data Loader, you must specify the actual path in both VersionData
and PathOnClient. VersionData identifies the location and extracts the format and PathOnClient identifies the type
of document being uploaded.

**•** SOQL queries on the ContentVersion object return all versions of the document. SOSL searches on the ContentVersion object return
only the most recent version of the document.

**•** To query a file that is accessible only through a record share, you must specify the content ID of the file. When SOQL querying the
ContentVersion object, either the `ContentVersionId` or the ContentDocumentId must be compounded by an AND
operator.

For example,
```
  SELECT FileExtension, Title FROM ContentVersion
  WHERE (ContentDocumentId = '<ContentDocumentId>' or Id='<ContentVersionId>') and
  IsLatest=true
  SELECT Id, VersionData, FileExtension, Title FROM ContentVersion
  WHERE ContentDocumentId='<ContentDocumentId>' AND FirstPublishLocationId =
  '<FirstPublishLocationId>'

```
**•** If you query versions in the API, versions with a PublishStatus of `Upload Interrupted` are not returned.

**•** Documents published into a personal library assume the default record type that is set for the user profile of the person publishing
the document (General, if no default is set for the user profile).

Note: An administrator can rename the default (Content Version Layout) page layout.

**•** Contact Manager, Group, Professional, Enterprise, Unlimited, and Performance Edition customers can publish a maximum of 200,000
new versions per 24–hour period. Developer Edition and trial users can publish a maximum of 2,500 new versions per 24–hour
period.

**•** Custom validation rules can prevent an update of documents published into a personal library via the API.

##### Applying Tags to ContentVersion Records

Tags can be applied to ContentVersion records using either Enterprise or Partner API.

To apply tags to a ContentVersion record, set a value in the TagCsv field. For example, setting this field to one,two,three creates
and associates three tags to that version.

**•** The maximum length of the `TagCsv` field is 2,000 characters.

**•** The maximum length of an individual tag is 100 characters.

**•** When tags are applied to a version, the content is indexed automatically and the tags are searchable.


-----

**•** You can't apply tags to a `TagCsv` that is published into a personal library. You can apply tags to a `TagCsv` that's in a shared
library or folder.

**•** You can't apply tags using the ContentDocument object.

**•** You can't change or delete tag names. You can remove tags from a document, but that doesn't delete the tag.

**•** Tags are case insensitive. You can't have two tags with the same name even if they use different uppercase and lowercase letters.
The case of the original tag is always used.

To delete tags from a ContentVersion record, perform a standard API update, and remove any values from the `TagCsv` field that you
want to delete. For example, if the original `TagCsv` is `one,two,three, perform an API update specifying one,three` in the
`TagCsv` field to delete two. To delete all tags from a ContentVersion you perform a standard API update by setting the field to null.

If you create a ContentVersion record and want to revise it via the API, you insert another ContentVersion record but associate it to the
same ContentDocument record as the original. This has an impact on tagging:

**•** If you insert the revision and do not set any value in the TagCsv field, any tags applied to the previous version are automatically
applied to the new version.

**•** If you insert the revision and specify a new `TagCsv` field, no tags transfer over and the tags you specify are applied instead.

When you perform a SOQL query for a ContentVersion record and select the TagCsv field, all the tags associated with that record are
returned. The tags in the string are always ordered alphabetically even if they were inserted in a different order. You can't use the
`TagCsv` field as part of a filter in a SOQL query. You can't query all tags in your organization.

Library tagging rules:

**•** API tagging respects the tagging restrictions that exist on any library that the document is published into. For example, if the library
is in restricted tagging mode and only allows tags `one,three, you can't save a version with a` `TagCsv` of `one,two,three.`

**•** If the library is in guided tagging mode, you can apply tags to the ContentVersion. You can't query the value of guided tags on a
library, but you can query the tagging model of a library.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ContentVersionChangeEvent on page 67 (API version 55.0)**
Change events are available for the object.

**ContentVersionHistory**

History is available for tracked fields of the object.

SEE ALSO:

ContentDocument

ContentVersionHistory
