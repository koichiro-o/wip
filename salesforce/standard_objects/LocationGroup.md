#### LocationGroup

Represents a group of Omnichannel Inventory locations, providing an aggregate view of inventory availability across those locations.
Omnichannel Inventory can create an inventory reservation for an order at the location group level, then assign the reservation to one
or more locations in the group as needed. This object is available in API version 51.0 and later.

You can define location groups according to the logic of your business needs. For example, a location group can represent the warehouses
in a geographic region, or it can include the fulfillment centers associated with a particular online storefront.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Omnichannel Inventory orgs.

##### Fields

```
Description
ExternalReference
IsEnabled
LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the location group.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used when OCI is integrated with B2C Commerce to associate the location group with an
inventory list in B2C Commerce. This value must match the inventory list ID in B2C Commerce.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the location group is in use. If set to `false, then inventory functions`
ignore this location group and its data isn’t synchronized with OCI. The default value is true.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


-----

```
LastViewedDate
LocationGroupName
OwnerId
ShouldSyncWithOci

##### Associated Objects

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the location group.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this location group. Default value is the API user that
created the record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether to synchronize inventory data for this location group with Omnichannel
Inventory. The default value is `true.`


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LocationGroupChangeEvent (API version 62.0)**
Change events are available for the object.

**LocationGroupFeed**

Feed tracking is available for the object.

**LocationGroupHistory**

History is available for tracked fields of the object.


-----

**LocationGroupOwnerSharingRule**

Sharing rules are available for the object.

**LocationGroupShare**

Sharing is available for the object.

SEE ALSO:

Location

LocationGroupAssignment

_[B2B Commerce and D2C Commerce Developer Guide: Inventory Data Model](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/b2b-b2c-comm-data-model-inventory.html)_
