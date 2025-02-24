#### ShapeRepresentation

Contains information about the shape of an org. The shape of an org includes licenses and limits information. You can easily create
scratch orgs based on a source org’s shape. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A free-form text field for you to enter a description of this org shape. This field has a maximum
length of 255 characters.


-----

```
LastReferencedDate
LastViewedDate
Name
Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the org shape was last referenced. This field is read-only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the org shape was last viewed. This field is read-only.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The alias for the org shape.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Status of this org shape. You can use an org shape when it’s Active. This field is read-only.

Possible values are:

**•** `Active`

**•** `Error`

**•** `InProgress`

**•** `Inactive`

**•** `New`

