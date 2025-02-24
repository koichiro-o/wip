#### Entitlement

Represents the customer support an account or contact is eligible to receive. This object is available in API version 18.0 and later.
Entitlements may be based on an asset, product, or service contract.

##### Supported Calls
```
create(), delete(), describeLayout(), getDeleted(), getUpdated(), query(), retrieve(), search(),
undelete(), update(), upsert()

 Fields

```
```
AccountId
AssetId
AssetWarrantyID
BusinessHoursId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Account associated with the entitlement.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the Asset associated with the entitlement. Must be a valid asset ID.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the asset warranty record. Must be a valid asset warranty ID.
AssetWarranty is available only with Field Service.

**Type**
reference


-----

```
CasesPerEntitlement
ContractLineItemId
EndDate
IsPerIncident
LastReferencedDate

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the BusinessHours associated with the entitlement. Must be a valid
business hours ID.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of cases the entitlement supports.

This field is only available if IsPerIncident is `true.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the ContractLineItem associated with the entitlement. Must be a valid
ID.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The last day the entitlement is in effect.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Update

**Description**
Indicates whether the entitlement is limited to supporting a specific number of cases
(true) or not (false).

**Type**
date

**Properties**
Filter, Nillable, Sort, Update


-----

```
LastViewedDate
LocationID
Name
SvcApptBookingWindowsId
RemainingCases

```

**Description**
The timestamp when the current user last accessed this record, a record related to
this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value
is null, the user might have only accessed this record or list view
(LastReferencedDate) but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Location associated with the entitlement. Must be a valid location ID.

**Type**
string

**Properties**
Create, Filter, Update

**Description**
Required. Name of the entitlement.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The operating hours that the entitlement’s work orders should respect. The label in
the user interface is Operating Hours. Available only if Field Service is enabled.

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
The number of cases the entitlement can support. This field decreases in value by
one each time a case is created with the entitlement.


-----

```
RemainingWorkOrders
ServiceContractId
SlaProcessId
StartDate
Status
SvcApptBookingWindows

```

This field is only available if IsPerIncident is selected.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of agreed work orders remaining to be created.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the ServiceContract associated with the entitlement. Must be a valid
ID.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the SlaProcess associated with the entitlement. This field is available in version
19.0 and later.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The first date the entitlement is in effect.

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Status of the entitlement, such as `Expired.`

**Type**
reference


-----

```
Type
WorkOrdersPerEntitlement

##### Associated Objects

```

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The operating hours of the entitlement. This field is visible only if Field Service is
enabled.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The type of entitlement, such as Web or phone support.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Total number of work orders available for this entitlement.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EntitlementChangeEvent (API version 44.0)**
Change events are available for the object.

**EntitlementFeed (API version 23.0)**
Feed tracking is available for the object.

**EntitlementHistory**

History is available for tracked fields of the object.

SEE ALSO:

EntitlementContact

SlaProcess
