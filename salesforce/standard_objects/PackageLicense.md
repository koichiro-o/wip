#### PackageLicense

```

**Description**
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943YAS`


Represents a license for an installed managed package. This object is available in API version 31.0 and later.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
AllowedLicenses
ExpirationDate
IsAvailableForIntegrations
IsProvisioned
NamespacePrefix

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of users allowed to use the package.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the package license expires.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for internal use.

**Type**
string

**Properties**
Filter, Group, Sort


-----

```
Status
UsedLicenses

##### Usage

```

**Description**
The namespace prefix associated with the package.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the license. Possible values are: `Active,` `Expired,` `Free, and` `Trial.`

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of users who have a license to the package.


Use this object to determine the number of licenses allowed and in use for a managed package installed in your organization.

The following example demonstrates the use of the API to manage licenses for a package. The example defines an Apex class that does
the following.

**•** Retrieves the PackageLicense record for the specified package (identified by its namespace prefix).

**•** Defines a function that returns a list of all users with the specified profile.

**•** Creates a UserPackageLicense record for each user with that profile, which has the effect of assigning a license for the package to
all users with that profile.

**•** Returns an error message if the number of users exceeds the number of available licenses.


-----
