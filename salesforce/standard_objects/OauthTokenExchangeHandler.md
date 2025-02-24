#### OauthTokenExchangeHandler

Represents a token exchange handler. The token exchange handler also consists of an Apex class. During the OAuth 2.0 token exchange
flow, the token exchange handler is used to validate tokens from an external identity provider and to map users to Salesforce. This object
is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Special Access Rules

 Fields

**Field**
```
Description
DeveloperName
IsEnabled
IsUserCreationAllowed
Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A description for your token exchange handler.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the handler.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the handler is enabled for the token exchange flow.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the handler can set up new users. During the token exchange flow, the
Apex handler maps users from the identity provider to Salesforce. If the
`IsUserCreationAllowed` field is `true, the` `canCreateUser` boolean in the
```
  getUserForTokenSubject method is true, and the user doesn’t exist in Salesforce,

```
the handler sets up a new User object, which Salesforce automatically inserts to finish creating
the user.

The default value is `false.`

**Type**
picklist


-----

```
MasterLabel
NamespacePrefix

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the language used in the org where the token exchange handler was created.

Possible values are:

**•** `da—Danish`

**•** `de—German`

**•** `en_US—English`

**•** `es—Spanish`

**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`

**•** `ja—Japanese`

**•** `ko—Korean`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the token exchange handler record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the


-----

```
SupportedTokenTypesAccessToken
SupportedTokenTypesIdToken
SupportedTokenTypesJwt
SupportedTokenTypesRefreshToken
SupportedTokenTypesSaml2

```
```
  namespacePrefix__componentName notation. The namespace prefix can have

```
one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports OpenID Connect ID tokens from the identity provider.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports tokens from the identity provider that are in JWT
format, such as JWT-based access tokens.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports OAuth 2.0 refresh tokens from the identity provider.

**Type**
boolean


-----

```
TokenHandlerApexId

```

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports SAML 2.0 assertions from the identity provider.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Apex class associated with the token exchange handler. The class contains methods to
validate the token and map users to Salesforce. It must extend the
`Oauth2TokenExchangeHandler` Apex class.

This field is a relationship field.

**Relationship Name**
TokenHandlerApex

**Relationship Type**
Lookup

**Refers To**
ApexClass

