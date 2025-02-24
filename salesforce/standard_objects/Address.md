#### Address

Represents a mailing, billing, or home address.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

The following access checks must be enabled:

**•** Industries Insurance

**•** Retail Execution

**•** Industries Visit

**•** Field Service

**•** Order Management

**–** Perms: FulfillmentOrder, OrderSummary,AdvancedOrderManagement, OrderCCS

**–** Prefs: OrdersEnabled, EnhancedCommerceOrders

**•** Public Sector

**•** Employee Experience

**•** Contact Tracing For Employees

You can create an address only when creating a location.

##### Fields

```
Address
AddressType
City

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The full address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Picklist of address types. The values are:

**•** Mailing

**•** Shipping

**•** Billing

**•** Home

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Country
Description
DrivingDirections
GeocodeAccuracy
LastReferencedDate
LastViewedDate

```

**Description**
The address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address country.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of the address.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Directions to the address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. A geocoding service typically provides this value based on the
address’s latitude and longitude coordinates.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user referenced this record.

**Type**
dateTime


-----

```
Latitude
LocationType
Longitude
Name

```

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date on which a user viewed this record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal
places.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Filter, Group, Sort, Update

**Description**
Picklist of location types. The available values are:

**•** Warehouse (default)

**•** Site

**•** Van

**•** Plant

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal
places.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the address.


-----

```
ParentId
PostalCode
State
Street
TimeZone

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A lookup field to the parent location.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address postal code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address state.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Picklist of available time zones.


-----

##### Usage

Important: “Address” in Salesforce can also refer to the Address compound field found on many standard objects. When referencing
the Address object in your Apex code, always use `Schema.Address` instead of `Address` to prevent confusion with the
standard Address compound field. If referencing both the address object and the Address field in the same snippet, you can
differentiate between the two by using System.Address for the field and `Schema.Address` for the object.

##### Associated Object

This object has the following associated object. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AddressHistory (API version 62.0)**
History is available for tracked fields of the object.
