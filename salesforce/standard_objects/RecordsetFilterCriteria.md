#### RecordsetFilterCriteria

```
Represents a set of filters that can be used to match service appointments or assets based on your criteria fields. For example, you can
create recordset filter criteria so that only service appointments that satisfy the filter criteria are matched to the filtered shifts, and likewise
only maintenance work rules that satisfy your criteria are matched to assets. This object is available in API version 50.0 and later. Assets
and maintenance work rules are available in API version 52.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
Description
FilteredObject
IsActive
LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the recordset filter criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object used to define the filter criteria. Available in API version 52.0 or later.

Possible values are:

**•** `Asset`

**•** `ServiceAppointment`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the recordset filter criteria is associated with shifts or maintenance work
rules (true) or not (false).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
LogicalOperator
Name
OwnerId
SourceObject

```

**Description**
The date when the recordset filter criteria was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria was last viewed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Defines the logic to evaluate multiple recordset filter criteria rules. Available in API version
53.0 and later.

Possible values are:

**•** `AND`

**•** `OR`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recordset filter criteria.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the recordset filter criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


-----

Usage Rate Field

Usage Rate Unit

##### Usage


**Description**
The source object that the filtered criteria are applied to. Shifts and maintenance work rules
are available in API version 52.0 and later. Appointment bundle objects are available in API
version 53.0 and later.

Possible values are:

**•** `ApptBundleAggrPolicy—Appointment Bundle Aggregation Policy`

**•** `ApptBundleConfig—Appointment Bundle Config`

**•** `Shift`

**•** `ContractLineOutcome`

**•** `MaintenanceWorkRule`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Stores the daily usage rate of the asset. The unit for the usage rate must be per day.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines the rate for Usage Rate Field.

Possible values are:

**•** DAYS


Let's say an employee is open to working a 9 am to 5 pm shift on a Sunday but only for emergency appointments. In this case, the
`SourceObject` is `Shift` and the `FilteredObject` is `ServiceAppointment. The service appointments available for`
that shift are filtered for emergency appointments using the `RecordsetFilterCriteriaRule object.`

RecordSetFilterCriteria isn’t available for report types.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**RecordsetFilterCriteriaFeed**

Feed tracking is available for the object.


-----

**RecordsetFilterCriteriaHistory**

History is available for tracked fields of the object.

**RecordsetFilterCriteriaOwnerSharingRule**

Sharing rules are available for the object.

**RecordsetFilterCriteriaShare**

Sharing is available for the object.
