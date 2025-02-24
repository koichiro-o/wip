#### DatacloudCompany

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
A unique number that identifies the parent DataAssessementFieldMetric record.

This is a relationship field.

**Relationship Name**
DataAssessmentFieldMetric

**Relationship Type**
Lookup

**Refers To**
DataAssessmentFieldMetric

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value in the matched field.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this value appears in this field.


Represents the fields for Data.com company records. This object is available in API version 30.0 or later.


-----

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

##### Supported Calls
```
describeLayout(), describeSObjects(), query()

 Fields

```
```
ActiveContacts
AnnualRevenue
City
CompanyId

```

**Type**
int

**Properties**
Nillable

**Description**

The number of active contacts that are associated with a company.

**Type**
currency

**Properties**
Filter, Nillable

**Description**

The amount of money that the company makes in 1 year. Annual revenue is
measured in US dollars.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The name of the city where the company is located.

**Type**
string

**Properties**
Filter, Nillable


-----

```
Country
CountryCode
Description
DunsNumber
EmployeeQuantityGrowthRate

```

**Description**

A unique numerical identifier for the company and theData.com identifier for a
company.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A string that represents the standard abbreviation for the country where the
company is located.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A standardized name for countries of the world.

**Type**
string

**Properties**
Nillable

**Description**

A brief synopsis of the company that provides a general overview of the company
and what it does.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A randomly generated nine-digit number that’s assigned by Dun & Bradstreet
(D&B) to identify unique business establishments.

**Type**
double

**Properties**
Nillable


-----

```
ExternalId
Fax
FortuneRank
FullAddress
IncludedInSnP500

```

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique numerical identifier for the company. The ExternalId is a
system-generated number.

**Type**
phone

**Properties**
Nillable

**Description**

The telephone number that’s used to send and receive faxes.

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
Group, Nillable

**Description**
The complete address of a company, including Street, City, State, and Zip.

**Type**
string

**Properties**
Group, Nillable


-----

```
Industry
IsInCrm
IsInactive
IsOwned
NaicsCode

```

**Description**
A true or false value. If true, the company is listed in the S&P 500 Index. If
```
  false, the company isn’t listed in the S&P 500 Index.

```
**Type**
string

**Properties**
Nillable

**Description**
A description of the type of industry such as Telecommunications, Agriculture,
or Electronics.

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**

Whether the record is in Salesforce (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**

A true or false response. True, the company record is not active. False, the
company record is active.

**Type**
boolean

**Properties**
Defaulted on create

**Description**

A true or false value. True, your organization owns the record. False, your
organization doesn’t own the record.

**Type**
string

**Properties**
Filter, Nillable


-----

```
NaicsDesc
Name
NumberOfEmployees
Ownership
Phone

```

**Description**

A value that represents the North American Industry Classification System (NAICS)
code. NAICS was created to provide details about a business’s service orientation.
The code descriptions are focused on what a business does.

**Type**
string

**Properties**
Nillable

**Description**

A description of the NAICS classification.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The company’s name.

**Type**
int

**Properties**
Filter, Nillable

**Description**

The number of employees working for the company.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The type of ownership of the company:

**•** `Public`

**•** `Private`

**•** `Government`

**•** `Other`

**Type**
phone


-----

```
PremisesMeasure
PremisesMeasureReliability
PremisesMeasureUnit
PriorYearEmployees
PriorYearRevenue

```

**Properties**
Nillable

**Description**

A numeric string containing the primary telephone number for the company.

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


-----

```
SalesTurnoverGrowthRate
Sic
SicCodeDesc
SicDesc
Site

```

**Type**
double

**Properties**
Nillable

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A numeric value that represents the Standard Industrial Codes (SIC). SIC is a
numbering convention that indicates what type of service a business provides.
It is a four-digit value.

**Type**
string

**Properties**
Group, Nillable

**Description**
The SIC numeric code and descsciption for a company.

**Type**
string

**Properties**
Nillable

**Description**

A description of the SIC classification.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

An organizational status of the company.

**•** Branch: a secondary location to a headquarter location

**•** Headquarter: a parent company with branches or subsidiaries

**•** Single Location: a single business with no subsidiaries or branches


-----

```
State
StateCode
Street
TickerSymbol
TradeStyle

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The two-letter standard abbreviation for a state.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A standard two-letter abbreviation for states and territories of the United States.
The state where the company is located. The abbreviation can also be a province
or other equivalent to a state, depending on the country where the company is
located.

**Type**
string

**Properties**
Nillable

**Description**

A postal address for the company.

**Type**
string

**Properties**
Nillable

**Description**

The symbol that uniquely identifies companies that are traded on public stock
exchanges.

**Type**
string

**Properties**
Nillable

**Description**

A legal name under which a company conducts business.


-----

```
UpdatedDate
Website
YearStarted
Zip

##### Usage

```

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**

The last date and time when the information for this company was updated.

**Type**
url

**Properties**
Nillable

**Description**

The standard URL for the company’s home page.

**Type**
string

**Properties**
Nillable

**Description**

The year when the company was founded.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A numeric postal code that’s designated for the address.


Use the DatacloudCompany object to search the Data.com database for companies with the specific criteria that you enter. Use this
object to find company records that you are interested in purchasing for your organization. Data.com APIs use the term “company,”
which is similar to Salesforce term “accounts.”

Important: DatacloudCompany can’t be used in Apex test methods, because an external web service call is required to access
it. These calls are not allowed in Apex test methods.
