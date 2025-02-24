#### DandBCompany

```

**Description**
Required. Represents the individual object related to this customer record.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total revenue amount gained from this customer.


Represents a Dun & Bradstreet[®] company record, which is associated with an account added from Data.com. This object is available in
API version 25.0 and later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Warning: You can update fields in the DandBCompany object; however, field changes may be overwritten by Data.com Clean
jobs or by using the Data.com Clean button.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Only organizations with Data.com Premium Prospector or Data.com Premium Clean can access this object.


-----

##### Fields

**Field Name**
```
Address
City
CompanyCurrencyIsoCode
Country
CountryAccessCode

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where a company is physically located. Maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The code used to represent a company’s local currency. This data is provided by
the International Organization for Standardization (ISO) and is based on their
three-letter currency codes. For example, USD is the ISO code for United States
Dollar. Maximum size is 3 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where a company is physically located. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The required code for international calls. Maximum size is 4 characters.


-----

```
CurrencyCode
Description
DomesticUltimateBusinessName
DomesticUltimateDunsNumber
DunsNumber

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency in which the company’s sales volume is expressed. The full list of
values can be found at the Optimizer Resources page maintained by Dun &
Bradstreet. Maximum size is 4 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A brief description of the company, which may include information about its
history, its products and services, and its influence on a particular industry.
Maximum size is 32000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.
Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number for the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.
Maximum size is 9 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
EmployeeQuantityGrowthRate
EmployeesHere
EmployeesHereReliability
EmployeesTotal

```

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking. Maximum size is 9 characters.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of employees at a specified location, such as a branch location.
Maximum size is 15 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `EmployeesHere` figure. Available values include:

**•** 0—Actual number

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of employees in the company, including all subsidiary and
branch locations. This data is only available on records that have a value of


-----

```
EmployeesTotalReliability
FamilyMembers
Fax
FifthNaics
FifthNaicsDesc

```

`Headquarters/Parent` in the LocationStatus field. Maximum size
is 15 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `EmployeesTotal` figure. Available values include:

**•** 0—Actual number

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

A blank value indicates this data is unavailable.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of family members, worldwide, within an organization, including
the Global Ultimate, its subsidiaries (if any), and its branches (if any). Maximum
size is 5 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company’s facsimile number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string


-----

```
FifthSic
FifthSic8
FifthSic8Desc
FifthSicDesc
FipsMsaCode

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
FipsMsaDesc
FortuneRank
FourthNaics
FourthNaicsDesc
FourthSic

```

**Description**
The Federal Information Processing Standards (FIPS) and the Metropolitan
Statistical Area (MSA) codes identify the organization’s location. The MSA codes
are defined by the US Office of Management and Budget. Maximum size is 5
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s FIPS MSA code. Maximum size is 255
characters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
FourthSic8
FourthSic8Desc
FourthSicDesc
GeoCodeAccuracy

```

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Available values include:

**•** A – `Non-US rooftop accuracy`

**•** B – `Block level`

**•** C – `Places the address in the correct city`

**•** D – `Rooftop level`

**•** I – `Street intersection`

**•** M – `Mailing address level`


-----

```
GlobalUltimateBusinessName
GlobalUltimateDunsNumber
GlobalUltimateTotalEmployees
ImportExportAgent

```


**•** N – `Not matched`

**•** P – `PO BOX location`

**•** S – `Street level`

**•** T – `Census tract level`

**•** Z – `ZIP code level`

**•** 0 (zero)– `Geocode could not be assigned`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the Global Ultimate, which is the highest entity within an
organization’s corporate structure and may oversee branches and subsidiaries.
Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number of the Global Ultimate, which is the highest entity within
an organization’s corporate structure and may oversee branches and subsidiaries.
Maximum size is 9 characters.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of employees at the Global Ultimate, which is the highest entity
within an organization’s corporate structure and may oversee branches and
subsidiaries. Maximum size is 15 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies whether a business imports goods or services, exports goods or services,
and/or is an agent for goods. Available values include:

**•** A—Importer/exporter/agent


-----

```
IncludedInSnP500
Latitude
LegalStatus
LocationStatus

```


**•** B—Importer/exporter

**•** C—Importer

**•** D—Importer/agent

**•** E—Exporter/agent

**•** F—Agent (keeps no inventory and does not take title goods)

**•** G—None or data not available

**•** H—Exporter

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A true or false value. If `true, the company is listed in the S&P 500 Index. If`
```
  false, the company isn’t listed in the S&P 500 Index.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with longitude to specify a precise location, which is then used to assess
the Geocode Accuracy. Maximum size is 11 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies the legal structure of an organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies the organizational status of a company. Available values are `Single`
```
  location, Headquarters/Parent, and Branch. Available values

```
include:

**•** 0—Single location (no other entities report to the business)

**•** 1—Headquarters/parent (branches and/or subsidiaries report to the business)


-----

```
Longitude
MailingAddress
MailingCity
MailingCountry
MailingPostalCode

```


**•** 2—Branch (secondary location to a headquarters location)

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with latitude to specify a precise location, which is then used to assess the
Geocode Accuracy. Maximum size is 11 characters.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the mailing address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where a company has its mail delivered. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where a company has its mail delivered. Maximum size is 40
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code that a company uses on its mailing address. Maximum size is 20
characters.


