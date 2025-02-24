#### Location

Represents a warehouse, service vehicle, work site, or other element of the region where your team performs field service work. In API
version 49.0 and later, you can associate activities with specific locations. Activities, such as the tasks and events related to a location,
appear in the activities timeline when you view the location detail page. Also in API version 49.0 and later, Work.com users can view
Employees as a related list on Location records. In API version 51.0 and later, this object is available for Omnichannel Inventory and
represents physical locations where inventory is available for fulfilling orders.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
At least one of these features must be enabled:

**•** Commerce Store

**•** Contact Tracing for Employees

**•** Employee Experience

**•** Field Service

**•** Fulfillment Orders

**•** Health Cloud

**•** Industries Insurance

**•** Industries Visit

**•** Locations

**•** Omnichannel Inventory

**•** Public Sector

**•** Retail Execution

**•** Work.com

##### Fields

```
AssignedFoCount

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of fulfillment orders assigned to the location. Confirming held
fulfillment order capacity increments this value. To reset the location’s capacity,
set this value to 0.


-----

```
CloseDate
ConstructionEndDate
ConstructionStartDate
DefaultPickupTime
DefaultProcessingTime

```

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date the location closed or went out of service.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date construction ended at the location.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date construction began at the location.

**Type**
time

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default pickup time at the location.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default processing time at the location.


-----

```
DefaultProcessingTimeUnit
Description
DrivingDirections
ExternalReference
FoCapacity

```

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default processing time unit at the location. Possible values are:

**•** `Hours`

**•** `Days`

**•** `Weeks`

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of the location.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Directions to the location.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of a location.

**Type**
int


-----

```
FulfillingBusinessHours
FoCapacity
IsInventoryLocation
IsMobile

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of fulfillment orders that can be assigned to the location
per time period. If this value is null, then this location’s capacity isn’t limited.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Fulfilling business hours at the location.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 61.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of fulfillment orders that can be assigned to the location
per time period. If this value is null, then this location’s capacity isn’t limited.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location stores parts.

Note: This field must be selected if you want to associate the location
with product items.

**Type**
boolean


-----

```
LastReferencedDate
LastViewedDate
Latitude
Location
LocationLevel

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location moves. For example, a truck or tool box.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the location was last modified. Its label in the user interface is
```
  Last Modified Date.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the location was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location.

**Type**
location

**Properties**
Nillable

**Description**
The geographic location.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location’s position in a location hierarchy. If the location has no parent or
child locations, its level is 1. Locations that belong to a hierarchy have a level of


-----

```
LocationType
LogoId
Longitude
Name

```

1 for the root location, 2 for the child locations of the root location, 3 for their
children, and so forth.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Picklist of location types. It has no default values, so you must populate it before
creating any location records.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A ContentAsset representing a logo for the location.

This field is available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
Logo

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the location. For example, Service Van #4.


-----

```
OpenDate
OwnerId
ParentLocationId
PossessionDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date the location opened or came into service.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The location’s owner or driver.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location’s parent location. For example, if vans are stored at a warehouse
when not in service, the warehouse is the parent location.

This is a relationship field.

**Relationship Name**
ParentLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Priority
RemodelEndDate
RemodelStartDate
RootLocationId

```

**Description**
The date the location was purchased.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the location when routing orders. No default values are included.
Add values to the picklist and reference them in your custom routing logic.

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when remodel construction ended at the location.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when remodel construction started at the location.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read Only) The top-level location in the location’s hierarchy.

This is a relationship field.

**Relationship Name**
RootLocation

**Relationship Type**
Lookup

**Refers To**
Location


-----

```
ShouldSyncWithOci
ShouldTrackFoCapacity
TimeZone
VisitorAddressId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location should sync its data with Omnichannel Inventory.
The default value is `false.`

This field is available in API version 51.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location should track its fulfillment order capacity. The
default value is `false.`

This field is available when Order Management is installed and configured. By
default, it’s hidden by field-level security.

This field is available in API version 55.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Picklist of available time zones.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup to an account’s or client’s address.

This is a relationship field.

**Relationship Name**
VisitorAddress

**Relationship Type**
Lookup

**Refers To**
Address


-----

##### Usage

Before creating any location records, add at least one value to the Location Type picklist. LocationType is a required field.

To track your inventory in Salesforce, create product items, which represent the stock of a particular product a particular location. For
example, create a product item that represents the 500 bolts you have in stock at your Warehouse A location. Each product item must
be associated with a location.

To get a more granular picture of your field service operation, associate locations with service territories. For example, if a warehouse is
located in a particular service territory, add it as a service territory location.

Important: “Location” in Salesforce can also refer to the geolocation compound field found on many standard objects. When
referencing the Location object in your Apex code, always use Schema.Location instead of Location to prevent confusion
with the standard Location compound field. If referencing both the Location object and the Location field in the same snippet,
you can differentiate between the two by using `System.Location` for the field and `Schema.Location` for the object.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LocationChangeEvent (API version 48.0)**
Change events are available for the object.

**LocationFeed**

Feed tracking is available for the object.

**LocationHistory**

History is available for tracked fields of the object.

**LocationOwnerSharingRule**

Sharing rules are available for the object.

**LocationShare**

Sharing is available for the object.

SEE ALSO:

LocationGroup

LocationGroupAssignment

_[B2B Commerce and D2C Commerce Developer Guide: Inventory Data Model](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-inventory.html)_
