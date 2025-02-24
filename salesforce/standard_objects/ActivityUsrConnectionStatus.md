#### ActivityUsrConnectionStatus

Represents the status of the email connections for Einstein Activity Capture users. You can also see whether users accepted the required
terms of service to capture emails. This object is available in API version 54.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, enable Einstein Activity Capture in your org.

##### Fields

```
ConfigurationName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Einstein Activity Capture configuration that the user is assigned to.


-----

```
ConnectivityStatus
ContactsSynced
EmailAddress
EventsSynced

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the user’s email connection.

Possible values are:

**•** `ACTIVE`

**•** `DISABLED`

**•** `INITIALIZING`

**•** `NEEDSATTENTION`

**•** `NEEDSATTENTIONGLOBAL (used when an org-level connection isn’t working)`

**•** `NEEDSATTENTIONHYBRID (used when both org-level and user-level connections`
aren’t working)

**•** `PENDING`

**•** `PROCESSING`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of contacts synced after midnight between Salesforce and the user’s Microsoft
or Google email account. This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address that’s used to capture and sync data between Salesforce and the user’s
Microsoft or Google account.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of events synced after midnight between Salesforce and the user’s Microsoft
or Google email account. This field is available in API version 59.0 and later.


-----

```
ExternalId
GlobalOauthTermsState
IsTermsOfServiceAccepted
RecommendedActionDescription

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for future use.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the user’s terms of service status. When emails are enabled for Einstein Activity
Capture, each user must accept the terms of service.

Possible values are:

**•** `ACCEPTED`

**•** `DECLINED`

**•** `PENDING`

This field is available only if you use an org-level OAuth 2.0 or a service account authentication
method. In connection report CSV files downloaded from Einstein Activity Capture Status &
Metrics, this field is labeled Global Auth User Email Consent Status.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the user has accepted the Einstein Activity Capture terms of service or
not. When emails are enabled for Einstein Activity Capture, each user must accept the terms
of service.

The default value is `false.`

This field is available only if you use a user-level authentication method. In connection report
CSV files downloaded from Einstein Activity Capture Status & Metrics, this field is labeled
User Auth Terms of Service Accepted.

**Type**
string

**Properties**
Filter, Nillable, Sort


-----

```
RecommendedActionTitle
UserId
UserName
UserOnboardingStatus

```

**Description**
Recommended action to take when the user’s `ConnectivityStatus` is
```
  NEEDSATTENTION. Available in API version 58.0 and later.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reason for the user's ConnectivityStatus when the status is NEEDSATTENTION.
Available in API version 58.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username of the Einstein Activity Capture user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The initial sync status when the user connects Salesforce with their external email account
and syncs data for the first time. This field is available in API version 59.0 and later.

Possible values are:

**•** `NOT_STARTED`

**•** `IN_PROGRESS`

**•** `NOT_CONFIGURED`

**•** `COMPLETE`

**•** `FAILED`


-----
