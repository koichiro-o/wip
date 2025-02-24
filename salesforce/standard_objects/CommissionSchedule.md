#### CommissionSchedule

Represents a commission calculation and rate definition. Calculates commission values for a commissionable event.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ApplicableObject
CalcProcessInputMapping
CalcProcessOutput
CalcProcessOutputConvNotation

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
The object for which this Commission Schedule calculates commissions.

Possible values are:

**•** `Contract`

**•** `InsurancePolicy`

**•** `Producer`

**•** `Quote`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input mappings from the object fields to the variables used in the commission calculation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula applied to this Commission Schedule’s process output that calculates the final
commission amount.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An optimized version of the CalcProcessOutput formula that calculates the commission. Not
user-editable.


-----

```
CalculationProcessName
CalculationType
CommissionAmount
CommissionRate
CommissionStructureType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Integration Procedure, Calculation Matrix, or Calculation Procedure this
Commission Schedule uses for calculations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of calculation or process used when this Commission Schedule is used.

Possible values are:

**•** `Amount`

**•** `CalculationMatrix`

**•** `CalculationProcedure`

**•** `IntegrationProcedure`

**•** `Rate`

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The commission amount for the Commission Schedule when the process type is Amount.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The commission percentage for the Commission Schedule when the process type is Rate.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
EffectiveEndDate
EffectiveStartDate
IsActive
LastReferencedDate
LastViewedDate

```

**Description**
Indicates whether the commission calculation is Flat or Tiered when the process type is
Matrix.

Possible values are:

**•** `Flat`

**•** `Tiered`

The default value is `Flat.`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The effective end date of the Commission Schedule.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The effective start date of the Commission Schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Commission Schedule is active.

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId
TierDefinition

##### Associated Objects

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Commission Schedule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Internal-only. Applies when the CalculationType is CalculationMatrix.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommissionScheduleChangeEvent on page 67**
Change events are available for the object in API version 62.0 and later.

**CommissionScheduleFeed**

Feed tracking is available for the object.


-----

**CommissionScheduleHistory**

History is available for tracked fields of the object.

**CommissionScheduleOwnerSharingRule**

Sharing rules are available for the object.

**CommissionScheduleShare**

Sharing is available for the object.
