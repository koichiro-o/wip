#### SiteHistory

Represents the history of changes to the values in the fields of a site. This object is generally available in API version 18.0 and later.

To access this object, Salesforce Sites must be enabled for your organization.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

**•** Customer Portal users can't access this object.

**•** To view this object, you must have the “View Setup and Configuration” permission.


-----

##### Fields

**Field**
```
DataType
Field
NewValue
OldValue
SiteId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The last value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Site.

This is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup


-----

**Refers To**
Site
