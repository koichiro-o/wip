#### Solution

Represents a detailed description of a customer issue and the resolution of that issue.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
IsDeleted
IsHtml

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Solution is an HTML solution (true) or not (false).


-----

```
IsOutOfDate
IsPublished
IsPublishedInPublicKb
IsReviewed
LastReferencedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Read-only field that indicates whether a solution master has been updated since the translated
version was created (true) or not (false). Note that this field does not appear in the page
layout of master solutions.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Solution has been published (true) or not (false). A solution’s
published state does not affect how it can be used, or whether you can query, update, or
delete it. Label is Public.

Note: Prior to Spring ‘14, the label was Visible in Self-Service Portal.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Solution has been published as a Public Solution (true) or not
(false). Label is Visible in Public Knowledge Base.

This field only applies to solutions, not articles in the public knowledge base.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Solution has been reviewed (true) or not (false). This flag can
only be set indirectly via the `Status` picklist. Each predefined `Status` value implies an
`IsReviewed` value. Label is Reviewed.

**Type**
datetime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
OwnerId
ParentId
RecordTypeId

```

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view (LastReferencedDate),
but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who owns the Solution.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
ID of the master solution, if this is the translation of a master solution.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the RecordType to which the Solution is associated.


-----

```
SolutionLanguage
SolutionName
SolutionNote
SolutionNumber
Status

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
The language that the solution is written in, such as `French` or `Chinese`
```
  (Traditional).

```
**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. If a client application creates a new Solution and a value for this field is unspecified,
a hyphen (-), the default value for this field, is used. Limit: 255 characters. Label is Title.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The details of the Solution record. Limit: 32,000 characters. Label is Solution Details.

Note: If you have HTML Solutions enabled, any HTML tags used in this field are
verified before the object is created or updated. If invalid HTML is entered, an error is
thrown. Any JavaScript used in this field is removed before the object is created or
updated.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An identifying number that is assigned automatically when a solution is created. It can’t be
set directly, and it can’t be modified.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The status of the solution. Directly controls the `IsReviewed` value. To obtain
the status values in the picklist, a client application can query the SolutionStatus.


-----

```
TimesUsed

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times this solution has been used. Label is Num Related Case.


Use this object to manage your organization’s solutions. Client applications can create, update, delete, and query Attachment records
associated with a solution.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SolutionFeed (API version 18.0)**
Feed tracking is available for the object.

**SolutionHistory**

History is available for tracked fields of the object.

SEE ALSO:

CategoryData

CategoryNode
