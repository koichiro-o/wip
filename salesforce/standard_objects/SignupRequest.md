#### SignupRequest

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping rate group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shipping profile.

This field is a relationship field.

**Relationship Name**
ShippingProfile

**Relationship Type**
Lookup

**Refers To**
ShippingConfigurationSet


Represents a request for a new sign-up. SignupRequest isn’t supported in sandbox instances and will result in an error. This object is
available in API version 27.0 and later.

[Note: You’re limited to 20 sign-ups per day. To make additional sign-ups, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com)
For product, specify Sales. For topic, specify AppExchange & Managed Packages.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete()

 Fields

```
```
AuthCode
Company
ConnectedAppCallbackUrl
ConnectedAppConsumerKey

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
A one-time authorization code that can be exchanged for an OAuth access token and refresh
token using standard Salesforce APIs. It’s used with `ConnectedAppCallbackUrl` and
`ConnectedAppConsumerKey` when the specified connected app hasn’t been configured
with an X.509 certificate. The system provides this read-only field after the sign-up request
has been processed. This field is available in API version 29.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the company requesting the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
When used with ConnectedAppConsumerKey, specifies a connected app that’s approved
automatically during the sign-up creation. This field is available in API version 28.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
When used with ConnectedAppCallbackUrl, specifies a connected app that’s approved
automatically during the sign-up creation. This field is available in API version 28.0 and later.


-----

```
Country
CreatedOrgId
CreatedOrgInstance
Edition
ErrorCode

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The default value is the country of the requesting org. To override the default, enter the
two-character, uppercase ISO-3166 country code (Alpha-2 code). A complete list of the codes
[is located at https://www.iso.org/obp/ui/#search. The language of the trial org is](https://www.iso.org/obp/ui/#search)
auto-determined based on the value of this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character org ID of the trial org created. The system provides this read-only field after
the sign-up request has been processed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The server instance of the new trial org, for example, “na8.” This field is available in API version
29.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The Salesforce template that is used to create the trial org. Possible values are `Partner`
```
  Group, Professional, Partner Professional, Sales Enterprise,
  Professional TSO, Enterprise, Partner Enterprise, Service
  Professional, Enterprise TSO, Developer, and Partner Developer.

```
This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
FirstName
LastName
PreferredLanguage
ResolvedTemplateId
ShouldConnectToEnvHub

```

**Description**
The error code if the sign-up request isn’t successful. The system provides this read-only field
for support purposes.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The first name of the admin user for the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The last name of the admin user for the trial sign-up.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the trial org being created. Specify the language using a language code listed
[under Fully Supported Languages in Supported Languages in Salesforce Help. For example,](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)
use `zh_CN` for simplified Chinese. The value you select overrides the language set by the
locale. If you specify an invalid language, the org defaults to the default language of the country.
Likewise, if you specify a language that isn’t supported by the Salesforce edition associated
with your trial template, the trial org defaults to the default language of the country. This field
is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Populated during the sign-up request and for internal use by Salesforce. This field is available
in API version 35.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


-----

```
SignupEmail
SignupSource
Status
Subdomain
SuppressSignupEmails

```

**Description**
When set to true, the trial org is connected to the Environment Hub. The sign-up must take
place in the hub main org or a spoke org. This field is available in API version 35.0 and later.

**Type**
email

**Properties**
Create, Filter, Group, Sort

**Description**
The email address of the admin user for the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A user-specified description of the trial sign-up, up to 60 characters. This field is available in
API version 36.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the request. Possible values are `New,` `In Progress,` `Error, or Success.`
The default is New.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The My Domain name for the new trial org used in the org’s login and application URLs. In
Developer Edition orgs, your name must contain at least 3 characters and no more than 27
characters. In all other editions, it must be at least 3 characters and no more than 34 characters.
It can include letters, numbers, and hyphens, but you can’t start the name with a hyphen.

If you don’t choose a My Domain during sign-up, Salesforce assigns one for you based on your
company name. If you don’t like the one we set, you can change it.

[For details, see My Domain in Salesforce Help.](https://help.salesforce.com/articleView?id=domain_name_overview.htm&language=en_US)

**Type**
boolean


-----

```
TemplateId
TrialDays
TrialSourceOrgId
Username

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
When set to `true, no sign-up emails are sent when the trial org is created. This field is used`
for the Proxy Signup feature and is available in API version 29.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Trialforce template that is the basis for the trial sign-up. Salesforce
must approve the template. If you don’t specify an edition, a template ID is required.

**Type**
anyType

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
The duration of the trial sign-up in days. Must be equal to or less than the trial days for the
approved Trialforce template. If not provided, it defaults to the trial duration specified for the
Trialforce template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character org ID of the Trialforce Source Organization (TSO) from which the Trialforce
template was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The username of the admin user for the trial sign-up. It must follow the address convention
[specified in RFC822: www.w3.org/Protocols/rfc822/#z10.](http://www.w3.org/Protocols/rfc822/#z10)


-----

##### Usage

The Java class uses REST API to create a SignupRequest object. It authenticates to the Trialforce Management Organization (TMO) and
then posts a request to the SignupRequest object.

Here are the variables to specify in this example.

**•** SERVER—The name of the host server for the TMO, for example, yourInstance.salesforce.com.

**•** USERNAME—The admin username for the TMO.

**•** PASSWORD—The concatenation of the admin password and the security token for the TMO. To get an email with the security token,
from your personal settings in Salesforce, select Reset My Security Token and click Reset Security Token.

**•** CLIENT_ID—From Setup in Salesforce, in the Quick Find box, enter Apps, and then select Apps. Under Connected Apps, click New.
Enter values for the required fields (Callback URL is required, but you can initially set it to any valid URL because it’s not used). Grant
full access for the OAuth scopes in the Selected OAuth Scopes selector, and click Save. Then copy the value of Consumer Key and
use it for this variable.

**•** CLIENT_SECRET—On the same page, click Click to reveal. Then copy the value of Consumer Secret and use it for this variable.


-----

##### Error Codes

If the sign-up fails, the system generates an error code that can help you identify the cause. This table shows the most important error
codes.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**•** SignupRequestFeed–Feed tracking is available for the object.

**•** SignupRequestHistory–History is available for tracked fields of the object.


-----

**•** SignupRequestOwnerSharingRule–Sharing rules are available for the object

**•** SignupRequestShare–Sharing is available for the object.
