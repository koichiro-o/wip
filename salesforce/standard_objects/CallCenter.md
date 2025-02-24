#### CallCenter

Represents a call center, which is a logical representation of a single computer-telephony integration (CTI) system instance in an
organization.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
AdapterUrl
CustomSettings

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

An optional field that specifies the location of where the CTI adapter is hosted. For example,
```
  http://localhost:11000.

```
This field is available in API version 23.0 or later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**

Specifies settings in the call center definition file, such as whether the call center uses the
Open CTI, and SoftPhone properties, such as height in pixels.

This field is available for Open CTI and in API version 25.0 or later.


-----

```
Id
InternalName
Name
Version

##### Usage

```

**Type**
ID

**Properties**
Defaulted on create, Filter

**Description**
System field that uniquely identifies this call center. Label is Call Center ID. This ID is created
automatically when the call center is created.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**

The internal name of the call center.

Limit is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**

The name of the call center.

Limit is 80 characters.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The version of the CTI Toolkit used to create the call center (for versions 2.0 and later).

This field is available in API version 18.0 and later.


Create a call center or query an existing call center.
