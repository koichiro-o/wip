#### SandboxStatusEventLog

SandboxStatusEventLog stores details about Sandbox copies. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
CurrentSandboxOrganizationIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the current sandbox organization.


-----

```
PendingSandboxOrganizationIdentifier
RequestIdentifier
SandboxOrganizationIdentifier
Status
Timestamp
UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the target sandbox org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID. For example:
3nWgxWbDKWWDIk0FKfF5DV.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the target sandbox org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the sandbox copy.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example: 20130715233322.670.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: 00530000009M943YAS

.
