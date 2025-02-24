#### AuthSession

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the authentication provider associated with the allowlist.

This field is a relationship field.

**Relationship Name**
AuthProvider

**Refers To**
AuthProvider

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description for the allowlisted URL parameter.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the parameter, such as `ui_locales` or `login_hint.`


The AuthSession object represents an individual user session in your organization. This object is available in versions 29.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field Name**
```
CreatedDate
Id
IsCurrent
LastModifiedDate
LoginGeoId

```

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
The date and time this session was created. This field is a standard system field.

**Type**
id

**Properties**
Defaulted on create, Filter, Group, ID Lookup, Sort

**Description**
The current session’s ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true, the session is a member of the user’s current session family. This field`
is available in API version 37.0 and later.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
The date and time this session was last updated. A session expires when the
current date and time equals LastModifiedDate + NumSecondsValid.
This field is a standard system field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a
login event. Due to the nature of geolocation technology, the accuracy of
geolocation fields (for example, country, city, postal code) can vary. This field is
available in API version 34.0 and later.


-----

```
LoginHistoryId
LoginType

```

This is a relationship field.

**Relationship Name**
LoginGeo

**Relationship Type**
Lookup

**Refers To**
LoginGeo

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for a successful login event. When a session is reused,
Salesforce updates the `LoginHistoryId` with the value from the most
recent login. This field is available in API version 33.0 and later.

This is a relationship field.

**Relationship Name**
LoginHistory

**Relationship Type**
Lookup

**Refers To**
LoginHistory

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of login used to access the session. Possible values are:

**•** `AJAX Toolkit`

**•** `Apex Office Toolkit`

**•** `AppExchange`

**•** `Application`

**•** `AppStore`

**•** `Certificate-based login`

**•** `Chatter Communities External User`

**•** `Chatter Communities External User Third Party SSO`

**•** `Community`

**•** `Customer Service Portal Third-Party SSO`


-----

```
LogoutUrl

```


**•** `Customer Service Portal`

**•** `DataJunction`

**•** `DB Replication`

**•** `Employee Login to Community`

**•** `Excel Integration`

**•** `Help and Training`

**•** `HOTP YubiKey`

**•** `Lightning Login`

**•** `Networks Portal API Only`

**•** `Offline Client`

**•** `Order Center`

**•** `Other Apex API`

**•** `Outlook Integration`

**•** `Partner Portal Third-Party SSO`

**•** `Partner Portal`

**•** `Partner Product`

**•** `Passwordless Login`

**•** `Remote Access 2.0`

**•** `Remote Access Client`

**•** `Sales Anywhere`

**•** `Salesforce Outlook Integration`

**•** `Salesforce.com Website`

**•** `SAML Chatter Communities External User SSO`

**•** `SAML Customer Service Portal SSO`

**•** `SAML Idp Initiated SSO`

**•** `SAML Partner Portal SSO`

**•** `SAML Sfdc Initiated SSO`

**•** `SAML Site SSO`

**•** `Self-Service`

**•** `Signup`

**•** `Sync`

**•** `SysAdmin Switch`

**•** `Third Party SSO`

**•** `Unknown`

**•** `Validate`

**Type**
string


-----

```
NumSecondsValid
ParentId
SessionSecurityLevel
SessionType
SourceIp

```

**Properties**
Filter, Nillable, Sort

**Description**
The page or view to display after users log out of an Experience Cloud site, or an
org if they authenticated using SAML. This field is available in API version 32.0
and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of seconds before the session expires, starting from the last update
time.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the parent session, if one exists (for example, if the current
session is for a canvas app). If the current session doesn’t have a parent, this value
is the current session’s own ID.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Standard or High, depending upon the authentication method used.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of session. Common ones are UI, Content, API, and Visualforce.

[For more information, see User Session Types in the Object Reference Guide.](https://help.salesforce.com/s/articleView?id=sf.security_session_types.htm&language=en_US)

**Type**
string


-----

```
UserType
UsersId

##### Usage

```

**Properties**
Filter, Group, Sort

**Description**
IP address of the end user’s device from which the session started. This address
can be an IPv4 or IPv6 address.

The `SourceIp` field doesn't support the `LIKE comparison operator.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The kind of user for this session. Types include Standard, Partner, Customer Portal
Manager, High Volume Portal, and CSN Only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s Salesforce user ID.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User


The AuthSession object exposes session data and enables read and delete operations on that data. For example, use this object to see
who is signed in to your org. Or you can use this object to create a tool to delete a session, ending that user’s session. For a user, only
their own sessions are available, while administrators can see all sessions.

You can’t change user sessions with this object. You can only read and delete them.
