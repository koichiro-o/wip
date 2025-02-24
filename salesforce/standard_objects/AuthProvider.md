#### AuthProvider

Represents an authentication provider (auth provider). An auth provider lets users log in to your Salesforce org from an external service
provider, such as Facebook, Google, or GitHub. This object is available in API version 27.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Only users with Customize Application and Manage AuthProviders permissions can access this object.

##### Fields

```
AppleTeam
AuthorizeUrl
ConsumerKey
ConsumerSecret

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when using Apple as a third-party authentication provider. A
10-character team ID, obtained from an Apple developer account. Available in
API version 48.0 and later.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required when creating an OpenID Connect authentication provider. The OAuth
authorization endpoint URL. Available in API version 29.0 and later. In API version
33.0 and later, for Salesforce-managed auth providers, leave the field blank to let
Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The app’s key that is registered at the third-party (external) authentication
provider. In API version 33.0 and later, for Salesforce-managed auth providers,
leave the field blank to let Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Nillable


-----

```
CustomMetadataTypeRecord
DefaultScopes
DeveloperName
EcKey

```

**Description**

The consumer secret of the authentication provider that is registered at the
third-party SSO provider. It’s used by the consumer for identification to Salesforce.
In API version 33.0 and later, for Salesforce-managed auth providers, leave the
field blank to let Salesforce supply and manage the value. You can create your
own consumer secret on create(). However, after you set it, you can’t change
the value.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when creating a custom authentication provider plug-in. The API name
of the custom authentication provider. Available in API version 36.0 and later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

For OpenID Connect authentication providers, the scopes to send with the
authorization request, if not specified when a flow starts. Available in API version
29.0 and later. In API version 33.0 and later, for Salesforce-managed auth providers,
leave the field blank to let Salesforce supply and manage the value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Required. Used when referring to the authentication provider from a program.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required when using Apple as a third-party authentication provider. Available
in API version 48.0 and later.


-----

```
ErrorUrl
ExecutionUserId
FriendlyName
IconUrl
IdTokenIssuer

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

A custom error URL for the authentication provider to use to report errors.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Required when specifying a registration handler class. The username of the
Salesforce admin or system user who runs the Apex handler, which provides the
context in which the Apex handler runs. For example, if the Apex handler creates
a contact, the creation can be easily traced back to the registration process. In
production, use a system user. The user must have the Manage Users permission.
Available in API version 27.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Required. A user-friendly name for the authentication provider.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The path to an icon to use as a button on the login page. Users click the button
to log in with the associated authentication provider, such as Twitter or Facebook.
Available in API version 32.0 and later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
LinkKickoffUrl
LogoutUrl
OauthKickoffUrl
OptionsIncludeOrgIdInId

```

**Description**

The source of the authentication token in `https:` URI format. This field is
available when configuring an OpenID Connect or Microsoft authentication
provider. If provided, Salesforce validates the returned id_token value. OpenID
Connect requires returning an `id_token` value with the `access_token`
value. Available in API version 30.0 and later.

**Type**
url

**Properties**
Nillable

**Description**
The URL for linking existing Salesforce users to a third-party account. This field is
read-only. Available in API version 43.0 and later.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The destination for users after they log out if they authenticated using single
sign-on. The URL must be fully qualified with an http or https prefix, such as
```
  https://acme.my.salesforce.com. Available in API version 33.0 and

```
later.

**Type**
url

**Properties**
Nillable

**Description**
The URL for obtaining OAuth access tokens for a third party. This field is read-only.
Available in API version 43.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Used to differentiate between users with the same user ID from two sources
(such as two sandboxes). If enabled (true), Salesforce stores the org ID of the
third-party identity in addition to the user ID. After you enable this setting, you


-----

```
OptionsIsPkceEnabled
OptionsRequireMfa
OptionsSendAccessTokenInHeader
OptionsSendClientCredentialsInHeader

