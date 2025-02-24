#### PackageInstallEventLog

PackageInstallEventLog stores details about package installation in the organization. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
ClientIp
CpuTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26.`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.


-----

```
ErrorType
IsManaged
IsPush
IsReleased
IsSuccessful
LoginKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A general categorization of any error that’s encountered.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the operation is performed on a managed package.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the package was installed as a result of a push upgrade.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the operation is performed on a released package.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if the package was successfully installed.

The default value is `false.`

**Type**
string


-----

```
OperationType
PackageName
RequestIdentifier
RunTime

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of package operation.

**Possible Values**

**•** INSTALL

**•** UPGRADE

**•** EXPORT

**•** UNINSTALL

**•** VALIDATE_PACKAGE

**•** INIT_EXPORT_PKG_CONTROLLER

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the package that’s being installed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID.`

For example: `3nWgxWbDKWWDIk0FKfF5DV.`

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
SessionKey
Timestamp
Uri
UserIdentifier
