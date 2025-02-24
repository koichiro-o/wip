#### ContactCleanInfo

Stores the metadata Data.com Clean uses to determine a contact record’s clean status. Helps you automate the cleaning or related
processing of contact records. ContactCleanInfo includes a number of bit vector fields.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Contact Clean Info provides a snapshot of the data in your Salesforce contact record and its matched Data.com record at the time the
Salesforce record was cleaned.

Contact Clean Info includes a number of bit vector fields, whose component fields each correspond to individual object fields and provide
related data or status information about those fields. For example, the bit vector field IsDifferent has an IsDifferentEmail
field. If the `IsDifferentEmail field’s value is` `False, that means the` `Email` field value is the same on the Salesforce contact
record and its matched Data.com record.

ContactCleanInfo bit vector fields include:

**•** `CleanedBy` indicates who (a user) or what (a Clean job) cleaned the contact record.

**•** `IsDifferent` indicates whether or not a field on the contact record has a value that differs from the corresponding field on the
matched Data.com record.

**•** `IsFlaggedWrong` indicates whether or not a field on the contact record has a value that is flagged as wrong to Data.com.

**•** `IsReviewed` indicates whether or not a field on the contact record is in a `Reviewed` state, which means that the value was
reviewed but not accepted.

##### Fields

```
Address

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address Compound Fields
for details on compound address fields.


-----

```
City
CleanedByJob
CleanedByUser
ContactId
ContactStatusDataDotCom

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact record was cleaned by a Data.com Clean job (true)
or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact record was cleaned by a Salesforce user (true)
or not (false).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the contact record was created.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the contact per Data.com. Values are: `Contact is Active`
```
  per Data.com, Phone is Wrong per Data.com, Email is
  Wrong per Data.com, Phone and Email are Wrong per
  Data.com, Contact Not at Company per Data.com, Contact
  is Inactive per Data.com, Company this contact
  belongs to is out of business per Data.com, Company

```

-----

```
Country
DataDotComID
Email
FirstName
IsDifferentCity
IsDifferentCountry

```
```
  this contact belongs to never existed per Data.com

```
or `Email address is invalid per Data.com.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the contact.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address for the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s first name.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `City` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean


-----

```
IsDifferentCountryCode
IsDifferentEmail
IsDifferentFirstName
IsDifferentLastName
IsDifferentPhone

```

**Properties**
Filter

**Description**
Indicates whether the contact’s `Country` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Country Code field value is different from`
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Email` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `First Name` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Last Name` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter


-----

```
IsDifferentPostalCode
IsDifferentState
IsDifferentStateCode
IsDifferentStreet
IsDifferentTitle

```

**Description**
Indicates whether the contact’s `Phone` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s Postal Code field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `State` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `State Code` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Street` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter


-----

```
IsFlaggedWrongAddress
IsFlaggedWrongEmail
IsFlaggedWrongName
IsFlaggedWrongPhone
IsFlaggedWrongTitle

```

**Description**
Indicates whether the contact’s `Title` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Address` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Email` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s Name field value is flagged as wrong to Data.com
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Phone` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsInactive
IsReviewedAddress
IsReviewedEmail
IsReviewedName
IsReviewedPhone

```

**Description**
Indicates whether the contact’s `Title` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the contact has been reported to Data.com as `Inactive`
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Address` field value is in a `Reviewed` state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Email` field value is in a `Reviewed` state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Name` field value is in a `Reviewed` state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsReviewedTitle
LastMatchedDate
LastName
LastStatusChangedById
LastStatusChangedDate

```

**Description**
Indicates whether the contact’s `Phone` field value is in a `Reviewed` state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Title` field value is in a `Reviewed` state
(true) or not (false).

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the contact record was last matched and linked to a Data.com record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s last name.

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


-----

```
Latitude
Longitude
Name
Phone
PostalCode
State

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of a billing address.
Data not currently provided.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Latitude` to specify the precise geolocation of a billing address.
Data not currently provided.

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Field label is Contact Clean Info Name. The name of the contact. Maximum
size is 255 characters.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number for the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
string


-----

```
Street
Title

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s title.


Developers can create triggers that read the Contact Clean Info fields to help automate the cleaning or related processing of contact
records.

Create a customized set of `Title` field values. Use triggers to map values from fields on imported or cleaned records onto a standard
set of values.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactCleanInfoChangeEvent (API version 62.0)**
Change events are available for the object.
