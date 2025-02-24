#### Calendar

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The version name.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When more than one enabled version matches an Expression Set call, and the
`StartDateTime` to EndDateTime spans overlap, the version with the highest Rank
is chosen.

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The first date on which this Expression Set Version is active.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number.


Represents a calendar. This can be a default user calendar, public calendar, resource calendar, or holiday calendar. This object is available
in API version 45.0 and later.

Newly created users are assigned a default calendar automatically. Similarly, holiday calendars are created automatically for each
organization.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), search()

```

-----

##### Special Access Rules

Users with "View Setup and Configuration" user permissions can create, edit, and delete public and resource calendars in the user
interface. All users, even those without the “View Setup and Configuration” user permission, can view calendars via the API.

##### Fields

All fields are readable only.

```
IsActive
Name
Type
UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates whether a user can save events to the calendar.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A user provided name that identifies the calendar. It is text-indexed for searchability. Note
that this is not an enumerated field; it can be any string to a maximum length of 80 characters.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the calendar. Possible values are:

**•** `Holiday` (Holiday Calendar)

**•** `Public` (Public Calendar)

**•** `Resource` (Resource Calendar)

**•** `User` (User Calendar)

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user that owns that calendar record. If Type=User, there’s a UserID associated
(foreign key reference to the user). Otherwise, the user field is null.


-----
