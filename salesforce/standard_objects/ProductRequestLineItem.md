#### ProductRequestLineItem

Represents a request for a part in field service. Product request line items are components of product requests.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled. You can't use product request line item as a master in an master detail relationship (through a custom
field) with a custom object with data.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the product request line item.

This is a relationship field.

**Relationship Name**
Account


-----

```
CareProgramEnrolleeId
CaseId
Description

```

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the care program enrollee associated with the product request line
item. This field is available from API version 49.0 and later.

This is a relationship field.

**Relationship Name**
CareProgramEnrollee

**Relationship Type**
Lookup

**Refers To**
CareProgramEnrollee

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The case associated with the product request line item.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Details not recorded in the provided fields.


-----

```
DestinationLocationId
LastReferencedDate
LastViewedDate
NeedByDate
ParentId

```

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

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product must be delivered by.

**Type**
reference


-----

```
Product2Id
ProductRequestLineItemNumber
QuantityRequested

```

**Properties**
Create, Filter, Group, Sort

**Description**
The product request that the line item belongs to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ProductRequest

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The product associated with the product request line item.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read Only) An auto-assigned number that identifies the product request line
item.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The amount requested.


-----

```
QuantityUnitOfMeasure
ShipToAddress
ShipToCity
ShipToCountry
ShipToGeocodeAccuracy
ShipToLatitude

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Units of the requested product; for example, grams, liters, or units. The picklist
values can be customized.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The physical address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address where the product is needed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address where the product is needed. See
Compound Field Considerations and Limitations for details on geolocation
compound fields.

Note: This field is available in the API only.

**Type**
double


-----

```
ShipToLongitude
ShipToPostalCode
ShipToState
ShipToStreet

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
product is needed. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places. See Compound Field Considerations and Limitations for
details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
product is needed. Acceptable values are numbers between –180 and 180 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the product is needed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address where the product is needed.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the product is needed.


-----

```
ShipmentType
SourceLocationId
Status
WorkOrderId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of shipment. The picklist includes the following values, which can be
customized:

**•** `Rush`

**•** `Overnight`

**•** `Next Business Day`

**•** `Pick Up`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Where the product is at the time of the request.

This is a relationship field.

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
The status of the shipment. The picklist includes the following values, which can
be customized:

**•** `Draft`

**•** `Submitted`

**•** `Received`

**Type**
reference


-----

```
WorkOrderLineItemId

##### Associated Objects

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work order for which the product is needed.

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
The work order line item for which the product is needed.

This is a relationship field.

**Relationship Name**
WorkOrderLineItem

**Relationship Type**
Lookup

**Refers To**
WorkOrderLineItem


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductRequestLineItemChangeEvent (API version 48.0)**
Change events are available for the object.

**ProductRequestLineItemFeed**

Feed tracking is available for the object.

**ProductRequestLineItemHistory**

History is available for tracked fields of the object.
