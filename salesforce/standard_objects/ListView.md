#### ListView

Represents a list view. A list view shows a set of records for an object, based on specific criteria. This object is available in API version 32.0
and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), search()

 Fields

```
```
DeveloperName
IsSoqlCompatible
LastModifiedById

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The fully qualified developer name of the list view.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the list view can be used with SOQL..

**Type**
User

**Properties**
Filter, Sort

**Description**
The ID of the user who last modified the list view.


-----

```
LastReferencedDate
LastViewedDate
Name
NamespacePrefix
SobjectType

##### Usage

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the list view was last referenced, with a precision of one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the list view was last viewed, with a precision of one second.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the list view.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the list view.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The API name of the sObject for the list view.


Use this object to retrieve the metadata for a pipeline inspection view.


-----
