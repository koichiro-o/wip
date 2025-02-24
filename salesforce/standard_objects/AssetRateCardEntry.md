#### AssetRateCardEntry

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the asset rate adjustment.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The maximum quantity for the adjustment to be applicable.


Stores the negotiated rate card entries that are associated with an asset in Revenue Cloud. This object is available in API version 62.0 and
later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available in orgs where Revenue Cloud is enabled.

##### Fields

```
AssetId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the asset rate card entry record.

This field is a relationship field.


-----

```
EndDate
Name
NegotiatedRate
RateCardEntryId

```

**Relationship Name**
Asset

**Relationship Type**
Master-detail

**Refers To**
Asset (the master object)

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the rate card's time period becomes inactive. The rate card becomes inactive
at 11:59:00 PM on the end date.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number assigned to the asset rate card entry. Read-only.

**Type**
double

**Properties**
Filter, Sort

**Description**
The base negotiated rate used to charge overage consumption.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the rate card entry record containing the catalog rates that's associated with the
asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateCardEntry

**Refers To**
RateCardEntry


-----

```
RateCardId
RateUnitOfMeasureId
StartDate
UsageResourceId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the rate card record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateCard

**Refers To**
RateCard

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the unit of measure record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
RateUnitOfMeasure

**Refers To**
UnitOfMeasure

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date when the rate card's time period becomes active. The rate card becomes active at
12:00:00 AM on the start date.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the usage resource record that's associated with the asset rate card entry.

This field is a relationship field.

**Relationship Name**
UsageResource


-----

**Refers To**
UsageResource
