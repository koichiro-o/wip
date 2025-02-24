#### DataMaskCustomValueLibrary

Represents a set of user-inputted values in a custom library in Data Mask. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with the Sandbox Data Mask managed package.

##### Fields

```
ContentType
Description
IsActive
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of value used in a field of the custom library.

Possible values are:

**•** `string`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the value in the custom library.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents whether the library is active or inactive for use.

The default value is `false.`

**Type**
dateTime


-----

```
LastViewedDate
Name
OwnerId
Type

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom library.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the custom library.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents how the values were added to the library.

Possible values are:

**•** `default`

**•** `user_defined`


-----

```
Values

##### Associated Objects

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The content of the value field for masking data.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**DataMaskCustomValueLibraryOwnerSharingRule on page 64**
Sharing rules are available for the object.

**DataMaskCustomValueLibraryShare on page 66**
Sharing is available for the object.
