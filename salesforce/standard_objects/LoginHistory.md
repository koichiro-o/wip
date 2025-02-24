#### LoginHistory

Represents the login history for all successful and failed login attempts for organizations and enabled portals. This object is available in
API version 21.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

With one exception, only users with Manage Users or Monitor Login History permissions can access this object. The exception is that, in
API version 37.0 and later, all users can retrieve their own login history records.

##### Fields

```
ApiType
ApiVersion
Application
AuthMethodReference
AuthenticationServiceId

```

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Indicates the API type, for example `Soap Enterprise. Label is API Type.`

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Displays the API version used by the client. Label is API Version.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The application used to access the organization. Label is Application.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The authentication method used by a third-party identification provider for an OpenID
Connect single sign-on protocol. This field is available in API version 51.0 and later. Label is
**Authentication Method Reference.**

**Type**
reference


-----

```
Browser
CipherSuite
ClientVersion
CountryIso

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for an authentication service for a login event. For example, you can use
this field to identify the SAML or authentication provider configuration with which the user
logged in. This field is available in API version 34.0 and later. Label is Authentication Service
**Id.**

This field is a polymorphic relationship field.

**Relationship Name**
AuthenticationService

**Relationship Type**
Lookup

**Refers To**
AuthProvider, SamlSsoConfig

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The current browser version. Label is Browser.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The TLS cipher suite used for the login. Values are OpenSSL-style cipher suite names, with
[hyphen delimiters. For more information, see OpenSSL Cryptography and SSL/TLS Toolkit.](https://www.openssl.org/source/)
This field is available in API version 37.0 and later.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Version of the API client. Label is Client Version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
ForwardedForIp
LoginGeoId
LoginSubType

```

