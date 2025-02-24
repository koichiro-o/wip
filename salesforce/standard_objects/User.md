#### User

Represents a user in your organization.

##### Supported Calls
```
create(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), update(), upsert()

 Special Access Rules

```
**•** To create or update a User record, you must have the Manage Internal Users permission. If the user is a Customer Portal user, you
must have the Manage Customer Users permission. If the user is a partner portal user, you must have the Manage External Users
permission. But the `describeSObjects` call always returns `createable` as `true.`

**•** If digital experiences is enabled, to create or update external users for Customer Portal, partner portal, or Experience Cloud sites, you
must also have the Manage External Users permission.

**•** Information in hidden fields in a user's profile isn’t searchable by external users (with a portal profile) in an Experience Cloud site.
For example, if a user in a site has a hidden email address and an external user searches for it, the user record isn’t returned in the
search results. Hidden field values also aren’t returned when external users perform searches on nonhidden fields. So if an external
user searches for a user's name (can’t be hidden), any hidden field values associated with the user record such as a hidden email
address aren’t returned in the search results.

But internal users belonging to the same Experience Cloud site can search for and view hidden field values in search results.

**•** When requested by portal users, queries that look up to the User object, such as `owner.name` or `owner.email` sometimes
don’t return values when the portal user making the request doesn’t have Read access to the User record being queried.

The behavior depends on the number of domains associated with the lookup field. If the object can look up to more than one
domain, `owner.name` returns a value, but other detail fields don’t. For example, Case owner can look up to the User or Queue
objects. In this case, portal users can see only the value of owner.name. Other User detail fields, such as `owner.email` or
`owner.phone` don’t return a value.

If the object can look up to only a single domain, such as Account owner, then no detail fields return values, including owner.name.

**•** To change ownership of a record by updating its `OwnerId` field, you must have both the Transfer Record permission and Read
access to the User record of the new record owner.

**•** To view the `NumberOfFailedLogins` field, you must have the Manage User permission.


-----

##### Fields

**Field**
```
AboutMe
AccountId

```
`Address` (beta)
```
Alias

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Information about the user, such as areas of interest or skills. This field is available even if
Chatter is disabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Account associated with a Customer Portal user.

This field is null for Salesforce users.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address Compound Fields for details on
compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user’s alias. For example, `jsmith.`


-----

```
BadgeText
BannerPhotoUrl
CallCenterId
City
CommunityNickname
CompanyName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Experience Cloud site role, displayed on the user profile page just below the user name.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's banner photo. This field is available in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If Salesforce CRM Call Center is enabled, represents the call center that this user is assigned
to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city associated with the user. Up to 40 characters allowed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name used to identify this user in the Experience Cloud site.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ContactId
Country
CountryCode
CurrentStatus

```

**Description**
The name of the user’s company.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Contact associated with this account. The contact must have a value in the
`AccountId` field or an error occurs.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country associated with the user. Up to 80 characters allowed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code associated with the user.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text that describes what the user is working on.


-----

```
DefaultCurrencyIsoCode
DefaultDivision
DefaultGroupNotificationFrequency
DelegatedApproverId

```

Note: If you update this field, the API automatically adds a post of type
`UserStatus` on the user’s profile in Chatter.

This field is deprecated in API version 25.0. To achieve similar behavior, post to the
user directly by creating a FeedItem with the user’s ParentId.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The user's default currency setting for new records. For example, if a user in France sets
`DefaultCurrencyIsoCode` to euros, then that’s their default currency.

Only applicable for organizations that use multiple currencies.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
This record’s default division. Only applicable if divisions are enabled.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The default frequency for sending the user's Chatter group email notifications
when the user joins groups. The valid values are:

**•** `P—Email on every post`

**•** `D—Daily digests`

**•** `W—Weekly digests`

**•** `N—Never`

The default value is `N. For Professional, Enterprise, Unlimited, and Developer Edition`
organizations that existed before API version 22.0, the default value remains `D.`

This field is available in API version 21.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable,Sort, Update


-----

```
Department
DigestFrequency
Division
Email
EmailEncodingKey

```

**Description**
Id of the user who is a delegated approver for this user.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company department associated with the user.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The send frequency of the user’s Chatter personal email digest. The valid values
are:

**•** `D` = Daily

**•** `W` = Weekly

**•** `N` = Never

The default value is `D.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The division associated with this user, similar to Department, and unrelated to
```
  DefaultDivision.

```
**Type**
email

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The user’s email address.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
EmailPreferencesAutoBcc
EmployeeNumber
EndDay
Extension
Fax
FederationIdentifier

```

**Description**
Required. The email encoding for the user, such as ISO-8859-1 or UTF-8.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether the user receives copies of sent emails. This option applies only if
compliance BCC emails aren’t enabled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s employee number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time of day that the user generally stops working. Used to define the times that display
in the user’s calendar. This field is available in API version 63.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s phone extension number.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s fax number.

**Type**
string


-----

```
FirstName
ForecastEnabled
FullPhotoUrl
GeocodeAccuracy

