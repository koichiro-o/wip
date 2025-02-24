#### ActivityFieldHistory

Represents a change in a field value for a tracked object or field. This object is a big object. This object is available in API version 55.0 and
later.

##### Supported Calls
```
delete()describeSObjects(), query(), retrieve()

 Special Access Rules

```
To see this object, users must have ViewAllData permissions.

##### Fields

```
ActivityId

```

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the task or event that changed.

This field is a polymorphic relationship field.

**Relationship Name**
Activity

**Refers To**
Event, Task


-----

```
ChangedById
ChangedDate
DataType

```

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the user who made the change.

This field is a relationship field.

**Relationship Name**
ChangedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the field value changed.

**Type**
picklist

**Properties**
Restricted picklist

**Description**
The type of the field with the changed value.

Possible values are:

**•** `Address`

**•** `AnyType`

**•** `AutoNumber`

**•** `Base64`

**•** `BitVector`

**•** `Boolean`

**•** `Content`

**•** `Currency`

**•** `DataCategoryGroupReference`

**•** `DateOnly`

**•** `DateTime`

**•** `Division`

**•** `Double`


-----

```
FieldName

```


**•** `DynamicEnum`

**•** `Email`

**•** `EncryptedBase64`

**•** `EncryptedText`

**•** `EntityId`

**•** `EnumOrId`

**•** `ExternalId`

**•** `Fax`

**•** `File`

**•** `HtmlMultiLineText`

**•** `HtmlStringPlusClob`

**•** `InetAddress`

**•** `Json`

**•** `Location`

**•** `MultiEnum`

**•** `MultiLineText`

**•** `Namespace`

**•** `Percent`

**•** `PersonName`

**•** `Phone`

**•** `Raw`

**•** `RecordType`

**•** `SfdcEncryptedText`

**•** `SimpleNamespace`

**•** `StringPlusClob`

**•** `Switchable_PersonName`

**•** `Text`

**•** `TimeOnly`

**•** `Url`

**•** `YearQuarter`

**Type**
string

**Properties**
Filter, Sort

**Description**
The name of the field changed.


-----

```
IsDataAvailable
NewValueDateTime
NewValueNumber
NewValueText
OldValueDateTime
OldValueNumber

```

**Type**
boolean

**Properties**
Defaulted on create

**Description**
Indicates whether valid data is available in the old and new value fields. This field is `false`
if, for example, the fields are encrypted or the changed values are too large, such as for
Description field types.

The default value is `false.`

**Type**
dateTime

**Properties**
Nillable

**Description**
The new value for date type fields.

**Type**
double

**Properties**
Nillable

**Description**
The new value for number type fields.

**Type**
string

**Properties**
Nillable

**Description**
The new value for all other field types that are not a date or number type.

**Type**
dateTime

**Properties**
Nillable

**Description**
Old value for date type fields.

**Type**
double


-----

```
OldValueText
Operation

##### Indexed Fields

```

**Properties**
Nillable

**Description**
Old value for number type fields.

**Type**
string

**Properties**
Nillable

**Description**
The old value for all other field types that are not a date or number type.

**Type**
picklist

**Properties**
Restricted picklist

**Description**
The operation of the field value change.

Possible values are:

**•** `delete`

**•** `update`


When you're querying ActivityFieldHistory with SOQL, you must specify indexed fields in the `WHERE` clause filter starting from the first
field defined in the index. If you specify a partial list of indexed fields, don't leave any gaps between indexed fields after the first field.
Here are the indexed fields for ActivityFieldHistory, listed from first to last in the index order.

1. `ActivityId`

2. `ChangedDate`

3. `ChangedById`

4. `FieldName`

5. `ActivityFieldChange`

For example, this SOQL query succeeds because the first three indexed fields are in the `WHERE` clause.


-----

If you remove the `ActivityId` field from the `WHERE` clause, the query fails.
```
SELECT ActivityId, OldValueText, NewValueText, FieldName, ChangedDate
FROM ActivityFieldHistory
WHERE ChangedDate >= :startDate AND ChangedDate <= :endDate
ORDER BY ChangedDate

```
SEE ALSO:

[Big Objects Implementation Guide: SOQL with Big Objects](https://developer.salesforce.com/docs/atlas.en-us.254.0.bigobjects.meta/bigobjects/big_object_querying.htm)

[Big Objects Implementation Guide: Big Objects](https://developer.salesforce.com/docs/atlas.en-us.254.0.bigobjects.meta/bigobjects/big_object.htm)
