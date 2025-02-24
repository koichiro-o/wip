#### PartnerFundAllocation

Represents allocated funds from a partner marketing budget for channel partners. This object is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
Amount
BudgetId
ChannelPartnerId
Description
LastReferencedDate
LastViewedDate

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Total amount of the allocation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the partner marketing budget.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the channel partner.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the allocation.

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


-----

```
OwnerId
Title
TotalApprovedFcs
TotalApprovedFrs
TotalReimbursedFcs

```

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the allocation.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The title of the allocation.

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

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of reimbursed fund claims.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**PartnerFundAllocationFeed**

Feed tracking is available for the object.

**PartnerFundAllocationHistory**

History is available for tracked fields of the object.

**PartnerFundAllocationOwnerSharingRule**

Sharing rules are available for the object.

**PartnerFundAllocationShare**

Sharing is available for the object.