```

**Properties**
Create, Filter, idLookup, Nillable, Sort, Update

**Description**
Indicates the value that must be listed in the `Subject` element of a Security Assertion
Markup Language (SAML) IDP certificate to authenticate the user for a client application using
single sign-on. This value must be specified if the `SAML User ID Type` is Assertion
contains Federation ID from the User record. Otherwise, this field can’t be edited.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s first name.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user is enabled for forecasts (true) or not (false). Forecast user
has access to the forecasts page.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the user's profile photo. This field is available even if Chatter is disabled.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo is uploaded, the URL returned for an older photo isn’t guaranteed to return a
photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its physical
address. A geocoding service typically provides this value based on the address’s latitude
and longitude coordinates.


-----

```
HasUserVerifiedEmail
HasUserVerifiedPhone
IndividualId
IsActive
IsPartner

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user's email is verified (true) or not (false). The default value is
```
  false. This field is available in API version 63.0 and later.

```
**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user's phone number is verified (true) or not (false). The default
value is false. This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this user. This field is available if Data Protection
and Privacy is enabled.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user has access to log in (true) or not (false). You can modify a
User's active status from the user interface or via the API.

**Type**
boolean


-----

```
IsPortalEnabled
IsPortalSelfRegistered
IsPrmSuperUser
IsProfilePhotoActive

```

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the user is a partner who has access to the partner portal (true) or not
(false). This field isn’t available for release 9.0 and later. Instead, use UserType with the
value `Partner` or `Power Partner.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an active, external, user has access to Experience Cloud sites or portals
(true) or not (false).

This field is only available if one of these conditions is true:

**•** Digital experiences is enabled and you have community or portal user licenses

**•** Portals are enabled

Note: Users with External Identity licenses can access Experience Cloud sites even
if the flag is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user is a Customer Portal user who self-registered for your organization's
Customer Portal (true) or not (false). This field isn’t available for release 9.0 and earlier.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Available for partner portal users only. Indicates whether the user has super user access in
the partner portal (true) or not (false).

This field is available in API version 24.0 and later.

Note: This field isn’t automatically enabled. Contact Salesforce to enable this field.

**Type**
boolean


-----

```
JigsawImportLimitOverride
LanguageLocaleKey
LastLoginDate
LastName

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has a profile photo (true) or not (false). This field is available
in API version 36.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data.com user’s monthly addition limit. The value must be between zero and the
organization’s monthly addition limit. Label is Data.com Monthly Addition Limit. This
field is available in API version 27.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The user’s language, such as French or Chinese (Traditional). Label is Language.

Note: In API version 47.0 and later, when using the DescribeSObjectResult API to
return PicklistEntry values from this picklist, the `active` value indicates whether
the language is in the user’s Displayed Languages (true) or the user’s Available
**Languages (false). All other languages aren’t in the returned active** value
array.

In API version 46.0 and earlier, the PicklistEntry active values indicate whether the
language is in either the user’s Displayed Languages or Available Languages lists
(true) or not in either list (false).

**Type**
dateTime

**Properties**
Filter, Sort, Nillable

**Description**
The date and time when the user last successfully logged in. This value is updated if 60
seconds elapses since the user’s last login.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
LastReferencedDate
LastViewedDate
Latitude
LocaleSidKey
Longitude

```

**Description**
Required. The user’s last name.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) but not viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the geolocation of an address. Acceptable values are
numbers between –90 and 90 up to 15 decimal places. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This field is a restricted picklist field. The value of the field affects formatting and
parsing of values, especially numeric values, in the user interface. It doesn’t affect the API.

The field values are named according to the language, and the country if necessary, using
two-letter ISO codes. The set of names is based on the ISO standard. You can also manually
set a user’s locale in the user interface, and then use that value for inserting or updating other
users via the API.

**Type**
double


-----

```
Manager
ManagerId
MediumBannerPhotoUrl
MiddleName

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the geolocation of an address. Acceptable values are
numbers between –180 and 180 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
User lookup field used to select the user's manager. This field establishes a hierarchical
relationship, preventing you from selecting a user that directly or indirectly reports to
themselves.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Id of the user who manages this user.

This is a relationship field.

**Relationship Name**
Manager

**Relationship Type**
Lookup

**Refers To**
User

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the medium-sized user profile banner photo.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
MobilePhone
Name
NumberOfFailedLogins
OfflineTrialExpirationDate
PasswordExpirationDate

```

**Description**
The user’s middle name. Maximum size is 40 characters. To enable this field, contact Salesforce
Customer Support.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s mobile device number.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and LastName. Limited to 203 characters, including
whitespaces.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of failed login attempts for the user’s account. When the maximum number of
failed login attempts is reached, the counter resets and the user’s account is locked. If there’s
a successful login before the maximum number of failed login attempts is reached, the
counter resets and the user’s account remains unlocked.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user’s Connect Offline trial expires.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Phone
PortalRole
PostalCode
ProfileId

```

