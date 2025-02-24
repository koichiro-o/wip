#### AssetWarranty

Defines the warranty terms applicable to an asset along with any exclusions and extensions. This object is available in API version 50.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AssetId
AssetWarrantyNumber
EndDate
ExchangeType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the asset this warranty term applies to.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The identifier of the asset warranty record.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which this warranty term expires.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of exchange offered by this warranty term.


-----

```
Exclusions
ExpensesCovered
ExpensesCoveredEndDate
IsTransferable
LaborCovered
LaborCoveredEndDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of any exclusions.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of expenses covered.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for expenses ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether the warranty term can be transferred to a new owner.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of labor covered.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for labor ends.


-----

```
LastReferencedDate
LastViewedDate
PartsCovered
PartsCoveredEndDate
Pricebook2Id
StartDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the asset warranty term was last modified. Its label in the user interface is
```
  Last Modified Date.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the asset warranty term was last viewed.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of parts covered.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which cover for parts ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the price book item associated with this asset warranty term.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update


-----

```
WarrantyTermId
WarrantyType

##### Associated Objects

```

**Description**
The date on which cover under this warranty term starts.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the warranty term this asset warranty term extends.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of the warranty.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetWarrantyChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.
