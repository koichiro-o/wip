#### DatacloudOwnedEntity

Represents fields in the DatacloudOwnedEntity object. The DatacloudOwnedEntity object tracks user-purchased records. This object is
available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
DataDotComKey
DatacloudEntityType
Name

```

**Type**
string

**Properties**
Create, Filter, Sort

**Description**

The Data.com contact or company record identification number used by the
DatacloudPurchaseUsage object to keep track of purchased records. This is
equivalent to the Data.com record ID for a contact or company.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Sort

**Description**

The type of Data.com record you want to purchase.

**•** 0—contact

**•** 1—company

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort


-----

```
PurchaseType
PurchaseUsageId
UserId

##### Usage

```

**Description**

An optional field used to name your record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

A read only field set by the API to identify the purchase type.

**•** Added

**•** Export

**•** API

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The unique identification number for the DatacloudPurchaseUsage object created
by making a REST POST request.

**•** 0—contact

**•** 1—company

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

A unique identifier for the user making the purchase.


The Datacloud object that tracks records that are purchased and owned by a specific user.
