#### IdeaTheme

Represents an invitation to zone members to submit ideas that are focused on a specific topic. This object is available in API version 26
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), query(), retrieve(), search(), undelete(), update(),

 Fields

```
```
Categories
CommunityId

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Customizable multi-select picklist used to organize ideas and idea themes into
logical groupings.

**Type**
reference


-----

```
CurrencyIsoCode
Description
EndDate
LastReferencedDate
StartDate

```

**Properties**
Create, Filter, Group, Nillable, Sort,

**Description**
The zone ID associated with the idea theme.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains
the ISO code for any currency allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Description of the idea theme.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date marking the end of the idea theme.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date that the idea theme begins.


-----

```
Status
Title

##### Usage

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Customizable picklist of values used to specify the status of the idea theme.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**

Title of the idea theme.


Use the object to track ideas that are submitted to an idea theme.
