#### RecentlyViewed

Represents records or list views that the current user has recently viewed or referenced (by viewing a related record). List views are
available in API version 29.0 and later.

##### Supported Calls
```
describeSObjects(), query(), update()

 Special Usage Rules

```
The RecentlyViewed object doesn’t support the Event, Task, Report, KnowledgeArticle, and Article objects.

The RecentlyViewed object supports only certain objects, and supports list views only for those supported objects. Supported objects
have the fields `LastReferencedDate` and `LastViewedDate.`

Note: RecentlyViewed records for users who are members of several communities can’t be retrieved automatically into a map
via Apex. This is because records of a user with different networks can result in duplicate IDs that maps don’t support.

##### Fields

```
Alias
Email

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The alias on the record.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address on the record.


-----

```
FirstName
Id
IsActive
LastName
LastReferencedDate
LastViewedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name on the record. If the recently viewed record is a user, the value is the user’s
first name.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The ID of the recently viewed record or list view.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the recently viewed record is an active user (true) or not (false). This
field contains a value only if the recently viewed record is a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name on the record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update


-----

```
Name
NetworkId
Phone
ProfileId

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view (LastReferencedDate),
but not viewed it.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name on the recently viewed record or list view. If the recently viewed record is a user,
contact, or lead, the value is a concatenation of the `firstname` and `lastname` field
values.

**Type**
reference

**Properties**
Filter,Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this group is part of. This field is available only if digital
experiences is enabled in your org.

You can add a `NetworkId` only when creating a group. You can’t change or add a
`NetworkId` for an existing group. This field is available in API version 27.0 and later.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number on the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the recently viewed record is a user, this value is the user’s profile ID.

This field is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup


-----

```
Title
Type
UserRoleId

##### Usage

```

**Refers To**
Profile

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the recently viewed record is a user, this value is the title of the user; for example CFO or
CEO.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The object type for this recently viewed record or list view. Valid values include any standard
or custom objects that RecentlyViewed supports.

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


This object provides a heterogeneous list of different object types. The list consists of recently viewed records, records that were recently
referenced (a related record was viewed), or recently viewed list views. A record is considered viewed when the user sees the record
details, but not when the user sees the record in a list with other records. Use this object to programmatically construct a list of recently
viewed items specific to the current user. For example, use this object on a custom user interface or for search auto-complete options.
You can also retrieve a filtered list of records by object type (Type). The RecentlyViewed data is periodically truncated down to 200
records and 200 list views. RecentlyViewed data is retained for 90 days, after which it’s removed on a periodic basis.


-----

Use this query in your code to retrieve a list of all the records and list views that were recently viewed. The results are ordered from most
to least recent.
```
SELECT Id, Name
FROM RecentlyViewed
WHERE LastViewedDate !=null
ORDER BY LastViewedDate DESC

```
Use this query to retrieve data that was either viewed or referenced, but only for a limited set of objects.
```
SELECT Id, Name
FROM RecentlyViewed
WHERE Type IN ('Account', 'Contact', 'Plan__c')
ORDER BY LastViewedDate DESC

```
This query retrieves a list of all recently viewed contacts with contact-specific fields, such as the contact’s account name, and the custom
website field. Records are ordered from most to least recent.
```
SELECT Account.Name, Title, Email, Phone, Website__c
FROM Contact
WHERE LastViewedDate != NULL
ORDER BY LastViewedDate DESC
