#### DuplicateJobDefinition

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of records scanned as a result of invoking a duplicate job.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
List view metadata for displaying the duplicate record sets identified as result of
invoking a duplicate job.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time when a duplicate job was invoked.


Setup object defining a job that identifies duplicate record items globally.

This object is available in API versions 42.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.


-----

##### Fields

**Field Name**
```
DeveloperName
Language
MasterLabel
SobjectSubtype
SobjectType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the user who created a duplicate job.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language in the user’s personal settings.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the duplicate job.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The object subtype. Valid values are `Person Account` or `None.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object type: account, contact, or lead.


-----
