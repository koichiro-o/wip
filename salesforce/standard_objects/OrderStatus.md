#### OrderStatus

Represents the status of the order entity. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ApiName
IsDefault
MasterLabel
SortOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default order status value `(true)` or not `(false)` in the
picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this order status value. This display value is the internal label that doesn’t
get translated.

**Type**
int


-----

```
StatusCode

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the order status picklist. These numbers aren’t guaranteed
to be sequential, as some previous contract status values might have been deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the order.

Possible values are:

**•** `Activated`

**•** `Draft`


This object represents a value in the order status picklist. The order status picklist provides additional information about the status of an
Order, such as its current state (Draft or `Activated). You can query these records to retrieve the set of values in the order status`
picklist, and then use that information while processing Order objects to determine more information about a given order. For example,
the application could test whether a given order is activated based on its Status value and the value of the StatusCode property in the
associated OrderStatus object.
