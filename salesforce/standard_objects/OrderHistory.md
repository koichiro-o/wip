#### OrderHistory

Represents historical information about changes that have been made to the standard fields of the associated order, or to any custom
fields with history tracking enabled.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Fields

```
DataType
Field

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Name of the order field that was modified, or a special value to indicate some
other modification to the order.


-----

```
NewValue
OldValue
OrderId

##### Usage

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the modified order field. Maximum of 255 characters.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
Previous value of the modified order field. Maximum of 255 characters.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the order associated with this record.

This is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order


Order history entries are automatically created each time an order is modified.

Two rows are added to this record when foreign key fields change. One row contains the foreign key object names that display in the
online application. For example, `Jane Doe` is recorded as the name of a Contact. The other row contains the actual foreign key ID
that is only returned to and visible from the API.

This object respects field-level security on the parent object.

SEE ALSO:

Order


-----
