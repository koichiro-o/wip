#### ContentDocument

Represents a document that has been uploaded to a library in Salesforce CRM Content or Salesforce Files. This object is available in
versions 17.0 and later for Salesforce CRM Content. This object is available in API version 21.0 and later for Salesforce Files.

The maximum number of documents that can be published is 30,000,000. Archived files count toward this limit and toward storage
usage limits.

**•** Contact Manager, Group, Professional, Enterprise, Unlimited, and Performance Edition customers can publish a maximum of 200,000
new versions per 24-hour period.

**•** Developer Edition and trial users can publish a maximum of 2,500 new versions per 24-hour period.

##### Supported Calls
```
delete(), describeLayout()describeSObjects(), query(), retrieve(), search(), undelete(),
update()

 Special Access Rules

```
**•** By default, users (including users with the View All Data permission) can only query files they have access to, including:

**–** Salesforce Files in their personal library and in libraries they're a member of, regardless of library permissions (API version 17.0
and later).

**–** Salesforce Files they own, shared directly with them, posted on their profile, or posted on groups they can see (API version 21.0
and later).

Enable the Query All Files permission to let your View All Data users bypass the restrictions on querying files.

**–** Query All Files returns all files, including files in non-member libraries and files in unlisted groups.

**–** Users can’t edit, upload new versions, or delete files they don’t have access to.

**–** View All Data permission is required to enable Query All Files.

**•** For API version 62.0 and later, enable the Query Non Vetoed Files permission in Data Cloud orgs to let your users view and SOQL
query all public and non vetoed files in the org.

**•** Customer and Partner Portal users must have the View Content in Portal permission to query content in libraries where they have
access.

**•** A Salesforce CRM Content document can be deleted if any of the following are true:

**–** The document is published into a personal library or is in the user's upload queue.

**–** The document is published into a public library, the user trying to delete the document is the file owner, and is a member of
that library.

**–** The document is published into a public library and the user trying to delete the document is not the owner but has the Manage
Library or Delete Content library permission enabled.

For API version 25.0 and later, you can change ownership of Salesforce Files and Salesforce CRM Content documents.

**•** A user can change ownership of a Salesforce CRM Content document or Salesforce file if any of the following are true:


-----

**–** The user is the current owner.

**–** The user has the Modify All Data permission enabled.

**–** For a file in a Content Library, the user either has the Manage Salesforce CRM Content permission enabled, or has the Manage
Library permission enabled for the library containing the document.

Note: When the owner of a ContentDocument is changed, ContentDocumentLink may be triggered. This action deletes the
ContentDocumentLink to the old owner and inserts one to the new owner.

Note:

**–** The user who is becoming the owner of the document must be a visible user who is active, but the original owner can be
inactive.

**–** A document's owner can be changed to a user who doesn’t have access to the library that contains the document. Library
administrators must give the new owner membership to the library.

##### Fields

```
ArchivedById
ArchivedDate
ContentAssetId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the document.

This field is available in API version 24.0 and later.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the document was archived.

This field is available in API version 24.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
If the ContentDocument is an asset file, this field points to the asset. For most entities, the
value of this field is `null.`

This field is available in API version 38.0 and later.

This is a relationship field.


-----

```
ContentModifiedDate
ContentSize
Description
Division

```

**Relationship Name**
ContentAsset

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date the document was modified.
```
  ContentModifiedDate updates when, for example, the document is renamed or a

```
new document version is uploaded. When you’re uploading the first version of a document,
`ContentModifiedDate` can be set to the current time or anytime in the past.

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes.

This field is available in API version 31.0 and later.

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**

A description of the document.

This field is available in API version 31.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
FileExtension
FileType
IsArchived
IsInternalOnly
LastReferencedDate

```

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the document.

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of document, determined by the file extension.

This field is available in API version 31.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the document has been archived (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that a file is for internal use only. When `true, prevents users with the Query Non`
Vetoed Files permission from viewing and performing SOQL query on public and non vetoed
files in a Data Cloud org. Default value is `false.`

This field is available in API version 62.0 and later.

**Type**
datetime


-----

```
LastViewedDate
LatestPublishedVersionId
OwnerId

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the latest document version (ContentVersion).

This is a relationship field.

**Relationship Name**
LatestPublishedVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

**Type**
reference

**Properties**
Filter, Group, Sort, Update

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
ParentId
PublishStatus
SharingOption
SharingPrivacy

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the library that owns the document. Created automatically when inserting a
ContentVersion via the API for the first time.

This field is available in API version 24.0 and later when Salesforce CRM Content is enabled.

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
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Controls whether sharing is frozen for a file. Only administrators and file owners with
Collaborator access to the file can modify this field. Default is Allowed, which means that
new shares are allowed. When set to Restricted, new shares are prevented without
affecting existing shares.

This field is available in API versions 35.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only administrators and file owners with Collaborator
access to the file can modify this field.

Valid values are:


-----

```
Title

##### Usage

```


**•** `N—Default. Label is Visible to Anyone With Record Access`

**•** `P—The file is private on records but can be shared selectively with others. Label is`
**Private on Records.**

This field is available in API versions 41.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**

The title of a document.



**•** Use this object to retrieve, query, update, and delete the latest version of a document in a library or a Salesforce file. Use the
ContentVersion object to create, query, retrieve, search, edit, and update a specific version of a Salesforce CRM Content document
or Salesforce file.

**•** A document record is a container for multiple version records. You create a version to add a document to the system. The new
version contains the actual file data which allows the document to have multiple versions. The version stores the body of the uploaded
document.

**•** To create a document, create version via the ContentVersion object without setting the `ContentDocumentId. This process`
automatically creates a parent document record. When adding a new version of the document, you must specify an existing
`ContentDocumentId` which initiates the revision process for the document. When the latest version is published, the title,
owner, and publish status fields are updated in the document.

**•** You can’t add new versions of archived documents.

**•** When you delete a document, all versions of that document are deleted, including ratings, comments, and tags.

**•** A ContentDocument insert trigger executes when a file (ContentDocument) is added to the file library.

**•** A ContentDocument delete trigger executes when a file is deleted, but the cascaded ContentDocumentLink delete does not trigger
ContentDocumentLink triggers.

**•** The `query()` call doesn’t return archived documents. The `queryAll()` call returns archived documents.

**•** To query a file that is accessible only through a record share, you must specify the content ID of the file. When SOQL querying the
ContentDocument object, the `ContentDocumentId` must be compounded by an AND operator.

For example,
```
  SELECT Id, Title FROM ContentDocument
  WHERE (Id = '<ContentDocumentId>' and Title LIKE '%<title>%'
  SELECT Id, Title, MyCustomField_c FROM ContentDocument
  WHERE (Id IN ('<Id1>', '<Id2>')) AND (Title LIKE '%<title1>%' OR (Title LIKE '%<title2>%')

```
**•** If you query versions in the API, versions with a PublishStatus of `Upload Interrupted` are not returned.

**•** Assign topics to ContentDocument using `TopicAssignment` in API version 37.0 or later.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, associated objects are available in the same API version as this object.

**ContentDocumentChangeEvent on page 67 (API version 55.0)**
Change events are available for the object.

**ContentDocumentFeed (API version 20.0)**
Feed tracking is available for the object.

**ContentDocumentHistory**

History is available for tracked fields of the object.

SEE ALSO:

ContentDocumentHistory

ContentVersion
