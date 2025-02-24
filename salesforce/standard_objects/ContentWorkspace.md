#### ContentWorkspace

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rating of the file.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Comment made by the user who rated the file.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who rated the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


Represents a content library. This object is available in versions 17.0 and later.

Note: This object doesn’t apply to personal libraries.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

```
Note: create( ), update( ) and delete( ) on ContentWorkspace are supported in API version 40.0 and later only.


-----

##### Special Access Rules

**•** The Access Libraries user permission allows orgs to make libraries available to users without requiring that they have the legacy
Salesforce CRM Content license. This permission is available for profiles and permission sets on most standard user licenses, and isn’t
available for High Volume Customer Portal, Customer Community, or Chatter Free licenses. Available in API versions 40.0 and later.

**•** Users with the Create Libraries user perm or the Manage Salesforce CRM Content administrator permission can create libraries
(ContentWorkspaces) from the Libraries tab in Salesforce Classic and from the API.

**•** Customer and Partner Portal users can only edit the library document object if they have a Salesforce CRM Content feature license.

**•** Customer and Partner Portal users can query this object if they have the “View Content in Portal” permission. A user can query all
public libraries where they’re members, regardless of library permissions.

**•** Automated process users can’t publish documents to libraries (ContentWorkspaces).

##### Fields

```
DefaultRecordTypeId
Description
DeveloperName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the default content type for the library. Content types are the containers
for custom fields in Salesforce CRM Content.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text description of the content library.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the library in the API. Allows a link to the library to be
packaged when an asset file is added to a package. Although libraries aren’t a
packageable entity, references to libraries with a developer name will be
included in the package when asset files are packaged. These links can then
be restored in the target org.

This name can contain only underscores and alphanumeric characters, and
must be unique in your org. It must begin with a letter, not include spaces, not


-----

```
IsRestrictContentTypes
IsRestrictLinkedContentTypes
Name
NamespacePrefix
RootContentFolderId

```

end with an underscore, and not contain two consecutive underscores. Label
is Unique Name.

This field is available in API version 39.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether content types have been restricted (true) or
not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether linked content types have been restricted (true)
or not (false).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the library.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the library in the API. Allows a link to the library to be
packaged when an asset file is added to a package. Limit: 15 characters. This
field is available in API version 39.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of root folder of the library. This field is available in API version 39.0 and later.


-----

```
ShouldAddCreatorMembership
TagModel
WorkspaceImageId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Group

**Description**
Automatically create a library membership for the user creating the library. Note
this field isn’t meant for query and always returns false in query. This field is
available in API version 40.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of tagging assigned to a library. Valid values are:

**•** `U` — Unrestricted. No restrictions on tagging. Users can enter any tag when
publishing or editing content.

**•** `G` — Guided. Users can enter any tag when publishing or editing content,
but they’re also offered a list of suggested tags.

**•** `R` — Restricted. Users must choose from a list of suggested tags.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a library image. Image files can be assigned to libraries for branding and
easy identification. Library image is visible to all users, even if they aren’t library
members. This field is available in API version 43.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a library image. Image files can be assigned to libraries for branding and
easy identification. Library image is visible to all users, even if they are not library
members. This field is available in API version 43.0 and later.

This is a relationship field.

**Relationship Name**
WorkspaceImage


-----

```
WorkspaceType

##### Usage

```

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Differentiates between different types of libraries. Valid values are:

**•** `R` — Regular library

**•** `B` — Org asset library

This field is available in API version 39.0 and later.


Use this object to query libraries to find out where documents can be published.

If the content type isn’t specified when publishing a new version into a library, it is determined by the `DefaultRecordTypeId` of
the primary library.

As of 40.0, you can create, update, or delete a library via the API.

SEE ALSO:

ContentWorkspaceDoc
