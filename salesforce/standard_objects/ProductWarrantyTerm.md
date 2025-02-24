#### ProductWarrantyTerm

Defines the relationship between a product or product family and warranty term. This object is available in API version 50.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CoveredProductFamily
CoveredProductId
LastReferencedDate
LastViewedDate
ProductWarrantyTermNumber

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product family that the warranty term applies to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product that the warranty term applies to.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product warranty term was last modified. Its label in the user interface
is `Last Modified Date.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product warranty term was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The identifier for this product warranty term.


-----

```
WarrantyTermId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the warranty term.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ProductWarrantyTermChangeEvent (API version 62.0)**
Change events are available for the object.
