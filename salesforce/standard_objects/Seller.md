#### Seller

Represents the seller role of an individual with respect to a particular company or organization. This object is available in API version
53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ActiveFromDate
ActiveToDate
LastReferencedDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the seller’s role became active.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the seller’s role is no longer active.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
OwnerId
PartyId

```

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this seller.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this seller.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Represents the record based on the Individual object you want to associate the
seller with.

This is a relationship field.


-----

```
SalesAmount
SellerTier
SellerType

```

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total revenue amount gained from this seller.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The tier at which this seller is ranked.

Possible values are:

**•** `Bronze`

**•** `Gold`

**•** `Silver`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of sales this seller specializes in.

Possible values are:

**•** `Distributor`

**•** `Reseller`

**•** `SalesPartner`

**•** `Wholesaler`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SellerHistory on page 62**
History is available for tracked fields of the object.

**SellerShare on page 66**
Sharing is available for the object.
