#### ContentDistribution

Represents information about sharing a document externally. This object is available in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
**•** Content deliveries must be enabled to query content deliveries.

**•** Users (including users with the “View All Data” permission) can query only the files that they have access to. If the file is managed
by a Content Library, the user must have “Deliver Content” enabled in the library permission definition and be a member of the
library. If the file isn’t managed by a Content Library, the user must have the “Enable Creation of Content Deliveries for Salesforce
Files” permission.

**•** Users can query the `DistributionPublicUrl` and Password fields only if they are the file owner, if the file is shared with
them, or if the `RelatedRecordId specifies a record that the users can access.`

**•** If the shared document is deleted, the delete cascades to any associated ContentDistribution. The ContentDistribution is still queryable
by using the QueryAll verb.

**•** If the shared document is archived, the only fields that users can edit are ExpiryDate and PreferencesExpires.

**•** Customer Portal users can’t access this object.

**•** Chatter Free users can’t access this object.


-----

##### Fields

**Field Name**
```
ContentDocumentId
ContentDownloadUrl
ContentVersionId
DistributionPublicUrl
ExpiryDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the shared document.

**Type**
string

**Properties**
Sort, Nillable

**Description**
The link for downloading the file. This field is available in API version 40.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shared document version.

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

**Type**
string

**Properties**
Nillable, Sort

**Description**
URL of the link to the shared document.

**Type**
dateTime


-----

```
FirstViewDate
LastViewDate
Name
OwnerId

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when the shared document becomes inaccessible.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the shared document is first viewed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the shared document was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content delivery.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the shared document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User


-----

```
PdfDownloadUrl
Password
PreferencesAllowOriginalDownload
PreferencesAllowPDFDownload
PreferencesAllowViewInBrowser

```

**Type**
string

**Properties**
Sort, Nillable

**Description**
The link for downloading the file as a PDF. This field is available in API version
40.0 and later.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
A password that allows access to a shared document.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the shared document can be downloaded as the file type that it`
was uploaded as.

When `false, download availability depends on whether a preview of the file`
exists. If a preview exists, the file can’t be downloaded. If a preview doesn’t exist,
the file can still be downloaded.

If the shared document is a link, it can’t be downloaded.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the shared document can be downloaded as a PDF if the original`
file type is PDF or if a PDF preview has been generated.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, a preview of the shared document can be viewed in a Web browser.


-----

```
PreferencesExpires
PreferencesLinkLatestVersion
PreferencesNotifyOnVisit
PreferencesNotifyRndtnComplete
PreferencesPasswordRequired

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, access to the shared document expires on the date that’s specified
by `ExpiryDate.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, users see the most recent version of a shared document. When`
```
  false, users see the version of the document that’s shared, even if it isn’t the

```
most recent version.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the owner of the shared document is emailed the first time that`
someone views or downloads the shared document.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the owner of the shared document is emailed when renditions of`
the shared document that can be previewed in a Web browser are generated.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, a password, specified by` `Password, is required to access the`
shared document.


-----

```
RelatedRecordId
ViewCount

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record, such as an Account, Campaign, or Case, that the shared document
is related to.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Campaign, Case, Contact, EmailMessage, Lead, ListEmail, Opportunity

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times that the shared document has been viewed.


Use this object to create, update, delete, or query information about a document shared externally via a link or via Salesforce CRM Content
delivery.

The ContentDistribution object supports triggers before and after these operations: insert, update, delete. It supports triggers after
undelete.

Example: The VP of Marketing wants file authors to specify whether their files can be shared with external people using content
delivery. He also wants some files to have a password. You can add a custom field `DeliveryPolicy` on the ContentVersion
object. Make the custom field a picklist with the values, `Allowed,` `Blocked, and` `Password required. Add the field to`
the ContentVersion layout so that the user can set the delivery policy per file. Then, add an insert trigger for the ContentDistribution
object to enforce the rules based on the delivery policy set in the file.

Note: The `ContentVersionId` for ContentDistribution must be unique.

This trigger for the ContentDistribution object enforces the delivery policy rules for each file:


-----

The trigger calls this helper class:
```
   public class DeliveryPolicyHelper {
     public static String getContentVersionId(ContentDistribution cd) {
        if (cd.ContentVersionId != null) {
          return cd.ContentVersionId;
        } else {
          String versionId = [select LatestPublishedVersionId from ContentDocument
   where Id = :cd.ContentDocumentId].get(0).LatestPublishedVersionId;
          return versionId;
        }
     }
     public static boolean requirePassword(ContentDistribution cd) {
        return cd.PreferencesPasswordRequired;
     }
   }

```
Important: Apex has a per organization limit of 10 concurrent requests that last longer than 5 seconds. A trigger that uploads
files can easily hit this limit.
