#### OrderItemSummaryChange

Represents a change to an OrderItemSummary, usually a reduction in quantity due to a cancel or return. Corresponds to a change order
item. This object is available in API version 48.0 and later.

This object is used for calculations and doesn’t have a default record page.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs.

##### Fields

```
ChangeOrderItemId
ChangeType
CurrencyIsoCode

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated change order item.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of change represented by the OrderItemSummaryChange.

Possible values are:

**•** `Add` (available in API version 54.0 and later)

**•** `Cancel`

**•** `DeliveryChargeAdjustment`

**•** `ProductAdjustment`

**•** `Return`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
IsPreFulfillment
OrderItemSummary
ChangeNumber
OrderItemSummaryId
OrderSummaryId
Reason

```

**Description**
ISO code for the currency of the OrderSummary associated with the
OrderItemSummaryChange. The default value is USD.

Possible values are:

**•** `DKK—Danish Krone`

**•** `EUR—Euro`

**•** `GBP—British Pound`

**•** `USD—U.S. Dollar`

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the change occurs before the OrderItemSummary has been fulfilled.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the OrderItemSummaryChange.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderItemSummary to which the change applies.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary to which the associated OrderItemSummary belongs.

**Type**
picklist


-----

```
 ReasonText

##### Associated Objects

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reason for the change. You can customize this list.

The list has one default value:

**•** `Unknown`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Details about the reason for change.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderItemSummaryChangeChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

OrderItem

OrderItemSummary
