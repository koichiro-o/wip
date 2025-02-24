#### ExternalDataUserAuth

Stores authentication settings for a Salesforce user to access an external system. The external system must be defined in an external data
source or a named credential that’s configured to use per-user authentication. This object is available in API version 27.0 and later.

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
AuthProviderId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the authentication provider, which defines the service that
provides the login process and approves access to the external system.

Only users with the “Customize Application” and “Manage AuthProviders”
permissions can view this field.

This field is available in API version 39.0 and later.

This is a relationship field.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup


-----

```
ExternalDataSourceId
Password
Protocol

```

**Refers To**
AuthProvider

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Salesforce ID of the external data source or named credential that defines the
external system.

This is a polymorphic relationship field.

**Relationship Name**
ExternalDataSource

**Relationship Type**
Lookup

**Refers To**
ExternalDataSource, NamedCredential

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Password portion of the credentials for the Salesforce user to access the external
system.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies whether to use OAuth, password authentication, or no authentication
when the user accesses the external system.

Additional authentication protocols are supported for the Amazon DynamoDB,
Amazon Athena, Snowflake, GraphQL, and OData 4.01 external data sources.

**•** AwsSv4

**•** Basic

**•** Custom

**•** Jwt

**•** JwtExchange


-----

```
UserId
Username

##### Usage

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce user who’s accessing the external system.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Username portion of the credentials for the Salesforce user to access the external
system.


These authentication settings enable a Salesforce user to access an external system. The external system is defined in Salesforce as one
of the following.

**•** External data source—Provides access to external objects, whose data is stored outside the Salesforce organization.

**•** Named credential—Enables the user’s actions to trigger authenticated callouts to the endpoint that’s specified in the named
credential.

If you grant users access to the external data source or named credential via permission sets or profiles, those users can manage their
[own authentication settings. See Store Authentication Settings for External Systems in the Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.external_authentication.htm&language=en_US)

SEE ALSO:

ExternalDataSource

NamedCredential
