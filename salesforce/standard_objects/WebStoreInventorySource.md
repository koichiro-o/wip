#### WebStoreInventorySource

Used to configure the inventory source for a webstore. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
InventoryCacheTtl
InventoryDimension
IsBopisEnabled
IsDefault

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Amount of time in seconds before cache expires.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies which field within inventory levels to use to determine availability.

Possible values are `AvailableToFulfill,AvailableToOrder,OnHand.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the location supports buy online, pick up in store.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default inventory source value (true) or not (false).

The default value is `false.`


-----

```
IsEnabled
LastReferencedDate
LastViewedDate
LocationSourceExtRef
LocationSourceId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the default inventory source is active.

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Group, Nillable

**Description**
The external reference identifier associated with the `LocationSourceId.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location ID or location group ID for this webstore.

This field is a polymorphic relationship field.

**Relationship Name**
LocationSource

**Relationship Type**
Lookup


-----

```
Name
ReservationDurationInSeconds
WebStoreId

```

**Refers To**
Location, LocationGroup

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The source name for this entity.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The amount of time in seconds that a reservation stays active and doesn’t expire. Required
for implementations using Omnichannel Inventory.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique store ID related to this inventory source.

This field is a relationship field.

**Relationship Name**
WebStore

**Relationship Type**
Lookup

**Refers To**
WebStore

