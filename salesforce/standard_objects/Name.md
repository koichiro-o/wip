#### Name

Non-queryable object that provides information about foreign key traversals when the foreign key has more than one parent.

This object is used to retrieve information from related records where the related record can be from more than one object type (a
polymorphic foreign key). For example, the owner of a case can be either a user or a group (queue). This object allows retrieval of the
owner name, whether the owner is a user or a group (queue). You can use a describe call to access the information about parents for
an object, or you can use the `who,` `what, or` `owner` fields (depending on the object) in SOQL queries. This object can’t be directly
accessed.

##### Supported Calls
```
describeSObjects()

 Fields

```
```
Alias

```

**Type**
string


-----

```
Email
FirstName
IsActive
LastName
LastReferencedDate

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user alias. This field contains a value only if the related record is a user.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the user or group (queue).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the user, contact, or lead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related record is an active user (true) or not (false). This field
contains a value only if the related record is a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name of the user, contact, or lead.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.


-----

```
LastViewedDate
MiddleName
Name
Phone
Profile
ProfileId

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view (LastReferencedDate),
but not viewed it.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The middle name of the user contact, or lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the parent of the object queried. If the parent is a user, contact, or lead, the
value is a concatenation of the FirstName, MiddleName, LastName, and Suffix
fields of the related record.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the user. This field contains a value only if the related record is a user.

**Type**
reference

**Properties**
Filter, Nillable

**Description**
The Profile of the user. Only populated if the related record is a user.

**Type**
reference


-----

```
Suffix
Title
Type
Username

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user’s Profile. Only populated if the related record is a user.

This field is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name suffix of the user, contact, or lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the user, for example CFO or CEO.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
A list of the types of sObject that can be an owner of this object. You can use this field to
filter on a type of owner, for example, return only the leads owned by a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
UserRole
 UserRoleId

##### Usage

```

**Description**
Contains the name that a user enters to log into the API or the user interface. The value for
this field is in the form of an email address, and is only populated if the related record is a
user.

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Name of the `Role` played by the user. Only populated for user rows.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user role associated with this object.

This field is a relationship field.

**Relationship Name**
UserRole

**Relationship Type**
Lookup

**Refers To**
UserRole


To query on relationships where the parent can be more than one type of object, use `who,` `what, or` `owner` relationship fields.

SEE ALSO:

Overview of Salesforce Objects and Fields
