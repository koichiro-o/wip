#### LiveChatObjectAccessConfig

Represents the action you can perform on a specified object by the Chat API. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, enable Chat. To see the list of objects you can find or create in the UI using this API, enable the "Turns on findOrCreate
in chat API" permission. You can find this permission in the Chat Settings page of the Setup UI.

##### Fields

```
AccessType
ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The API action you can perform on the object specified in `SobjectType.`

Possible values are:

**•** `Create`

**•** `Find`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated LiveChatObjectAccessDefinition record.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup


-----

```
SobjectType

```
SEE ALSO:

LiveChatObjectAccessDefinition


**Refers To**
LiveChatObjectAccessDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The object that the action specified by `AccessType` applies to.

Possible values are all standard and custom objects. Custom objects are available as picklist
values in API version 55.0 and later.

