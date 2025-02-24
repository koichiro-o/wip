#### SvcCatalogItemDef

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of catalog items that has the eligibility rule.


Represents a service catalog item that can be requested by a service catalog user. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), search(),
update(), upsert()

 Special Access Rules

```
To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

##### Fields

```
Description
DeveloperName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The definition of the catalog item. This field is visible on the Service Catalog page.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
FlowName
FulfillmentFlowId
ImageId
ImageReference

```

**Description**
The unique developer name for the catalog item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow called when the user navigates to the request page for the catalog item. Available
in API version 55.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the fulfillment flow. Available in API version 56.0 and later.

This field is a relationship field.

**Relationship Name**
FulfillmentFlow

**Relationship Type**
Lookup

**Refers To**
SvcCatalogFulfillmentFlow

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The image ID used for the catalog item.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
string


-----

```
InternalNotes
IsActive
IsAvailableToAllCustomers
IsFeatured

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Derived field from ImageId to expose ContentAssetId on item definitions. Available
in API version 61.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A place for the Service Catalog Builder to leave internal notes about the catalog item.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived field from `Status` to indicate whether the service catalog item is active.

The default value is `false.`

Available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Udpate

**Description**
Indicates whether the Service Catalog item is available to all customers. The default value is
```
  false.

```
Available in API version 61.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a catalog item is marked as a favorite for the org. Favorites display as a
featured item on the Service Catalog home page.

The default value is `false.`


-----

```
IsGuestAccessible
IsOutOfSync
Language
Product
Status

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Service Catalog item can be accessed by guest users. The default value
is `false.`

Available in API version 61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the fulfillment flow that the Service Catalog item is based on has been
updated. Available in API version 58.0 and later.

The default value is `false. If value is` `true, try updating and saving the service catalog`
item again.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Supported languages for catalog items.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The product associated with the Service Catalog item. The value is derived from UsageType.
Available in API version 59.0 and later.

Possible values are:

**•** `FinancialServices`

**•** `ServiceCatalog—Default`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


-----

```
UsageType
