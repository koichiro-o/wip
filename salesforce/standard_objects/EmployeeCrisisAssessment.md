#### EmployeeCrisisAssessment

Represents a crisis assessment of an Employee. This object is available in API version 48.0 and later. In API version 49.0 and later, this
object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom page layouts.

For Work.com, when an employee responds to a wellness survey, an EmployeeCrisisAssessment record is created based on an employee's
answers.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object, you must be assigned a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission.

##### Fields

```
Assessment

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s COVID-19 status at the time of the assessment.

Possible values are:

**•** `COVID-19 Immune or Recovered`

**•** `COVID-19 No Symptoms`

**•** `COVID-19 Symptoms or Exposed`

**•** `COVID-19 Test Negative`

**•** `COVID-19 Test Positive`


-----

```
AssessmentDate
AssessmentNumber
CrisisId
EmployeeId
LastReferencedDate
LastViewedDate

```


**•** `Declined`

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date of the assessment. Required

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The assessment record number.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Crisis that this assessment is associated with.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The Employee that this assessment is associated with.

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
OwnerId
SourceAssessment
SourceSystem

##### Associated Objects

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record in the source system that drove this assessment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source system that drove this assessment.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EmployeeCrisisAssessmentHistory (API version 49.0)**
History is available for tracked fields of the object.

**EmployeeCrisisAssessmentOwnerSharingRule**

Sharing rules are available for the object.

**EmployeeCrisisAssessmentShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide: Extend Work.com with Custom Solutions](https://developer.salesforce.com/docs/atlas.en-us.254.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_


-----
