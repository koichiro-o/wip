#### DatacloudContact

The fields and properties for Data.com contact records. This object is available in API version 30.0 or later.


-----

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
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
CompanyId
CompanyName
ContactId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The city where the company is located.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The unique numerical identifier for the company and the Data.com company
identification number or Data.com Key.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the company.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The unique numeric identifier for this contact.


-----

```
Country
Department
Email
ExternalId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The standard abbreviation or name for the country where the company is located.

Note: You can enter a comma-separated list of countries; however, for
a country that uses a comma in its name, leave out the comma. For
example, enter “Taiwan, ROC” as Taiwan ROC.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist

**Description**

The department in the company that the contact is affiliated with. The values of
this field are fixed enumerated values.

**•** `Engineering`

**•** `Finance`

**•** `Human Resources`

**•** `IT`

**•** `Marketing`

**•** `Operations`

**•** `Other`

**•** `Sales`

**•** `Support`

**Type**
email

**Properties**
Filter, Nillable

**Description**

A business email address for the contact.

**Type**
string

**Properties**
Filter, Nillable, Sort


-----

```
FirstName
IsInCrm
IsInactive
IsOwned
LastName

```

**Description**

A unique system-generated numerical identifier for the contact.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The first name of the contact.

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
Whether the record is active (false) or not (true).

**Type**
boolean

**Properties**
Defaulted on create

**Description**

**•** `True: You own this record.`

**•** `False: You do not own this record.`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The last name of the contact.


-----

```
Level
Phone
SocialHandles
State
Street

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A human resource label that designates a person’s level in the company. The
values of this field are fixed enumerated values.

**•** `C-Level`

**•** `VP`

**•** `Director`

**•** `Manager`

**•** `Staff`

**•** `Other`

**Type**
phone

**Properties**
Nillable

**Description**
The direct-dial telephone number for the contact.

**Type**
string

**Description**
The social handles for this contact. Social handles are a normalized URL and user
name for social media accounts such as, LinkedIn, Facebook, and Twitter. This
field is response-only.

The DatacloudSocialHandles object is a child of the DatacloudContact object.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The state where the company is located, which can also be a province or other
equivalent to a state, depending on the country where the company is located.

**Type**
string


-----

```
Title
UpdatedDate
Zip

##### Usage

```

**Properties**
Nillable

**Description**

The street address for the company where the contact works.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Title of the contact such as CEO or Vice President.

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**

The last date and time when the information for a contact was updated.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The postal or zip code for the address.


This object searches the Data.com database for contacts with the specific criteria that you enter. Use this object to find contact records
that you are interested in purchasing for your organization.

Important: DatacloudContact can’t be used in Apex test methods, because an external web service call is required to access it.
These calls are not allowed in Apex test methods.
