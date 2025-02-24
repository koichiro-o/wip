#### SamlSsoConfig

Represents a SAML Single Sign-On configuration.This object is available in API version 32.0 and later.

Single sign-on is a process that allows network users to access all authorized network resources without having to log in separately to
each resource. Single sign-on allows you to validate usernames and passwords against your corporate user database or other client
application rather than having separate user passwords managed by Salesforce.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only users with the View Setup and Configuration permission or both the Customize Application and Modify
All Data permissions can access this object.

##### Fields

```
AttributeFormat
AttributeName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For SAML 2.0 only and when identityLocation is set to Attribute.
Possible values include unspecified, emailAddress, or persistent.
All legal values can be found in the “Name Identifier Format Identifiers” section
[of the Assertions and Protocols SAML 2.0 specification.](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
Audience
DeveloperName
ErrorUrl
ExecutionUserID

```

**Description**
The name of the identity provider’s application. Get this name value from your
identity provider.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The Issuer, also called the “Entity ID.” The value is a URL that uniquely identifies
the SAML identity provider.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package, and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
When there's an error during login, specify the URL of the page where users are
directed. It must be publicly accessible, such as a public site Visualforce page.
The URL can be absolute or relative.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
IdentityLocation
IdentityMapping
Issuer

```

**Description**

The user that runs the Apex handler class. The user must have the “Manage Users”
permission. A user is required if you specify a SAML JIT handler class.

This is a relationship field.

**Relationship Name**
ExecutionUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The location in the assertion where a user is identified. Valid values are:

**•** `SubjectNameId—The identity is in the <Subject>` statement of the
assertion.

**•** `Attribute—The identity is specified in an` `<AttributeValue>,`
located in the <Attribute> of the assertion.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The identifier that the service provider uses for the user during Just-in-Time user
provisioning. Valid values are:

**•** `Username—The user’s Salesforce username.`

**•** `FederationId—The federation ID from the user object; the identifier`
that’s used by the service provider for the user.

**•** `UserId—The user ID from the user’s Salesforce organization.`

**Type**
string

**Properties**
Filter, idLookup, Group, Sort

**Description**
Also called the “Entity ID.” The value is a URL that uniquely identifies the SAML
identity provider.


-----

```
Language
LoginUrl
LogoutUrl
MasterLabel
NamespacePrefix

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The language for the organization.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
For SAML 2.0 only: The URL where Salesforce sends a SAML request to start the
login sequence.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
For SAML 2.0 only: The URL to direct users to where they click the Logout link.
The default is https://salesforce.com.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The text that’s used to identify the Visualforce page in the Setup area of Salesforce.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.


-----

```
OptionsSpInitBinding
OptionsUseConfigRequestMethod
OptionsUseSameDigestAlgoForSigning
OptionsRequireMfaSaml

```


**•** In Developer Edition orgs, NamespacePrefix is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
boolean

**Properties**
Filter

**Description**

The service provider initiated request binding, either HTTP Redirect (true) or
HTTP POST (false).

**Type**
boolean

**Properties**
Filter

**Description**
If `true, applies the selected Request Signature Method (RSM) during single`
logout. If `false, the default RSM (RSA-SHA1) is applied.`

**Type**
boolean

**Properties**
Filter

**Description**
If true, uses a SAML digest algorithm based on the selected Request Signature
Method (RSM). For example, if the selected RSM is `RSA-SHA256, the digest`
algorithm is set to `SHA-256.`

If false, uses the default digest algorithm (SHA-1), regardless of the selected
RSM.

This field is available in API version 55.0 and later. You can edit this field only for
legacy SAML configurations created before the Spring ’22 release. For
configurations created after Spring ’22, this field is `true` by default.

**Type**
boolean


-----

```
OptionsUserProvisioning
RequestSignatureMethod
SamlJitHandlerId

```

**Properties**
Filter

**Description**
Requires multi-factor authentication (MFA) for single sign-on with this SAML
configuration based on the MFA status of each user. For this setting to trigger
MFA, you must apply MFA directly to users via one of two methods. 1) Assign
the user permission Multi-Factor Authentication for User Interface Logins. 2)
Enable the org setting Require multi-factor authentication (MFA) for all direct UI
logins to your Salesforce org.

**Type**
boolean

**Properties**
Filter

**Description**
If `true, Just-in-Time user provisioning is enabled, which creates users on the`
fly the first time that they try to log in. Specify `Federation ID` for the
`identityMapping` value to use this feature.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The method that’s used to sign the SAML request. Valid values are:

**•** `RSA-SHA1`

**•** `RSA-SHA256`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The name of an existing Apex class that implements the
`Auth.SamlJitHandler` interface.

This is a relationship field.

**Relationship Name**
SamlJitHandler

**Relationship Type**
Lookup


-----

```
SingleLogoutBinding
SingleLogoutUrl
ValidationCert
Version

```

**Refers To**
ApexClass

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Determines where to put the LogoutRequest or LogoutResponse in the SAML
request during single logout (SLO). The value is base64 encoded. Valid values
are:

**•** `RedirectBinding` — Sent in the query string, deflated.

**•** `PostBinding` — Sent in the POST body, not deflated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SAML single logout endpoint. This URL is the endpoint where Salesforce
sends LogoutRequests (when Salesforce initiates a logout), or LogoutResponses
(when the identity provider initiates a logout).

**Type**
string

**Properties**
Filter, Sort

**Description**
The certificate that’s used to validate the request. Get this certificate value from
your identity provider.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The SAML version. Valid values are:

**•** `SAML1_1`

**•** `SAML2_2`


-----
