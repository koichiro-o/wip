#### Bookmark

Represents a link between opportunities that share common information.

This object is available to organizations with the Similar Opportunities feature enabled.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Fields

**Field**
```
ID
FromId
ToId
 IsDeleted

##### Usage

```

**Type**
ID

**Properties**
Defaulted on create, Filter

**Description**
ID of the bookmark. Label is Bookmark ID.

**Type**
ID

**Properties**
Filter

**Description**
The originating opportunity. Label is Bookmarked From ID

**Type**
ID

**Properties**
Filter

**Description**
The opportunity to which the originating opportunity is linked. Label is Bookmarked To
**ID.**

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.


The Bookmark object works with the Opportunity object only.

Use this read-only object to query the bookmarks between opportunities in your organization. In the online application, users can search
for opportunities that share attributes with their opportunity. The user can then bookmark the appropriate opportunities for future
reference.


-----
