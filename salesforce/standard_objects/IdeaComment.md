#### IdeaComment

Represents a comment that a user has submitted in response to an idea.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
undelete(), update(), upsert()

```
Note: When performing a SOSL search on IdeaComment objects, Idea objects are also searched.


-----

##### Fields

**Field**
```
CommentBody
CommunityId
CreatorFullPhotoUrl
CreatorName
CreatorSmallPhotoUrl

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Body of the submitted comment.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The zone ID associated with the idea. Once you create an idea, you can’t change the zone
ID associated with that idea.

Note: API version 12 does not support zone ID. If you create an idea in version 12,
your idea is automatically posted to the oldest zone that you have permission to
access.

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
Name of the user who posted the idea or commented on the idea. This field is available in
API version 28.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo. This field is available in API version 28.0 and later.


-----

```
IdeaId
IsHtml
UpVotes

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the idea on which this comment was made.

This is a relationship field.

**Relationship Name**
Idea

**Relationship Type**
Lookup

**Refers To**
Idea

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. If this value is `true, your organization has the Ideas HTML editor enabled, and`
the `CommentBody field may contain HTML. If this value is` `false, the HTML editor is`
disabled and the `CommentBody` field only contains regular text.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Total number of up votes for the question.


Note: If you import these records, and need to set the value for an audit field, such as CreatedDate, contact Salesforce. Audit
fields are automatically updated during API operations unless you request to set these fields yourself.

##### Usage

Use this object to track comments on ideas, which are users' text responses to ideas.

SEE ALSO:

Idea

Vote


-----
