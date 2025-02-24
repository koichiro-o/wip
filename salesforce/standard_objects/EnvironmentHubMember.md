#### EnvironmentHubMember

Represents a member organization in the Environment Hub. This object is available in API version 29.0 and later.

[Note: You can create only 20 member orgs per day. If you need to create additional orgs, log a support case in the Salesforce](https://partners.salesforce.com)
[Partner Community. For product, specify Platform. For topic, specify AppExchange & Managed Packages.](https://partners.salesforce.com)

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update()

 Fields

```
```
Description

```

**Type**
textarea

**Properties**
Nillable, Update


-----

```
DisplayName
EnvironmentHubId
Instance
IsFedIdSsoMatchAllowed
IsSandbox
MemberEntity

```

**Description**
A brief description of this org.

**Type**
string

**Properties**
Filter, Group, Nillable,Sort, Update

**Description**
The name that the user has specified for this member org.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The Org ID of this member’s Environment Hub org.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the instance where the Environment Hub member org resides.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if single sign-on (SSO) has been enabled based on matching the Federation
ID. The default is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the member org is a sandbox (true) or not (false). This field is available
in API version 36.0 and later.

**Type**
string


-----

```
MemberType
Name
OrgEdition
OrgStatus

```

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique Org ID of the member org for this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of member org for this record. Possible values include Branch Org, Patch
```
  Org, Release Org, Sandbox Org, Trialforce Management Org,

```
and `Trialforce Source Org.`

Note: Only one member type at a time is stored. Member type is determined
according to this hierarchy: (1) Sandbox, (2) Release, (3) Trialforce Source Org
(TSO), (4) Patch, (5) Branch, and (6) Trialforce Management Org (TMO). For
example, if an org is both a sandbox and a TMO, the value of `MemberType` is
```
    Sandbox Org.

```
**Type**
string

**Properties**
Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the member org for this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The org’s edition, for example, Enterprise Edition or Unlimited Edition.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The licensing or creation status of this org. Possible values include `Active,` `Demo,`
```
  Deleted, Free, Inactive, and Trial.

```

-----

```
Origin
SSOMappedUsers
ServiceProviderId
ShouldAddRelatedOrgs
ShouldEnableSSO
SsoStatus

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The method by which this org was added to the Environment Hub. Possible values are
```
  autoDiscovered, userAdded, and provisioned.

```
**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of mapped users in this member org. This field is available in API
version 36.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service provider for this member org. This field is available in API version
36.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Status of the connection of related orgs to the hub. Possible values are `done,`
```
  notRequested, pending, and requested.

```
**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If SSO should be enabled when this member org is added. The default is `false.`

**Type**
picklist


-----

```
SsoUsernameFormula

##### Usage

```

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If SSO has been enabled for this org. Possible values are:

**•** `Enabled—Single sign-on is enabled.`

**•** `Disabled—Single sign-on is disabled.`

**•** `Pending—Single sign-on is in the process of being enabled.`

**•** `Failed—Single sign-on enablement failed. Contact Salesforce support for`
assistance.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The custom formula for matching users in the hub and member orgs.


Use this object to access and modify settings of member orgs in the Environment Hub.
