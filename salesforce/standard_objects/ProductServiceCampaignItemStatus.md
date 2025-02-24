#### ProductServiceCampaignItemStatus

Represents a status for a product service campaign item in field service. This object is available in API version 51.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
ApiName
IsDefault
MasterLabel
SortOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the status value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the status value is the default status on product service campaign items when
```
  true. Only one status value can be the default.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the picklist value in the UI.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
StatusCode

##### Usage

```

**Description**
The value’s position in the dropdown list in the UI.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status category that the value corresponds to. The Status Category field has seven values
that are identical to the default Status values.


The Status field on product service campaign items comes with the following values:

**•** New—Product service campaign item created, but there hasn’t been any activity.

**•** In Progress—Work has begun.

**•** On Hold—Work is paused.

**•** Completed—Work is complete.

**•** Cannot Complete—Work couldn’t be completed.

**•** Closed—All work and associated activity is complete.

**•** Canceled—Work is canceled, typically before any work began.

The ProductServiceCampaignItemStatus object corresponds to the Status field. Adding a value to the Status field—for example, Canceled
By Supplier—creates a product service campaign item status record, and vice versa.

Note: Product service campaign items also come with a Status Category field whose values are identical to the default status
values. If you create custom status values, you must indicate which category it belongs to. For example, if you create a Customer

`Absent` value, add it to the `Cannot Complete` [category. To learn which processes reference StatusCategory, see How are](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
[Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)
