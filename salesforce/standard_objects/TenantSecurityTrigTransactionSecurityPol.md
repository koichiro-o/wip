#### TenantSecurityTrigTransactionSecurityPol

Stores metric details related to Transaction Security Policy triggering events. This object is available in API version 63.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is read only.

##### Fields

```
ApexClass
ApexIdentifier
ClientIp
DetailIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Apex class used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Apex code used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP, such as
a login from AppExchange, is shown as “Salesforce.com IP”.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


-----

```
FlowIdentifier
FlowName
LoginKey
MetricIdentfier
MetricsType
Name

```

**Description**
The ID of the individual detail record. This field is unique within your organization.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Flow used to evaluate the policy.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the type of metric that was counted. This field is unique within your organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of data collected.

**Type**
string


-----

```
Policy Identifier
PolicyName
PolicyOutcome
PolicyType
RequestIdentifier

```

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the metric for which data is being collected.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the policy being evaluated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the policy being evaluated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the transaction policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The real time action selected for the policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier.


-----

```
RowVersion
SessionKey
Tenant
TenantName
Timestamp
Triggered Timestamp

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The ID of the tenant of this triggered the Transaction Security Policy event.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the tenant where this triggered Transaction Security Policy happened.

**Type**
dateTime

**Properties**
Filter, Group, idLookup, Sort

**Description**
The access time of Salesforce services in GMT. Milliseconds are the most granular setting.

**Type**
dateTime

**Properties**
Filter, Group, idLookup, Sort

**Description**
The time at which the Transaction Security event was generated.


-----

```
Uri
UserIdentifier
Username

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The URI of the page that’s receiving the request.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The username of the user who’s using Salesforce services through the UI or the API.

