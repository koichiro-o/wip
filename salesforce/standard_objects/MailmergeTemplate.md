#### MailmergeTemplate

Represents a mail merge template (a Microsoft Word document) used for performing mail merges for your organization.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
**•** All users can view this object, but you need the “Customize Application” permission to modify it.

**•** Customer Portal users can’t access this object.

##### Fields

```
Body
BodyLength

```

**Type**
base64

**Properties**
Create

**Description**
Required. Microsoft Word document to use as a mail merge template. Due
to limitations with Microsoft Word mail merge templates, your client
application can specify the Body field when creating these records, but not
when updating them. Limit: 5 MB.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Length of the Microsoft Word document.


-----

```
Description
Filename
IsDeleted
LastUsedDate
Name
SecurityOptionsAttachmentHasFlash

```

**Type**
string

**Properties**
Create, Filter,Group, Nillable, Sort, Update

**Description**
Required. Text description of this mail merge template. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. File name of the Microsoft Word document that was uploaded as
a mail merge template. Limit: 255 characters in length.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or
not (false). Label is Deleted.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this MailmergeTemplate was last used.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this mail merge template.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
SecurityOptionsAttachmentHasXSSThreat
SecurityOptionsAttachmentScannedforFlash
SecurityOptionsAttachmentScannedForXSS

##### Usage

```

**Description**
Required. True if Flash Injection was detected in the attachment.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if a cross site scripting threat was detected in the attachment.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if the attachment has been scanned for Flash Injection.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if the attachment has been scanned for a cross site scripting
threat.


Use this object to manage mail merge templates for your organization.

SEE ALSO:

Overview of Salesforce Objects and Fields
