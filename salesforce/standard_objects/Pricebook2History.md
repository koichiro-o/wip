#### Pricebook2History

Represents historical information about changes that have been made to the standard fields of the associated Pricebook2, or to any
custom fields with history tracking enabled. This object is available in API version 63.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

This object is always read-only.

##### Fields

```
Pricebook2Id

```

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
DataType
Field
IsDeleted
NewValue

```

**Description**
ID of the Pricebook2 associated with this record.

This is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

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
Name of the price book field that was modified, or a special value to indicate some other
modification to the price book.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
This is a standard system field. Label is Deleted.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the modified price book field. Maximum of 255 characters.


-----

```
 OldValue

##### Usage

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
Previous value of the modified price book field. Maximum of 255 characters.


Price book history entries are indirectly created each time a price book is modified.

Two rows are added to this record when foreign key fields change. One row contains the foreign key object names that display in the
online application. For example, `Jane Doe` is recorded as the name of a Contact. The other row contains the actual foreign key ID
that is only returned to and visible from the API.

This object respects field level security on the parent object.

SEE ALSO:

Pricebook2
