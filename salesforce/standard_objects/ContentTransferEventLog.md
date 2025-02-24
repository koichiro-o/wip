#### ContentTransferEventLog

ContentTransferEventLog stores information about content transfer events, such as downloads, uploads, and previews. This information
includes events performed on files and attachments to records. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), query()

```

-----

##### Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
DocumentIdentifier
FilePreviewType
FileSize
FileType
OperationType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the document that’s being shared.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the file preview.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of rendition being added (bytes).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the file version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation that’s being performed.


-----

```
RequestIdentifier
Timestamp
UserIdentifier
VersionIdentifier

```

**Possible Values**

**•** `meta_deploy`

**•** `meta_list`

**•** `meta_retrieve`

**•** `meta_synchronous_create`

**•** `meta_synchronous_read`

**•** `meta_synchronous_upsert`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID.`

For example: `3nWgxWbDKWWDIk0FKfF5DV.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943YAS`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the content version.


-----
