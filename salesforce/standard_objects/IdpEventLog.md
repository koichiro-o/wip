#### IdpEventLog

Represents the Identity Provider Event Log. This log records both problems and successes with inbound SAML or OpenID Connect
authentication requests from another app provider. It also records outbound SAML responses when Salesforce is acting as an identity
provider. This object is available in API version 39.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
AppId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the app provider seeking authentication.


-----

```
AuthSessionId
ErrorCode

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the authentication session.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The error code for the authentication issue.

Possible values are:

**•** `AppAccessDenied—Error: App access denied`

**•** `AppBlocked—Error: App blocked`

**•** `ClientUnapproved—Error: Invalid grant`

**•** `CodeExpired—Error: Expired authorization code`

**•** `ForceAuthNLogout—User logged out due to forced authentication request`

**•** `InternalError—Error: Internal Error`

**•** `InvalidAuthnRequest—Error: Unable to parse AuthnRequest from service`
provider

**•** `InvalidClientCredentials—Error: Invalid client credentials`

**•** `InvalidCode—Error: Invalid authorization code`

**•** `InvalidDeviceId—Error: Invalid device ID`

**•** `InvalidIdpEndpoint—Error: Invalid Identity Provider Endpoint URL`

**•** `InvalidIssuer—Error: Invalid Issuer`

**•** `InvalidScope—Error: Invalid scope(s)`

**•** `InvalidSessionLevel—Error: Invalid session level`

**•** `InvalidSettings—Error: IdP certificate is invalid or does not exist`

**•** `InvalidSignature—Error: Invalid Signature`

**•** `InvalidSp—Error: Misconfigured or invalid service provider`

**•** `InvalidSpokeSp—Error: Invalid spoke SP settings`

**•** `InvalidUserCredentials—Error: Invalid user credentials`

**•** `NoAccess—Error: User does not have access to this service provider`

**•** `NoCustomAttrValue—Error: User does not have a value for the subject custom`
attribute

**•** `NoCustomField—Error: Custom field not found`

**•** `NoSpokeId—Error: No Spoke ID found`


-----

```
IdentityUsed
InitiatedBy
OptionsHasLogoutUrl
SamlEntityUrl

```


**•** `NoSubdomain—Error: No My Domain deployed in the org`

**•** `NoUserFedId—Error: User does not have a Federation Identifier selected`

**•** `OauthError—OAuth Error`

**•** `Success`

**•** `UnableToResolve—Error: Unable to resolve request into a Service Provider`

**•** `UnknownError—Unknown Error`

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The identity (username) of the user being authenticated.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The code describing how the authentication request was initiated.

Possible values are:

**•** `IdP—IdP-Initiated SAML`

**•** `OauthAuthorize—OAuth Authorization`

**•** `OauthTokenExchange—OAuth Token Exchange`

**•** `SP—SP-Initiated SAML`

**Type**
boolean

**Properties**
Filter

**Description**
Whether a logout URL has been assigned to the app. This URL is where users are redirected
when they log out.

**Type**
string

**Properties**
Filter, Sort

**Description**
The authentication URL of the SAML provider.


-----

```
 SsoType
 Timestamp
 UserId
