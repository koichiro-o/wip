#### GeoState

Represents a state. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The GeoState object is available if B2B Commerce or D2C Commerce is enabled.

##### Fields

```
Description
GeoCountryId
IsoCode

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the GeoCountry associated with this GeoState.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry

**Type**
string

**Properties**
Create, Filter, Group, Sort


-----

```
LastReferencedDate
LastViewedDate
Name

```
SEE ALSO:

GeoCountry


**Description**
Two-letter ISO code of the state as defined in the org’s State-Country picklist. This field is
unique within your organization

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed data in this record, a record related to
this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't view it directly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the state that corresponds with the ISO code.

