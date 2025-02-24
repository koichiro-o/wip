#### DatacloudDandBCompany

Represents a set of read-only fields that are used to return D&B company data from Data.com API calls. This object is available in API
version 30.0 or later.


-----

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
City
CompanyCurrencyIsoCode
CompanyId
Country

```

**Type**
string

**Properties**
Nillable

**Description**

The name of the city where the company is physically located.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The code used to represent a company’s local currency. This data is provided by
the International Organization for Standardization (ISO) and is based on their
three-letter currency codes. For example, USD is the ISO code for United States
Dollar.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique numeric identifier for a company.

**Type**
string

**Properties**
Nillable


-----

```
CountryAccessCode
CurrencyCode
Description
DomesticUltimateBusinessName
DomesticUltimateDunsNumber

```

**Description**

The country where a company is physically located.

**Type**
string

**Properties**
Nillable

**Description**

The required code for international calls.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The currency in which the company’s sales volume is expressed.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of the company, which may include information about its
history, its products and services, and its influence on a particular industry.

**Type**
string

**Properties**
Nillable

**Description**

The primary name of the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.

**Type**
string

**Properties**
Nillable

**Description**

The D-U-N-S number for the Domestic Ultimate, which is the highest-ranking
subsidiary, specified by country, within an organization’s corporate structure.


-----

```
DunsNumber
EmployeeQuantityGrowthRate
EmployeesHere
EmployeesHereReliability
EmployeesTotal

```

**Type**
string

**Properties**
Filter, Nillable

**Description**

The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking.

**Type**
double

**Properties**
Nillable

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
double

**Properties**
Nillable

**Description**

The number of employees at a specified location, such as a branch location.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The reliability of the EmployeesHere figure. Available values are `Actual`
```
  number, Low, Estimated (for all records), Modeled (for
  non-US records). A blank value indicates this data is unavailable.

```
**Type**
double

**Properties**
Nillable


-----

```
EmployeesTotalReliability
ExternalId
FamilyMembers
Fax
FifthNaics

```

**Description**

The total number of employees in the company, including all subsidiary and
branch locations. This data is available only on records that have a value of
`Headquarters/Parent` in the LocationStatus field.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The reliability of the EmployeesTotal figure. Available values are Actual
```
  number, Low, Estimated (for all records), Modeled (for
  non-US records). A blank value indicates this data is unavailable.

```
**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A system generated numeric identification.

**Type**
int

**Properties**
Nillable

**Description**

The total number of family members, worldwide, within an organization, including
the Global Ultimate, its subsidiaries (if any), and its branches (if any).

**Type**
phone

**Properties**
Nillable

**Description**

The company’s facsimile number.

**Type**
string

**Properties**
Nillable


-----

```
FifthNaicsDesc
FifthSic
FifthSic8
FifthSic8Desc
FifthSicDesc

```

**Description**

A NAICS code that’s used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

A Standard Industrial Classification (SIC) code that’s used to further classify an
organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable


-----

```
FipsMsaCode
FipsMsaDesc
FortuneRank
FourthNaics
FourthNaicsDesc

```

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable

**Description**

The Federal Information Processing Standards (FIPS) and the Metropolitan
Statistical Area (MSA) codes identify the organization’s location. The MSA codes
are defined by the US Office of Management and Budget.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s FIPS MSA code.

**Type**
int

**Properties**
Defaulted on create, Group, Nillable

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable


-----

```
FourthSic
FourthSic8
FourthSic8Desc
FourthSicDesc
GeoCodeAccuracy

```

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

**Type**
string

**Properties**
Group, Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
picklist

**Properties**
Nillable, Restricted picklist


-----

```
GlobalUltimateBusinessName
GlobalUltimateDunsNumber
GlobalUltimateTotalEmployees
ImportExportAgent

```

**Description**

The level of accuracy of a location’s geographical coordinates compared with its
physical address. Available values include `Rooftop level,` `Street`
```
  level, Block level, Census tract level, Mailing address
  level, ZIP code level, Geocode could not be assigned,
  Places the address in the correct city, Not matched,
  State or Province Centroid, Street intersection, PO
  BOX location, Non-US rooftop accuracy, County Centroid,
  Sub Locality-Street Level, and Locality Centroid

