#### ShippingCarrier

Shipping company or carrier responsible for transporting goods or packages. Examples include UPS, FedEx, and USPS. This object is
available in API version 61.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The ShippingCarrier object is available only if the B2B Commerce or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
ExternalReference
LastReferencedDate
LastViewedDate
Name
OwnerId

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

**Properties**
Filter, Nillable, Sort

**Description**
The date the record was last viewed.

**Type**
text

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the shipping carrier associated with the delivery.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this ShippingCarrier object. Default value is the user logged
in to the API to perform the create.

This is a polymorphic relationship field.


-----

**Relationship Name**
Owner

**Refers To**
Group, User
