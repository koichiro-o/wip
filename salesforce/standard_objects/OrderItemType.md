#### OrderItemType

Shows whether the order product is a product line or charge line. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ApiName
IsDefault

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean


-----

```
MasterLabel
SortOrder
TypeCode

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default order item type status value (true) or not (false)
in the picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this order item type status value. This display value is the internal label that
doesn’t get translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the order item status picklist. These numbers aren’t
guaranteed to be sequential, as some previous contract status values might have been
deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Code indicating the type of order item.

Possible values are:

**•** `Charge—API Name DeliveryCharge.`

**•** `Product—For API Name Product.`

