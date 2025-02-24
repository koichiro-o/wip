#### AttachedContentNote

This read-only object contains all ContentNote objects associated with an object. This object is available in API version 35.0 and later.

##### Supported Calls
```
describeSObjects()

 Special Access Rules

```
**•** Notes must be enabled.

**•** Chatter must be enabled.

##### Fields

```
ContentDocumentId
ContentSize

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the attached `ContentNote`

**Type**
int


-----

```
FileExtension
FileType
LinkedEntityId
TextPreview
Title

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

Size of the note in bytes.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the attached `ContentNote.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of file for the note. All notes have a file type of `SNOTE.`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

ID of the record the `ContentNote` is attached to.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A preview of the note, up to 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

Title of the note.


-----

##### Usage

Use this object to list all `ContentNote` objects attached to an object.

To retrieve ContentNote objects, issue a describe call on an object, which returns a describe result for each note created or attached.
You can’t directly query this object.
