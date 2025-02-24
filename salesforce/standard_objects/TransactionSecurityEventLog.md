#### TransactionSecurityEventLog

Transaction Security event logs contain details about policy execution. Legacy transaction security policy details are supported in API
version 38.0 and later. Enhanced transaction security policy details are supported in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
ApexIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
ClientIp
CpuTime
EvaluationTime
EventName
FlowIdentifier
LoginKey

```

**Description**
The ID of the Apex code used to evaluate the policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”. For example: 96.43.144.26.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time in milliseconds used to evaluate the policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the event, which is `Transaction Security Event.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow used to evaluate the policy.

**Type**
string


-----

```
PolicyIdentifier
PolicyOutcome
PolicyType
RequestIdentifier

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
```
  GeJCsym5eyvtEK2I.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the policy being evaluated. For example: `00530000009M943.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the transaction policy.

Possible values are:

**•** `Error—The policy caused an undefined error when it executed.`

**•** `ExemptNoAction—The user is exempt from transaction security policies, so the`
policy didn’t trigger.

**•** `MeteringBlock—The policy took longer than 3 seconds to process, so the user was`
blocked from performing the operation.

**•** `MeteringNoAction—The policy took longer than 3 seconds to process, but the`
user isn't blocked from performing the operation.

**•** `NoAction—The policy didn't trigger.`

**•** `Notified—A notification was sent to the recipient.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The real time action selected for the policy.

**Type**
string


-----

```
Result
RunTime
SendEmailNotification
SendInAppNotification
SessionKey

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Globally unique id for a given request. For example: `3nWgxWbDKWWDIk0FKfF5DV.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The outcome of evaluating the policy. For example: `NOT TRIGGERED.`

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to send an email notification. The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to send an in-app notification. The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started. For example:
```
  d7DEq/ANa7nNZZVD.

```

-----

```
Timestamp
TriggeredTimestamp
Uri
UserIdentifier
