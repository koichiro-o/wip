#### PartnerFundClaim

Represents a claim of funds from the partner marketing budget by a channel partner. This object is available in API version 41.0 and later.

##### Supported Calls
```
create()delete()describeLayout()describeSObjects()getDeleted()getUpdated()query()retrieve()
search()update(), upsert()

 Fields

```
```
AllocationId
Amount
BudgetId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the partner fund allocation.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Amount of the claim.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
ChannelPartnerId
Description
LastReferencedDate
LastViewedDate
OwnerId

```

**Description**
ID of the partner marketing budget.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the channel partner.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the fund claim.

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

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the fund claim.


-----

```
RequestId
Status
Title

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the partner fund request.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable Restricted picklist, Sort, Update

**Description**
Status of the fund claim. Values are:

**•** `Draft`

**•** `Approved`

**•** `Rejected`

**•** `Paid`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Title of the fund claim.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**PartnerFundClaimFeed**

Feed tracking is available for the object.

**PartnerFundClaimHistory**

History is available for tracked fields of the object.

**PartnerFundClaimOwnerSharingRule**

Sharing rules are available for the object.

**PartnerFundClaimShare**

Sharing is available for the object.


-----
