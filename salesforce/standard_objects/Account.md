#### Account

Represents an individual account, which is an organization or person involved with your business (such as customers, competitors, and
partners).

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), merge(),
query(), retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Experience Cloud site or Customer Portal users can access their own accounts and any account shared with them.


-----

##### Fields

**Field Name**
```
AccountNumber
AccountSource
ActivityMetricId
ActivityMetricRollupId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Account number assigned to this account (not the unique, system-generated ID assigned
during creation). Maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the account record. For example, `Advertisement` or `Trade Show.`
The source is selected from a picklist of available values, which are set by an administrator.
Each picklist value can have up to 40 characters.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.


-----

```
AnnualRevenue
BillingAddress
BillingCity
BillingCountry
BillingCountryCode

```

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Estimated annual revenue of the account.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the billing address. Read-only. For details on compound address
fields, see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the account’s billing address.


-----

```
BillingGeocodeAccuracy
BillingLatitude
BillingLongitude
BillingPostalCode
BillingState
BillingStateCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the billing address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
Compound Field Considerations and Limitations for details on geolocation compound fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. Maximum size is 80 characters.

**Type**
picklist


-----

```
BillingStreet
ChannelProgramLevelName
ChannelProgramName
CleanStatus

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the account’s billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for the billing address of this account.

**Type**
string

**Properties**
Group, Nillable

**Description**
Read only. Name of the channel program level the account has enrolled. If this account has
enrolled more than one channel program level, the oldest channel program name is displayed.

**Type**
string

**Properties**
Group, Nillable

**Description**
Read only. Name of the channel program the account has enrolled. If this account has enrolled
more than one channel program, the oldest channel program name is displayed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the record’s clean status as compared with Data.com..

Possible values are:

**•** `AcknowledgedThe label on the account record detail page is` `Reviewed.`

**•** `Different`

**•** `Inactive`

**•** `Matched—The label on the account record detail page is` `In Sync.`

**•** `NotFound`

**•** `PendingThe label on the account record detail page is` `Not Compared.`


-----

```
ConnectionReceivedId
ConnectionSentId
Description
DunsNumber

```


**•** `SelectMatch`

**•** `Skipped`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text description of the account. Limited to 32,000 KB.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit number
assigned to every business location in the Dun & Bradstreet database that has a unique,
separate, and distinct operation. D-U-N-S numbers are used by industries and organizations
around the world as a global standard for business identification and tracking. Maximum
size is 9 characters. This field is available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.


-----

```
Fax
Industry
IsCustomerPortal
IsPartner

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Fax number for the account.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An industry associated with this account. For example, `Biotechnology. Maximum size`
is 40 characters.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the account has at least one contact enabled to use the org's Experience
Cloud site or Customer Portal (true) or not (false). This field is available if Customer
Portal is enabled OR digital experiences is enabled.

If your org is enabled to use Content Security Policy (CSP) features, then this field is visible
on the Account object even if those features are later disabled.

If you change this field's value from true to false, you can disable up to 100 Experience
Cloud site or Customer Portal users associated with the account and permanently delete all
of the account's site roles and groups. You can't restore deleted site roles and groups.

Exclude this field when merging accounts.

This field can be updated in API version 16.0 and later.

Tip: We recommend that you update up to 50 contacts simultaneously when
changing the accounts on contacts enabled for an Experience Cloud site. We also
recommend that you make this update after business hours.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the account has at least one contact enabled to use the org's partner
portal (true) or not (false). This field is available if partner relationship management


-----

```
IsPersonAccount
IsPriorityRecord
Jigsaw

```

(partner portal) is enabled OR digital experiences is enabled and you have partner portal
licenses.

If you change this field's value from `true` to `false, you can disable up to 15 partner`
portal users associated with the account and permanently delete all of the account's partner
portal roles and groups. You can't restore deleted partner portal roles and groups.

Disabling a partner portal user in the Salesforce user interface or the API doesn’t change this
field's value from `true` to `false.`

Even if this field's value is `false, you can enable a contact on an account as a partner`
portal user via the API.

Exclude this field when merging accounts.

This field can be updated in API version 16.0 and later.

