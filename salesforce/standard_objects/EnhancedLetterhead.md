#### EnhancedLetterhead

Represents an enhanced letterhead that can be associated with a Lightning email template that doesn’t use the Salesforce Merge
Language (SML). This object is available in API version 46.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), describeLayout(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Description

```

**Type**
string


-----

```
LastReferencedDate
LastViewedDate
LetterheadFooter
LetterheadHeader
Name

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the contents of the header and footer.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this enhanced letterhead was last used.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this enhanced letterhead was last viewed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the enhanced letterhead’s footer.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the enhanced letterhead’s header.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the enhanced letterhead, such as Standard Company Letterhead.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EnhancedLetterheadFeed**

Feed tracking is available for the object.
