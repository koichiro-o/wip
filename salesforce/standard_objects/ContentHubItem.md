#### ContentHubItem

```

**Relationship Name**
ChildRecord

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the folder the file is in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder


Represents a file or folder in a Files Connect external data source, such as Microsoft SharePoint or OneDrive for Business. This object is
available in API version 33.0 and later.

##### Special Access Rules

Chatter and Files Connect must be enabled for the organization.

##### Supported Calls
```
describeSObjects(), query(), search()

 Fields

```
```
ContentHubRepositoryId

```

**Type**
reference


-----

```
ContentModifiedDate
ContentSize
Description
ExternalContentUrl
ExternalDocumentUrl

```

**Properties**
Filter, Group, Nillable

**Description**
The ID for the related external data source described by the ContentHubRepository
object.

**Type**
dateTime

**Properties**
Nillable

**Description**
Date the file or folder content last changed.

**Type**
int

**Properties**
Group, Nillable

**Description**
File or folder size.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
Explanation of item in external data source.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL of the document content in the external data source.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL of the detail page in the external data source.


-----

```
ExternalId
FileExtension
FileType
IsFolder
MimeType
Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID for the file or folder in the external data source.

**Type**
string

**Properties**
Group, Nillable

**Description**
File format extension, such as .doc or .pdf

**Type**
string

**Properties**
Group, Nillable

**Description**
Complete file type, such as “Microsoft Word Document.”

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether item is a folder or file.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
MIME type of the content.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the file or folder in the external data source.


-----

```
Owner
ParentId
Title
UpdatedBy

```

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
Username of the content owner in the external data source.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The ID of the parent folder for the record.

This field isn’t returned in queries or searches of the ContentHubItem object. It
supports only WHERE clauses, such as the following:
```
  WHERE ContentHubRepositoryId = <ID of external
  source> and ParentId = <ID of parent folder or
  record>.

```
Or specify WHERE ParentId = <name of root folder> to return
the children of the root folder.

Tip: The ParentId field supports both Salesforce IDs (in the format
“0CHxxx”) and external IDs.

**Type**
string

**Properties**
Group, Nillable

**Description**
The title that appears in the content, which often differs from the `Name` of the
containing file or folder.

**Type**
string

**Properties**
Group, Nillable

**Description**
Username for the person who last updated the file.


-----

##### Usage

The following SOQL query examples show how to retrieve files and folders from a Files Connect external data source. These examples
use placeholders for ID values for the repository ID and folder IDs. Before running these queries, replace the placeholders with valid ID
values for your external data source and folders.

Important: You must filter queries and searches on ContentHubItem with the ContentHubRepositoryId field; for
example, SELECT Id FROM ContentHubItem WHERE ContentHubRepositoryId = <ID of external
```
  data source>.

```
**Example 1: Get the ID and name of the root folder in an external file source.**
```
SELECT Id, Name
FROM ContentHubItem
WHERE ContentHubRepositoryId = '<repository ID>' AND ParentId = NULL

```
**Example 2: List all folders and files under the specified root folder.**
```
SELECT Id, Name
FROM ContentHubItem
WHERE ContentHubRepositoryId = '<repository ID>' AND ParentId = '<root folder ID>'

```
**Example 3: List all external file data sources by querying ContentHubRepository.**
```
SELECT DeveloperName
FROM ContentHubRepository

```
**Example 4: List all files and folders in a given folder and external file source.**
```
SELECT Id, Name
FROM ContentHubItem
WHERE ContentHubRepositoryId = '<repository ID>' AND ParentId = '<parent folder ID>'

```
**Example 5: To return only folders in the result set, add** `IsFolder = true` in the `WHERE` clause to a query that returns files and
folders. For example, the following query lists all folders under the root folder.
```
SELECT Id, Name
FROM ContentHubItem
WHERE ContentHubRepositoryId = '<repository ID>' AND ParentId = '<root folder ID>'
    AND IsFolder = true

```
**Example 6: Retrieve a link that is used to open the specified document in an external source.**
```
SELECT ExternalDocumentUrl
FROM ContentHubItem
WHERE ContentHubRepositoryId = '<repository ID>' AND Id = '<document ID>'

```
**SOSL Example: Retrieve the ID and name of all documents that contain the search string. The result set is limited to the first 10 documents.**


-----