```
**Type**
string

**Properties**
Nillable

**Description**

The primary name of the Global Ultimate, which is the highest entity within an
organization’s corporate structure and may oversee branches and subsidiaries.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The D-U-N-S number of the Global Ultimate, which is the highest-ranking entity
within an organization’s corporate structure and can oversee branches and
subsidiaries.

**Type**
double

**Properties**
Nillable

**Description**

The total number of employees at the Global Ultimate, which is the highest entity
within an organization’s corporate structure and may oversee branches and
subsidiaries.

**Type**
picklist

**Properties**
Nillable, Restricted picklist


-----

```
IncludedInSnP500
Industry
IsOwned
IsParent
Latitude

```

**Description**

Identifies whether a business imports goods or services, exports goods or services,
and/or is an agent for goods.

**Type**
string

**Properties**
Group, Nillable

**Description**
A true or false value. If true, the company is listed in the S&P 500 Index. If
```
  false, the company isn’t listed in the S&P 500 Index.

```
**Type**
string

**Properties**
Group, Nillable

**Description**
A description of the type of industry such as Telecommunications, Agriculture,
or Electronics.

**Type**
boolean

**Properties**
Defaulted on create

**Description**

A true or false value. True, your organization owns the record. False, your
organization doesn’t own the record.

**Type**
boolean

**Properties**
Defaulted on create,

**Description**
A true or false value. True, the company is a parent company. False, the company
isn’t a parent company. A parent company owns other companies.

**Type**
string

**Properties**
Nillable


-----

```
LegalStatus
LocationStatus
Longitude

```

**Description**

Used with longitude to specify a precise location, which is used to assess the
Geocode Accuracy.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Identifies the legal structure of an organization. Available values include
```
  Cooperative, Nonprofit organization, Local government
  body, Partnership of unknown type, and Foreign company.

```
**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**

Identifies the organizational status of a company. A numeric value represents
each value.

**Organizational status** **Numeric value**
```
  Single location: The business 0

```
has no branches or subsidiaries.
```
  Headquarters/Parent: A 1

```
parent company that owns more than
50 percent of another company. When
the company also has branches, it’s the
headquarters.
```
  Branch: A secondary location of a 2

```
business.

Note: Only the numeric value is accepted in an API request.

**Type**
string

**Properties**
Nillable


-----

```
MailingCity
MailingCountry
MailingState
MailingStreet
MailingZip

```

**Description**

Used with latitude to specify a precise location, which is used to assess the
Geocode Accuracy.

**Type**
string

**Properties**
Nillable

**Description**

The city where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The country where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The state where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The street address where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The postal zip code for the company.


-----

```
MarketingPreScreen
MarketingSegmentationCluster
MinorityOwned
Name
NationalId

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The probability that a company pays with a significant delay compared to the
agreed terms. The risk level is based on the standard Commercial Credit Score,
and ranges from low risk to high risk. Available values are `High risk of`
```
  delinquency, Low risk of delinquency, and Moderate risk
  of delinquency.

```
Important: Use this information for marketing pre-screening purposes
only.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
Twenty-two distinct, mutually exclusive profiles, created as a result of cluster
analysis of Dun & Bradstreet data for US organizations. Available values include
```
  High-Tension Branches of Insurance/Utility
  Industries, Rapid-Growth Large Businesses,
  Labor-Intensive Giants, Spartans, Main Street USA.

```
**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether an organization is owned or controlled by a member of a
minority group.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The primary or registered name of a company.

**Type**
string


-----

```
NationalIdType
OutOfBusiness
OwnOrRent
ParentOrHqBusinessName
ParentOrHqDunsNumber

```

**Properties**
Nillable

**Description**

The identification number used in some countries for business registration and
tax collection.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

A code value that identifies the type of national identification number that’s used.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether the company at the specified address has discontinued
operations.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company owns or rents the building it occupies.