**Description**
The ISO 3166 code for the country where the user’s IP address is physically located. For more
[information, see Country Codes - ISO 3166. This field is available in API version 37.0 and later.](http://www.iso.org/iso/country_codes.htm)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value in the `X-Forwarded-For` header of HTTP requests sent by the client. For
logins that use one or more HTTP proxies, the X-Forwarded-For header is sometimes
used to store the origin IP and all proxy IPs.

The ForwardedForIp field stores whatever value the client sends, which might not be
an IP address. The maximum length is 256 characters. Longer values are truncated. The
`ForwardedForIp` field isn’t populated for logins completed via OAuth flows or single
sign-on (SSO).

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a successful or
unsuccessful login event. The accuracy of geolocation fields like country, city, or postal code
can vary because of the nature of the technology. This field is available in API version 34.0
and later.

This field is a relationship field.

**Relationship Name**
LoginGeo

**Relationship Type**
Lookup

**Refers To**
LoginGeo

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of login flow used.

**•** `OauthClientCredentials–OAuth Client Credentials`


-----

```
LoginTime
LoginType

```


**•** `OauthHybridRefreshToken—OAuth Refresh Token for Hybrid`
```
   Apps

```
**•** `OauthHybridTokenExchange—OAuth Token Exchange for Hybrid`
```
   Apps

```
**•** `OauthHybridUserAgent–OAuth User-Agent for Hybrid Apps`

**•** `OauthHybridWebServer–OAuth Web Server for Hybrid Apps`

**•** `OauthOtpLogin—OAuth OTP Login`

**•** `OauthRefreshToken—OAuth Refresh Token`

**•** `OauthTokenExchange—OAuth Token Exchange`

**•** `OauthUserAgent–OAuth User-Agent`

**•** `OauthUserAgentIdToken–OAuth User-Agent with ID Token`

**•** `OauthUsernamePassword–OAuth Username-Password`

**•** `OauthWebServer–OAuth Web Server`

**•** `UiPasswordReset–UI Password Reset`

**•** `UsernamePasswordUiLogin–UI Username-Password`

Label is Login Subtype.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Time zone is based on GMT. Label is Login Time.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of login used to access the session.

**•** `AppExchange–AppExchange`

**•** `Application–Application`

**•** `Certificate–Certificate-based login`

**•** `ChatterCommunityPortalUnPwd–Chatter Communities External`
```
   User

```
**•** `ChatterCommunityThirdPartySso–Chatter Communities`
```
   External User Third Party SSO

```
**•** `CrossTenantLogin–Cross Tenant Login—For internal use only.`

**•** `EmployeeLoginToCommunity–Employee Login to Community`

**•** `HelpAndTraining–Help And Training`


-----

```
LoginUrl
NetworkId

```


**•** `IeOfflineClient–Offline Client`

**•** `LightningLogin–Lightning Login`

**•** `NetworksPortalApiOnly–Networks Portal API Only`

**•** `Oauth, Remote Access Client–Remote Access Client`

**•** `Oauth2, Remote Access 2.0–Remote Access 2.0`

**•** `OtherApi–Other Apex API`

**•** `Partner–Partner Product`

**•** `PasswordlessLogin–Passwordless Login`

**•** `Portal–Customer Service Portal`

**•** `PortalThirdPartySso–Customer Service Portal Third-Party`
```
   SSO

```
**•** `PrmPortalThirdPartySso–Partner Portal Third-Party SSO`

**•** `PrmPortal–Partner Portal`

**•** `Saml–SAML Idp Initiated SSO`

**•** `SamlChatterNetworks–SAML Chatter Communities External`
```
   User SSO

```
**•** `SamlCspPortal–SAML Customer Service Portal SSO`

**•** `SamlPrmPortal–SAML Partner Portal SSO`

**•** `SamlSite–SAML Site SSO`

**•** `Saml2–SAML Sfdc Initiated SSO`

**•** `SelfService–SelfService`

**•** `ThirdPartySso–Third Party SSO`

Label is Login Type.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL from which the login request is coming. Label is Login URL.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site that the user is logging in to. This field is available in API
version 31.0 and later, if Salesforce Experience Cloud sites are enabled for your org.


-----

```
OptionsIsGet
OptionsIsPost
Platform
SourceIp
Status

```

**Type**
boolean

**Properties**
Filter

**Description**
The HTTP method used for the session login is a GET request.

**Type**
boolean

**Properties**
Filter

**Description**
The HTTP method used for the session login is a POST request.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Operating system on the login machine. Label is Platform.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the incoming client request that first reaches Salesforce during a login. For
example, `126.7.4.2.`

For clients that redirect through one or more HTTP proxies, this field stores the IP address of
the first proxy to reach Salesforce. To better identify the origin IP for these cases, check the
`ForwardedForIp` field instead.

The `SourceIp` field doesn't support the `LIKE comparison operator.`

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Displays the status of the attempted login. Status is either success or a reason for failure.
Label is Status.


-----

```
TlsProtocol
UserId

##### Usage

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The TLS protocol used for the login. Possible values are:

**•** `TLS 1.0`

**•** `TLS 1.1`

**•** `TLS 1.2`

**•** `TLS 1.3`

**•** `Unknown`

This field is available in API version 37.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user logging in. Label is User ID.


Not all fields are filterable. You can only filter on the following fields:

**•** `AuthenticationServiceId`

**•** `CipherSuite`

**•** `CountryIso`

**•** `Id`

**•** `LoginTime`

**•** `LoginType`

**•** `LoginUrl`

**•** `NetworkId`

**•** `OptionsIsGet`

**•** `OptionsIsPost`

**•** `TlsProtocol`

**•** `UserId`

The API allows you to do many powerful queries. A few examples are:


-----

Simple query showing UserId & LoginTime for each user `SELECT UserId, LoginTime from LoginHistory;`

Query showing logins only after a specified date and time `SELECT UserId, LoginTime from LoginHistory`
```
                          WHERE LoginTime > 2010-09-20T22:16:30.000Z;

```

Query showing logins for a specific time interval

Query showing the authentication service for a SAML login event,
where Id=AuthenticationServiceId from LoginHistory

Query showing the authentication service for an authentication
provider login event, where
`Id=AuthenticationServiceId` from LoginHistory
