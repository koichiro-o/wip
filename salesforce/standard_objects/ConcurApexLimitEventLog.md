#### ConcurApexLimitEventLog

Concurrent Apex Limit event logs contain information about long-running concurrent Apex requests in your org that Salesforce terminated
after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5 seconds are counted towards
your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards the limit.) When the long-running
requests exceed the org default limit, additional long-running requests are denied. This object is available in API version 55.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To access this object, you must have the View Event Log Object Data user permission.

##### Fields

```
RequestCount

```

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
Count of requests with an established Apex context executing for longer than 5 seconds in
your org.


-----

```
RequestIdentifier
RequestLimit
RequestUri
Timestamp
UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier. For example:`
```
  3nWgxWbDKWWDIk0FKfF5DV.

```
**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Maximum count of requests with an established Apex context that can execute for longer
than 5 seconds. When `RequestCount` reaches this limit, then additional long-running
Apex requests are terminated. (Asynchronous requests don’t count towards the limit.) See
_[Apex Developer Guide: Lightning Platform Apex Limits. For example:](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_non_transactional_gov_limits_section)_ `10.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the long-running Apex request that Salesforce terminated. For example:
```
  /apex/ApexClassName.

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
```
  2020-01-20T19:12:26.965Z. Milliseconds are the most granular setting.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943.`


-----
