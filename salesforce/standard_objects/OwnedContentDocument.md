#### OwnedContentDocument

Represents a file owned by a user. This object is available in version 30.0 and later.

##### Supported Calls
```
describeSObjects()

 Fields

```
```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the document.


-----

```
ContentSize
ContentUrl
ExternalDataSourceName
ExternalDataSourceType

```

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Size of the document in bytes.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL for links and Google Docs. This field is set only for links and Google Docs,
and is one of the fields that determine the `FileType.`

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the external data source in which the document is stored. This field is
set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of external data source in which the document is stored. This field is set
only for external documents that are connected to Salesforce.

This field is available in API version 35.0 and later.


-----

```
FileExtension
FileType
OwnerId
Title

```

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

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the owner of the document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

Title of the document.


-----
