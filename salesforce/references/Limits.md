### Limits

List information about limits in your org. For each limit, this resource returns the maximum allocation and the remaining allocation based
on usage. Tabulated limits returned by the API are accurate within five minutes of resource consumption. For consistent values of this
REST API, avoid concurrent or rapid requests.

This resource is available in REST API version 29.0 and later for API users with the View Setup and Configuration permission.

#### Syntax

**URI**
```
  /services/data/vXX.X/limits/

```
**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Response Body**

|Limit Label|Description|
|---|---|
|Analytics||
|AnalyticsExternalDataSizeMB|Maximum amount of external data in bytes that can be uploaded daily via REST API|
|ConcurrentAsyncGetReportInstances|Concurrent REST API requests for asynchronous report run results|
|ConcurrentEinsteinDataInsightsStoryCreation|Concurrent Einstein Discovery data insights story creation via REST API|
|ConcurrentEinsteinDiscoveryStoryCreation|Concurrent Einstein Discovery story creation via REST API|
|ConcurrentSyncReportRuns|Concurrent synchronous report runs via REST API|
|HourlyAsyncReportRuns|Hourly asynchronous report runs via REST API|
|HourlySyncReportRuns|Hourly synchronous report runs via REST API|
|HourlyDashboardRefreshes|Hourly dashboard refreshes via REST API|


-----

|Limit Label|Description|
|---|---|
|HourlyDashboardResults|Hourly REST API requests for dashboard results|
|HourlyDashboardStatuses|Hourly dashboard status requests via REST API|
|DailyAnalyticsDataflowJobExecutions|Daily analytics dataflow job executions via REST API|
|DailyAnalyticsUploadedFilesSizeMB|Daily cumulative size of analytics files uploaded, in MB|
|DailyEinsteinDataInsightsStoryCreation|Daily Einstein Discovery data insight stores created via REST API|
|DailyEinsteinDiscoveryPredictAPICalls|Daily cumulative number of predicted Einstein Discovery REST API requests|
|DailyEinsteinDiscoveryPredictionsByCDC|Daily cumulative number of predicted Einstein Discovery change data capture add-ons created|
|DailyEinsteinDiscoveryOptimizationJobRuns|Daily cumulative number of Einstein Discovery optimization job runs|
|DailyEinsteinDiscoveryStoryCreation|Daily cumulative number of Einstein Discovery stories created via REST API|
|MonthlyEinsteinDiscoveryStoryCreation|Monthly cumulative number of Einstein Discovery stories created via REST API|
|Email||
|MassEmail|Daily number of mass emails that are sent to external email addresses via Apex or APIs|
|SingleEmail|Daily number of single emails that are sent to external email addresses Note: For orgs created before Spring ’19, the daily limit is enforced only for emails sent via Apex and Salesforce APIs except for REST API. For orgs created in Spring ’19 and later, the daily limit is also enforced for email alerts, simple email actions, Send Email actions in flows, and REST API. If one of the newly counted emails can’t be sent because your org has reached the limit, we notify you by email and add an entry to the debug logs.|
|Lightning Platform REST and Bulk APIs||
|CreateCustom|Maximum number of allowed custom permission sets. This limit is available for API version 41.0 and later.|
|DailyApiRequests|Daily API calls|
|DailyAsyncApexExecutions|Daily number of asynchronous Apex method executions, which include batch Apex, future methods, Queueable Apex, and scheduled Apex|
|DailyAsyncApexTests|Daily number of asynchronous Apex test executions. This limit is available in API version 56.0 and later.|
|DailyBulkApiBatches (API version 49.0 and later) or DailyBulkApiRequests (API version 48.0 and earlier)|Daily Bulk API and Bulk API 2.0 batches In Bulk API, batches are used by both ingest and query operations. In Bulk API 2.0, batches are used only by ingest operations.|


-----

|Limit Label|Description|
|---|---|
|DailyBulkV2QueryFileStorageMB|Daily storage for queries in Bulk API 2.0 (measured in MB). This limit is available in API version 47.0 and later.|
|DailyBulkV2QueryJobs|Daily number of query jobs in Bulk API 2.0. This limit is available in API version 47.0 and later.|
|PermissionSets|Maximum number of allowed permission sets. Corresponds to the “Permission sets: maximum (created and added as part of an installed managed AppExchange package)” feature allocation. This limit is available in API version 41.0 and later.|
|Platform Events||
|These values apply only to platform events. They don’t apply to change data capture events.||
|HourlyPublishedPlatformEvents|High-volume platform event notifications published per hour|
|HourlyPublishedStandardVolumePlatform Events|Standard-volume platform event notifications published per hour (You can no longer define standard-volume events. New platform events are high volume by default.)|
|DailyStandardVolumePlatformEvents|Daily standard-volume platform event notifications delivered to CometD clients (You can no longer define standard-volume events. New platform events are high volume by default.)|
|PlatformEventTriggersWithParallelProcessing|Number of Apex platform event triggers that you can configure for parallel subscriptions|
|Platform Events and Change Data Capture||
|These values apply to platform events and change data capture events.||
|DailyDeliveredPlatformEvents|Org Without Add-On License: Daily Usage and Default Allocation To get the number of high-volume platform events and change events delivered to CometD and Pub/Sub API clients, empApi Lightning components, and event relays in the last 24 hours, use DailyDeliveredPlatformEvents. This value doesn’t apply to other subscribers, such as Apex triggers, flows, and processes. This value applies to orgs that haven’t purchased the high-volume platform event or Change Data Capture add-on. Usage tracking frequency: DailyDeliveredPlatformEvents is updated within a few minutes after event delivery.|
|MonthlyPlatformEvents (API version 47.0 and earlier)|Org With Add-On License: Monthly Event Delivery Usage If your org purchased the high-volume platform event or Change Data Capture add-on, use MonthlyPlatformEvents. Or to get the usage-based entitlement, see the entry for MonthlyPlatformEventsUsageEntitlement in this table.|