**Type**
string

**Properties**
Nillable

**Description**

The primary name of the parent or headquarters company.

**Type**
string

**Properties**
Filter, Nillable


-----

```
Phone
PremisesMeasure
PremisesMeasureReliability
PremisesMeasureUnit
PrimaryNaics

```

**Description**

The D-U-N-S number for the parent or headquarters.

**Type**
phone

**Properties**
Nillable

**Description**
A company’s primary telephone number.

**Type**
int

**Properties**
Group, Nillable

**Description**
A numeric value for the measurement of the premises.

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
string

**Properties**
Nillable

**Description**

The six-digit North American Industry Classification System (NAICS) code is the
standard used by business and government to classify business establishments
according to their economic activity for the purpose of collecting, analyzing, and
publishing statistical data related to the US business economy.


-----

```
PrimaryNaicsDesc
PrimarySic
PrimarySic8
PrimarySic8Desc
PrimarySicDesc

```

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on its NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

The four-digit SIC code that’s used to categorize business establishments by
industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
The eight-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
[Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 8](http://www.dnboptimizer.com/knowledge-center/optimizer-resources.html)
characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on its SIC code.


-----

```
PriorYearEmployees
PriorYearRevenue
PublicIndicator
Revenue
SalesTurnoverGrowthRate
SalesVolume

```

**Type**
int

**Properties**
Group, Nillable

**Description**

The total number of employees for the prior year.

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue for the prior year.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether ownership of the company is public or private.

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue of a company in US dollars.

**Type**
double

**Properties**
Nillable

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
double

**Properties**
Nillable


-----

```
SalesVolumeReliability
SecondNaics
SecondNaicsDesc
SecondSic
SecondSic8

```

**Description**

The total annual sales revenue in the headquarters’ local currency. Dun &
Bradstreet tracks revenue data for publicly traded companies, Global Ultimates,
Domestic Ultimates, and some headquarters.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The reliability of the SalesVolume figure.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable


-----

```
SecondSic8Desc
SecondSicDesc
SixthNaics
SixthNaicsDesc
SixthSic

```

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.


-----

```
SixthSic8
SixthSic8Desc
SixthSicDesc
SmallBusiness
State
StockExchange

```

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether the company is designated a small business as defined by the
Small Business Administration of the US government.

**Type**
string

**Properties**
Nillable

**Description**

The state where a company is physically located.

**Type**
string


-----

```
StockSymbol
Street
Subsidiary
ThirdNaics
ThirdNaicsDesc

```

**Properties**
Nillable

**Description**

The corresponding exchange for a company’s stock symbol, for example, NASDAQ
or NYSE.

**Type**
string

**Properties**
Nillable

**Description**

The abbreviation that’s used to identify publicly traded shares of a particular
stock.

**Type**
string

**Properties**
Nillable

**Description**

The street address where a company is physically located.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company is more than 50 percent owned by another
organization.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable


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
corresponding NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable


-----

```
TradeStyle2
TradeStyle3
TradeStyle4
TradeStyle5
UsTaxId

```

**Description**

A name, different from its legal name, that an organization may use for conducting
business. Similar to “Doing business as” or “DBA”.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

The identification number for the company used by the Internal Revenue Service
(IRS) in the administration of tax laws. Also referred to as Federal Taxpayer
Identification Number.


-----

```
Website
WomenOwned
YearStarted
Zip

##### Usage

```

**Type**
url

**Properties**
Filter, Group, Nillable

**Description**

An organization’s primary website address.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company is more than 50 percent owned or controlled by
a woman.

**Type**
string

**Properties**
Nillable

**Description**

The year when the company was established or the year when current ownership
or management assumed control of the company.

**Type**
string

**Properties**
Nillable

**Description**

A five or nine-digit code that’s used to help sort mail.


Use this object to return D&B Company information. These fields are read-only.

Important: DatacloudDandBCompany can’t be used in Apex test methods, because an external web service call is required to
access it. These calls are not allowed in Apex test methods.


-----
