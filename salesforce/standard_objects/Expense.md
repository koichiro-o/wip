#### Expense

Represents an expense linked to a work order. Service resource technicians can log expenses, such as tools or travel costs. This object is
available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AccountId
Amount
CurrencyIsoCode
Description
Discount
ExpenseEndDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the account associated with the linked work order.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The amount of the expense.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only if the multicurrency feature is enabled. Contains the ISO code for any currency
allowed by the organization.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description for the expense.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage deducted from the `Subtotal` price. Available in version 51.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ExpenseNumber
ExpenseStartDate
ExpenseType
LastReferencedDate
LastViewedDate

```

**Description**
If the expense was incurred over multiple days, the Expense End Date is the last day that the
expense covers.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The number that uniquely identifies the expense.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the expense was incurred over multiple days, the Expense Start Date is the first day that
the expense covers.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of expense. Possible values are:

**•** `Billable`

**•** `Non-Billable`

The default value is `Billable.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
OwnerId
Quantity
Subtotal
Title
TotalPrice

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the expense record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of items purchased in this record. Available in version 51.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The subtotal price calculated as the product of `Quantity` and `UnitPrice. Available`
in version 51.0 and later.

This is a calculated field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A title that identifies the expense.

This field is available in API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TransactionDate
UnitPrice
WorkOrderId

##### Associated Objects

```

**Description**
The total price of the transaction which is equal to the discounted subtotal: `Subtotal`   (Discount  - `Subtotal). Available in version 51.0 and later.`

This is a calculated field.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The day that the expense was incurred, or the payment date for the expense.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The price of one item on the record. Available in version 51.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work order associated with the expense.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ExpenseChangeEvent (API version 55.0)**
Change events are available for the object.

**ExpenseFeed**

Feed tracking is available for the object.

**ExpenseHistory**

History is available for tracked fields of the object.

**ExpenseOwnerSharingRule**

Sharing rules are available for the object.

**ExpenseShare**

Sharing is available for the object.


-----