-----

```
MailingState
MailingStreet
MarketingPreScreen
MarketingSegmentationCluster
MinorityOwned

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where a company has its mail delivered. Maximum size is 20 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where a company has its mail delivered. Maximum size is 255
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The probability that a company will pay with a significant delay compared to the
agreed terms. The risk level is based on the standard Commercial Credit Score,
and ranges from low risk to high risk. Available values include:

**•** L—Low risk of delinquency

**•** M—Moderate risk of delinquency

**•** H—High risk of delinquency

Important: Use this information for marketing pre-screening purposes
only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Twenty-two distinct, mutually exclusive profiles, created as a result of cluster
analysis of Dun & Bradstreet data for US organizations.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
Name
NationalId
NationalIdType
OutOfBusiness
OwnOrRent

```

**Description**
Indicates whether an organization is owned or controlled by a member of a
minority group. Available values include:

**•** Y—Minority owned

**•** N—Not minority owned

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The primary or registered name of a company. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identification number used in some countries for business registration and
tax collection. Maximum size is 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
A code value that identifies the type of national identification number used. The
full list of resources can be found at the Optimizer Resources page maintained
by Dun & Bradstreet. Maximum size is 5 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the company at the specified address has discontinued
operations. Available values include:

**•** Y—Out of business

**•** N—Not out of business

**Type**
picklist


-----

```
ParentOrHqBusinessName
ParentOrHqDunsNumber
Phone
PostalCode
PremisesMeasure

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company owns or rents the building it occupies. Available
values include:

**•** 0—Unknown or not applicable

**•** 1—Owns

**•** 2—Rents

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the parent or headquarters company. Maximum size is 255
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number for the parent or headquarters. Maximum size is 9 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A company’s primary telephone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code that corresponds to a company’s physical location. Maximum
size is 20 characters.

**Type**
int


-----

```
PremisesMeasureReliability
PremisesMeasureUnit
PrimaryNaics
PrimaryNaicsDesc
PrimarySic

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A numeric value for the measurement of the premises.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The six-digit North American Industry Classification System (NAICS) code is the
standard used by business and government to classify business establishments
according to their economic activity for the purpose of collecting, analyzing, and
publishing statistical data related to the US business economy. The full list of
values can be found at the Optimizer Resources page maintained by Dun &
Bradstreet. Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its NAICS code.
Maximum size is 120 characters.

**Type**
string


-----

```
PrimarySic8
PrimarySic8Desc
PrimarySicDesc
PriorYearEmployees

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The four-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 4
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The eight-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 8
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its SIC code.
The full list of values can be found at the Optimizer Resources page maintained
by Dun & Bradstreet. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its SIC code.
Maximum size is 80 characters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of employees for the prior year.


-----

```
PriorYearRevenue
PublicIndicator
SalesTurnoverGrowthRate
SalesVolume
SalesVolumeReliability

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The annual revenue for the prior year.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether ownership of the company is public or private. Available values
include:

**•** Y—Public

**•** N—Private

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total annual sales revenue in the headquarters’ local currency. Dun &
Bradstreet tracks revenue data for publicly traded companies, Global Ultimates,
Domestic Ultimates, and some headquarters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `SalesVolume` figure. Available values include:

**•** 0—Actual number


-----

```
SecondNaics
SecondNaicsDesc
SecondSic
SecondSic8
SecondSic8Desc

```


**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
SecondSicDesc
SixthNaics
SixthNaicsDesc
SixthSic
SixthSic8

```

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
SixthSic8Desc
SixthSicDesc
SmallBusiness
State
StockExchange

```

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the company is designated a small business as defined by the
Small Business Administration of the US government. Available values include:

**•** Y—Small business site

**•** N—Not small business site

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where a company is physically located. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
StockSymbol
Street
Subsidiary
ThirdNaics
ThirdNaicsDesc

```

**Description**
The corresponding exchange for a company’s stock symbol. For example: NASDAQ
or NYSE. Maximum size is 16 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The abbreviation used to identify publicly traded shares of a particular stock.
Maximum size is 6 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where a company is physically located. Maximum size is 255
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company is more than 50 percent owned by another
organization. Available values include:

**•** 0—Not subsidiary of another organization

**•** 3—Subsidiary of another organization

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ThirdSic
ThirdSic8
ThirdSic8Desc
ThirdSicDesc
TradeStyle1

```

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
TradeStyle2
TradeStyle3
TradeStyle4
TradeStyle5
URL
UsTaxId

```

**Description**
A name, different from its legal name, that an organization may use for conducting
business. Similar to “Doing business as” or “DBA”. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An organization’s primary website address. Maximum size is 104 characters.

**Type**
string


-----

```
WomenOwned
YearStarted

##### Usage

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identification number for the company used by the Internal Revenue Service
(IRS) in the administration of tax laws. Also referred to as Federal Taxpayer
Identification Number. Maximum size is 9 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company is more than 50 percent owned or controlled by
a woman. Available values include:

**•** Y—Owned by a woman

**•** N—Not owned by a woman, or unknown

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The year the company was established or the year when current ownership or
management assumed control of the company. Maximum size is 4 characters.


Use this object to manage D&B Company records in your organization.
