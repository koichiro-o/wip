#### BrowserPolicyViolation

Represents a violation related to the Trusted URLs and Trusted URLs for External Redirects allowlists. These violations include blocked
resource requests based on your content security policy (CSP) and blocked redirections. This object is available in API version 61.0 and
later.

Note: We recommend that you manage this object through the Trusted URL and Browser Policy Violations list in Setup. See
[Manage Trusted URL and Browser Policy Violations in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.security_trusted_urls_csp_violations.htm&language=en_US)

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
Only users with the Customize Application and Modify All Data permissions can access this object.

##### Fields

```
DeveloperName
Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The developer name of the violation.

Only users with View DeveloperName or View Setup and Configuration permission can view,
group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The language for the blocked request.


-----

```
MasterLabel
NamespacePrefix
UntrustedUrl
ViolationContext
ViolationType

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Master label for this violation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace prefix for this violation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The URL associated with the blocked request, without the path. For example, if a blocked
requested resource is an image with the URL
`https://www.example.com/images/image1.png, the UntrustedUrl` is
```
  https://www.example.com.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the `ViolationType` is `img-src (image),` `font-src (fonts), or`
```
  frame-src (iframe content), the content security policy (CSP) context for the

```
request. The CSP context controls which pages can load content from a CspTrustedSite.

Possible values are:

**•** `Lightning—The blocked request is related to a Lightning Experience page.`

**•** `Not Applicable—ViolationContext isn’t applicable to this violation. For`
example, violations with a `ViolationType` of `Redirection.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


-----

**Description**
The violation type. Possible values are:

**•** `img-src–At least one request to load an image file from the URL was blocked because`
the `UntrustedUrl` [isn’t a CspTrustedSite object with this CSP directive.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

**•** `font-src–At least one request to load a font from the URL was blocked because the`
`UntrustedUrl` [isn’t a CspTrustedSite object with this CSP directive.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

**•** `frame-src–At least one request to load content in an iframe that originated from`
the URL was blocked because the `UntrustedUrl isn’t a CspTrustedSite object with`
this CSP directive.

**•** `MalformedUrl–At least one redirection to this URL failed because the`
`UntrustedUrl` is malformed.

**•** `Redirect–At least one redirection to this URL was blocked because the`
`UntrustedUrl` [isn’t a RedirectWhitelistUrl object.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_redirectwhitelisturl.htm)

##### Usage

[We recommend that you manage this object through the Trusted URL and Browser Policy Violations list in Setup. See Manage Trusted](https://help.salesforce.com/s/articleView?id=sf.security_trusted_urls_csp_violations.htm&language=en_US)
[URL and Browser Policy Violations in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.security_trusted_urls_csp_violations.htm&language=en_US)

Note: To generate this object, Salesforce samples resource violations. This approach captures frequent violations while preserving
performance. Resource violations generated for testing purposes are unlikely to generate a new BrowserPolicyViolation. To see all
CSP violations for your org with detailed information about each violation, use the CSP Violation Event Type.

Because blocked redirections occur less frequently, all blocked redirections are captured as a BrowserPolicyViolation. For detailed
information about each blocked redirection, use the Blocked Redirect Event Type.

When you delete a BrowserPolicyViolation, only the logged event is removed. If your allowlists still block those requests, a new
BrowserPolicyViolation is generated the next time a matching request occurs.
