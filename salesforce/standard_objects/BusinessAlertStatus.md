#### BusinessAlertStatus

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the alert record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The previous designation that's related to the job alert.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the previous employer that's related to the job alert.


Represents information about the read status of an insight alert. This object is available in API version 57.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The BusinessAlertStatus object is available only if the ERI Growth User or ERI Starter User license is enabled.

##### Fields

```
BusinessAlertId
IsAlertRead
Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The insight alert related to the status.

This field is a relationship field.

**Relationship Name**
BusinessAlert

**Relationship Type**
Lookup

**Refers To**
BusinessAlert

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the insight alert is read by the user (true) or not (false).

The default value is `false.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Specifies the activation status of the insight alert.


-----

```
UserId
