#### ServiceTerritory

```


**•** `updatesOrgSettings`

**•** `updatesOrgValues`

**•** `sortApps`

**•** `setForecastingUserFeatureLicense`

**•** `recalculatePermissionSetGroup`

**•** `deploysMetadata`

**•** `createsSetupEntityAccess`

**•** `clearGuidanceCenterCache`

**•** `callsConnectApi`

**•** `assignsPermissionSets`

**•** `assignsPermissionSetGroups`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Additional details about the TaskAction parameter, including how much of the action
has been processed.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the changes included in the task.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the task.


Represents a geographic or functional region in which work can be performed in Field Service, Salesforce Scheduler, or Workforce
Engagement. This object is available in API version 38.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
Address
AvgTravelTime
City
Country

```

**Type**
address

**Properties**
Filter

**Description**
An address to associate with the territory. For example, you can list the address
of the territory’s headquarters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The average travel time for this service territory. The value is added to the Work
Capacity Usage for each scheduled service appointment in the service territory.
Available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the associated address. Maximum length is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country to associate with the territory. Maximum length is 80 characters.


-----

```
Description
GeocodeAccuracy
IsActive
LastReferencedDate
LastViewedDate
Latitude

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the territory.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.This field is available in the API only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the service territory is meant to be used. If a territory is inactive,
you can’t add members to it or link it to work orders, work order line items, or
service appointments.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory was last modified. Its label in the user interface is
```
  Last Modified Date.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory was last viewed.

**Type**
double


-----

```
Longitude
Name
OperatingHoursId
ParentTerritoryId

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address
associated with the territory. Acceptable values are numbers between –90 and
90 with up to 15 decimal places.This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address
associated with the territory. Acceptable values are numbers between –180 and
180 with up to 15 decimal places.This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the territory.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The territory’s operating hours, which indicate when service appointments within
the territory can occur. Service resources who are members of a territory
automatically inherit the territory’s operating hours unless different hours are
specified on the resource record.

This field is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
reference


-----

```
PostalCode
State
Street
TopLevelTerritoryId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The territory’s parent service territory, if it has one. For example, a `Northern`
`California` territory can have a State of California territory as
its parent. A service territory hierarchy can contain up to 10,000 territories.

This field is a relationship field.

**Relationship Name**
ParentTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address associated with the territory. Maximum length is
20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address associated with the territory. Maximum length is 80
characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name of the address associated with the territory.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
TravelModeId
TravelTimeBuffer
TypicalInTerritoryTravelTime

```

**Description**
(Read only) The top-level territory in a hierarchy of service territories. Depending
on where a territory lies in the hierarchy, its top-level territory can be the same
as its parent.

This field is a relationship field.

**Relationship Name**
TopLevelTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the TravelMode used for travel time calculations. The travel mode includes
information about the type of transportation, such as a car or walking, whether
a vehicle can take toll roads, and whether a vehicle is transporting hazardous
materials.

This field is a relationship field.

**Relationship Name**
TravelMode

**Relationship Type**
Lookup

**Refers To**
TravelMode

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Add additional time to driving time, such as time to find parking or to walk to
the site. This value overrides the Travel Time Buffer value defined in Field Service
Settings | Scheduling | Routing.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

**Description**
Estimated number of minutes needed to travel from one location to another
within the service territory. You can use this field in Apex customization.

##### Usage

If you want to use service territories, determine which territories to create. Depending on how your business works, you can create
territories based on cities or counties, or on functional categories such as sales versus service. If you plan to build out a hierarchy of service
territories, create the highest-level territories first.

For example, you can create a hierarchy of territories to represent the areas where your team works in California. Include a top-level
territory named `California, three child territories named` `Northern California,` `Central California, and`
```
Southern California, and a series of third-level territories corresponding to California counties. Assign service resources to each

```
county territory to indicate who is available to work in that county.

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**ServiceTerritoryChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceTerritoryFeed**

Feed tracking is available for the object.

**ServiceTerritoryHistory**

History is available for tracked fields of the object.

**ServiceTerritoryOwnerSharingRule**

Sharing rules are available for the object.

**ServiceTerritoryShare**

Sharing is available for the object.
