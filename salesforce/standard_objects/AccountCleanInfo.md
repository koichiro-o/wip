#### AccountCleanInfo

Stores the metadata Data.com Clean uses to determine an account record’s clean status. AccountCleanInfo helps you automate the
cleaning or related processing of account records.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Account Clean Info provides a snapshot of the data in your Salesforce account record and its matched Data.com record at the time the
Salesforce record was cleaned.

Account Clean Info includes a number of bit vector fields, whose component fields each correspond to individual object fields and
provide related data or status information about those fields. For example, the bit vector field `IsDifferent has an`
`IsDifferentState` field. If the `IsDifferentState` field’s value is `False, that means the` `State` field value is the same
on the Salesforce account record and its matched Data.com record.

AccountCleanInfo bit vector fields include:

**•** `CleanedBy` indicates who (a user) or what (a Clean job) cleaned the account record.

**•** `IsDifferent` indicates whether or not a field on the account record has a value that differs from the corresponding field on the
matched Data.com record.

**•** `IsFlaggedWrong` indicates whether or not a field on the account record has a value that is flagged as wrong to Data.com.

**•** `IsReviewed` indicates whether or not a field on the account record is in a `Reviewed` state, which means that the value was
reviewed but not accepted.

Their individual bits are defined here.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Fields

```
```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the account record was created.


-----

```
AccountSite
Address
AnnualRevenue
City
CleanedByJob
CleanedByUser

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information about the account’s location, such as single location, headquarters,
or branch.

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
Estimated annual revenue of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account record was cleaned by a Data.com Clean job
(true) or not (false).

**Type**
boolean

**Properties**
Filter


-----

```
CompanyName
CompanyStatusDataDotCom
Country
DandBCompanyDunsNumber
DataDotComId

```

**Description**
Indicates whether the account record was cleaned by a Salesforce user (true)
or not (false).

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
The status of the company per Data.com. Values are: `Company is In`
`Business per Data.com` or `Company is Out of Business`
```
  per Data.com.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The D-U-N-S Number on the D&B Company record (if any) that is linked to the
account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the company.


-----

```
Description
DunsNumber
DunsRightMatchConfidence
DunsRightMatchGrade
Fax
Industry

```

**Type**
textarea

**Properties**
Nillable

**Description**
A description of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account’s DUNSRight confidence code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account’s DUNSRight match grade.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account’s fax number.

**Type**
picklist


-----

```
IsDifferentAccountSite
IsDifferentAnnualRevenue
IsDifferentCity
IsDifferentCompanyName
IsDifferentCountry

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The industry the account belongs to.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `AccountSite` field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s AnnualRevenue field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `City` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `AccountName` field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter


-----

```
IsDifferentCountryCode
IsDifferentDandBCompanyDunsNumber
IsDifferentDescription
IsDifferentDunsNumber
IsDifferentFax

