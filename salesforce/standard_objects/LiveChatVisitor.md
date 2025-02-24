#### LiveChatVisitor

Represents a website visitor who has started or tried to start a chat session. This object is available in API version 24.0 and later.

##### Supported Calls
```
create(), delete(), getDeleted(), getUpdated(), query(), retrieve(), undelete(), update(),
upsert()

 Fields

```
```
LastReferencedDate

```

**Type**
date

**Properties**
Filter, Nillable, Sort, Update


-----

```
LastViewedDate
Name
SessionKey

##### Usage

```

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
(LastReferencedDate) but not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of the visitor

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The session key used to uniquely identify the visitor.


Use this object to query and manage live chat visitors.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**LiveChatVisitorChangeEvent (API version 62.0)**
Change events are available for the object.


-----
