#### TravelMode

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the language is available for translation (true) or not (false).

Specify translators for each language through the Translation Language Setup page.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the translated values for this language display to users (true) or not
(false).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language code. See the Salesforce Help for a full list of languages and their codes.


Represents a travel mode used for travel time calculations. The records include information about the type of transportation (such as
Car or Walking), whether a vehicle can take toll roads, and whether a vehicle is transporting hazardous materials. This object is available
in API version 54.0 and later.


-----

##### Fields

**Field**
```
CanUseTollRoads
IsLocked
IsTransportingHazmat
LastReferencedDate
LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the vehicle is allowed to drive on toll roads.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the travel model record is locked or not.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the vehicle is transporting hazardous materials.

The default value is `false.`

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


-----

```
MayEdit
Name
OwnerId
TransportType

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate=)
but not viewed it.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the travel model record can be edited or not.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the travel mode.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of transportation.

Possible values are:


-----

**•** `Bicycle`

**•** `Car-Default.`

**•** `Heavy Truck`

**•** `Light Truck`

**•** `Walking`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TravelModeFeed**

Feed tracking is available for the object.

**TravelModeOwnerSharingRule**

Sharing rules are available for the object.

**TravelModeShare**

Sharing is available for the object.