```

**Description**
Indicates whether the account’s `Country` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Country Code` field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `DandBCompanyID` field value is different
from the corresponding value on its matched Data.com record (true) or not
(false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Description` field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s DunsNumber field value is different from the
D-U-N-S Number on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter


-----

```
IsDifferentIndustry
IsDifferentNaicsCode
IsDifferentNaicsDescription
IsDifferentNumberOfEmployees
IsDifferentOwnership

```

**Description**
Indicates whether the account’s `Fax` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Industry` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `NaicsCode` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s NaicsDescription field value is different
from the corresponding value on its matched Data.com record (true) or not
(false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `NumberOf Employees` field value is
different from the corresponding value on its matched Data.com record (true)
or not (false).

**Type**
boolean

**Properties**
Filter


-----

```
IsDifferentPhone
IsDifferentPostalCode
IsDifferentSic
IsDifferentSicDescription
IsDifferentState

```

**Description**
Indicates whether the account’s `Ownership` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Phone` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s PostalCode field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Sic` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `SicDescription` field value is different
from the corresponding value on its matched Data.com record (true) or not
(false).

**Type**
boolean

**Properties**
Filter


-----

```
IsDifferentStateCode
IsDifferentStreet
IsDifferentTickerSymbol
IsDifferentTradestyle
IsDifferentWebsite

```

**Description**
Indicates whether the account’s `State` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s State Code field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `State` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `TickerSymbol` field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s Tradestyle field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter


-----

```
IsDifferentYearStarted
IsFlaggedWrongAccountSite
IsFlaggedWrongAddress
IsFlaggedWrongAnnualRevenue
IsFlaggedWrongCompanyName

```

**Description**
Indicates whether the account’s `Website` field value is different from the
corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `YearStarted` field value is different from
the corresponding value on its matched Data.com record (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s AccountSite field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Address` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `AnnualRevenue` field value is flagged as
wrong to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsFlaggedWrongDescription
IsFlaggedWrongDunsNumber
IsFlaggedWrongFax
IsFlaggedWrongIndustry
IsFlaggedWrongNaicsCode

```

**Description**
Indicates whether the account’s CompanyName field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s Description field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `DunsNumber` field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s Fax field value is flagged as wrong to Data.com
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Industry` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsFlaggedWrongNaicsDescription
IsFlaggedWrongNumberOfEmployees
IsFlaggedWrongOwnership
IsFlaggedWrongPhone
IsFlaggedWrongSic

```

**Description**
Indicates whether the account’s `NaicsCode` field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NaicsDescription` field value is flagged
as wrong to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s NumberOfEmployees field value is flagged
as wrong to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Ownership` field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Phone` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsFlaggedWrongSicDescription
IsFlaggedWrongTickerSymbol
IsFlaggedWrongTradestyle
IsFlaggedWrongWebsite
IsFlaggedWrongYearStarted

```

**Description**
Indicates whether the account’s Sic field value is flagged as wrong to Data.com
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `SicDescription` field value is flagged as
wrong to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `TickerSymbol` field value is flagged as
wrong to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Tradestyle` field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Website` field value is flagged as wrong to
Data.com (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsInactive
IsReviewedAccountSite
IsReviewedAddress
IsReviewedAnnualRevenue
IsReviewedCompanyName

```

**Description**
Indicates whether the account’s YearStarted field value is flagged as wrong
to Data.com (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the account has been reported to Data.com as `Inactive`
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s AccountSite field value is in a Reviewed
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s Address field value is in a Reviewed state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `AnnualRevenue` field value is in a
`Reviewed` state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsReviewedDandBCompanyDunsNumber
IsReviewedDescription
IsReviewedDunsNumber
IsReviewedFax
IsReviewedIndustry

```

**Description**
Indicates whether the account’s CompanyName field value is in a Reviewed
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `DandBCompanyID` field value is in a
`Reviewed` state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s Description field value is in a Reviewed
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `DunsNumber` field value is in a `Reviewed`
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s Fax field value is in a Reviewed state (true)
or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsReviewedNaicsCode
IsReviewedNaicsDescription
IsReviewedNumberOfEmployees
IsReviewedOwnership
IsReviewedPhone

```

**Description**
Indicates whether the account’s `Industry` field value is in a `Reviewed`
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NaicsCode` field value is in a `Reviewed`
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NaicsDescription` field value is in a
`Reviewed` state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NumberOfEmployees` field value is in a
`Reviewed` state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Ownership` field value is in a `Reviewed`
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsReviewedSic
IsReviewedSicDescription
IsReviewedTickerSymbol
IsReviewedTradestyle
IsReviewedWebsite

```

**Description**
Indicates whether the account’s `Phone` field value is in a `Reviewed` state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s Sic field value is in a Reviewed state (true)
or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `SicDescription` field value is in a
`Reviewed` state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s TickerSymbol field value is in a Reviewed
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Tradestyle` field value is in a `Reviewed`
state (true) or not (false).

**Type**
boolean

**Properties**
Filter, Update


-----

```
IsReviewedYearStarted
LastMatchedDate
LastStatusChangedById
LastStatusChangedDate
Latitude

```

**Description**
Indicates whether the account’s Website field value is in a Reviewed state
(true) or not (false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s YearStarted field value is in a Reviewed
state (true) or not (false).

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the account record was last matched and linked to a Data.com record.

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
The date on which the record’s Clean Status field value was last changed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of a billing address.
Data not currently provided.


-----

```
Longitude
NaicsCode
NaicsDescription
Name
NumberOfEmployees
Ownership

```

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
Filter, Group, Nillable, Sort

**Description**
The six-digit North American Industry Classification System (NAICS) code is the
standard used by business and government to classify business establishments
into industries, according to their economic activity for the purpose of collecting,
analyzing, and publishing statistical data related to the U.S. business economy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A brief description of an organization’s line of business, based on its NAICS code.

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Field label is Account Clean Info Name. The name of the account. Maximum
size is 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of employees working at the account.

**Type**
picklist


-----

```
Phone
PostalCode
Sic
SicDescription
State

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Ownership type for the account, for example Private, Public, or Subsidiary.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Standard Industrial Classification code of the company’s main business
categorization, for example, 57340 for Electronics.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A brief description of an organization’s line of business, based on its SIC code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.


-----

```
Street
TickerSymbol
Tradestyle
Website
YearStarted

##### Usage

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock market symbol for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A name, different from its legal name, that an organization can use for conducting
business. Similar to “Doing business as” (DBA).

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The website of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The year the company was established or the year when current ownership or
management assumed control of the company.


Administrators can modify a limited set of AccountCleanInfo fields from the Account Clean Info page.


-----

Developers can create triggers that read the Account Clean Info fields to help automate the cleaning or related processing of account
records. For example, you might create a trigger that reads the `Clean Status` field on the Account object. If an account record’s
`Clean Status field value is Different` but the record has no Billing Street value, the trigger could update the record’s
status to `Not Compared.`

Create triggers that read AccountCleanInfo fields to help automate the cleaning or related processing of account records. For example:

**•** Keep account records’ status `InSync` if the only difference from matched records is the `Phone format (for example, (415)`
`353-8000` on the account record versus `415 353 8000` on the matched Data.com record).
```
  trigger AccountPhoneTrigger on Account (before update) {
    for (Account account: Trigger.new) {
      Account oldAccount = Trigger.oldMap.get(account.ID);
      if (account.CleanStatus == 'Different') {
         List <AccountCleanInfo> cleanInfo = [Select Id, IsDifferentPhone,
  IsReviewedPhone, Phone from AccountCleanInfo where AccountId = :account.Id];
         if (cleanInfo.size() > 0 && cleanInfo[0].IsDifferentPhone &&
  cleanInfo[0].Phone.StartsWith('+')) {
           // if Data.com phone number is marked Different but starts with ‘+’,
  ignore this
           // and set the status to “Reviewed”
           AccountCleanInfo cleanInfoToUpdate = new AccountCleanInfo();
           cleanInfoToUpdate.Id = cleanInfo[0].Id;
           cleanInfoToUpdate.IsReviewedPhone = true;
           update cleanInfoToUpdate;
           account.CleanStatus = 'Reviewed';
         }
      }
    }
  }

```
**•** Create a customized set of `Industry` field values for accounts. Use triggers to map values from fields on imported or cleaned
records onto a standard set of values.

**•** Read the `CleanStatus` field value on the Account object. If that value is `Different, but a Salesforce record has no street`
address value, update the record’s status to `Not Compared.`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AccountCleanInfoChangeEvent (API version 62.0)**
Change events are available for the object.
