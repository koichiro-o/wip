#### Snippet

Represents a snippet, which is a container for rich text that can be reused across Account Engagement emails and email templates. This
object is available in API version 47.0 and later.

##### Supported Calls
```
create(),delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Snippets are available in Account Engagement business units with the Sales, CRM, or Service permission set license.

##### Fields

```
Description
DeveloperName
LastReferencedDate
LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the snippet. Limited to 32 KB.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. This field value is unique to your org and is required for a Snippet to be resolved
in marketing content. Label is API Name.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
Type
Value

##### Associated Objects

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the snippet.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of content a snippet includes. Allowable values are: Date, Image, Link, Text. This
field is for organizational purposes.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body content of a snippet. This field can contain plain or rich text. The value of a snippet
is resolved when a marketing email is sent. The field does not support emojis, HTML, or image
files.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SnippetFeed**

Feed tracking is available for the object.
