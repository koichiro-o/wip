#### ExternalDataSource

Represents an external data source, which defines connection details for integration with data and content that are stored outside the
Salesforce org. This object is available in API version 27.0 and later.


-----

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
From API version 48.0 onwards, only authenticated internal and external users can access this object.

##### Fields

```
AuthProviderId
CustomConfiguration

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salesforce ID of the authentication provider, which defines the service that provides the login
process and approves access to the external system.

Only users with the “Customize Application” and “Manage AuthProviders” permissions can
view this field.

This field is available in API version 39.0 and later.

This is a relationship field.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider

**Type**
textarea

**Properties**
Nillable

**Description**
A JSON-encoded configuration string that defines parameters specific to the type of external
data source.


-----

```
DeveloperName
Endpoint
isWritable
Language

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With this
field, a developer can change the object’s name in a managed package and the changes are
reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
textarea

**Properties**
Nillable

**Description**
The URL of the external system, or if that URL is defined in a named credential, the named
credential URL.

A named credential URL contains the scheme callout:, the name of the named credential,
and an optional path. For example: callout:My_Named_Credential/some_path.
You can append a query string to a named credential URL. Use a question mark (?) as the
separator between the named credential URL and the query string. For example:
```
  callout:My_Named_Credential/some_path?format=json.

```
**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Lets the Lightning Platform and users in this org create, update, and delete records for external
objects associated with the external data source. The external object data is stored outside
the org. By default, external objects are read only.

Available only for Salesforce Connect external data sources. Available in API version 35.0 and
later. However, with the cross-org adapter for Salesforce Connect, you can set this field to
`true` only in API version 39.0 and later.

**Type**
picklist


-----

```
MasterLabel
NamedCredentialId
NamespacePrefix
PrincipalType

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the `MasterLabel.`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Master label for the external data source. This internal label doesn’t get translated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce ID of the referenced named credential for an external data source. Required
for Salesforce Connect adapters for Amazon DynamoDB, Amazon Athena, GraphQL, and
OData 4.01. For connecting to other external data sources, the field must be null. This field is
available in API version 58.0 and later.

This is a relationship field.

**Relationship Name**
NamedCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
**Type**
picklist


-----

```
Protocol
Repository
Type

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies whether the org uses one set (NamedUser), multiple sets (PerUser), or no
(Anonymous) credentials to access the external system. Each set of credentials corresponds
to a login account on the external system. Corresponds to `Identity Type` in the user
interface.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies whether to use OAuth, password authentication, or no authentication to access the
external system.

Some types of external data sources support only one value.

**•** For cloud-based Files Connect external systems, select Oauth 2.0.

**•** For on-premises systems, select Password Authentication.

**•** For Simple URL data sources, select No Authentication.

Additional authentication protocols are supported for the Amazon DynamoDB, Amazon
Athena, Snowflake, GraphQL, and OData 4.01 external data sources.

**•** AwsSv4

**•** Basic

**•** Custom

**•** Jwt

**•** JwtExchange

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used for SharePoint Online. An optional name of the repository in the data source. Not
applicable to all data source types.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the adapter that connects to the external system.


-----

##### Usage

Define an external data source to connect to data or content that’s stored outside the Salesforce org. Then create external objects, which
map to the external system’s data and behave similarly to custom objects.

Note: Some external data source fields rely on per-user authentication to connect with an external system. If an admin edits one
of these fields, then the previously authenticated credentials can get invalidated, requiring individual users to reauthenticate.

SEE ALSO:

ExternalDataUserAuth

NamedCredential
