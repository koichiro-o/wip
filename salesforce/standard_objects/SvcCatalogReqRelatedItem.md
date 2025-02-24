#### SvcCatalogReqRelatedItem

Represents an item related to a Service Catalog Request. This object is available in API version 53.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object, get the Service Catalog permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

##### Fields

```
Name
RelatedExternalId
RelatedInternalRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the related item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text containing an ID from any external system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Salesforce record related to this request. This reference must be for an object that has
the following characteristics.

**•** It's a standard object.

**•** It must allow custom fields.

**•** It's referencable (that is, it can be the target of a lookup).

**•** It can be the target of a custom lookup field.

**•** It contains a Name field.

**•** It isn't dependent on a junction object.

**•** It isn't a virtual object or a setup object.

This is a polymorphic relationship field.


-----

```
SvcCatalogRequestId
