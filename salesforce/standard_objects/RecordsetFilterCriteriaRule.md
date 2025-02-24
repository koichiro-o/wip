#### RecordsetFilterCriteriaRule

Represents a rule using fields from the designated source object to create filters on the filtered, or target, object. RecordsetFilterCriteriaRule
is associated with the RecordsetFilterCriteria object. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
CriteriaField
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The field the filter rule is applied to. Asset fields are available in API version 52.0 and later.

Possible values are derived from the source object’s standard and custom fields. Possible
standard source objects are `Asset` and `ServiceAppointment. The format is, for`
example, `Asset.PricingSource` or
```
  ServiceAppointment.GroupAppointmentAccessType. All standard and

```
custom fields are allowed except those with these field types:

**•** `encryptedstring`

**•** `multipicklist`

**•** `textarea`

**•** `url`

**Type**
dateTime


-----

```
LastViewedDate
NextOccurence
Operator

```

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria rule was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the recordset filter criteria rule was last viewed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This field’s value is compared to the Usage Field to determine if the rule is true.

Possible values are derived from the source object’s standard and custom fields. Possible
standard source objects are `Asset` and `ServiceAppointment. The format is, for`
example, `Asset.PricingSource` or
```
  ServiceAppointment.GroupAppointmentAccessType. All standard and

```
custom fields are allowed except those with these field types:

**•** `encryptedstring`

**•** `multipicklist`

**•** `textarea`

**•** `url`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The relational operator between CriteriaField and Value. Available in API version
52.0 or later.

Possible values are:

**•** `Equals—Default`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `LessOrEqual`

**•** `LessThan`


-----

```
RecordsetFilterCriteriaId
RecordsetFilterCriteriaRuleNumber
Type
Value
Usage Rate Field

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the RecordsetFilterCriteria record to associate this rule with.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically assigned number of the recordset filter criteria rule.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of criteria rule. Possible values are:

**•** `Criteria—Default`

**•** `Usage`

**•** `UsageCounter— Usage(Counter)`

**•** `UsageDuration— Usage(Duration)`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The expected value of `CriteriaField` applied to the filter rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Stores the daily usage rate of the asset. The unit for the usage rate must be per day. Possible
values are derived from the source object’s standard and custom fields. Possible standard
source objects are `Asset` and `ServiceAppointment. The format is, for example,`


-----

```
Usage Rate Unit

##### Usage

```

`Asset.PricingSource` or
```
  ServiceAppointment.GroupAppointmentAccessType.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines the rate for Usage Rate Field.

Possible values are:

**•** DAYS


If you want to create a filter rule for service appointments with a dispatched status, set `CriteriaField` to
`ServiceAppointment.Status` and `Value` to `Dispatched. Then add the ID from a RecordsetFilterCriteria record to`
`RecordsetFilterCriteriaId` to associate this rule with a filter criteria for shifts.
