#### Shipment

Represents the transport of inventory in field service or a shipment of order items in Order Management.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
At least one of these features must be enabled:

**•** Order Management

**•** Field Service

**•** B2B Commerce

**•** Health Cloud Visit Inventory

**•** Consumer Goods Cloud Retail Execution


-----

##### Fields

**Field Name**
```
ActualDeliveryDate
DeliveredToId
DeliveryMethodId
Description
DestinationLocationId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product was delivered.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The person or entity the product was delivered to.

This is a polymorphic relationship field.

**Relationship Name**
DeliveredTo

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The delivery method used for the shipment.

This field is available in API version 51.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Details not recorded in the provided fields

**Type**
reference


-----

```
ExpectedDeliveryDate
FulfillmentOrderId
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The place the product is to be delivered.

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
Create, Filter, Nillable, Sort, Update

**Description**
Date the product is expected to be delivered.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The fulfillment order that the shipment belongs to.

This field is available in API version 51.0 and later.

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


-----

```
OrderSummaryId
OwnerId
Provider
ReturnOrderId

```

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order summary associated with the shipment.

This field is available in API version 51.0 and later.

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
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company or person making the transfer.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For a return Shipment, the associated ReturnOrder.

This field is available in API version 53.0 and later.


-----

```
ShipFromAddress
ShipFromCity
ShipFromCountry
ShipFromCountryCode
ShipFromGeocodeAccuracy

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The place the product is coming from. The compound form of the ship to address.
Read-only. For details on compound address fields, see Address Compound
Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the shipment originates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address where the shipment originates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A two letter uppercase country code conforming to the ISO 3166-1 alpha-2
standard.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address where the shipment originates.
See Compound Field Considerations and Limitations for details on geolocation
compound fields.

Note: This field is available in the API only.


-----

```
ShipFromLatitude
ShipFromLongitude
ShipFromPostalCode
ShipFromState
ShipFromStateCode

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
shipment originates. Acceptable values are numbers between –90 and 90 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
shipment originates. Acceptable values are numbers between –180 and 180 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the shipment originates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address where the shipment originates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ShipFromStreet
ShipToAddress
ShipToCity
ShipToCountry
ShipToCountryCode

```

**Description**
A two letter uppercase state code conforming to the ISO 3166-1 alpha-2 standard.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the shipment originates.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The physical address where the shipment is delivered. The compound form of
the ship to address. Read-only. For details on compound address fields, see
Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city of the address where the shipment is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address where the shipment is delivered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A two letter uppercase country code conforming to the ISO 3166-1 alpha-2
standard.


-----

```
ShipToGeocodeAccuracy
ShipToLatitude
ShipToLongitude
ShipToName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address where the shipment is delivered.
See Compound Field Considerations and Limitations for details on geolocation
compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address where the
shipment is delivered. Acceptable values are numbers between –90 and 90 with
up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address where the
shipment is delivered. Acceptable values are numbers between –180 and 180
with up to 15 decimal places. See Compound Field Considerations and Limitations
for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The shipment recipient.


-----

```
ShipToPostalCode
ShipToState
ShipToStateCode
ShipToStreet
ShipmentNumber
SourceLocationId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the shipment is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address where the shipment is delivered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A two letter uppercase state code conforming to the ISO 3166-1 alpha-2 standard.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street of the address where the shipment is delivered.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the shipment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field service location where the shipment originates.


-----

```
Status
TotalItemsQuantity
TrackingNumber
TrackingUrl

```

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the shipment. The picklist includes the following values, which can
be customized:

**•** `Shipped—The product is in transit.`

**•** `Delivered—The product is at the source location.`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total quantity of items included in the shipment. This value is calculated as
the sum of the quantities of the shipment items in the shipment.

This field is available in API version 51.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Tracking number for the shipment.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL of website used for tracking the shipment.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShipmentChangeEvent (API version 48.0)**
Change events are available for the object.

**ShipmentFeed**

Feed tracking is available for the object.

**ShipmentHistory**

History is available for tracked fields of the object.

**ShipmentOwnerSharingRule**

Sharing rules are available for the object.

**ShipmentShare**

Sharing is available for the object.

SEE ALSO:

ShipmentItem
