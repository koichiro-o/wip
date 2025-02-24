#### IndividualHistory

Represents the history of changes to values in the fields of a data privacy record, based on the Individual object. This object is available
in versions 42.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

**•** This object is available if Data Protection and Privacy is enabled.

**•** The Individual object isn’t available to Customer Community, Partner Community, and Customer Portal users.

##### Fields

```
DataType
Field
IndividualId
NewValue

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
The name of the changed field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the data privacy record. Label is Individual ID.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
anyType

**Properties**
Nillable, Sort


-----

```
OldValue

##### Usage

```

**Description**
The updated value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.


Use this object to identify changes to data privacy records.

This object respects field-level security on the parent object.
