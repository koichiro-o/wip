#### CorsWhitelistEntry

Represents an entry in the cross-origin resource sharing (CORS) allowlist. Origins included in the allowlist can request REST resources
from that Salesforce org.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
create(), delete(), query(), retrieve(), update(), upsert()

 Fields

```
```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
Language
MasterLabel

```

**Description**
The unique name of the record in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
This field is automatically generated but you can supply your own value if you create the
record using the API.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

This picklist contains the following fully-supported languages:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined
translations.

**•** Swedish: `sv`

**•** Thai: `th The Salesforce user interface is fully translated to Thai, but Help is in English.`

**Type**
string


-----

```
NamespacePrefix
UrlPattern

##### Usage

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Primary label for the CORS allowlist entry.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For managed packages, this field is the namespace prefix assigned to the package. For
unmanaged packages, this field is blank.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The origin URL pattern must include the HTTPS protocol (unless you’re using your localhost)
and a domain name, and can include a port. The wildcard character (*) is supported and
must be in front of a second-level domain name. For example,
`https://*.example.com` adds all subdomains of example.com to the allowlist.

The origin URL pattern can be an IP address. But an IP address and a domain that resolve to
the same address aren’t the same origin, and you must add them to the CORS allowlist as
separate entries.

Google Chrome[™] and Mozilla[®] Firefox[®] browser extensions are also allowed as resources in
API version 53 and later. Chrome extensions must use the prefix chrome-extension://
and 32 characters without digits or capital letters, for example
```
  chrome-extension://abdkkegmcbiomijcbdaodaflgehfffed. Firefox

```
extensions must use the prefix `moz-extension://` and an 8-4-4-4-12 format of small
alphanumeric characters, for example
```
  moz-extension://1234ab56-78c9-1df2-3efg-4567891hi1j2.

```

Cross-Origin Resource Sharing (CORS) allows web browsers to request resources from other origins. For example, using CORS, the
JavaScript for a web application at https://www.example.com can request a resource from
```
https://www.salesforce.com. To allow access to supported Salesforce APIs, Apex REST resources, and Lightning Out from

```
JavaScript code in a web browser, add the requesting origin to your Salesforce CORS allowlist.

If a browser that supports CORS makes a request to an origin in the Salesforce CORS allowlist, Salesforce returns the origin in the
`Access-Control-Allow-Origin` HTTP header, along with any additional CORS HTTP headers. If the origin isn’t included in
the allowlist, Salesforce returns HTTP status code 403.


-----

Important: CORS doesn’t support requests for unauthenticated resources, including OAuth endpoints. You must pass an OAuth
token with requests that require it.

[CORS is a W3C recommendation to enable browsers to request resources from origins other than their own.](http://www.w3.org/TR/cors/)
