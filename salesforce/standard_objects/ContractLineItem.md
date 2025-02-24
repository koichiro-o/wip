#### ContractLineItem


**Type**
picklist

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Name of the role played by the Contact on this Contract, such as Decision Maker, Approver,
Buyer, and so on. Must be unique—there can't be multiple records in which the
`ContractId, ContactId, and Role` values are identical. Different contacts can play
the same role on the same contract. A contact can play different roles on the same contract.


Represents a product covered by a service contract (customer support agreement). This object is available in API version 18.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AssetId
Description

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the Asset associated with the contract line item. Must be a valid asset ID.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the contract line item.


-----

```
Discount
EndDate
LastReferencedDate
LastViewedDate
LineItemNumber

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Update

**Description**
The discount for the product as a percentage.

When updating, if you specify Discount without specifying TotalPrice, the
`TotalPrice` will be adjusted to accommodate the new `Discount` value, and the
`UnitPrice` will be held constant.

If you specify both `Discount` and Quantity, you must also specify either
`TotalPrice` or UnitPrice so the system can determine which one to automatically
adjust.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The last day the contract line item is in effect.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Update


-----

```
ListPrice
LocationId
ParentContractLineItemId
PricebookEntryId
Product2Id

```

**Description**
Automatically-generated number that identifies the contract line item.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Corresponds to the `UnitPrice` on the PricebookEntry that is associated with this line
item, which can be in the standard pricebook or a custom pricebook. A client application
can use this information to show whether the unit price (or sales price) of the line item differs
from the pricebook entry list price.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location associated with the contract line item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The line item’s parent line item, if it has one.

**Type**
reference

**Properties**
Create, Filter, Update

**Description**
Required. ID of the associated PricebookEntry.

Only exists if Product2 is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product related to the contract line item.


-----

```
Quantity
RootContractLineItemId
ServiceContractId
StartDate
Status
Subtotal

```

**Type**
double

**Properties**
Create, Filter, Update

**Description**
Number of units of the contract line item (product) included in the associated service contract.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level line item in a contract line item hierarchy. Depending on where a
line item lies in the hierarchy, its root could be the same as its parent.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the ServiceContract associated with the contract line item. Must be a valid
service contract ID.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The first day the contract line item is in effect.

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Status of the contract line item.

**Type**
currency

**Properties**
Filter, Nillable


-----

```
TotalPrice
UnitPrice

##### Associated Objects

```

**Description**
Contract line item's sales price multiplied by the Quantity.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
This field is available only for backward compatibility. It represents the total price of the
ContractLineItem

If you specify `Discount` and Quantity, this field or UnitPrice is required.

This field is nillable, but you can't set both TotalPrice and UnitPrice to null in the
same update request. To insert the TotalPrice for a contract line item via the API (given
only a unit price and the quantity), calculate this field as the unit price multiplied by the
quantity.

**Type**
currency

**Properties**
Create, Filter, Update

**Description**
The unit price for the contract line item. In the user interface, this field’s value is calculated
by dividing the total price of the contract line item by the quantity listed for that line item.
Label is Sales Price.

This field or `TotalPrice` is required. You can’t specify both.

If you specify `Discount` and Quantity, this field or TotalPrice is required.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineItemChangeEvent (API version 44.0)**
Change events are available for the object.

**ContractLineItemFeed**

Feed tracking is available for the object.

**ContractLineItemHistory**

History is available for tracked fields of the object.


-----
