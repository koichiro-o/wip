#### AutomatedActionParameter

Represents the values or field references evaluated by the automated action. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AutomatedActionId
DataType
IsLocked
MayEdit

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the automated action.

This field is a relationship field.

**Relationship Name**
AutomatedAction

**Relationship Type**
Lookup

**Refers To**
AutomatedAction

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of the value or field reference value.

Possible values are:

**•** `Boolean`

**•** `Double`

**•** `Int`

**•** `None`

**•** `String`

**•** `ValueList`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action parameter record is locked or not.

The default value is `false.`

**Type**
boolean


-----

```
ParameterName
ReferenceField
Value

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action parameter record can be edited or not.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the invocable action parameter the value maps to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reference to the field that’s resolved at runtime. For example, LeadID. If `Value` has a
value, this field is null.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value to be passed to the invocable action parameter at runtime. If ReferenceField
has a value, this field is null.