```

can’t disable it. Applies only to a Salesforce-managed auth provider. Available in
API version 32.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If set to true, the authentication provider uses the OAuth 2.0 Proof Key for Code
Exchange (PKCE) extension, which improves the security of the provider’s
authorization flow. This field applies only to these providerType values:

**•** `Custom`

**•** `Facebook`

**•** `Google`

**•** `Microsoft`

**•** `OpenIdConnect`

**•** `Salesforce.`

This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Requires multi-factor authentication (MFA) for single sign-on with this auth
provider based on the MFA status of each user. For this setting to trigger MFA,
you must apply MFA directly to users via one of two methods. 1) Assign the user
permission Multi-Factor Authentication for User Interface Logins. 2) Enable the
org setting Require multi-factor authentication (MFA) for all direct UI logins to
your Salesforce org.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

If enabled (true), the access token is sent to the UserInfoUrl in a header
instead of a query string. Available in API version 30.0 and later.

**Type**
boolean


-----

```
OptionsSendSecretInApis
PluginId
ProviderType

```

**Properties**
Create, Filter, Update

**Description**

Required when creating an OpenID Connect authentication provider. If enabled
(true), the client credentials are sent in a header to the `tokenUrl instead`
of a query string. The credentials are in the standard OpenID Connect Basic
Credentials header format, which is `Basic <token>, where` `<token>` is
the base64-encoded string "clientkey:clientsecret". Available in
API version 30.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

Determines whether the encrypted consumer secret appears in API responses.
If enabled (default), the secret appears in the response. If disabled (false),
responses don’t include the consumer secret. For security, you can disable the
setting. However, keep in mind that:

**•** By disabling this setting, the consumer secret is excluded from API responses
in all API versions.

**•** Change sets and other metadata deployments break because both the
consumer key and secret are expected. To fix this problem, insert the
consumer key manually during deployment.

Available in API version 47.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An existing Apex class that extends the
`Auth.AuthProviderPluginClass` abstract class. Available in API version
39.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Required. The third-party authentication provider to use. Valid values include:


-----

```
RegistrationHandlerId
SsoKickoffUrl

```


**•** `Apple. Available in API version 48.0 and later.`

**•** `Bitbucket—Provides authentication for a Bitbucket` provider. Enables
you to connect to Bitbucket from a Lightning Platform application. When
logged in to Bitbucket, the app can makes calls to Bitbucket APIs. The
`Bitbucket` provider isn’t available as an SSO provider, so users can’t log
in to a Salesforce org using their Bitbucket login credentials. Available in API
version 61.0 and higher.

**•** `Custom—A provider configured with a custom authentication provider`
plug-in. Available in API version 36.0 and later.

**•** `Facebook.`

**•** `GitHub—Provides authentication for a` `GitHub` provider. Used to log in
users of your Lightning Platform app to GitHub using OAuth. When logged
in to GitHub, your app can make calls to GitHub APIs. The GitHub provider
isn’t available as an SSO provider, so users can’t log in to your Salesforce org
using their GitHub login credentials. Available in API version 35.0 and later.

**•** `Google.`

**•** `Janrain.`

**•** `LinkedIn. Available in API version 32.0 and later.`

**•** `Microsoft. Provides authentication for all services that can be accessed`
via Microsoft Azure Active Directory. Available in API version 55.0 and later.

**•** `MicrosoftACS—Microsoft Access Control Service provides authentication`
for a Microsoft Office 365 service, like SharePoint Online. The
`MicrosoftACS` provider doesn't support SSO. Available in API version
31.0 and later.

**•** `OpenIdConnect. Available in API version 29.0 and later.`

**•** `Salesforce.`

**•** `Slack. Available in API version 54.0 and later.`

**•** `Twitter. Available in API version 32.0 and later.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

An existing Apex class that implements the Auth.RegistrationHandler
interface.

**Type**
url

**Properties**
Nillable


-----

```
TokenUrl
UserInfoUrl

```

**Description**
The URL for performing SSO into Salesforce from a third party by using its
third-party credentials. This field is read-only. Available in API version 43.0 and
later.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The OAuth token endpoint URL of an OpenID Connect authentication provider.
Available in API version 29.0 and later. In API version 33.0 and later, for
Salesforce-managed auth providers, leave the field blank to let Salesforce supply
and manage the value.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

The OpenID Connect endpoint URL of the OpenID Connect authentication
provider. Available in API version 29.0 and later. In API version 33.0 and later, for
Salesforce-managed auth providers, leave the field blank to let Salesforce supply
and manage the value.

