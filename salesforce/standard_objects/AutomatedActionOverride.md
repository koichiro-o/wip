#### AutomatedActionOverride

Represents a modified attribute of a shared automated action. For example, the modified attribute can contain customizations for your
business. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Fields

```
```
FieldName
IsLocked

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the field to override.

**Type**
boolean


-----

```
IsRelatedRecordOverridable
MayEdit
Name
RelatedRecordApiName
RelatedRecordId

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action override record is locked or not.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the parent automated action record can be overridden.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action override record can be edited or not.

The default value is `false.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the automated action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The object name of the `RelatedRecordId.`

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
Value

##### Associated Objects

```

**Description**
ID of the automated action.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
AutomatedAction, FtestUser

**Type**
textarea

**Properties**
Create, Update

**Description**
The overridden value used for `FieldName.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AutomatedActionOverrideOwnerSharingRule on page 64**
Sharing rules are available for the object.

**AutomatedActionOverrideShare on page 66**
Sharing is available for the object.
