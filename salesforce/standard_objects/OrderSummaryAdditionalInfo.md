#### OrderSummaryAdditionalInfo

Stores information related to OrderSummary including context around the order, such as inventory reservation details, order origination,
and other values that Einstein uses to perform order analysis. Only reservation details can be stored in this object. This object is available
in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

##### Fields

```
AdjustmentsVersion

```

**Type**
text

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the adjustment algorithm that was used to create adjustments for this order


-----

```
CurrencyIsoCode
InventoryReservationExtRef
InventoryReservationIdentifier
InventoryReservationMessage
InventoryReservationState

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code for the currency of the OrderSummary associated with the
OrderSummaryAdditionalInfo.

Possible values are:

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Holds an external reference identifier for tracking the inventory reservation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Inventory reservation identifier for the order, if available. Since this value can come from
external systems, the value type has no lookup or enforcement.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Holds any details or other relevant information that can further explain the status of the
reservation.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the reservation, if available.


-----

```
Name
OrderId
OrderSummaryId

```

Possible values are:

**•** `DEFERRED`

**•** `NOT_APPLICABLE`

**•** `PERMANENT`

**•** `TEMPORARY`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderSummaryAdditionalInfo record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Unique ID of the order associated with this record.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID of the associated OrderSummary to which the specific OrderSummaryAdditionalInfo
applies.

This field is a relationship field.

**Relationship Name**
OrderSummary

**Relationship Type**
Lookup

**Refers To**
OrderSummary


-----

```
OwnerId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the ID of the user who
created the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderSummaryAdditionalInfoFeed on page 54**
Feed tracking is available for the object.

**OrderSummaryAdditionalInfoOwnerSharingRule on page 64**
Sharing rules are available for the object.

**OrderSummaryAdditionalInfoShare on page 66**
Sharing is available for the object.

SEE ALSO:

OrderSummary
