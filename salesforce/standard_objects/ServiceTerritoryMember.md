#### ServiceTerritoryMember

Represents a service resource who can be assigned in a service territory in Field Service, Salesforce Scheduler, or Workforce Engagement.
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
Address
City

```

**Type**
address

**Properties**
Filter

**Description**
The member’s address. You may want to list the related service resource’s address
in this field.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the member’s address. Maximum length is 40 characters.


-----

```
Country
EffectiveEndDate
EffectiveStartDate
GeocodeAccuracy
LastReferencedDate

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the member’s address. Maximum length is 80 characters.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the service resource is no longer a member of the territory. If the
resource will be working in the territory for the foreseeable future, leave this field
blank. This field is mainly useful for indicating when a temporary relocation ends.

**Type**
datetime

**Properties**
Create, Filter, Sort, Update

**Description**
The date when the service resource becomes a member of the service territory.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

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
The date when the territory member was last modified. Its label in the user
interface is `Last Modified Date.`


-----

```
LastViewedDate
Latitude
Longitude
MemberNumber
OperatingHoursId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the territory member was last viewed.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the member’s
address. Acceptable values are numbers between –90 and 90 with up to 15
decimal places.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the member’s
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

Note: This field is available in the API only.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read only) An auto-generated number identifying the service territory member.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The operating hours assigned to the service territory member. If no operating
hours are specified, the member is assumed to use their parent service territory’s


-----

```
PostalCode
ServiceResourceId
ServiceTerritoryId

```

operating hours. If a member needs special operating hours, create them in Setup
and select them in the Operating Hours lookup field on the member’s
detail page.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the member’s address. Maximum length is 20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource assigned to the service territory.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The service territory that the service resource is assigned to.

This is a relationship field.

**Relationship Name**
ServiceTerritory


-----

```
State
Street
TerritoryType

```

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the member’s address. Maximum length is 80 characters.

**Type**
textarea

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name of the member’s address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Primary, Secondary, or Relocation.

**•** The primary territory is typically the territory where the resource works most
often—for example, near their home base. Service resources can only have
one primary territory.

**•** Secondary territories are territories where the resource can be assigned to
appointments if needed. Service resources can have multiple secondary
territories.

**•** Relocation territories represent temporary moves for service resources. If
you’re using the Field Service managed packages with the scheduling
optimizer, resources with relocation territories are always assigned to services
within their relocation territories during the specified relocation dates; if they
don’t have a relocation territory, the primary territories are favored over the
secondary.

For example, a service resource might have the following territories:

**•** Primary territory: `West Chicago`

**•** Secondary territories:

**–** `East Chicago`


-----

**–** `South Chicago`

**•** Relocation territory: Manhattan, for a three-month period

##### Usage

If you delete a service territory with members, the service resources who were members no longer have any connection to the territory.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceTerritoryMemberChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceTerritoryMemberFeed**

Feed tracking is available for the object.

**ServiceTerritoryMemberHistory**

History is available for tracked fields of the object.
