#### UserDefinedLabel

Represents a label created by a user to help organize, track, and find records. This object is available in API version 61.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Color
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Hexadecimal value of the color used to help organize the UserDefinedLabel records.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly. For example,
accessed through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate is not null, the user accessed this record or list view indirectly.
For example, accessed through a list view or related record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the UserDefinedLabel record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
TotalAssignments
Type

##### Associated Objects

```

**Description**
ID of the user or group that owns the label.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Calculated field. Number of related UserDefinedLabelAssignment records. Available in API
version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of user-defined label.

Possible values are:

**•** `Starred`

**•** `Tag`

**•** `User`


This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**UserDefinedLabelOwnerSharingRule on page 64**
Sharing rules are available for the object.

**UserDefinedLabelShare on page 66**
Sharing is available for the object.
