#### Organization

Represents key configuration information for an organization.

Executing a SOQL SELECT query returns the value of fields in this object, but no value is visible for some of the fields.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields


`Address` (beta)
```
AllowsSelfServiceLogin
City
ComplianceBccEmail

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address
Compound Fields for details on compound address fields.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Update

**Description**
Indicates whether the organization allows Self-Service login (true)
or not (false).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Name of the city for the organization's address.

**Type**
email


-----

```
Country
CountryCode
DailyWebToCaseCount
DailyWebToCaseLimit
DailyWebToLeadCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for compliance blind carbon copies. Limit: 80
characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the country for the organization's address. Limit: 80
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the organization’s address. Enable state
and country/territory picklists to use this field. For more information,
[see Enable and Disable State and Country/Territory Picklists in](https://help.salesforce.com/s/articleView?id=sf.admin_state_country_picklist_enable.htm&type=5&language=en_US)
Salesforce Help.

**Type**
int

**Properties**
Filter, Nillable

**Description**
The number of web form submissions that have been converted to
cases for the day.

**Type**
int

**Properties**
Filter, Nillable

**Description**
The maximum number of web form submissions that can be
converted to cases per day.

**Type**
int


-----

```
DailyWebToLeadLimit
DefaultAccountAccess
DefaultAccountAndContactAccess

```

**Properties**
Filter, Nillable

**Description**
The number of web form submission that have been converted to
leads for the day

**Type**
int

**Properties**
Filter, Nillable

**Description**
The maximum number of web form submissions that can be
converted to leads per day.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
In API version 10.0 and later, represents the default access level for
accounts, contracts, and assets. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

In versions before 10.0,
```
  DefaultAccountAndContactAccess represented this

```
value.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Default access level for accounts, contacts, contracts, and assets.
This field is supported for backward compatibility only and is not
available in API version 10.0 or later. In version 10.0 and later, use
either DefaultAccountAccess or
```
  DefaultContactAccess.

```

-----

```
DefaultCalendarAccess
DefaultCampaignAccess
DefaultCaseAccess
DefaultContactAccess

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for calendars. The possible values are listed,
followed by the user interface labels in parentheses:

**•** `HideDetails` (Hide Details)

**•** `HideDetailsInsert` (Hide Details and Add Events)

**•** `ShowDetails` (Show Details)

**•** `ShowDetailsInsert` (Show Details and Add Events)

**•** `AllowEdits` (Full Access)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for campaigns. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for cases. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ReadEditTransfer`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
DefaultLeadAccess
DefaultLocaleSidKey
DefaultOpportunityAccess

```

**Description**
Default access level for contacts. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ControlledByParent`

In versions before 10.0,
```
  DefaultAccountAndContactAccess represented this

```
value.

Note: When `DefaultContactAccess` is set to
“Controlled by Parent,” you can’t update the
```
    ContactAccessLevel field.

```
**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for leads. The possible values are:

**•** `NoneRead`

**•** `Edit`

**•** `ReadEditTransfer`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Default locale SID key.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for opportunities. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ControlledByLeadOrContact`


-----

```
DefaultPricebookAccess
DefaultTerritoryCaseAccess
DefaultTerritoryContactAccess

```


**•** `ControlledByCampaign`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default access level for price books. The possible values are listed,
followed by the user interface labels in parentheses:

**•** `None` (No access)

**•** `Read` (Read only)

**•** `ReadSelect` (Use)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Default access level for cases associated with accounts in territories.
The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Default access level for contacts associated with accounts in
territories. The possible values are:

**•** `NoneRead`

**•** `Edit`

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

Note: When `DefaultContactAccess` is set to
“Controlled by Parent” you can’t update this field.


-----

```
DefaultTerritoryOppAccess
Division
Fax
FiscalYearStartMonth
HomepageHtml

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Default access level for opportunities in territories.

Valid values:

**•** `NoneRead`

**•** `Edit`

**•** `ControlledByLeadOrContact`

**•** `ControlledByCampaign`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The name of the division for this organization. This field is not related
to the Division object.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Fax number. Limit: 40 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number that corresponds to the month that this organization's fiscal
year starts.

**Type**
textarea

**Properties**
Nillable, Update


-----

```
InstanceName
IsSandbox
LanguageLocaleKey
LastWebToCaseDate
LastWebToLeadDate

```

**Description**
The Home tab custom links and company message for this
organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. The name of the instance. Available in API version 31.0
or later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the current organization is a sandbox
(true) or production (false) instance. Available in API version
31.0 or later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The same as Language, the two-to-five character code which
represents the language and locale ISO code. This controls the
language for labels displayed in an application.

**Type**
dateTime

**Properties**
Filter, Nillable

**Description**
The last date that a web form submission was converted to a case.

**Type**
dateTime

**Properties**
Filter, Nillable


-----

```
Latitude
Longitude
MaxActionsPerRule
MaxRulesPerEntity
MonthlyPageViewsEntitlement

```

**Description**
The last date that a web form submission was converted to a lead.

**Type**
double

**Properties**
Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –90 and 90 up to
15 decimal places. For details on geolocation compound fields, see
Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –180 and 180 up
to 15 decimal places. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
int

**Properties**
Filter, Nillable

**Description**
Maximum number of actions per workflow, assignment, escalation,
and auto-response rules. This field is unavailable in version 15.0 and
later.

**Type**
int

**Properties**
Filter, Nillable

**Description**
Maximum number of rules per object, inclusive of workflow,
assignment, escalation, and auto-response rules. This field is
unavailable in version 15.0 and later.

**Type**
int


-----

```
MonthlyPageViewsUsed
Name
NamespacePrefix

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of page views allowed for the current calendar month
for the sites in your organization. To access this field, Salesforce Sites
must be enabled for your organization.This field is generally available
in API versions 18.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of page views used in the current calendar month for
the sites in your organization. To access this field, Salesforce Sites
must be enabled for your organization. This field is generally available
in API versions 18.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The name of the organization.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each
Developer Edition org that creates a managed package has a unique
namespace prefix. Limit: 15 characters. You can refer to a component
in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the
namespace prefix of the org for all objects that support it, unless
an object is in an installed managed package. In that case, the
object has the namespace prefix of the installed managed
package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.


-----

```
OrganizationType
Phone
PostalCode
PreferencesEventScheduler
PreferencesRequireOpportunityProducts

```


**•** In orgs that are not Developer Edition orgs,
`NamespacePrefix` is set only for objects that are part of
an installed managed package. All other objects have no
namespace prefix.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Edition of the organization, for example Enterprise Edition or
Unlimited Edition.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Phone number for the organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the address of the organization. Limit: 20 characters.

**Type**
boolean

**Properties**
Update

**Description**
Indicates whether opportunities require products (true) or not
(false).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether opportunities require products (true) or not
(false).


-----

```
PreferencesS1BrowserEnabled
PreferencesTerminateOldestSession
PreferencesTransactionSecurityPolicy
PrimaryContact
ReceivesAdminInfoEmails

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the Salesforce mobile web is enabled for all users
in your organization (true) or is disabled for all users (false).

This field is available in API version 29.0 or later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the oldest login session is automatically closed
when a policy specifying the maximum number of sessions is
triggered.

This field is available in API version 35.0 or later.

Note: As of API version 50.0, this field is removed.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the Transaction Security feature has been enabled.

This field is available in API version 35.0 or later.

Note: As of API version 50.0, this field is removed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Name of the primary contact for the organization. Limit: 80
characters.

**Type**
boolean


-----

```
ReceivesInfoEmails
SelfServiceCasePlural
SelfServiceCaseSingle
SelfServiceCaseSubmitRecordTypeId
SelfServicDefaultCaseOrigin

```

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the organization receives administrator emails
(true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the organization receives informational email
from Salesforce (true) or not (false).

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The plural version of the term used to represent the Case object in
the Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The singular version of the term used to represent the Case object
in the Self-Service portal.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the record type associated with a case submitted via the
Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update


-----

```
SelfServiceEmailSenderAddress
SelfServiceEmailSenderName
SelfServiceEmailUserOnCaseCreationTemplateId
SelfServiceEnabledForResponseRules
SelfServiceFeatureConfig

```

**Description**
The default origin of a case submitted via the Self-Service portal.

**Type**
email

**Properties**
Filter, Nillable, Update

**Description**
The Self-Service email address from which new Self-Service user and
password email messages are sent, such as support@acme.com.

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The name associated with the email address in the
```
  SelfServiceEmailSenderAddress field, such as Acme
  Customer Support.

```
**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when email is sent to a Self-Service
user when he or she creates a case.

**Type**
boolean

**Properties**
Filter, Nillable, Update

**Description**
Indicates whether the Self-Service portal is enabled for auto-response
rules (true) or not (false).

**Type**
int

**Properties**
Filter, Nillable, Update


-----

```
SelfServiceLogoutUrl
SelfServiceMaxNumSuggestions
SelfServiceNewCommentCheckedByDefault
SelfServiceNewCommentTemplateId
SelfServiceNewPassTemplateId

```

**Description**
An integer representing the active Self-Service feature configuration
for this organization.

**Type**
url

**Properties**
Filter, Nillable, Update

**Description**
The Web page that displays when a Self-Service user logs out of the
Self-Service portal.

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
The maximum number of suggested solutions allowed for a
Self-Service case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Update

**Description**
If `true, When a customer notification is automatically sent when`
a new comment is added to a case.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used to send a notification to
Self-Service users when a public comment is added to one of their
cases.

**Type**
reference

**Properties**
Filter, Nillable, Update


-----

```
SelfServiceNewUserTemplateId
SelfServicePageHeight
SelfServicePageWidth
SelfServiceSelfClosedCaseStatus
SelfServiceSolutionCategoryAvailable

```

**Description**
The ID of the email template used when new passwords are
generated for Self-Service users.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when new Self-Service users are
enabled.

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
The maximum height in pixels of Self-Service pages.

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
The maximum width in pixels of Self-Service pages.

**Type**
picklist

**Properties**
Filter, Nillable, Update

**Description**
The default status for cases closed by Self-Service users.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Update

**Description**
Indicates whether solution categories are available in the Self-Service
portal (true) or not (false).


-----

```
SelfServiceSolutionCategoryStartNodeId
SelfServiceSolutionPlural
SelfServiceSolutionSingle
SelfServiceStyleSheetUrl
SelfServiceWelcomePageConfig
SelfServiceWelcomeText

```

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the top-level category in the Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The plural version of the term used to represent the Solution object
in the Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
The singular version of the term used to represent the Solution object
in the Self-Service portal.

**Type**
url

**Properties**
Filter, Nillable, Update

**Description**
The public URL of your organization's Self-Service portal stylesheet.

**Type**
int

**Properties**
Filter, Nillable, Update

**Description**
Integer that represents the welcome page configuration for the
Self-Service portal.

**Type**
string

**Properties**
Filter, Nillable, Update


-----

```
SignupCountryIsoCode
State
StateCode
Street
TrialExpirationDate
TimeZoneSidKey

```

**Description**
The custom welcome message displayed at the top of the
Self-Service home page when Self-Service users log in. Limit: 32,000
characters.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO country code specified by the user for a sign-up request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
State of the address of the organization. Limit: 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the organization’s address.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Street address for the organization. Limit: 255 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that this organization's trial license expires.

**Type**
picklist


-----

```
UiSkin
UsesStartDateAsFiscalYearName
UsesWebToCase
UsesWebToLead
WebToCaseAssignedEmailTemplateId

```

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Identifies the default time zone of the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort,
Update

**Description**
The user interface theme selected for the organization.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the calendar year when the fiscal year begins is
referred to as the year of the company's fiscal year (true) or not
(false). For example, if the fiscal year begins in February 2006, a
`true` value means the fiscal year is FY2006, and a `false` value
means the fiscal year is FY2007.

**Type**
boolean

**Properties**
Filter, Nillable, Update

**Description**
Indicates whether this organization can use Web-to-Case (true)
or not (false).

**Type**
boolean

**Properties**
Filter, Nillable, Update

**Description**
Indicates whether this organization can use Web-to-Lead (true)
or not (false).

**Type**
reference


-----

```
WebToCaseCreatedEmailTemplateId
WebToCaseDefaultCreatorId
WebToCaseDefaultOrigin

##### Usage

```

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when a new case is assigned to
a user via Web-to-Case.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the email template used when a new case is created via
Web-to-Case.

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID of the user specified as the default creator of cases created
via Web-to-Case.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The default value for the Case Origin field on cases submitted via
Web-to-Case. Limit: 40 characters.


Query this object to obtain information about an organization's settings. Only one organization object exists per organization.

SEE ALSO:

Overview of Salesforce Objects and Fields
