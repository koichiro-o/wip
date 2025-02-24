#### Employee2

Represents an employee within a company or an organization. This object is available in API version 62.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if Talent Recruitment Management is enabled in your org. To access the object, you need one of these permission
sets.

**User Type** **Permission Set**

Internal Users Talent Recruitment Management Specialist Access

Salesforce Platform Users
Talent Recruitment Management Hiring Manager Access


-----

##### Fields

**Field**
```
AlternateEmail
ContactId
CurrencyIsoCode
EmployeeNumber

```

OR

Talent Recruitment Management Employee Access

**Details**

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s alternate email address.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The contact associated with the employee.

**Relationship Name**
Contact

**Relationship Type**
Master-detail

**Refers To**
Contact (the master object)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO currency code for the post-authorization request.

Valid value is:

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
string


-----

```
EmployeeStatus
EmployeeType
EmploymentType

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The employee's unique ID for their organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The employee's current work status.

Valid values are:

**•** `Active`

**•** `Inactive`

**•** `Leave`

**•** `Terminated`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The employee's full-time or part-time status.

Valid values are:

**•** `Alumnus`

**•** `Contractor`

**•** `Permanent`

**•** `Intern`

**•** `Temporary`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's full-time or part-time status.

Valid values are:

**•** `Full-Time`

**•** `Part-Time`


-----

```
InternalOrganizationUnitId
LastReferencedDate
LastViewedDate
Name
StatusEndDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The internal organization unit associated with the employee.

**Relationship Name**
InternalOrganizationUnit

**Refers To**
InternalOrganizationUnit

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

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that the user only accessed the record or a related list view
(LastReferencedDate), but not viewed the record itself.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the employee record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The planned end date for the employee’s status.


-----

```
StatusStartDate

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The start date of the employee’s current status.

