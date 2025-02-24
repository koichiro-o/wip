#### ChangeRequestRelatedItem

Represents a junction object that relates a ChangeRequest to an Asset. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Asset ID that’s linked to the ChangeRequest.

This field is a relationship field.

**Relationship Name**
Asset


-----

```
ChangeRequestId
Comment
ImpactLevel
Name

```

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ChangeRequest ID that’s linked to the Asset.

This field is a relationship field.

**Relationship Name**
ChangeRequest

**Relationship Type**
Lookup

**Refers To**
ChangeRequest

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the change request as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The related item's impact on the change request.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `High.`

**Type**
string


-----

```
RelationshipType

##### Associated Objects

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the item that's related to the change request.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how the ChangeRequest and Asset records relate to each other.

Possible values are:

**•** `Broke Item`

**•** `Fixed Item`

The default value is `Broke Item.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestRelatedItemChangeEvent on page 67**
Change events are available for the object.

**ChangeRequestRelatedItemFeed on page 54**
Feed tracking is available for the object.

**ChangeRequestRelatedItemHistory on page 62**
History is available for tracked fields of the object.