**Description**
The date and time when the user’s password expires. This field is available in API version 63.0
and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s phone number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role of the user in the Customer Portal (either Executive, Manager, User, or PersonAcount).

In API version 15.0 and earlier, if you set this field to null, the system automatically included
a portal role. In API version 16.0 and above, when you set this field to null, a portal role is not
automatically created. When this field is null and a ContactId is provided, the user is
assigned to the User role.

The Update property is available in API version 43.0 and later.

The field is available if Customer Portal is enabled OR digital experiences is enabled and
Experience Cloud sites have available partner portal, Customer Portal, or High-Volume Portal
User licenses.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s postal or ZIP code. Label is Zip/Postal Code.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the user’s Profile. Use this value to cache metadata based on profile. In earlier
releases, this was `RoleId.`

If you change the user’s profile, the user’s license also changes, because every profile belongs
to exactly one user license type.


-----

```
ReceivesAdminInfoEmails
ReceivesInfoEmails
SenderEmail
SenderName
Signature

```

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user receives email for administrators from Salesforce (true) or not
(false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the user receives informational email from Salesforce (true) or not
(false).

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address used as the From address when the user sends emails. This address is the
same value shown in Setup on the My Email Settings page.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name used as the email sender when the user sends emails. This name is the same value
shown in Setup on the My Email Settings page.

**Type**
textarea


-----

```
SmallBannerPhotoUrl
SmallPhotoUrl
StartDay
State
StateCode

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The signature text added to emails. This text is the same value shown in Setup on the My
Email Settings page.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the small user profile banner photo.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the user's profile photo. This field is available even if Chatter is
disabled.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo is uploaded, the URL returned for an older photo isn’t guaranteed to return a
photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time of day that the user generally starts working. Used to define the times that display
in the user’s calendar. This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state associated with the User. Up to 80 characters allowed.

**Type**
picklist


-----

```
Street
Suffix
TimeZoneSidKey
Title
Username

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code associated with the user.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address associated with the User.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s name suffix. Maximum size is 40 characters. To enable this field, contact Salesforce
Customer Support.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This field is a restricted picklist field. A User time zone affects the offset used when
displaying or entering times in the user interface. But the API doesn’t use a User time zone
when querying or setting values.

Values for this field are named using region and key city, according to ISO standards. You
can also manually set one User time zone in the user interface, and then use that value for
creating or updating other User records via the API.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user’s business title, such as Vice President.

**Type**
string


-----

```
UserPermissionsCallCenterAutoLogin
UserPermissionsChatterAnswersUser
UserPermissionsInteractionUser
UserPermissionsJigsawProspectingUser

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Contains the name that a user enters to log in to the API or the user interface. The
value for this field must be in the form of an email address, using all lowercase characters. It
must also be unique across all organizations. If you try to create or update a User with a
duplicate value for this field, the operation is rejected.

Each inserted User also counts as a license. Every organization has a maximum number of
licenses. If you attempt to exceed the maximum number of licenses by inserting User records,
the create request is rejected.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required if Salesforce CRM Call Center is enabled. Indicates whether the user is enabled to
use the auto login feature of the call center (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the portal user is enabled to use the Chatter Answers feature (true) or
not (false). This field defaults to `false` when a Customer Portal user is created from
the API.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user can run flows or not. Label is Flow User.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
UserPermissionsKnowledgeUser
UserPermissionsLiveAgentUser
UserPermissionsMarketingUser
UserPermissionsOfflineUser
UserPermissionsSFContentUser

```

**Description**
Indicates whether the user is allocated one Data.com user license (true) or not (false).
The Data.com user lets the user add Data.com contact and lead records to Salesforce in
supported editions. Label is Data.com User.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is enabled to use Salesforce Knowledge (true) or not (false).
Label is Knowledge User.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is enabled to use Chat (true) or not (false). Label is Live
**Agent User.**

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. Indicates whether the user is enabled to manage campaigns in the user interface
(true) or not (false). Label is Marketing User.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. Indicates whether the user is enabled to use Offline Edition (true) or not (false).
Label is Offline User.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
UserPermissionsSiteforceContributorUser
UserPermissionsSiteforcePublisherUser
UserPermissionsSupportUser
UserPermissionsWirelessUser

```

**Description**
Indicates whether the user is allocated one Salesforce CRM Content User License (true) or
not (false). Label is Salesforce CRM Content User. The Salesforce CRM Content User
license grants the user access to the Salesforce CRM Content application.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is allocated one Site.com Contributor feature license (true) or
not (false). Label is Site.com Contributor User. The Site.com Contributor feature license
grants the user access to the Site.com application. Users with a Contributor license can use
Site.com Studio to edit site content only.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the user is allocated one Site.com Publisher feature license (true) or not
(false). Label is Site.com Publisher User. The Site.com Publisher feature license grants
the user access to the Site.com application. Users with a Publisher license can build and style
websites, control the layout and functionality of pages and page elements, and add and edit
content.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the user can use the Salesforce console.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required if the Wireless permission is enabled. Indicates whether the user is enabled to use
Wireless Edition (true) or not (false). Label is Wireless User.


-----

```
UserPermissionsWorkDotComUserFeature
UserPreferencesActivityRemindersPopup
UserPreferencesAllowConversationReminders
UserPreferencesApexPagesDeveloperMode

```

Note: As of November 2005, Salesforce Wireless Edition is no longer available for
purchase. You can continue to use Wireless Edition through the end of your existing
contract term if you are:

**•** A Professional Edition customer and purchased Wireless Edition before November
7, 2005.

**•** An Enterprise Edition customer who signed or renewed their Salesforce contract
before November 7, 2005.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the WDC feature is enabled for the user (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, a reminder window automatically opens when an activity reminder is due.`
Corresponds to the `Trigger alert when reminder comes due` checkbox at
the Reminders page in the personal settings in the user interface.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, voice and call reminders are displayed as notification cards in Lightning`
Experience. Corresponds to the Show conversation reminders in Lightning
`Experience` checkbox in the Activity Reminders page in the personal settings in the user
interface.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, indicates that the user has enabled developer mode for editing Visualforce`
pages and controllers.


-----

```
UserPreferencesAutoForwardCall
UserPreferencesContentEmailAsAndWhen
UserPreferencesContentNoEmail
UserPreferencesEnableAutoSubForFeeds

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the user receives Dialer calls simultaneously in their browser and on their`
forwarding number.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When false, a user with Salesforce CRM Content subscriptions receives a once-daily email
summary if activity occurs on the subscribed content, libraries, tags, or authors. To receive
email, the UserPreferencesContentNoEmail field must also be `false.`

The default value is `false.`

Note: This field is only visible when Salesforce CRM Content is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When false, a user with Salesforce CRM Content subscriptions receives email notifications
if activity occurs on the subscribed content, libraries, tags, or authors. To receive real-time
email alerts, set this field to `false` and set the
```
  UserPreferencesContentEmailAsAndWhen field to true.

```
The default value is `false.`

Note: This field is only visible when Salesforce CRM Content is enabled.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, the user automatically subscribes to feeds for any objects that the user creates.
This field is available in API version 25.0 and later.


-----

```
UserPreferencesDisableAllFeedsEmail
UserPreferencesDisableAutoSubForFeeds
UserPreferencesDisableBookmarkEmail
UserPreferencesDisableChangeCommentEmail
UserPreferencesDisableEndorsementEmail

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email for all updates to Chatter feeds, based`
on the types of feed emails and digests the user has enabled. This field is available in API
version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When false, the user automatically subscribes to feeds for any objects that the user creates.
This field is deprecated in API version 25.0 and later. Starting with API version 25.0, use
```
  UserPreferencesEnableAutoSubForFeeds to enable or disable auto-follow

```
for objects a user creates.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email every time someone comments on a`
Chatter feed item after the user has bookmarked it. This field is available in API version 24.0
and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email every time someone comments on a`
change the user has made, such as an update to their profile. This field is available in API
version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
UserPreferencesDisableFileShareNotificationsForApi
UserPreferencesDisableFollowersEmail
UserPreferencesDisableLaterCommentEmail
UserPreferencesDisableLikeEmail
UserPreferencesDisableMentionsPostEmail

```

**Description**
When `false, the member automatically receives email every time someone endorses`
them for a topic.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, email notifications are sent from the person who shared the file to the users`
that the file is shared with. This field is available in API version 25.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email every time someone starts following`
the user in Chatter. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email every time someone comments on a`
feed item after the user has commented on the feed item. This field is available in API version
24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email every time someone likes their post or`
comment. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
UserPreferencesDisableProfilePostEmail
UserPreferencesDisableSharePostEmail
UserPreferencesDisableFeedbackEmail
UserPreferencesDisCommentAfterLikeEmail
UserPreferencesDisMentionsCommentEmail

```

**Description**
When false, the user automatically receives email every time they’re mentioned in posts.
This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When false, the user automatically receives email every time someone posts to the user’s
profile. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email every time their post is shared. This`
field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives emails related to WDC feedback. The user`
receives these emails when someone requests or offers feedback, shares feedback with the
user, or reminds the user to answer a feedback request.

This field isn’t visible as of API version 54.0.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email every time someone comments on a`
post that the user liked. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
UserPreferencesDisableMessageEmail
UserPreferencesDisableRewardEmail
UserPreferencesDisableWorkEmail
UserPreferencesDisProfPostCommentEmail
UserPreferencesEnableVoiceCallRecording

```

**Description**
When `false, the user automatically receives email every time the user is mentioned in`
comments. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email for Chatter messages sent to the user.`
This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives emails related to WDC rewards. The user`
receives these emails when someone gives a reward to the user.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user receives emails related to WDC feedback, goals, and coaching. The`
user must also sign up for individual emails listed on the WDC email settings page. When
```
  true, the user doesn’t receive any emails related to WDC feedback, goals, or coaching even

```
if they’re signed up for individual emails.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `false, the user automatically receives email every time someone comments on`
posts on the user’s profile. This field is available in API version 24.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
UserPreferencesEnableVoiceLocalPresence
UserPreferencesEventRemindersCheckboxDefault
UserPreferencesHideBiggerPhotoCallout
UserPreferencesHideChatterOnboardingSplash
UserPreferencesHideCSNDesktopTask

```

**Description**
When `true, voice call recording is enabled for the user.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, local numbers are shown when the user calls customers with Sales Dialer.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, a reminder popup is automatically set on the user's events. Corresponds to
the `By default, set reminder on Events to...` checkbox on the
Reminders page in the user interface. This field is related to UserPreference and customizing
activity reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, users can choose to hide the callout text below the large profile photo.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the initial Chatter onboarding prompts don’t appear.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the Chatter recommendations panel never displays the recommendation to`
install Chatter Desktop. This field is available in API version 26.0 and later.


-----

```
UserPreferencesHideCSNGetChatterMobileTask
UserPreferencesHideEndUserOnboardingAssistantModal
UserPreferencesHideLightningMigrationModal
UserPreferencesHideSecondChatterOnboardingSplash
UserPreferencesHideS1BrowserUI
UserPreferencesHideSfxWelcomeMat

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, the Chatter recommendations panel never displays the recommendation to
install Chatter Mobile. This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the secondary Chatter onboarding prompts don’t appear.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls the interface that the user sees when logging in to Salesforce from a supported
mobile browser. If `false, the user is automatically redirected to the Salesforce mobile`
web. If `true, the user sees the full Salesforce site. The default value is false. Label is`
**Salesforce User.**

This field is available in API version 29.0 or later.

**Type**
boolean


-----

```
UserPreferencesJigsawListUser
UserPreferencesLightningExperiencePreferred
UserPreferencesLiveAgentMiawSetupDeflection
UserPreferencesNativeEmailClient

```

**Properties**
Create, Filter, Update

**Description**
Controls whether a user sees the Lightning Experience new user message. That message
welcomes users to the new interface and provides step-by-step instructions that describe
how to return to Salesforce Classic.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the user is a Data.com List user so shares record additions from a pool.`
UserPermissionsJigsawProspectingUser must also be set to `true. Label is Data.com List`
**User. This field is available in API version 27.0 and later.**

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, redirects the user to the Lightning Experience interface. Label is Switch to`
**Lightning Experience. This field is available in API version 35.0 and later.**

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, disables the pop-up to deflect users on Chat setup nodes to the Messaging`
setup. The default value is `false. This field is available in API version 59.0 and later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Use this field to set a default email preference for the user’s native email client. This field is
available in API version 47.0 and later. The default value is `false, corresponding to the`
Salesforce docked email composer.


-----

```
UserPreferencesOptOutOfTouch
UserPreferencesOutboundBridge
UserPreferencesPathAssistantCollapsed
UserPreferencesProcessAssistantCollapsed
UserPreferencesReceiveNoNotificationsAsApprover

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
This field is deprecated in API version 29.0. When `false, the user automatically accesses`
the Salesforce Touch app when logging in to Salesforce from an iPad. If `true, automatic`
access to the Salesforce Touch app is turned off and the user’s iPad is directed to the full
Salesforce site instead. The default value is false.

Note: Salesforce Touch must be enabled before this field is visible.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, outbound calls are made through the user’s phone.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, Sales Path appears collapsed or hidden to the user. This field is available in API
version 35.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, Sales Path appears collapsed or hidden to the user. This field is available in API
versions 33.0 and 34.0 only. In API versions 35.0 and later, use
```
  UserPreferencesPathAssistantCollapsed.

```
**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls email notifications from the approval process for approvers.


-----

```
UserPreferencesReceiveNotificationsAsDelegatedApprover

```


**•** If `true, emails are disabled.`

**•** If `false, emails are enabled.`

The default value is `false.`

Note: The `Receive Approval Request Emails setting in the UI`
controls this field and the
```
    UserPreferencesReceiveNotificationsAsDelegatedApprover

```
field.

**•** Setting: If I’m an approver or delegated approver

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: Only if I’m an approver

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

**•** Setting: Only if I’m a delegated approver

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: Never

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Controls email notifications from the approval process for delegated approvers.

**•** If `true, emails are enabled.`

**•** If `false, emails are disabled.`

The default value is `false.`

Note: The `Receive Approval Request Emails setting in the UI`
controls this field and the
`UserPreferencesReceiveNoNotificationsAsApprover` field.

**•** Setting: If I’m an approver or delegated approver


-----

```
UserPreferencesReminderSoundOff
UserPreferencesShowCityToExternalUsers

```

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: Only if I’m an approver

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = false

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

**•** Setting: Only if I’m a delegated approver

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = true

**•** Setting: Never

Result:

**–** UserPreferencesReceiveNoNotificationsAsApprover = true

**–** UserPreferencesReceiveNotificationsAsDelegatedApprover = false

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, a sound automatically plays when an activity reminder is due. Corresponds to
the Play a reminder sound checkbox on the Reminders page in the user interface.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the city field in the user’s contact information. City is visible only to
internal members of the user’s organization when:

**•** This field is `false. When` `false, this field returns the value #N/A.`

City is visible to external members in an Experience Cloud site when:

**•** This field is `true, or`

**•** This field is false but UserPreferencesShowCityToGuestUsers is true,
which overrides this field’s value.

External users are users with Community, Customer Portal, or partner portal licenses.


-----

```
UserPreferencesShowCityToGuestUsers
UserPreferencesShowCountryToExternalUsers
UserPreferencesShowCountryToGuestUsers

```

The default value is false. This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the city field in the user’s contact information. When `true, city is`
visible to guest users. Guest users can access public Site.com and Salesforce sites, and public
pages in Experience Cloud sites, via the Guest User license associated with each site. When
```
  false, this field returns the value #N/A.

```
When `true, this field overrides the value false` in
```
  UserPreferencesShowCityToExternalUsers, making the user’s city visible

```
to external members.

The default value is `false. This field is available in API version 28.0 and later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the country field in the user’s contact information. Country is visible
only to internal members of the user’s organization when:

**•** This field is `false. When` `false, this field returns the value #N/A.`

Country is visible to external members in an Experience Cloud site when:

**•** This field is `true, or`

**•** This field is `false` but UserPreferencesShowCountryToGuestUsers is
```
   true, which overrides this field’s value.

```
External users are users with Community, Customer Portal, or partner portal licenses.

The default value is `false. This field is available in API version 26.0 and later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the country field in the user’s contact information. When `true,`
country is visible to guest users. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license associated with each
site. When false, this field returns the value `#N/A.`


-----

```
UserPreferencesShowEmailToExternalUsers
UserPreferencesShowEmailToGuestUsers
UserPreferencesShowFaxToExternalUsers

```

When `true, this field overrides the value false` in
```
  UserPreferencesShowCountryToExternalUsers, making the user’s country

```
visible to external members.

The default value is `false. This field is available in API version 28.0 and later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the email address field in the user’s contact information. Email
address is visible only to internal members of the user’s organization when this field is false.
Email address is visible to external members in an Experience Cloud site when this field is
```
  true. External users are users with Community, Customer Portal, or partner portal licenses.

```
When false, this field returns the value `#N/A. The default value is` `false. This field is`
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the email address field in the user’s contact information. When
```
  true, the email address is visible to guest users. Guest users can access public Site.com

```
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true, this field overrides the value false` in
```
  UserPreferencesShowEmailToExternalUsers, making the user’s email address

```
visible to guests.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the fax number field in the user’s contact information. Fax number
is visible only to internal members of the user’s organization when this field is `false. Fax`
number is visible to external members in an Experience Cloud site when this field is `true.`
External users are users with Community, Customer Portal, or partner portal licenses.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 26.0 and later.


-----

```
UserPreferencesShowFaxToGuestUsers
UserPreferencesShowManagerToExternalUsers
UserPreferencesShowManagerToGuestUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the fax number field in the user’s contact information. When true,
the fax number field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true, this field overrides the value false` in
```
  UserPreferencesShowFaxToExternalUsers, making the user’s fax number

```
visible to guests.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the manager field in the user’s contact information. Manager is
visible only to internal members of the user’s organization when this field is false. Manager
is visible to external members in an Experience Cloud site when this field is `true. External`
users are users with Community, Customer Portal, or partner portal licenses.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the manager field in the user’s contact information. When `true,`
the manager field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true, this field overrides the value false` in
```
  UserPreferencesShowManagerToExternalUsers, making the user’s manager

```
visible to guests.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 34.0 and later.


-----

```
UserPreferencesShowMobilePhoneToExternalUsers
UserPreferencesShowMobilePhoneToGuestUsers
UserPreferencesShowPostalCodeToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the mobile device number field in the user’s contact information.
The number is visible only to internal members of the user’s organization when this field is
```
  false. The number is visible to external members in an Experience Cloud site when this

```
field is `true. External users are users with Community, Customer Portal, or partner portal`
licenses.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the mobile phone field in the user’s contact information. When
```
  true, the mobile phone field is visible to guest users. Guest users can access public Site.com

```
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true, this field overrides the value false` in
```
  UserPreferencesShowMobilePhoneToExternalUsers, making the user’s

```
mobile phone visible to guests.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s contact information. Postal
code is visible only to internal members of the user’s organization when:

**•** This field is `false. When` `false, this field returns the value #N/A.`

Postal code is visible to external members in an Experience Cloud site when:

**•** This field is `true, or`

**•** This field is false but UserPreferencesShowPostalCodeToGuestUsers
is `true, which overrides this field’s value.`

External users are users with Community, Customer Portal, or partner portal licenses.


-----

```
UserPreferencesShowPostalCodeToGuestUsers
UserPreferencesShowProfilePicToGuestUsers
UserPreferencesShowStateToExternalUsers

```

The default value is `false. This field is available in API version 26.0 and later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the postal or ZIP code field in the user’s contact information. When
```
  true, postal code is visible to guest users. Guest users can access public Site.com and

```
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site. When `false, this field returns the value` `#N/A.`

When `true, this field overrides the value false in`
```
  UserPreferencesShowPostalCodeToExternalUsers, making the user’s

```
postal code visible to external members.

The default value is false. This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the user’s profile photo. When true, the photo is visible to guest
users in an Experience Cloud site. Guest users can access public Site.com and Salesforce sites,
and public pages in Experience Cloud sites, via the Guest User license associated with each
site.

When false, this field returns the stock photo. The default value is false. This field is
available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the state field in the user’s contact information. State is visible only
to internal members of the user’s organization when:

**•** This field is `false. When` `false, this field returns the value #N/A.`

State is visible to external members in an Experience Cloud site when:

**•** This field is `true, or`

**•** This field is `false` but UserPreferencesShowStateToGuestUsers is
```
   true, which overrides this field’s value.

```
External users are users with Community, Customer Portal, or partner portal licenses.


-----

```
UserPreferencesShowStateToGuestUsers
UserPreferencesShowStreetAddressToExternalUsers
UserPreferencesShowStreetAddressToGuestUsers

```

When `false, this field returns the value` `#N/A. The default value is` `false. This field is`
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the state field in the user’s contact information. When `true, state`
is visible to guest users. Guest users can access public Site.com and Salesforce sites, and
public pages in Experience Cloud sites, via the Guest User license associated with each site.
When false, this field returns the value `#N/A.`

When `true, this field overrides the value false` in
UserPreferencesShowStateToExternalUsers, making the user’s state visible to external
members.

The default value is `false. This field is available in API version 28.0 and later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the street address field in the user’s contact information. The address
is visible only to internal members of the user’s organization when this field is `false. The`
address is visible to external members in an Experience Cloud site when this field is `true.`
External users are users with Community, Customer Portal, or partner portal licenses.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 26.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the street address field in the user’s contact information. When
```
  true, the street address field is visible to guest users. Guest users can access public Site.com

```
and Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true, this field overrides the value false` in
```
  UserPreferencesShowStreetAddressToExternalUsers, making the user’s

```
street address visible to guests.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 34.0 and later.


-----

```
UserPreferencesShowTitleToExternalUsers
UserPreferencesShowTitleToGuestUsers
UserPreferencesShowWorkPhoneToExternalUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the business title field in the user’s contact information. Title is visible
only to internal members of the user’s organization when:

**•** This field is `false. When` `false, this field returns the value #N/A.`

Title is visible to external members in an Experience Cloud site when:

**•** This field is `true, or`

**•** This field is `false` but UserPreferencesShowTitleToGuestUsers is
```
   true, which overrides this field’s value.

```
External users are users with Community, Customer Portal, or partner portal licenses.

The default value is `true. This field is available in API version 26.0 and later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the business title field in the user’s contact information. When true,
title is visible to guest users. Guest users can access public Site.com and Salesforce sites, and
public pages in Experience Cloud sites, via the Guest User license associated with each site.
When false, this field returns the value `#N/A.`

When `true, this field overrides the value false` in
UserPreferencesShowTitleToExternalUsers, making the user’s title visible to external members.

The default value is `false. This field is available in API version 28.0 and later.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the work phone number field in the user’s contact information. The
number is visible only to internal members of the user’s organization when this field is
```
  false. The number is visible to external members in an Experience Cloud site when this

```
field is `true. External users are users with Community, Customer Portal, or partner portal`
licenses.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 26.0 and later.


-----

```
UserPreferencesShowWorkPhoneToGuestUsers
UserPreferencesSortFeedByComment
UserPreferencesSuppressEventSFXReminders
UserPreferencesSuppressTaskSFXReminders

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates the visibility of the work phone field in the user’s contact information. When true,
the work phone field is visible to guest users. Guest users can access public Site.com and
Salesforce sites, and public pages in Experience Cloud sites, via the Guest User license
associated with each site.

When `true, this field overrides the value false` in
```
  UserPreferencesShowWorkPhoneToExternalUsers, making the user’s work

```
phone visible to guests.

When `false, this field returns the value #N/A. The default value is` `false. This field is`
available in API version 34.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies the data value used in sorting a user’s feed. When true, the feed is sorted by most
recent comment activity. When `false, the feed is sorted by post date.`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, event reminders don’t appear. Corresponds to the Show event reminders
**in Lightning Experience checkbox on the Activity Reminders page in the user interface.**
This field is related to UserPreference and customizing activity reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, task reminders don’t appear. Corresponds to the Show task reminders in
**Lightning Experience. checkbox on the Activity Reminders page in the user interface. This**
field is related to UserPreference and customizing activity reminders.


-----

```
UserPreferencesTaskRemindersCheckboxDefault
UserPreferencesUserDebugModePref
UserRoleId
UserType

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When true, a reminder popup is automatically set on the user's tasks. Corresponds to the
`By default, set reminder on Tasks to...` checkbox on the Reminders
page in the user interface. This field is related to UserPreference and customizing activity
reminders.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true, the Lightning Component framework executes in debug mode for the user.`
Corresponds to the Debug Mode checkbox on the Advanced User Details page of personal
settings in the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user’s UserRole. Label is Role ID.

This is a relationship field.

**Relationship Name**
UserRole

**Relationship Type**
Lookup

**Refers To**
UserRole

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort, Restricted picklist

**Description**

The category of user license. Each `UserType` is associated with one or more UserLicense
records. Each UserLicense is associated with one or more profiles. In API version 10.0 and
later, valid values include:


-----

```
WirelessEmail

##### Usage

```


**•** Standard: user license. This user type also includes Salesforce Platform and Salesforce
Platform One user licenses. Label is Standard.

**•** PowerPartner: User whose access is limited because they’re a partner and typically access
the application through a partner portal or Experience Cloud site. Label is Partner.

**•** CspLitePortal: user whose access is limited because they’re an org's customer and access
the application through a Customer Portal or Experience Cloud site. Label is High Volume
**Portal.**

**•** CustomerSuccess: user whose access is limited because they’re an org's customer and
access the application through a Customer Portal. Label is Customer Portal User.

**•** PowerCustomerSuccess: user whose access is limited because they’re an org's customer
and access the application through a Customer Portal. Label is Customer Portal
**Manager.**

Users with this license type can view and edit data they directly own or data owned by
or shared with users below them in the Customer Portal role hierarchy.

**•** CsnOnly: user whose access to the application is limited to Chatter. This user type includes
Chatter Free and Chatter moderator users. Label is Chatter Free.

**•** Guest: user whose access is limited because they’re an unauthenticated user without
login credentials. Label is Guest.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Wireless email address associated with this user. For use with Salesforce Wireless Edition.
This field is available only if the Wireless and Email permissions are enabled for your
organization.

Note: As of November 2005, Salesforce Wireless Edition is no longer available for
purchase. You can continue to use Wireless Edition through the end of your existing
contract term if you are:

**•** A Professional Edition customer and purchased Wireless Edition before November
7, 2005.

**•** An Enterprise Edition customer who signed or renewed their Salesforce contract
before November 7, 2005.


Use this object to query information about users and to provision and modify users in your organization. Unlike other objects, the records
in the User table represent actual users—not data owned by users. Any user can query or describe User records.


-----

For example, the following SOQL code finds users with a particular user role.
```
SELECT Id, Username
FROM User
WHERE UserRoleId='00ED0000000xicT'

```
Each portal user is associated with a portal account. A portal account can have a maximum of three portal roles (Executive, Manager,
and User). You can select the default number of roles to be created from the user interface. The role hierarchy is maintained when you
insert and delete portal roles, and roles are created bottom-up. Deleting the User role causes the Manager role to be renamed to User
role. Deleting both the Executive and User roles causes the Manager role to be renamed to User role. Before deleting a role, you must
assign users under that role to another role.

##### Deactivate Users

You can’t delete a user in the user interface or the API. You can deactivate a user in the user interface; and you can deactivate or disable
a Customer Portal or partner portal user in the user interface or the API. Because users can never be deleted, we recommend that you
exercise caution when creating them.

[Be aware of the expected behaviors when deactivating users. See Considerations for Deactivating Users. The user interface provides](https://help.salesforce.com/s/articleView?id=sf.users_deactivate_considerations.htm&language=en_US)
options to auto-remove a user from teams, but the removal isn’t supported in API.

If you deactivate a user, any EntitySubscription where the user is associated with the ParentId or SubscriberId field, meaning all subscriptions
both to and from the user, are soft deleted. If the user is reactivated, the subscriptions are restored. However, if you deactivate multiple
users at once and these users follow each other, their subscriptions are hard deleted. In this case, the user-to-user EntitySubscription is
deleted twice (double deleted). Such subscriptions can’t be restored upon user reactivation.

##### Passwords

For security reasons, you can’t query User passwords via the API or the user interface. But the API allows you to set and reset User
passwords using the `setPassword()` and `resetPassword()` calls. The password lockout status and the ability to reset the
User locked-out status isn’t available via the API. Check and reset the User password lockout status using the user interface.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserChangeEvent (API version 44.0)**
Change events are available for the object.

**UserFeed (API version 18.0)**
Feed tracking is available for the object.

**UserShare**

Sharing is available for the object.

SEE ALSO:

_[SOAP API Developer Guide: Frequently-Occurring Fields](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/sforce_api_objects_fequently_occurring_fields.htm)_

UserRole

UserLicense


-----
