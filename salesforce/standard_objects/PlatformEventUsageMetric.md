#### PlatformEventUsageMetric

```
Contains usage data for event publishing and delivery to CometD and Pub/Sub API clients, empApi Lightning components, and event
relays. If Enhanced Usage Metrics isn't enabled, usage data is available for the last 24 hours, ending at the last hour, and for historical
daily usage. In API 58.0 and later, you can enable Enhanced Usage Metrics to get usage data by event name and client for granular time
intervals. PlatformEventUsageMetric contains separate usage metrics for platform events and change data capture events. This object
is available in API version 50.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
Client

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
EndDate
EventName
EventType

```

**Description**
This field is available only when Enhanced Usage Metrics is enabled. The ID of the client. The
`Client` field is populated for subscriber clients for event delivery usage. For publisher
clients, the `Client` field is populated if the client ID is available; it is empty otherwise.

The `Client` field can be one of these values.

**•** For a Streaming API (CometD) client and the empApi Lightning component, the client
ID is the ID of the CometD session.

**•** For a Pub/Sub API client, the client ID is in this format: pub-sub-api-timestamp.
The timestamp is the current UTC time in milliseconds when the client connection started.

**•** For an event relay, the client ID is in this format: relay-client-timestamp. The
timestamp is the current UTC time in milliseconds when the client connection started.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end date and time in UTC used for querying usage metrics. The date granularity is hourly.

To get usage data for the last 24 hours, the end date is the current date in UTC. The time is
the current time in UTC rounded down to the previous hour. For example, 11:23 is 11:00 and
the date format is: 2020-08-04T11:00:00.000Z

To get historical data, the end date in UTC is the end of the date range with hours specified
as 0. For example: 2020-08-04T00:00:00.000Z. To query a date range, you can use the < or
<= operators.

[For the date format to use, see Date Formats and Date Literals in the SOQL and SOSL Reference.](https://developer.salesforce.com/docs/atlas.en-us.254.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is available only when Enhanced Usage Metrics is enabled. The API name of a
custom platform event or a change event.

**•** Custom platform event with the label My Event: `My_Event__e`

**•** Change event example: `AccountChangeEvent`

When you query usage metrics for `EventName, specify the` `UsageType` field in the
`SELECT` or `WHERE` clause.

**Type**
picklist


-----

```
ExternalId
Name
StartDate

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The type of event you would
like to query usage metrics for, such as a change event or a custom platform event.

Possible values are:

**•** `CHANGE_EVENT—A Change Data Capture event.`

**•** `CUSTOM_PLATFORM_EVENT—A platform event that an admin defined in your`
Salesforce org.

When you query usage metrics for `EventType, specify the` `UsageType` field in the
`SELECT` or `WHERE` clause.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the metric to get usage for.

Possible values are:

**•** `CHANGE_EVENTS_DELIVERED—Number of change data capture events delivered`
to CometD and Pub/Sub API clients, empApi Lightning components, and event relays

**•** `CHANGE_EVENTS_PUBLISHED—Number of change data capture events published`

**•** `PLATFORM_EVENTS_DELIVERED—Number of platform events delivered to CometD`
and Pub/Sub API clients, `empApi` Lightning components, and event relays

**•** `PLATFORM_EVENTS_PUBLISHED—Number of platform events published`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The start date and time in UTC used for querying usage metrics. The date granularity is hourly.


-----

```
TimeSegment
UsageType

```

To get usage data for the last 24 hours, the start date is the previous day in UTC. The time is
the current time in UTC rounded down to the previous hour. For example, 11:23 is 11:00 and
the date format is: 2020-08-03T11:00:00.000Z

To get historical data, the start date is the start of the date range with hours specified as 0.
For example: 2020-08-03T00:00:00.000Z. To specify a date range, you can use the > or >=
operators.

If Enhanced Usage Metrics is enabled, keep in mind these tips.

**•** Make sure the time span between `StartDate` and `EndDate` is valid for the
`TimeSegment` value chosen.

**•** The maximum date range that you can specify between StartDate and EndDate
is 60 days.

[For the date format to use, see Date Formats and Date Literals in the SOQL and SOSL Reference.](https://developer.salesforce.com/docs/atlas.en-us.254.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The time interval used for
aggregating usage data returned in the query results. Valid TimeSegment values depend
on the time range specified with `StartDate` and `EndDate.`

Possible values are:

`Daily` Usage data is aggregated for Valid only if the time range

each day within the specified specified with StartDate
time range. and EndDate in the query

is at least 24 hours.

`Hourly` Usage data is aggregated for Valid only if the time range

each hour within the specified with StartDate
specified time range. and EndDate in the query

is between one hour and 24
hours.

`FifteenMinutes` Usage data is aggregated for Valid only if the time range

each 15-minute period specified with StartDate
within the specified time and EndDate in the query
range. is between 15 minutes and

one hour.

**Type**
picklist

|Col1|Col2|Col3|
|---|---|---|
|Daily|Usage data is aggregated for each day within the specified time range.|Valid only if the time range specified with StartDate and EndDate in the query is at least 24 hours.|
|Hourly|Usage data is aggregated for each hour within the specified time range.|Valid only if the time range specified with StartDate and EndDate in the query is between one hour and 24 hours.|
|FifteenMinutes|Usage data is aggregated for each 15-minute period within the specified time range.|Valid only if the time range specified with StartDate and EndDate in the query is between 15 minutes and one hour.|


-----

```
Value

##### Usage

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available when Enhanced Usage Metrics is enabled. The type of event usage
metrics to query for, such as event publishing or event delivery. Use this field with the
`EventName` or `EventType` fields.

Possible values are:

**•** `PUBLISH—Usage metrics for published events.`

**•** `DELIVERY—Usage metrics for events that were delivered to subscribers.`

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The usage value for the specified metric and date range.


[For more information, see Monitor Platform Event Publishing and Delivery Usage in the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/platform_events_monitor_usage.htm)
