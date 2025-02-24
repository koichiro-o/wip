#### ListEmailRecipientSource

For a list email in Salesforce, represents the dynamically defined sources of recipient email addresses. Each record represents a link to a
single list view or campaign that is examined when the list email is sent. Has a one-to-many relationship with ListEmail. This object is
available in API version 41.0 and later.

The visibility and accessibility of this object is inherited from the related list email.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), getDeleted(), getUpdated(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
ListEmailId
Name
SourceListId
SourceType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The related list email record. Required on record creation; read-only otherwise.

This is a relationship field.

**Relationship Name**
ListEmail

**Relationship Type**
Lookup

**Refers To**
ListEmail

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated name of the list email recipient source.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The id of a list view to send the list email to. Read-only except when list email is
in draft state.

This is a polymorphic relationship field.

**Relationship Name**
SourceList

**Relationship Type**
Lookup

**Refers To**
Campaign, ListView, Topic

**Type**
reference


-----

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Read-only except when list email is in draft state.

Valid values:

**•** Include
