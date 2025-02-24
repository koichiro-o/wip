#### ContentNote

Represents a note created with the enhanced note taking tool, released in Winter ‘16. This object is available in API version 32.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), search(), update()

 Special Access Rules

```
**•** Notes must be enabled.

##### Fields

```
Content
ContentModifiedDate

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
The content or body of the note, which can include properly formatted HTML or plain text.
When a document is uploaded or downloaded via the API, it must be base64 encoded (for
upload) or decoded (for download). Any special characters within plain text in the Content
field must be escaped. You can escape special characters by calling
```
  content.escapeHtml4(). If the input contains unsafe HTML characters or new lines,

```
we automatically strip them out before saving the content.

**Type**
dateTime


-----

```
ContentSize
FileExtension
FileType
IsReadOnly
LastViewedDate

```

**Properties**
Filter, Nillable, Sort

**Description**
Date the document was modified. ContentModifiedDate updates when, for example, the
document is renamed or a new document version is uploaded.

This field is available in API version 48.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Size of the note in bytes.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
File extension of the note.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of file for the note. All notes have a file type of `SNOTE.`

**Type**
boolean

**Properties**
Defaulted on create, Group, Sort

**Description**
Indicates whether the note is read only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date the note was last viewed. This field is available in API version 35.0 and later.


-----

```
LatestContentId
LatestPublishedVersionId
OwnerId
SharingPrivacy

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup to the note's ContentBody. This field is available in API version 52.0 and later.

This is a relationship field.

**Relationship Name**
LatestContent

**Relationship Type**
Lookup

**Refers To**
ContentBody

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the ContentVersion for the latest published version of the note.

**Type**
reference

**Properties**
Create (for users assigned the Set Audit Fields Upon Creation permission), Defaulted on
create, Filter, Group, Sort, Update (for users assigned the Set Audit Fields Upon Creation
permission)

**Description**
ID of the owner of the note.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only administrators and file owners with Collaborator
access to the file can modify this field. Default is Visible to Anyone With Record
```
  Access. When set to Private on Records, the file is private on records but can

```
be shared selectively with others.

This field is available in API versions 41.0 and later.


-----

```
TextPreview
Title

##### Usage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A preview of the note’s content. This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**
Title of the note.



**•** Use ContentNote to create, query, retrieve, search, edit, and update notes.

**•** ContentNote is built on ContentVersion, and so it has many of the same usages.

**•** Not all fields can be set for notes. Only the `Content` and `Title` fields can be updated.

**•** The maximum file size you can upload via SOAP API is 50 MB. When a document is uploaded or downloaded via the API, it’s converted
to base64. This conversion increases the document size by approximately 37%. Account for the base64 conversion increase so that
the file you plan to upload is less than 50 MB after conversion.

**•** You can convert old Note records to Lightning Experience, so users can view and edit notes from the Notes & Attachments related
list in Lightning Experience. Users can edit their converted notes, which are accessible from the Notes related list and Notes tab.
Copy old Note records to newly created ContentNote records. Users assigned the Set Audit Fields Upon Creation permission can set
the owner, created date, and last modified date on ContentNote records.

**•** SOQL and SOSL queries on the ContentNote return only the most recent version of the note.

**•** To relate a note to a record, use ContentDocumentLink. Review the LinkedEntityID field in ContentDocumentLink
for a list of objects that notes can relate to.

For example, the following Apex code creates a note and escapes any special characters so they’re converted to their HTML equivalents.

Note: Apex code doesn’t need to be encoded to base64 before it’s uploaded and downloaded.
```
ContentNote cn = new ContentNote();
cn.Title = 'test1';
String body = 'Hello World. Before insert/update, escape special characters such as ", ',
 &, and other standard escape characters.';
cn.Content = Blob.valueOf(body.escapeHTML4());
insert(cn);

```
In this example, the following code creates a note using text that is already formatted as HTML, so it doesn’t need to be escaped.


-----
