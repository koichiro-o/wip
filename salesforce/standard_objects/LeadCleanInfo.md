#### LeadCleanInfo

Stores the metadata Data.com Clean uses to determine a lead record’s clean status. Helps you automate the cleaning or related processing
of lead records.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Lead Clean Info provides a snapshot of the data in your Salesforce lead record and its matched Data.com record at the time the Salesforce
record was cleaned.

Lead Clean Info includes a number of bit vector fields, whose component fields each correspond to individual object fields and provide
related data or status information about those fields. For example, the bit vector field IsDifferent has an IsDifferentTitle
field. If the IsDifferentTitle field’s value is False, that means the Title field value is the same on the Salesforce lead record
and its matched Data.com record.

LeadCleanInfo bit vector fields include:

**•** `CleanedBy` indicates who (a user) or what (a Clean job) cleaned the lead record.

**•** `IsDifferent` indicates whether or not a field on the lead record has a value that differs from the corresponding field on the
matched Data.com record.

**•** `IsFlaggedWrong` indicates whether or not a field on the lead record has a value that is flagged as wrong to Data.com.

**•** `IsReviewed` indicates whether or not a field on the lead record is in a `Reviewed` state, which means that the value was
reviewed but not accepted..

Their individual bits are defined here

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

```

-----

##### Fields

**Field Name**
```
Address
AnnualRevenue
City
CleanedByJob
CleanedByUser
CompanyDunsNumber

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Estimated annual revenue of the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead record was cleaned by a Data.com Clean job (true)
or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead record was cleaned by a Salesforce user (true) or
not (false).

**Type**
string


-----

```
CompanyName
ContactStatusDataDotCom
Country
DandBCompanyDunsNumber

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the company.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the contact associated with the lead per Data.com. Values are:
```
  Contact is Active per Data.com, Phone is Wrong per
  Data.com, Email is Wrong per Data.com, Phone and
  Email are Wrong per Data.com, Contact Not at Company
  per Data.com, Contact is Inactive per Data.com,
  Company this contact belongs to is out of business
  per Data.com, Company this contact belongs to never

```
`existed per Data.com` or `Email address is invalid per`
```
  Data.com.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
DataDotComCompanyId
DataDotComId
Email
FirstName
Industry
IsDifferentAnnualRevenue

```

**Description**
The D-U-N-S Number on the D&B Company record (if any) that is linked to the
lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the company associated with the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the contact associated with the lead.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lead’s email address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lead’s first name.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The industry the lead belongs to.

**Type**
boolean


-----

```
IsDifferentCity
IsDifferentCompanyDunsNumber
IsDifferentCompanyName
IsDifferentCountry
IsDifferentCountryCode

```

**Properties**
Filter

**Description**
Indicates whether the lead’s `AnnualRevenue` field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s City field value is different from the corresponding
value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Company D-U-N-S Number` field value is
different from the corresponding value on its matched Data.com record (true)
or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Company Name` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Country` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean


-----

```
IsDifferentDandBCompanyDunsNumber
IsDifferentEmail
IsDifferentFirstName
IsDifferentIndustry
IsDifferentLastName

```

**Properties**
Filter

**Description**
Indicates whether the account’s `Country Code field value is different from`
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s D&B Company D-U-N-S Number field value
is different from the corresponding value on its matched Data.com record (true)
or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Email` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `First Name` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Industry` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean


-----

```
IsDifferentNumberOfEmployees
IsDifferentPhone
IsDifferentPostalCode
IsDifferentState
IsDifferentStateCode

```

**Properties**
Filter

**Description**
Indicates whether the lead’s `Last Name` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s No. of Employees field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Phone` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Postal Code` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `State` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter


-----

```
IsDifferentStreet
IsDifferentTitle
IsFlaggedWrongAddress
IsFlaggedWrongAnnualRevenue
IsFlaggedWrongCompanyDunsNumber

```

**Description**
Indicates whether the account’s State Code field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Street` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the lead’s `Title` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Address` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s Annual Revenue field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsFlaggedWrongCompanyName
IsFlaggedWrongEmail
IsFlaggedWrongIndustry
IsFlaggedWrongName
IsFlaggedWrongNumberOfEmployees

```

**Description**
Indicates whether the lead’s `Company D-U-N-S Number` field value is
flagged as wrong to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Company Name` field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s Email field value is flagged as wrong to Data.com
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Industry` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Name` field value is flagged as wrong to Data.com
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsFlaggedWrongPhone
IsFlaggedWrongTitle
IsInactive
IsReviewedAddress
IsReviewedAnnualRevenue

```

**Description**
Indicates whether the lead’s `No. of Employees field value is flagged as`
wrong to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s Phone field value is flagged as wrong to Data.com
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s Title field value is flagged as wrong to Data.com
(true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the lead has been reported to Data.com as `Inactive`
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Address` field value is in a `Reviewed` state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsReviewedCompanyDunsNumber
IsReviewedCompanyName
IsReviewedDandBCompanyDunsNumber
IsReviewedEmail
IsReviewedIndustry

```

**Description**
Indicates whether the lead’s Annual Revenue field value is in a Reviewed
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Company D-U-N-S Number` field value is in
a `Reviewed state (true) or not (false).`

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `Company Name` field value is in a `Reviewed`
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s D&B Company D-U-N-S Number field value
is in a `Reviewed state (true) or not (false).`

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s Email field value is in a Reviewed state (true)
or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsReviewedName
IsReviewedNumberOfEmployees
IsReviewedPhone
IsReviewedTitle
LastMatchedDate

```

**Description**
Indicates whether the lead’s `Industry` field value is in a `Reviewed` state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s Name field value is in a Reviewed state (true)
or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s `No. of Employees field value is in a`
`Reviewed` state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s Phone field value is in a Reviewed state (true)
or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the lead’s Title field value is in a Reviewed state (true)
or not (false).

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the lead record was last matched and linked to a Data.com record.


-----

```
LastName
LastStatusChangedById
LastStatusChangedDate
Latitude
LeadId
Longitude

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lead’s last name.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of who or what last changed the record’s `Clean Status` field value:
a Salesforce user or a Clean job.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the record’s `Clean Status field value was last changed.`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of a billing address.
Data not currently provided.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the lead record was created.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
Name
NumberOfEmployees
Phone
PostalCode
State
Street

```

**Description**
Used with `Latitude` to specify the precise geolocation of a billing address.
Data not currently provided.

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Field label is Lead Clean Info Name. The name of the lead. Maximum size is 255
characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of employees working at the lead.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number for the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
textarea


-----

```
Title

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The lead’s title.


Developers can create triggers that read the Lead Clean Info fields to help automate the cleaning or related processing of lead records.
