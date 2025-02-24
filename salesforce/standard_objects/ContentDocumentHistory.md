#### ContentDocumentHistory

Represents the history of a document. This object is available in versions 17.0 and later.

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

##### Fields

```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument


-----

```
DataType
Division
Field
NewValue

```

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

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
Filter, Group, Sort, Restricted picklist

**Description**
The name of the field that was changed. Possible values include:

**•** `contentDocPublished—The document is published into a library.`

**•** `contentDocUnpublished—The document is archived or removed from a library,`
either directly or when the owning library is changed.

**•** `contentDocRepublished—The document is removed from the archive.`

**•** `contentDocFeatured—The document is featured.`

**•** `contentDocSubscribed—The document is subscribed to.`

**•** `contentDocUnsubscribed—The document is no longer subscribed to.`

**Type**
anyType

**Properties**
Nillable, Sort


-----

```
OldValue

##### Usage

```

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The latest value of the field before it was changed.


Use this read-only object to query the history of a document.

SEE ALSO:

ContentDocument
