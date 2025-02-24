#### PartnerMarketingBudget

Represents a budget that provides funds to channel partners for selling and marketing products and services. This object is available in
API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Fields

```
```
Amount
ChannelPartnerId
Description

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Total amount of the budget.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the channel partner. This field is available in API version 45.0 and later.

**Type**
textarea


-----

```
EndDate
IsIgnoreValidation
LastReferencedDate
LastViewedDate
OwnerId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the budget.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the budget is no longer available.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When enabled, ignores restrictions related to the child objects connected to the
budget. Note that individual totals for allocation amounts, request amounts, and
claims amounts cannot exceed the total of their parent budget. Field is default
off (false) on create. Once enabled (true), this field cannot be disabled. This field
is available in API version 44.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
reference


-----

```
StartDate
Title
TotalAllocatedAmount
TotalApprovedFcs
TotalApprovedFrs
TotalReimbursedFcs

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the budget.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the budget becomes available.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Title of the budget.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total funds allocated to channel partners or as a fund pool.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of approved fund claims.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of approved fund requests.

**Type**
currency


-----

```
Type

##### Associated Objects

```

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of reimbursed fund claims.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of budget. Values are:

**•** `Co-Operated Budget—Funds accrue based on a percentage of partner`
sales. The funds are available based on previous activity.

**•** `Marketing Funds—Funds are issued to partners in advance of sales.`
The funds are awarded based on predicted or expected behavior.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**PartnerMarketingBudgetFeed**

Feed tracking is available for the object.

**PartnerMarketingBudgetHistory**

History is available for tracked fields of the object.

**PartnerMarketingBudgetOwnerSharingRule**

Sharing rules are available for the object.

**PartnerMarketingBudgetShare**

Sharing is available for the object.
