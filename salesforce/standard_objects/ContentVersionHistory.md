#### ContentVersionHistory

Represents the history of a specific version of a document. This object is available in version 17.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

**•** Customer and Partner Portal users must have the “View Content in Portal” permission to query content in libraries where they have
access.

**•** A user can query all versions of a document from their personal library and any version that is part of or shared with a library where
they are a member, regardless of library permissions.

Note: To record an event in `contentVersionViewed, make sure:`

**•** All files are published to a Content Library.

**•** The details page is viewed in Salesforce Classic.

##### Fields

```
ContentVersionId
DataType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the version.

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
Division
Field
NewValue
OldValue

```

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field that was changed. Possible values include:

**•** `contentVersionCreated—A new version is created.`

**•** `contentVersionUpdated—The title, description, or any custom field on the`
version is changed.

**•** `contentVersionDownloaded—A version is downloaded.`

**•** `contentVersionViewed—The version details are viewed.`

**•** `contentVersionRated—The version is rated.`

**•** `contentVersionCommented—The version receives a comment.`

**•** `contentVersionDataReplaced—The new version replaces the previous version,`
which can happen only when the new version is uploaded immediately after the previous
version.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort


-----

**Description**
The latest value of the field before it was changed.

##### Usage

Use this read-only object to query the history of a document version.

SEE ALSO:

ContentVersion
