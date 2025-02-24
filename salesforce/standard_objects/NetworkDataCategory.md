#### NetworkDataCategory

Represents data categories in Lightning Web Runtime (LWR) Experience Cloud Sites. This object is available in API version 59.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
This object is available only when your org has Digital Experiences and Knowledge or Service Catalog enabled.

##### Fields

```
DataCategoryGroupName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
DataCategoryName
Description
ImageId
Label
NetworkId

```

**Description**
Name of the data category group that contains one or more data categories.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the data category.

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the data category.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Image associated with the data category.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ManagedContent

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the data category shown in the UI.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
ID of the associated Experience site.

This field is a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network
