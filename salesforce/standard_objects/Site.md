#### Site

Represents a public website that is integrated with an org. This object is available in API version 16.0 and later.

To access this object, Digital Experiences, Salesforce Sites, or Site.com must be enabled.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the View Setup and Configuration permission.

##### Fields

```
AdminId
AnalyticsTrackingCode

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The site administrator designated as the contact for the site. This user receives
site-related communications from site visitors and from Salesforce.

This is a relationship field.

**Relationship Name**
Admin

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking code associated with your site. This code can be used by services
like Google Analytics to track page request data for your site.


-----

```
ArchiveStatus
ArchivedById
ArchivedDate
ClickjackProtectionLevel

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The archived status of a site. Possible values are:

**•** `NotArchived`

**•** `TemporaritlyArchived`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user that archived the site.

**Relationship Name:**
ArchivedBy

**Relationship Type:**
Lookup

**Refers To:**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the site was archived.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Sets the clickjack protection level. The options are:

**•** `AllowAllFraming—Allow framing by any page (no protection)`

**•** `SameOriginOnly—Allow framing by the same origin only`
(recommended)

**•** `NoFraming—Don’t allow framing by any page (most protection)`

This field is available in API version 30.0 and later.


-----

```
DailyBandwidthLimit
DailyBandwidthUsed
DailyRequestTimeLimit
DailyRequestTimeUsed
Description
GuestRecordDefaultOwnerId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The rolling 24-hour daily bandwidth limit for the sites in your organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The current rolling 24-hour daily bandwidth usage for the sites in your
organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The rolling 24-hour daily service request time limit for the sites in your
organization. Service request time is calculated as the total server time in minutes
required to generate pages for the site.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The current rolling 24-hour daily service request time for the sites in your
organization.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
An optional description of the site.

**Type**
reference


-----

```
GuestUserId
MasterLabel
MonthlyPageViewsEntitlement

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
A user in the Salesforce org that is the default owner of records created by
unauthenticated (guest) users.

This is a relationship field.

**Relationship Name**
GuestRecordDefaultOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The site or Experience Cloud sites specific user that anonymous, unauthenticated
users run as when interacting with the site.

This is a relationship field.

**Relationship Name**
GuestUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the site as it appears in the user interface.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
Name
OptionsAllowGuestPaymentsApi
OptionsAllowGuestSupportApi
OptionsAllowHomePage
OptionsAllowStandardAnswersPages

```

**Description**
The number of page views allowed for the current calendar month for the sites
in your organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name used when referencing the site in the API.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether unauthenticated guest users can access the Payments API
(true) or not (false). The default is false. This field is available in API version
49.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable unauthenticated users to access the Support API.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard page associated with the Home tab
(/home/home.jsp).

**Type**
boolean

**Properties**
Filter


-----

```
OptionsAllowStandardIdeasPages
OptionsAllowStandardLookups
OptionsAllowStandardPortalPages
OptionsAllowStandardSearch
OptionsBrowserXssProtection

```

**Description**
The option to enable standard pages associated with an answers Experience
Cloud site. If you want to use default Answers pages (such as AnswersHome),
enable these pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable standard pages associated with an Ideas Experience Cloud
site. If you want to use default Ideas pages (such as IdeasHome), enable these
pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard lookup pages. These are the windows
associated with lookup fields on Visualforce pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable authenticated users to access the standard Salesforce pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard search pages. To allow public users to perform
standard searches, enable these pages.

**Type**
boolean

**Properties**
Filter


-----

```
OptionsCachePublicVfPagesInProxies
OptionsContentSniffingProtection
OptionsCookieConsent
OptionsCspUpgradeInsecureRequests
OptionsEnableFeeds

```

**Description**
The option to enable the browser's cross-site scripting protection.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether proxy servers cache this site’s publicly available pages only for
unauthenticated guest users (true) or not (false). When this field is false,
this site’s cache-enabled Visualforce pages are cached in the web browser for
both authenticated and unauthenticated users. The default is true. See
[Configure Site Caching in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=sf.sites_caching.htm&language=en_US)

This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable content-sniffing protection.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether only required Salesforce-supplied cookies are allowed within
the site (true) or all cookies types are allowed: required, functional, and
advertising (false). The default is `false. This field is available in API version`
52.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
This field is removed in API version 52.0 and later. In API version 51.0 and earlier,
the value in the field is ignored.

**Type**
boolean


-----

```
OptionsHasStoredPathPrefix
OptionsRedirectToCustomDomain
OptionsReferrerPolicyOriginWhenCrossOrigin
OptionsRequireHttps

```

**Properties**
Filter

**Description**
The option that displays the Syndication Feeds related list, where you can create
and manage syndication feeds for users on your public sites. This field is visible
only if you have the feature enabled for your organization.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether this Experience Cloud site has a customized urlPathPrefix
(true) or instead uses the Experience Cloud site's UrlPathPrefix plus /s
(false). The default is false. In other sites, this field has no effect. This field
is available in API version 50.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether requests to this site’s system-managed URLs are redirected to
the HTTPS custom domain serving this site (true) or not (false).
System-managed site URLs end in *.my.salesforce-sites.com or
```
  *.my.site.com. In Experience Cloud sites, the default is false. In Salesforce

```
Sites, the default is true.

If multiple custom domains serve this site and this field is set to true, requests
are routed to the site’s primary custom URL only if it’s an HTTPS custom domain.
Otherwise, requests are redirected to the first HTTPS custom domain associated
with this site, in alphanumeric order. If no HTTPS custom domain serves this site,
this option has no effect.

This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable referrer policy (origin-when-cross-origin).

**Type**
boolean


-----

```
SiteType
Status
Subdomain
TopLevelDomain

```

**Properties**
Filter

**Description**
This field is removed in API version 52.0 and later. In API version 51.0 and earlier,
the value in the field is ignored.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Identifies whether the site is a Visualforce (Salesforce Sites) or a Site.com site.
`SiteType` is available in API version 21.0 and later. In API version 26.0 and
later, if Experience Cloud sites are enabled for your Salesforce org, the site could
also be a Network Visualforce or Network Site.com site.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status for the site. For example, `Active` or `In Maintenance.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If you enabled Salesforce Sites or Digital Experiences before you enabled enhanced
domains on your My Domain, this field returns this site’s previous subdomain.
For example, if your domain was `mycompany.force.com, then`
`mycompany` is the subdomain.

If you enabled Salesforce Sites or Digital Experiences after you enabled enhanced
domains, this field returns a null value.

**Type**
url

**Properties**
Filter, Nillable


-----

```
UrlPathPrefix

##### Usage

```

**Description**
The optional branded custom Web address that you registered with a third-party
domain name registrar. The custom Web address acts as an alias to your Salesforce
address.

Beginning with API version 21.0, `TopLevelDomain` is no longer available.
Instead, use the Domain and DomainSite objects.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique Salesforce URL that the public uses to access this site.


Use this read-only object to query or retrieve information on your site.

##### Associated Objects

This object has the following associated objects. Unless noted, these associated objects are available in the same API version as this
object.

**SiteFeed**

Feed tracking is available for the object.

**SiteHistory**

History is available for tracked fields of the object.
