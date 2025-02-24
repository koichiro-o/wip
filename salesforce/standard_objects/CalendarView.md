#### CalendarView

These calendars can be created and assigned to users other than the creator. Available calendars include object, shared, public, resource,
and user list calendars. Object calendars represent a calendar based on a Salesforce object, either standard or custom. This object is
available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
All fields and entities referenced by field values must be accessible by the CalendarView creator even if the creator isn’t the CalendarView
owner.

##### Fields

```
Color
CurrencyIsoCode
DateHandlingType

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Represents the color used in the background for records displayed in a user’s calendar view
within the user interface.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determined by the data type of the `StartField. Valid values include:`

**•** `Date`

**•** `Datetime`


-----

```
DisplayField
EndField
FillPattern
IsDisplayed
ListViewFilterId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the `SobjectType` field used as the subject for records displayed in a user’s
calendar view within the user interface.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An optional field that represents the sObjectType field used as the end time for records
displayed in a user’s calendar view within the user interface. Must be a date or dateTime field
that matches the type in `StartField.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the pattern displayed as the background for records displayed in a user’s calendar
view within the user interface. Valid values include:

**•** `verticalStripes`

**•** `ascDiagonalStripes`

**•** `descDiagonalStripes`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether users can see a calendar’s records in their calendar view in the user interface.
When `true, records are visible in the user’s calendar view. When` `false, records are`
hidden from the user’s calendar view. The default is true. IsDisplayed can be true
for up to 50 calendars.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Name
OwnerId
PublisherId

```

**Description**
References the ListView used to filter records represented by the CalendarView. ListView
must have the same sObjectType. If no `ListViewFilterId` is defined, the calendar
displays only records with the same owner as the CalendarView.

This is a relationship field.

**Relationship Name**
ListViewFilter

**Relationship Type**
Lookup

**Refers To**
ListView

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A user-provided name that identifies the calendar. This isn’t an enumerated field; it can be
any string to a maximum length of 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Represents the owner of the CalendarView.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents the user, user list, public, or resource calendar from where event data is populated.

This is a polymorphic relationship field.


-----

```
SobjectType
StartField

##### Usage

```

**Relationship Name**
Publisher

**Relationship Type**
Lookup

**Refers To**
Calendar, ListView, User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of standard or custom Salesforce object that is used to create records for the
CalendarView. Use the API name of the desired `SobjectType.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the SobjectType field used as the start time for records displayed in a user’s
calendar view within the user interface. Must be a date or dateTime field type.


To distribute a CalendarView to multiple users, IDs can be pulled from a group, user list, or profile. For this example, a CalendarView
based on opportunity close dates is being distributed to a sales team in a public group, Sales Group:


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalendarViewChangeEvent (API version 62.0)**
Change events are available for the object.
