#### LocationTrustMeasure

Represents the COVID safety protocols that your business follows. For example, enforcement of masks, social distancing, cleanliness,
and capacity limits. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
IconUrl
IsVisibleInPublic
LastReferencedDate
LastViewedDate
LocationExternalReference

```

**Description**
A brief description of the safety protocol. For example, “Employees and customers are required
to wear a mask in the store.”

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A public image URL to display for the LocationTrustMeasure object.

**Type**
boolean

**Properties**
Create, defaulted on create, Filter, Group, Sort, Update

**Description**
If true, displays the LocationTrustMeasure object on your site. If false, hides the
LocationTrustMeasure object on your site.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the record was last viewed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An ID assigned to the LocationTrustMeasure objects for a particular location.


-----

```
LocationId
Name
OwnerId
SortOrder
Title

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID for the location associated with the LocationTrustMeasure.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned name for the LocationTrustMeasure.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner for this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which to display LocationTrustMeasure objects on your site.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the safety protocol. For example, Enforcement of Masks.