Tip: We recommend that you update up to 50 contacts simultaneously when
changing the accounts on contacts enabled for an Experience Cloud site. We also
recommend that you make this update after business hours.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Label is Is Person Account. Indicates whether this account has a record type of
Person Account (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the account as important (True) or not (False). The
default value is `false. Available in API version 60.0 and later.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the ID of a company in Data.com. If an account has a value in this field, it means
that the account was imported from Data.com. If the field value is `null, the account was`
not imported from Data.com. Maximum size is 20 characters. Available in API version 22.0
and later. Label is Data.com Key. This field is available on business accounts, not person
accounts.


-----

```
JigsawCompanyId
LastActivityDate
LastReferencedDate
LastViewedDate
MasterRecordId

```

Important: The Jigsaw field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Do not modify the value in the
`Jigsaw` field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the company in reference to `Jigsaw.`

Important: The Jigsaw field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
`Jigsaw` field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is one of the following, whichever is the most recent:

**•** Due date of the most recent event logged against the record.

**•** Due date of the most recently closed task associated with the record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate), but
not viewed it.

**Type**
reference


-----

```
NaicsCode
NaicsDesc
Name

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object was deleted as the result of a merge, this field contains the ID of the record that
was kept. If this object was deleted for any other reason, or has not been deleted, the value
is `null.`

This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The six-digit North American Industry Classification System (NAICS) code is the standard
used by business and government to classify business establishments into industries,
according to their economic activity for the purpose of collecting, analyzing, and publishing
statistical data related to the U.S. business economy. Maximum size is 8 characters. This field
is available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an org’s line of business, based on its NAICS code. Maximum size is 120
characters. This field is available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
NumberOfEmployees
OperatingHoursId
OwnerId

```

**Description**
Required. Label is Account Name. Name of the account. Maximum size is 255 characters.
If the account has a record type of Person Account:

**•** This value is the concatenation of the FirstName, MiddleName, LastName, and
`Suffix` of the associated person contact.

**•** You can't modify this value.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label is Employees. Number of employees working at the company represented by this
account. Maximum size is eight digits.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The operating hours associated with the account. Available only if Field Service is enabled.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this account. Default value is the user logged in to
the API to perform the create.

If you have set up account teams in your org, updating this field has different consequences
depending on your version of the API:

**•** For API version 12.0 and later, sharing records are kept, as they are for all objects.

**•** For API version before 12.0, sharing records are deleted.


-----

```
Ownership
ParentId
PersonActionCadenceAssigneeId

```


**•** For API version 16.0 and later, users must have the “Transfer Record” permission in order
to update (transfer) account ownership using this field.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Ownership type for the account, for example Private, Public, or Subsidiary.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent object, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the sales rep designated to work the lead through their assigned cadence. This
field is available in API version 47.0 and later when the Sales Engagement license is enabled.
To see this field, the user also needs the Sales Engagement User or Sales Engagement Quick
Cadence Creator user permission set.

This field is a polymorphic relationship field.


-----

```
PersonActionCadenceId
PersonActionCadenceState
PersonIndividualId

```

**Relationship Name**
PersonActionCadenceAssignee

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the lead’s assigned cadence. This field is available in API version 46.0 and later when
the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.

This is a relationship field.

**Relationship Name**
PersonActionCadence

**Refers To**
ActionCadence

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the current action cadence tracker. This field is available in API version 50.0 and
later when the Sales Engagement license is enabled. To see this field, the user also needs
the Sales Engagement User or Sales Engagement Quick Cadence Creator user permission
set.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `Initializing`

**•** `Paused`

**•** `Processing`

**•** `Running`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
PersonScheduledResumeDateTime
Phone
PhotoUrl
Rating

```

**Description**
ID of the data privacy record associated with this person’s account. This field is available if
you enabled Data Protection and Privacy in Setup.

Available in API version 42.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. This field is available in API version 54.0 and later when the Sales Engagement
license is enabled. To see this field, the user also needs the Sales Engagement User or Sales
Engagement Quick Cadence Creator user permission set.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number for this account. Maximum size is 40 characters.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance (for example,
https://yourInstance.salesforce.com/) to generate a URL to request the social network
profile image associated with the account. Generated URL returns an HTTP redirect (code
302) to the social network profile image for the account.

Blank if Social Accounts and Contacts isn't enabled for the org or if Social Accounts and
Contacts is disabled for the requesting user.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account’s prospect rating, for example Hot, Warm, or Cold.


-----

```
RecordTypeId
Salutation
ShippingAddress
ShippingCity
ShippingCountry
ShippingCountryCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record type assigned to this object.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Honorific added to the name for use in letters, etc. This field is available on person accounts.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields for
details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. City maximum size is 40 characters

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. Country maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ShippingGeocodeAccuracy
ShippingLatitude
ShippingLongitude
ShippingPostalCode
ShippingState

```

**Description**
The ISO country code for the account’s shipping address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the shipping address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with ShippingLongitude to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. For
details on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. Postal code maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. State maximum size is 80 characters.


-----

```
ShippingStateCode
ShippingStreet
Sic
SicDesc
Site
TickerSymbol

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the account’s shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address of the shipping address for this account. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Standard Industrial Classification code of the company’s main business categorization, for
example, 57340 for Electronics. Maximum of 20 characters. This field is available on business
accounts, not person accounts.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an org’s line of business, based on its SIC code. Maximum length is 80
characters. This field is available on business accounts, not person accounts.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the account’s location, for example `Headquarters` or `London. Label is`
**Account Site. Maximum of 80 characters.**

**Type**
string


-----

```
Tradestyle
Type
Website
YearStarted

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The stock market symbol for this account. Maximum of 20 characters. This field is available
on business accounts, not person accounts.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A name, different from its legal name, that an org may use for conducting business. Similar
to “Doing business as” or “DBA”. Maximum length is 255 characters. This field is available on
business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of account, for example, Customer, Competitor, or Partner.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The website of this account. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when an org was legally established. Maximum length is 4 characters. This field is
available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.


-----

##### IsPersonAccount Fields

These fields are the subset of person account fields that are contained in the child person contact record of each person account. If the
`IsPersonAccount` field has the value `false, the following fields have a null value and can't be modified. If` `true, the fields can`
be modified.

Person account fields only show when person accounts are enabled. Person accounts are disabled by default.

```
FirstName
LastName
MiddleName
PersonAssistantName
PersonAssistantPhone

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the person for a person account. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Last name of the person for a person account. Required if the record type is a person account
record type. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Middle name of the person for a person account. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s assistant name. Label is Assistant. Maximum size is 40 characters.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s assistant phone. Label is Asst. Phone. Maximum size is 40 characters.


-----

```
PersonBirthDate
PersonContactId
PersonDepartment
PersonEmail
PersonEmailBouncedDate

```

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The birthday of the contact associated with this person account. Label is Birthdate. The year
portion of the PersonBirthDate field is ignored in filter criteria, including report filters,
list view filters, and SOQL queries. For example, the following SOQL query returns person
accounts with birthdays later in the year than today:
```
  SELECT FirstName, LastName, PersonBirthDate
  FROM Account
  WHERE Birthdate > TODAY

```
**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID for the contact associated with this person account. Label is Contact ID.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The department. Label is Department. Maximum size is 80 characters.

**Type**
email

**Properties**
Create, Filter, Nillable, Update

**Description**
Email address for this person account. Label is Email.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Update

**Description**
If bounce management is activated and an email sent to the person account bounces, the
date and time the bounce occurred.


-----

```
PersonEmailBouncedReason
PersonGenderIdentity
PersonHasOptedOutOfEmail
PersonHomePhone
PersonLeadSource
PersonMailingAddress

```

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
If bounce management is activated and an email sent to the person account bounces, the
reason the bounce occurred

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The person’s internal experience of their gender, which may or may not correspond to the
person’s designated sex at birth. Label is Gender Identity.

**Type**
boolean

**Properties**
Create, Filter, Nillable, Update

**Description**
Indicates whether the person account has opted out of email (true) or not (false). Label
is Email Opt Out.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The home phone number for this person account. Label is Home Phone.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s lead source. Label is Lead Source.

**Type**
address

**Properties**
Filter, Nillable


-----

**Description**
The compound form of the person account mailing address. Read-only. For details on
compound address fields, see Address Compound Fields.

**•** `PersonMailingCity` **Type**

**•** `PersonMailingCountry` string

**•** `PersonMailingPostalCode` **Properties**
Create, Filter, Nillable, Update

**•** `PersonMailingState`
**Description**
Details about the mailing address for this person account. Labels are Mailing City, Mailing
**Country, Postal Code, and State. Maximum size for city and country is 40 characters.**
Maximum size for postal code and state is 20 characters.



**•** `PersonMailingCountryCode` **Type**

**•** `PersonMailingStateCode` picklist
**Properties**
Create, Filter, Group, Nillable, Sort, Update

```
PersonMailingGeocodeAccuracy
PersonMailingLatitude
PersonMailingLongitude

```

**Description**
The ISO country or state code for the mailing address of the person account.

**Type**
picklist

**Properties**
Retrieve, Query, Restricted picklist, Nillable

**Description**
Accuracy level of the geocode for the person’s mailing address. For details on geolocation
compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with PersonMailingLongitude to specify the precise geolocation of a person
account’s mailing address. Acceptable values are numbers between –90 and 90 with up to
15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
PersonMailingStreet
PersonMobilePhone

```

**Description**
Used with `PersonMailingLatitude` to specify the precise geolocation of a person
account’s mailing address. Acceptable values are numbers between –180 and 180 with up
to 15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations on page 19.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
The mailing street address for this person account. Label is Mailing Street. Maximum size
is 255 characters.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The mobile phone number for this person account. Label is Mobile.



**•** `PersonOtherCity` **Type**

**•** `PersonOtherCountry` string

**•** `PersonOtherPostalCode` **Properties**
Create, Filter, Nillable, Update

**•** `PersonOtherState`
**Description**
Details about the alternate address for this person account. Labels are Other City, Other
**Country, Other Zip/Postal Code, and Other State.**

**•** `PersonOtherCountryCode` **Type**

**•** `PersonOtherStateCode` picklist
**Properties**
Create, Filter, Group, Nillable, Sort, Update

```
PersonOtherLatitude

```

**Description**
The ISO country or state code for the alternate address of the person account.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
PersonOtherLongitude
PersonOtherPhone
PersonOtherStreet
PersonPronouns

```

**Description**
Used with `PersonOtherLongitude` to specify the precise geolocation of a person
account’s alternate address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `PersonOtherLatitude` to specify the precise geolocation of a person
account’s alternate address. Acceptable values are numbers between –180 and 180 with up
to 15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The alternate phone number for this person account. Label is Other Phone.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s alternate street address. Label is Other Street.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The individual’s personal pronouns, reflecting their gender identity. Others can use these
pronouns to refer to the individual in the third person. The entry is selected from a picklist
of available values, which the administrator sets. Maximum 40 characters. Label is Pronouns.

Possible values are:

**•** `He/Him`

**•** `He/They`

**•** `Not Listed`


-----

```
PersonReportsToId
PersonTitle
Suffix

```


**•** `She/Her`

**•** `She/They`

**•** `They/Them`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort Update

**Description**
ID of the person account or contact that this person account reports to.

This field doesn't appear if `enableReportsToOnPersonAccountin the`
AccountSettings metadata type is `false.`

Available in API version 62.0 and later.

This is a relationship field.

**Relationship Name**
PersonReportsTo

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s title. Label is Title. Maximum size is 80 characters. When converting a
lead to a person account, the conversion fails if the lead’s Title field contains more than 80
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name suffix of the person for a person account. Maximum size is 40 characters.


Note: If you are importing Account data into Salesforce and need to set the value for an audit field, such as `CreatedDate,`
contact Salesforce. Audit fields are automatically updated during API operations unless you request to set these fields yourself.


-----

##### Usage

Use this object to query and manage accounts in your org. Client applications can create, update, delete, or query Attachment records
associated with an account via the API.

Client applications can also create or update account objects by converting a Lead via the `convertLead()` call.

If the values in the IsPersonAccount Fields are not null, you can't change `IsPersonAccount` to `false` or an error occurs.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AccountChangeEvent (API version 44.0)**
Change events are available for the object.

**AccountFeed (API version 18.0)**
Feed tracking is available for the object.

**AccountHistory (API version 11.0)**
History is available for tracked fields of the object.

**AccountOwnerSharingRule**

Sharing rules are available for the object.

**AccountShare**

Sharing is available for the object.

SEE ALSO:

AccountShare

AccountTeamMember

_[SOAP API Developer Guide: Person Account Record Types](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/sforce_api_guidelines_personaccounts.htm)_
