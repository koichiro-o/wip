#### ContentWorkspacePermission

Represents a library permission. This object is available in API version 40.0 and later.

A library permission is a group of privileges assigned to each content library member. It determines which tasks a member can perform
in a particular library. The same user can have a different library permission in each of his or her libraries.

Note: Library permissions do not apply to personal libraries. All library users can save files in their personal libraries.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(),update(), upsert()

 Special Access Rules

```
The ability to create permissions requires either the Manage Salesforce CRM Content admin perm or the Manage Content Permissions
user perm.

##### Fields

```
Description

```

**Type**
textarea


-----

```
Name
PermissionsAddComment
PermissionsAddContent
PermissionsAddContentOBO
PermissionsArchiveContent

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**
Name of the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to post comments to any content in the library and view all comments
in the library. Users can edit or delete their own comments.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to publish new content to the library, upload new content versions, or
restore archived (deleted) content. Content authors can also change any tags associated
with their content and archive or delete their own content.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to choose an author when publishing content in the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to archive and restore any content in the library.


-----

```
PermissionsChatterSharing
PermissionsDeleteContent
PermissionsDeliverContent
PermissionsFeatureContent
PermissionsManageWorkspace

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to make content from this library accessible outside of the library, sharing
with a record or in Chatter. From a record or from Chatter, select a file from the library and
attach it to a record or a post.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to delete any content in the library. Authors can undelete their own
content from the Recycle Bin.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to share content outside the org via a content delivery or public link.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to identify any content in the library as “featured.”

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to perform any action in the library. This privilege is required to edit a
library’s name and description, add or remove library members, or delete a library. Manage
Library is a super permission which provides all other permission options listed except Deliver
Content. Creating a library requires the Manage Salesforce CRM Content app permission or
Create Libraries system permission.


-----

```
PermissionsModifyComments
PermissionsOrganizeFileAndFolder
PermissionsTagContent
PermissionsViewComments
Type

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to edit or delete comments made to any content in the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to create, rename, and delete folders in libraries.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to add tags when publishing content or editing content details in the
library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to view comments.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides the type of access a user has to a library. Valid values are:

**•** Library Administrator

**•** Author

**•** Viewer

**•** Custom


-----
