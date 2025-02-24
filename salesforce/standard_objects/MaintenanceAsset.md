#### MaintenanceAsset

Represents an asset covered by a maintenance plan in field service. Assets can be associated with multiple maintenance plans.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

Field Service must be enabled.

##### Fields

**Field Name**
```
AssetId
ContractLineItemId
LastReferencedDate
LastViewedDate
MaintenanceAssetNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The asset associated with the maintenance asset.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contract line item associated with the maintenance asset. This field can only list
a contract line item that is associated with the asset, and whose parent service
contract is associated with the parent maintenance plan.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the maintenance asset was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort


-----

```
MaintenancePlanId
NextSuggestedMaintenanceDate
WorkTypeId

##### Associated Objects

```

**Description**
An auto-assigned number that identifies the maintenance asset.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Maintenance plan associated with the maintenance asset.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The suggested date of service for the maintenance asset’s first work order (not
the date the work order is created). This corresponds to the work order’s
```
  SuggestedMaintenanceDate. If left blank when the maintenance asset

```
is created, this field inherits its initial value from the related maintenance plan.

This field auto-updates after each batch is generated. Its label in the user interface
is Date of the first work order in the next batch.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Work type associated with the maintenance asset. Work orders generated from
the maintenance plan inherit its work type’s duration, required skills and products,
and linked articles. Maintenance assets covered by the plan use the same work
type, though you can update them to use a different one.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MaintenanceAssetChangeEvent (API version 48.0)**
Change events are available for the object.

**MaintenanceAssetFeed**

Feed tracking is available for the object.

**MaintenanceAssetHistory**

History is available for tracked fields of the object.


-----
