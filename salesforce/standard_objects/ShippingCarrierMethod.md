#### ShippingCarrierMethod

Shipping service provided by a shipping carrier. Examples include Ground, 2Day, and NextDay. Service depends on the range of transit
times available for each carrier. This object is available in API version 61.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The ShippingCarrierMethodId object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
ExternalReference
LastReferencedDate
LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique code, reference, or identifier for the shipping carrier associated with the delivery. Can
be used for internal tracking or integration purposes.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the record was last modified. Its label in the user interface is `Last`
```
  Modified Date.

```
**Type**
dateTime


-----

```
MaxTransitTime
MinTransitTime
Name
OwnerId

```

**Properties**
Filter, Nillable, Sort

**Description**
The date the record was last viewed.

**Type**
integer

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Maximum amount of time required for the carrier to transport and deliver an order. Measured
in a specific unit, such as days, hours, or weeks.

For example, if the maximum transit time is set to 3, the carrier takes no more than 3 units
of the specified transit time unit to deliver the order.

**Type**
integer

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum amount of time required for the carrier to transport and deliver an order. Measured
in a specific unit, such as days, hours, or weeks.

For example, if the minimum transit time is set to 1, the carrier takes at least 1 unit of the
specified transit time unit to deliver the order.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping carrier associated with the delivery.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this ShippingCarrierMethod object. Default value is the
user logged in to the API to perform the create.

This is a polymorphic relationship field.


-----

```
ShippingCarrierId
TransitTimeUnit

```

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Id of the company or service responsible for transporting and delivering the order to the
customer.

This is a relationship field.

**Relationship Name**
ShippingCarrier

**Refers To**
ShippingCarrier

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Unit of measurement used for transit time. Specifies the time interval in which the minimum
and maximum transit times are expressed.

The available options are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

