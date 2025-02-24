#### WarrantyTerm

Represents warranty terms defining the labor, parts, and expenses covered, along with any exchange options, provided to rectify issues
with products. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Code
Description
EffectiveStartDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A code or other identifier associated with this warranty term.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the warranty term.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date on which the warranty term became available for use.

Possible values are:

**•** `InstallDate`

**•** `ManufactureDate`


-----

```
ExchangeType
Exclusions
ExpensesCovered
ExpensesCoveredDuration
ExpensesCoveredUnitOfTime

```


**•** `PurchaseDate`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of exchange offered.

Possible values are:

**•** `AdvanceExchange`

**•** `Loaner`

**•** `ReturnExchange`

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
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The duration for which expenses are covered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit in which expenses covered duration is measured.

Possible values are:


-----

```
IsActive
IsTransferable
LaborCovered
LaborCoveredDuration
LaborCoveredUnitOfTime

```


**•** `Days`

**•** `Months`

**•** `Weeks`

**•** `Years`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether the warranty term is active.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether the warranty can be transferred to a new owner.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of labor covered.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The duration for which labor is covered.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit in which labor covered duration is measured.

Possible values are:

**•** `Days`


-----

```
LastReferencedDate
LastViewedDate
OwnerId
PartsCovered
PartsCoveredDuration
PartsCoveredUnitOfTime

```


**•** `Months`

**•** `Weeks`

**•** `Years`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the warranty term was last modified. Its label in the user interface is `Last`
```
  Modified Date.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the warranty term was last viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The warranty term’s assigned owner.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of parts covered.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The duration for which parts are covered.

**Type**
picklist


-----

```
Pricebook2Id
WarrantyDuration
WarrantyTermName
WarrantyType

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit in which parts covered duration is measured.

Possible values are:

**•** `Days`

**•** `Months`

**•** `Weeks`

**•** `Years`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the price book item associated with this warranty term.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The duration of the warranty offered by this term.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the warranty term.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The type of warranty.

Possible values are:

**•** `Repair`

**•** `Standard`


-----

```
WarrantyUnitOfTime

##### Associated Objects

```


**•** `Supplier`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit in which the warranty duration is measured.

Possible values are:

**•** `Days`

**•** `Months`

**•** `Weeks`

**•** `Years`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**WarrantyTermChangeEvent**

Change events are available for the object.