-----

|Limit Label|Description|
|---|---|
||To get the monthly delivery usage for both high-volume platform events and change events to CometD and Pub/Sub API clients, empApi Lightning components, and event relays, use MonthlyPlatformEvents. This value doesn’t apply to other subscribers, such as Apex triggers, flows, and processes. Usage tracking frequency: MonthlyPlatformEvents is updated within a few minutes after event delivery.|
|MonthlyPlatformEventsUsageEntitlement (API version 48.0 and later)|Org With Add-On License: Monthly Usage-Based Entitlement If your org purchased the high-volume platform event or Change Data Capture add-on, use MonthlyPlatformEventsUsageEntitlement. This value is the monthly entitlement and usage of event delivery to CometD and Pub/Sub API clients, empApi Lightning components, and event relays and is incremented for each client. This value doesn’t apply to other subscribers, such as Apex triggers, flows, and processes. This value includes usage for both high-volume platform events and change events. Usage tracking frequency: MonthlyPlatformEventsUsageEntitlement is updated daily. The entitlement is reset every month after your contract start date. Entitlement usage is computed only for production orgs. It’s not available in sandbox or trial orgs. For more information, see Usage-based Entitlement Fields. With an add-on license, you can exceed the maximum entitlement by a certain amount. As a result, the remaining value returned can be negative if you exceeded the maximum value. Use MonthlyPlatformEventsUsageEntitlement with API version 48.0 or later to get an accurate event delivery usage based on the first day of your contract. In API version 47.0 and earlier, the MonthlyPlatformEvents value returns the usage based on the first of the month instead of the contract start date.|
|Private Connect||
|PrivateConnectOutboundCalloutHourlyLimitMB|Maximum amount of data in bytes that can be transferred per hour via outbound private connections.|
|Salesforce Connect||
|HourlyLongTermIdMapping|Hourly new long-term external record ID mappings|
|HourlyODataCallout|Hourly OData callouts|
|HourlyShortTermIdMapping|Hourly new short-term external record ID mappings|
|Salesforce Developer Experience||


-----

|Limit Label|Description|
|---|---|
|ActiveScratchOrgs|The maximum number of scratch orgs you can have at any given time based on the edition type. Allocation becomes available if you delete a scratch org or if a scratch org expires.|
|DailyScratchOrgs|The maximum number of successful scratch org creations you can initiate in a rolling (sliding) 24-hour window. Allocations are determined based on the number of scratch orgs created in the preceding 24 hours.|
|Package2VersionCreates|Daily number of package versions that you can create. Applies to unlocked and second-generation managed packages.|
|Package2VersionCreatesWithoutValidation|Daily number of package versions that skip validation that you can create. Applies to unlocked and second-generation managed packages.|
|Salesforce Functions||
|DailyFunctionsApiCallLimit (API version 53.0 and later)|Daily API calls in an org with Functions. Values are visible only if Salesforce Functions is enabled. For more information, see Functions Limits.|
|Storage||
|DataStorageMB|Data storage (MB) The API user must have the Manage Users permission.|
|FileStorageMB|File storage (MB) The API user must have the Manage Users permission.|
|Streaming API—Durable (API version 37.0 and later)||
|DailyDurableGenericStreamingApiEvents|Generic events notifications delivered in the past 24 hours to all CometD clients|
|DailyDurableStreamingApiEvents|PushTopic event notifications delivered in the past 24 hours to all CometD clients|
|DurableStreamingApiConcurrentClients|Concurrent CometD clients (subscribers) across all channels and for all event types|
|Streaming API (API version 36.0 and earlier)||
|DailyGenericStreamingApiEvents|Generic events notifications delivered in the past 24 hours to all CometD clients|
|DailyStreamingApiEvents|PushTopic event notifications delivered in the past 24 hours to all CometD clients|
|StreamingApiConcurrentClients|Concurrent CometD clients (subscribers) across all channels and for all event types|
|Workflows||
|DailyWorkflowEmails|Daily workflow emails|
|HourlyTimeBasedWorkflow|Hourly workflow time triggers|


-----

#### Example

See List Org Limits.
