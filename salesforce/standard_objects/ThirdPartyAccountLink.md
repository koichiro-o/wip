#### ThirdPartyAccountLink

Represents the list of external users who authenticated using an authentication provider. This object is available in API version 32.0 and
later.

A list of third-party account links is generated when users of an organization authenticate using an external authentication provider. Use
this object to list and revoke a given user's social sign-on connections (such as Facebook[©]).

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
[If you try to use Apex DML operations and then query this object in the same call, you get an](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexref.meta/apexref/apex_dml_section.htm) `UncommittedWork` error with this
description.
```
A callout was unsuccessful because of pending uncommitted work related to a process, flow,
 or Apex operation.
Commit or roll back the work, and then try again.

```
To avoid this error, execute DML operations and queries in separate, asynchronous calls.

##### Fields

```
Handle
IsNotSsoUsable

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The username in the third-party system.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Sort


-----

```
Provider
RemoteIdentifier
SsoProvider
SsoProviderId

```

**Description**
Support for single sign-on.

If true, the link can't be used for a single sign-on flow. It's only available OAuth
access and refresh tokens.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The third-party account provider name.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The unique ID for the user in the third-party system.

**Type**
AuthProvider

**Properties**
Filter, Nillable, Sort

**Description**
The foreign key to the AuthProvider on page 876 of the third-party system.

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The ID associated with the SsoProvider value.

This is a relationship field.

**Relationship Name**
SsoProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider


-----

```
SsoProviderName
ThirdPartyAccountLinkKey
UserId

##### Usage

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name associated with the AuthProvider of the third-party system, in case
the user has no access to the provider foreign key (the SsoProvider value).

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
A concatenated string including the organization ID, the SsoProviderId
value, the SsoProvider value, and the RemoteIdentifier value.

**Type**
reference

**Properties**
Filter, Nillable, Sort

**Description**
The Salesforce user associated with this third-party account link.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


Admins (with the Manage Users permission) querying this object can see all the links for all users in the organization. Without the Manage
Users permission, users can only retrieve their own links. Users sometimes don't have access to the SsoProvider value (the foreign
key). In this case, use the SsoProviderName to render the name of the provider for the associated link.

Use the Apex method `Auth.AuthToken.revokeAccess()` to revoke a link. To use this method, the `IsNotSsoUsable`
field must be `false.`

To make the ThirdPartyAccountLink standard object writable for Salesforce admins, contact Salesforce Customer Support. With this
feature, you can easily add or delete third-party account links using the API, but you can’t update existing account links.

In API version 34.0 and later, this object was enhanced to help manage high instance counts. A query() call returns up to 500 rows.
A queryMore() call returns 500 more, up to 2500 total. No more records are returned after 2500. To make sure that you don’t miss any


-----

records, issue a COUNT() query in a SELECT clause for ThirdPartyAccountLink. This query gives you the total number of records. If there
are more than 2500 records, use these options to manage your results.

**•** Divide queries by filtering on fields like `UserId` to return subsets of less than 2500 records.

**•** Use `OFFSET` to get batches of 2500 records. Start with an `OFFSET` of 0 and then increment by 2500. If you use this option, we
recommend that you also use LIMIT to limit each query to 2500.

For example, use an initial query with this structure.
```
  SELECT <desired fields> FROM ThirdPartyAccountLink LIMIT 2500 OFFSET 0

```
Then, run another query with an offset of 2500.
```
  SELECT <desired fields> FROM ThirdPartyAccountLink LIMIT 2500 OFFSET 2500

```
Continue to increase the offset by 2500 until you have results for all records.
