#### ConnectedApplication

Represents a connected app and its details; all fields are read-only.

Connected apps link client applications, third-party services, other Salesforce organizations, apps, and resources to your organization.
The connected app configuration specifies authorization and security settings for these resources. This object exposes the settings for
a specified connected app.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
MobileSessionTimeout
MobileStartUrl
Name
NamedUserUvidTimeout

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Length of time after which the system logs out inactive mobile users.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**

Users are directed to this URL after they’ve authenticated when the app is accessed
from a mobile device.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The unique name for this object.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
OptionsAllowAdminApprovedUsersOnly
OptionsAppIssueJwtTokenEnabled

```

**Description**

The timeout value for a JSON Web Token (JWT)-based access token that contains
a unique visitor ID (UVID) and that is issued to a named user..

Possible values are:

**•** `1—1 Minute`

**•** `5—5 Minutes`

**•** `10—10 Minutes`

**•** `15—15 Minutes`

**•** `30—30 Minutes`

Available in API version 59.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**

Indicates whether access is limited to users granted approval to use the connected
app by an administrator. Manage profiles for the app by editing each profile’s
Access list.

**Type**
boolean

**Properties**
Filter

**Description**

If set to `true, the connected app is enabled to issue JWT-based access tokens.`
For installed apps, JWT-based access tokens must also be enabled in your
connected app policies.

Available in API version 59.0 and later.


`OptionsCodeCredentialGuestEnabled` Reserved for future use.

`OptionsFullContentPushNotifications` For internal use only.

```
OptionsHasSessionLevelPolicy

```

**Type**
boolean

**Properties**
Filter

**Description**

Specifies whether the connected app requires a High Assurance level session.


-----

`OptionsIsInternal` For internal use only.

```
OptionsRefreshTokenValidityMetric
OptionsTokenExchangeManageBitEnabled
PinLength
RefreshTokenValidityPeriod
StartUrl

```

**Type**
boolean

**Properties**
Filter

**Description**

Specifies whether the refresh token validity is based on duration or inactivity. If
```
  true, the token validity is measured based on the last use of the token;

```
otherwise, it’s based on the token duration.

**Type**
boolean

**Properties**
Filter

**Description**

If `true, the OAuth 2.0 token exchange flow is enabled.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

For mobile apps, this field is the PIN length requirement for users of the connected
app. Valid values are `4, 5,` `6,` `7, or` `8.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The duration of an authorization token until it expires in hours, months, or days
as set in the connected app management page.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**

If the app isn’t accessed from a mobile device, users are directed to this URL after
they’ve authenticated.


-----

```
UvidTimeout
