#### ProductRequest

Represents an order for a part or parts in field service.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

Authenticated external users can create and update ProductRequest objects.

##### Fields

```
AccountId
CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the product request.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The case associated with the product request.

This is a relationship field.

**Relationship Name**
Case


-----

```
CurrencyIsoCode
Description
DestinationLocationId
LastReferencedDate

```

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for
any currency allowed by the organization. The label in the user interface is
```
  Currency ISO Code.

```
**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text field for details not recorded in the provided fields.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the product is delivered.

This is a relationship field.

**Relationship Name**
DestinationLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
NeedByDate
OwnerId
ProductRequestNumber
ShipToAddress

```

**Description**
The date when the product request was last modified. Its label in the user interface
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product must be delivered by.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shipment.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned number that identifies the shipment.

**Type**
address


-----

```
ShipToCity
ShipToCountry
ShipToGeocodeAccuracy
ShipToLatitude
ShipToLongitude

```

**Properties**
Filter, Nillable

**Description**
The address that the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city that the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country that the product is to be delivered to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The accuracy of the geocode for the shipping address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location where the product is to be delivered to.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location where the product is to be delivered to.


-----

```
ShipToPostalCode
ShipToState
ShipToStreet
ShipmentType
SourceLocationId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the product is to be delivered to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the state where the product is to be delivered to.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where the product is to be delivered to.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment. The picklist includes the following values by default:

**•** None

**•** Rush

**•** Overnight

**•** Next Business Day

**•** Pick Up

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location the product is shipped from.

This is a relationship field.


-----

```
Status
WorkOrderId
WorkOrderLineItemId

```

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the product transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order that the product request is related to.

This is a relationship field.

**Relationship Name**
WorkOrder

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order line item that the product request is related to.

This is a relationship field.

**Relationship Name**
WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductRequestChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductRequestFeed**

Feed tracking is available for the object.

**ProductRequestHistory**

History is available for tracked fields of the object.

**ProductRequestOwnerSharingRule**

Sharing rules are available for the object.

**ProductRequestShare**

Sharing is available for the object.
