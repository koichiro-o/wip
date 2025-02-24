#### Employee

```

**Description**
Developer name for the EmbeddedServiceConfig.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of label for this embedded component. The value corresponds to the label within
a label group (substate of chat state or page type).


Represents an employee within a company or organization. This object is available in API version 48.0 and later. In API version 49.0 and
later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom
page layouts.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search() undelete(), update(), upsert()

 Special Access Rules

```
To access this object, you must have a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission or have the Employee Management and Employee User add-on licenses.

##### Fields

```
AboutMe
AlternateEmail

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Information about the employee, such as areas of interest or skills. Values can be provided
on Employee’s profile page. This field is available even if Chatter is disabled.

**Type**
email


-----

```
Availability
AvailabilityEndDate
AvailabilityStartDate
BannerPhotoUrl

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s alternate email address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s availability status.

Possible values are:

**•** `In The Office`

**•** `Out Of Office`

**•** `Out Sick`

**•** `PTO`

**•** `Volunteering Time Off`

**•** `Working Remotely`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end date of the Employee’s availability, inclusive of the date.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start date of the Employee’s availability, inclusive of the date.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the employee's banner photo. Available in API v51.0 and later.


-----

```
CurrentWellnessStatus
DateOfBirth
Email
EmployeeNumber
EmployeeStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s current wellness status.

Possible values are:

**•** `Available To Work`

**•** `Remote Work Only`

**•** `Unavailable`

**•** `Unknown`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s date of birth.

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The employee’s email address. This field is unique within your organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The employee's employment ID for the organization they were hired into. This
field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee's current work status.

Possible values are:


-----

```
EmploymentType
FirstName
FullPhotoUrl
Gender

```


**•** `Active`

**•** `Inactive`

**•** `Leave`

**•** `Terminated`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's full-time or part-time status.

Possible values are:

**•** `Full-Time`

**•** `Part-Time`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee’s first name.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the employee's profile photo. The URL is updated every time a photo
is uploaded and reflects the most recent photo. If a newer photo has been uploaded, the
URL returned for an older photo isn’t guaranteed to return a photo. Query this field for the
URL of the most recent photo. Available in API v51.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s gender.

Possible values are:

**•** `Female`

**•** `Male`


-----

```
HomeAddress
HomeCity
HomeCountry
HomeGeocodeAccuracy

```


**•** `Non-Binary / Non-Conforming`

**•** `Other`

**•** `Prefer Not to State`

**•** `Transgender Female`

**•** `Transgender Male`

**Type**
address

**Properties**
Filter, Nillable

**Description**
The employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city for the employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The county for the employee’s home address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of an employee’s home address geographical coordinates compared
with its physical address. A geocoding service typically provides this value based on the
address’s latitude and longitude coordinates.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`


-----

```
HomeLatitude
HomeLongitude
HomePhone
HomePostalCode
HomeState

```


**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with HomeLongitude to specify the precise geolocation of the employee’s home
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with HomeLatitude to specify the precise geolocation of the employee’s home address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s home phone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code for the employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
HomeStreet
IndividualId
InternalOrganizationUnitId
JobProfile
LastName
LastReferencedDate

```

**Description**
The state for the employee’s home address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street for the employee’s home address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Individual record that this employee is assigned to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the InternalOrganizationUnit this employee is assigned to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s job profile at the company.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee’s last name.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
LocationId
ManagerId
MediumPhotoUrl
MiddleName

```

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Location that this employee is assigned to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Employee record of the employee's manager.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the medium-sized employee's profile photo. The URL is updated
every time a photo is uploaded and reflects the most recent photo. If a newer photo has
been uploaded, the URL returned for an older photo isn’t guaranteed to return a photo.
Query this field for the URL of the most recent photo. Available in API v51.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s middle name.


-----

```
Name
NameSuffix
OutOfOfficeMessage
OwnerId
PreferredFirstName
PreferredPronoun

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A compound field of `Employee.FirstName,` `Employee.MiddleName, and`
```
  Employee.LastName.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s suffix.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The message portion of the employee availability. This message can provide reasons or
details about the change in availability. The maximum length of this string is 40 characters.

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
The name the employee prefers to be called.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
RelatedPersonId
SmallPhotoUrl
StatusAsOf
StatusEndDate

```

**Description**
The employee's preferred pronoun.

Possible values are:

**•** `He/Him/His`

**•** `Other/Ask Me`

**•** `She/Her/Hers`

**•** `They/Them/Theirs`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links an employee to a person account with a unique value. Reserved for future use. Don’t
edit it.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the small-sized employee's profile photo. The URL is updated every
time a photo is uploaded and reflects the most recent photo. If a newer photo has been
uploaded, the URL returned for an older photo isn’t guaranteed to return a photo. Query this
field for the URL of the most recent photo. Available in API v51.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Required. Start date of the employee’s current status.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Planned end date for the employee’s status.


-----

```
TimeZone
UserId
WorkPhone
WorkerType
WorkingHoursEnd

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone which the employee’s work hours fall within.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field to associate an Employee record with a user in the org. The field is optional and
unique.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's formatted work phone number including country code and extension.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The type of worker for the employee.

Possible values are:

**•** `Alumnus`

**•** `Contractor`

**•** `Employee`

**•** `Intern`

**•** `Temporary`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The end time of the employee’s working hours.


-----

```
WorkingHoursStart

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The start time of the employee’s working hours.


This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**EmployeeHistory (API version 49.0)**
History is available for tracked fields of the object.

**EmployeeOwnerSharingRule**

Sharing rules are available for the object.

**EmployeesShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide: Extend Work.com with Custom Solutions](https://developer.salesforce.com/docs/atlas.en-us.254.0.workdotcom_dev_guide.meta/workdotcom_dev_guide/wdc_cc_dev_workplace_cc_solution.htm)_
