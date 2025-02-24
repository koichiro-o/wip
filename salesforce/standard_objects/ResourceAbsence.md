#### ResourceAbsence

Represents a time period in which a service resource is unavailable to work in Field Service, Salesforce Scheduler, or Workforce Engagement.
This object is available in API version 38.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
Field Service or Workforce Engagement must be enabled.

##### Fields

```
AbsenceNumber
Address

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the absence.

**Type**
address


-----

```
City
Country
Description
End
GeocodeAccuracy

```

**Properties**
Filter

**Description**
The compound form of the address associated with the absence.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address associated with the absence. Maximum length is 40
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address associated with the absence. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the absence.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the absence ends.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
LastReferencedDate
LastViewedDate
Latitude
Longitude

```

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource absence was last modified. Its label in the user
interface is `Last Modified Date.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource absence was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address
associated with the absence. Acceptable values are numbers between –90 and
90 with up to 15 decimal places.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address
associated with the absence. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.

Note: This field is available in the API only.


-----

```
Postal Code
ResourceId
Start
State
Street

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address associated with the absence. Maximum length is
20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The absent service resource.

This is a relationship field.

**Relationship Name**
Resource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the absence begins.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address associated with the absence. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Type

##### Usage

```

**Description**
The street number and name of the address associated with the absence.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The type of absence: `Meeting, Training, Medical, or Vacation. The`
default value is Vacation. You can add custom values if needed, but the name
`Break` is reserved for the Field Service managed package.


Resource absences you define periods of time when a service resource is unavailable to work. Unless you’re using the Field Service
managed package, service resources can still be assigned to appointments that conflict with their absences.

Tip: Create a trigger that sends an approval request to a supervisor when a service resource creates an absence.

If you’re not using the Field Service managed package, a calendar view isn’t available for individual service resources.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ResourceAbsenceChangeEvent (API version 48.0)**
Change events are available for the object.

**ResourceAbsenceFeed**

Feed tracking is available for the object.

**ResourceAbsenceHistory**

History is available for tracked fields of the object.
