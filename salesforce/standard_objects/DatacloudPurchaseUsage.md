#### DatacloudPurchaseUsage

Represents an object used to identify and track Data.com record purchases. This object is available in API version 30.0 or later.


-----

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
DatacloudEntityType
Description
Name
PurchaseType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The type of Data.com record you want to purchase.

**•** 0—indicates contact entity type.

**•** 1—indicates company entity type.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

An optional field. You can add a description for your purchase.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**

An optional field used to name your record.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


-----

```
Usage
UserId
UserType

##### Usage

```

**Description**

A read only field set by the API to identify the purchase type.

**•** Added

**•** Export

**•** API

**Type**
double

**Properties**
Filter, Sort

**Description**

A read only field set by the API. It is used to track the points used to purchase
records.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

A read only field set by the API that identifies the user purchasing the records.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

A read only field set by the API with 2 user types.

**•** Monthly Usage

**•** List Pool User


The DatacloudPurchaseUsage object allows you to track Data.com record purchases for CRM users.


-----
