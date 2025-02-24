#### IframeWhiteListUrl

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of SSO. Options are:

**•** 0–SAML

**•** 1–OpenID Connect

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time on which the event occurred.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user seeking authentication.


Represents a list of trusted external domains that you allow to frame your Embedded Service, Surveys, and Visualforce pages. This object
is available in API version 45.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
Context

```

**Type**
picklist


-----

```
Url

##### Usage

```

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of content in the iframe.

Valid values are:

**•** `LightningOut—Reserved for future use. Available in API version 60.0`
and later

**•** `Surveys`

**•** `VisualforcePages`

**•** `DisclosureAndComplianceHubConnector`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique domain that is allowed to frame your Visualforce pages, surveys, or
Disclosure and Compliance Hub Connector. Accepts these formats: example.com,
*example.com, and https://example.com.


To use this object for framing Visualforce pages, on Session Settings in Setup, select Enable clickjack protection for customer
**Visualforce pages either with headers disabled or with standard headers. These options both allow framing of Visualforce pages**
on trusted external domains and provide clickjack protection.

Alternatively, you can customize session settings via the SecuritySettings Metadata API type. To use the IframeWhiteListUrl object, set
either the enableClickjackNonsetupUser or enableClickjackNonsetupUserHeaderless field to `true. For`
[more information, see SecuritySettings in the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_securitysettings.htm)
