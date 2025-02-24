#### ContentDistributionView

Represents information about views of a shared document. This read-only object is available in API version 32.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve(), update()

 Special Access Rules

```
**•** Content deliveries must be enabled to query content deliveries.

**•** Users (including users with the “View All Data” permission) can query only the files that they have access to. If the file is managed
by a Content Library, the user must have “Deliver Content” enabled in the library permission definition and be a member of the
library. If the file isn’t managed by a Content Library, the user must have the “Enable Creation of Content Deliveries for Salesforce
Files” permission.

**•** ContentDistributionView can be deleted by an admin.

**•** If the shared document is deleted, the delete cascades to any associated ContentDistributionView. The ContentDistributionView is
still queryable by using the `QueryAll` verb.


-----

**•** Customer Portal users can’t access this object.

**•** Chatter Free users can’t access this object.

##### Fields

**Field Name**
```
DistributionId
IsDownload
IsInternal
ParentViewId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the content delivery that the document is part of.

This is a relationship field.

**Relationship Name**
Distribution

**Relationship Type**
Lookup

**Refers To**
ContentDistribution

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the shared document is downloaded; `false` if the shared document
is viewed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the shared document is viewed by a user in the same organization;
`false` if viewed by an external user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of this instance of accessing the shared document.


-----

##### Usage

Use this read-only object to query information about users who are accessing shared documents.
