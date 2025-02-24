#### InsufficientAccessEventLog

Insufficient Access event logs contain details about errors relating to insufficient record access This object is available in API version 61.0
and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.


-----

##### Fields

**Field**
```
AccessError
ActualLoggedInUserIdentifier
ErrorDescription
ErrorTimestamp
ObjectType

```

**Type**
String

**Description**
The type of insufficient access error that the user received. Valid values are:

**•** `DATA_NOT_AVAILABLE—The record is no longer accessible. For example, a record`
was deleted and moved to the Recycle Bin.

**•** `INVALID_TYPE—The record type doesn’t exist.`

**•** `NO_ACCESS—The user doesn’t have the required access level to complete the`
attempted action on the record.

**Example**
```
  NO_ACCESS

```
**Type**
Id

**Description**
The ID of the user who initiated the action that caused the insufficient access error. For
example, a user attempts to transfer ownership of a record to a teammate, but the operation
fails because the teammate doesn’t have the required access.

**Example**
```
  005XXXXXXXXXXXX

```
**Type**
String

**Description**
Description of the insufficient access error that the user received.

**Example**
User 005XXXXXXXXXXXX doesn't have full access for the record 001XXXXXXXXXXXX.

**Type**
String

**Description**
The time in GMT that the insufficient access error occurred.

**Example**
```
  20130715233322.670

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
RecordIdentifier
RequestIdentifier
RequestedAccessLevel
Timestamp
UserIdentifier

```

**Description**
The object for which the user received the insufficient access error.

**Type**
String

**Description**
The ID of the record that the user doesn’t have access to.

**Example**
```
  001XXXXXXXXXXXX

```
**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events.

**Example**
```
  3nWgxWbDKWWDIk0FKfF5DV

```
**Type**
String

**Description**
The access level required by the user’s attempted action on the record. Valid values are:

**•** `DELETE`

**•** `FULL`

**•** `READ`

**•** `TRANSFER`

**•** `WRITE`

**Example**
```
  FULL

```
**Type**
dateTime

**Description**
The access time of Salesforce services in GMT.

**Example**
```
  20130715233322.670

```
**Type**
Id

**Description**
The ID of the user for whom the insufficient access error occurred, either when the user
couldn’t access a record, the user couldn’t complete an operation, or the user was the


-----

intended recipient of a record transfer that failed because the user didn’t have the required
access.

**Example**
```
                005XXXXXXXXXXXX
