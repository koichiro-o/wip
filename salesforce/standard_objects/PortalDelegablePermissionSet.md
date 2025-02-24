#### PortalDelegablePermissionSet

PortalDelegablePermissionSet is a base platform object used to store permission sets that can be assigned by a delegated portal/external
user admin (DPUA) to portal users. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
DeveloperName

```

**Type**
string


-----

```
Language
MasterLabel
PermissionSetId
ProfileId

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique string used to identify the record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used in the org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique string to identify the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the permission set the DPUA profile can assign to other portal users.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the DPUA profile.

