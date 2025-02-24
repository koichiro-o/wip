#### CspTrustedSite

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the category.

This field is a relationship field.

**Relationship Name**
ProductCategory

**Relationship Type**
Lookup

**Refers To**
ProductCategory

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies if CryptoProdCatgWalletGroup is active and functional, or inactive and disabled.

Possible values are:

**•** `Active`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether the list of wallets is for minting allowlist or for executing an airdrop.

Possible values are:

**•** `Airdrop`

**•** `Allowlist`


Represents a trusted URL. For each CspTrustedSite, you can specify Content Security Policy (CSP) directives and permissions policy
directives. Each CSP directive allows Lightning components, third-party APIs, and WebSocket connections to access a resource type
from the trusted URL. If the Permissions-Policy HTTP header is enabled, each permissions policy directive grants the trusted URL access
to a browser feature. In API version 58.0 and earlier, CspTrustedSite included only CSP directives and was referred to as CSP Trusted Sites
in Salesforce Setup. Available in API version 39.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
CanAccessCamera
CanAccessMicrophone
Context

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite can access the user’s camera. The default value is
```
  false.

```
This field takes effect only when the enablePermissionsPolicy field equals true
and the `grantCameraAccess` field equals `TrustedUrls` in the SecuritySettings
metadata API type.

This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite can access the user’s microphone. The default value
is `false.`

This field takes effect only when the enablePermissionsPolicy field equals true
and the `grantMicrophoneAccess` field is `TrustedUrls` in the SecuritySettings
metadata API type.

This field is available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Declares the scope of the CSP directives for this trusted URL.

Possible values are:

**•** `All—Apply the CSP directives to all supported context types.`

**•** `Communities—Apply the CSP directives to Experience Builder sites only.`

**•** `FieldServiceMobileExtension—Apply the CSP directives to the Field Service`
Mobile Extensions only.


-----

```
Description
DeveloperName
EndpointUrl

```


**•** `LEX—Apply the CSP directives to Lightning Experience only.`

**•** `VisualForce—Apply the CSP directives to custom Visualforce pages only. This value`
is available in API version 55.0 and later.

For custom Visualforce pages, content is restricted to trusted URLs only if the page’s
`cspHeader` attribute is set to `true.`

This field is available in API version 44.0 and later.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the trusted URL. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the trusted URL.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The URL for this CspTrustedSite.

This field must include a domain name and can include a port. For example,
`https://example.com` or `https://example.com:8080.`

To reduce repetition, you can use the wildcard character `*` (asterisk). For example,
```
  *.example.com. For a third-party API, the URL must begin with https://. For example,
  https://example.com. For a WebSocket connection, the URL must begin with wss://.

```
For example, `wss://example.com.`

Otherwise, the URL cannot be malformed. Examples of malformed URLs that fail a syntax
check are `malformed^url.example.com, and`
```
  https://{subdomain}.example.com.

```
To add a URL based on parameters, build the URL before you update the `EndpointUrl`
field.


-----

```
IsActive
IsApplicableToConnectSrc
IsApplicableToFontSrc
IsApplicableToFrameSrc
IsApplicableToImgSrc
IsApplicableToMediaSrc

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite is active.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load URLs using script interfaces from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load fonts from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load resources contained in `<iframe>` elements from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load images from this trusted URL.

**Type**
boolean


-----

```
IsApplicableToStyleSrc
Language
MasterLabel
NamespacePrefix

##### Usage

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load audio and video from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components can load style sheets from this trusted URL.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for the trusted URL.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Master label for this trusted URL.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace prefix for this trusted URL.


For each CSPTrustedSite, at least one field starting with `grantAccess or` `isApplicableTo` must be set to `true.`

In API versions 50.0 to 58.0, if all `isApplicable` fields are `false, the` `isApplicableToImgSrc` field is set to `true. In API`
version 49.0 and earlier, if all `isApplicable` fields are `false, those fields all default to` `true.`


-----

To ensure smooth integration across Salesforce products, Salesforce includes URLs in each of the CSP directives that correspond to the
`isApplicable` fields, even though those URLs aren’t defined as CspTrustedSite components. Salesforce regularly updates those
URLs based on the latest requirements.
