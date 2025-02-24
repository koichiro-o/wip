#### LocationShippingCarrierMethod

The available shipping carrier services associated with a location or location group. Allows the assignment of different shipping methods
to a specific location and enables flexibility and customization in the shipping process. This object is available in API version 61.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The LocationShippingCarrierMethod object is available only if the B2B Commerce or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
LastReferencedDate
LastViewedDate
LocationSourceId
Name
OwnerId

```

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

**Properties**
Filter, Nillable, Sort

**Description**
The date the record was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location source ID.

This is a polymorphic relationship field.

**Relationship Name**
LocationSource

**Refers To**
Location, LocationGroup

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the shipping carrier service associated with the location or location group.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
ShippingCarrierMethodId

```

**Description**
ID of the user who currently owns this LocationShippingCarrierMethod object. Default value
is the user logged in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Shipping carrier method ID.

This is a relationship field.

**Relationship Name**
ShippingCarrierMethod

**Refers To**
Location, ShippingCarrierMethod

