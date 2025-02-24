#### InvoiceAddressGroup

Stores the buyer's address information. This object is available in API version 50.0 and later.


-----

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), undelete()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

##### Fields

```
Address
City
Country
GeocodeAccuracy

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Buyer's address. Compound field that summarizes the invoice address group's address
component fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's city.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's country.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The accuracy rating for the geocode of the address group. The accuracy rating contains
information about the location of a latitude and longitude.


-----

```
InvoiceAddressGroupNumber
InvoiceId
Latitude
Longitude
PostalCode

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number, such as DOC-000001.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the invoice associated with the address group.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The buyer's latitude.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The buyer's longitude.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's postal code or ZIP code.


-----

```
State
Street

##### Associated Objects

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's state.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer's street.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**InvoiceAddressGroupHistory on page 62**
History is available for tracked fields of the object.
