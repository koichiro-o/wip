#### PartnerFundRequest

Represents a request for funds from the partner marketing budget by a channel partner. This object is available in API version 41.0 and
later.

##### Supported Calls
```
create(), delete()describeLayout()describeSObjects()
getDeleted()getUpdated()query()retrieve()search() update(), upsert()

 Fields

```
```
Activity
AllocationId
Amount
BudgetId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Activity that is covered by the funds, for example, a trade show or seminar.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the partner fund allocation.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Approved amount of request.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the partner marketing budget.


-----

```
ChannelPartnerId
Description
DesiredOutcome
LastReferencedDate
LastViewedDate
OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the channel partner.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the fund request.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Desired outcome if requested funds are used.

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


-----

```
RequestedAmount
Status
Title
TotalApprovedFcs
TotalReimbursedFcs

```

**Description**
ID of the owner of the fund request.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount of the fund request.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Group, Restricted picklist, Sort, Update

**Description**
Status of the fund request. Values are:

**•** `Draft`

**•** `Approved`

**•** `Rejected`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Title of the fund request.

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
Total amount of reimbursed fund claims.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**PartnerFundRequestFeed**

Feed tracking is available for the object.

**PartnerFundRequestHistory**

History is available for tracked fields of the object.

**PartnerFundRequestOwnerSharingRule**

Sharing rules are available for the object.

**PartnerFundRequestShare**

Sharing is available for the object.
