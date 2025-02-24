#### Idea

```

**Description**

The `TabDefinition` ID.

This is a relationship field.

**Relationship Name**
TabDefinition

**Relationship Type**
Lookup

**Refers To**
TabDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The icon’s theme.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The fully qualified URL for this icon.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The tab icon’s width in pixels. If the icon content type is an SVG type, height and
width values are not used.


Represents an idea on which users are allowed to comment and vote, for example, a suggestion for an enhancement to an existing
product or process. This object is available in API version 12 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```
Note: For other standard objects, the describeLayout() call returns the recordTypeMappings section that contains
the layout ID and picklist values for each record type. However, the `recordTypeMappings` section and the fields it includes
are not available for the Idea object.

When performing a SOSL search on Idea objects, IdeaComment objects are also searched.

##### Fields

```
AttachmentBody
AttachmentContentType
AttachmentLength
AttachmentName

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**

File data for the attachment. This field is available in API version 28.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Type of the attachment. This field is available in API version 28.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Size of the attachment in bytes. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Name of the attachment. This field is available in API version 28.0 and later.


-----

```
Body
Categories
Category
CommunityId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the Idea.

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable multi-select picklist used to organize Ideas into logical groupings.

Note: This field is only available if your organization has the `Categories` field
enabled. This field is enabled by default in organizations created after API version 14
was released. If the `Categories` field is enabled, API versions 13 and earlier do
not have access to either the `Categories` or `Category` fields.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable picklist of values used to organize Ideas into logical groupings.

Note: This field is not available if your organization has the multi-select
`Categories` field enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The zone ID associated with the idea. Once you create an idea, you can’t change the zone
ID associated with that idea.

Note: API version 12 does not support zone ID. If you create an idea in version 12,
your idea is automatically posted to the oldest zone that you have permission to
access.

This is a relationship field.

**Relationship Name**
Community


-----

```
CreatorFullPhotoUrl
CreatorName
CreatorSmallPhotoUrl
CurrencyIsoCode
IdeaThemeID

```

**Relationship Type**
Lookup

**Refers To**
Community

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the user who posted the idea or commented on the idea.

This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo. This field is available in API version 28.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifies the idea theme associated with the idea.


-----

```
IsDeleted
IsHtml
IsMerged
LastCommentDate
LastCommentId

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
Read-only. If this value is `true, your organization has the Ideas HTML editor enabled, and`
the Idea `Body` may contain HTML. If this value is `false, the HTML editor is disabled and`
the Idea `Body` only contains regular text.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether the idea has been merged with a parent idea (true) or not
(false). You can’t vote for or add comments to a merged idea.

Note: In API version 27, `IsMerged` replaces `IsLocked. Existing formula fields`
that use `IsLocked` must be edited to use `IsMerged.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the last comment (child IdeaComment object) was added.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The ID of the last comment (child IdeaComment object).

This is a relationship field.


-----

```
LastReferencedDate
LastViewedDate
NumComments
ParentIdeaId

```

**Relationship Name**
LastComment

**Relationship Type**
Lookup

**Refers To**
IdeaComment

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of comments (child IdeaComment objects) that users have submitted for the
given idea.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID associated with this idea's parent idea. When multiple ideas are merged together,
one idea becomes the parent (master) of the other ideas. The `ParentIdeaId` is
automatically set when you merge ideas.

This is a relationship field.

**Relationship Name**
ParentIdea


-----

```
RecordTypeId
Status
Title
VoteScore

```

**Relationship Type**
Lookup

**Refers To**
Idea

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record type assigned to this object.

This is a relationship field.

**Relationship Name**
RecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Customizable picklist of values used to specify the status of an idea.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The descriptive title of the idea.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The internal score of the Idea, used to sort Ideas on the Popular tab in the application user
interface. The internal algorithm that determines the score gives older votes less weight than


-----

```
VoteTotal

```

newer votes, simulating exponential decay. The score itself does not display in the application
user interface.

Note: Unlike other fields of type double, you can't use a SOQL aggregate function
with this field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
An Idea's total number of points. Each vote a user makes is worth ten points, therefore the
value of this field is ten times the number of votes an idea has received.

Note: Unlike other fields of type double, you can't use a SOQL aggregate function
with this field.


Note: If you are importing Idea data and need to set the value for an audit field, such as `CreatedDate, contact Salesforce.`
Audit fields are automatically updated during API operations unless you request to set these fields yourself..

##### Usage

Use this object to track ideas, which are written suggestions on which users can vote and comment.

SEE ALSO:

IdeaComment

Vote
