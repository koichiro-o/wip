### Using Event Monitoring

```
These examples use REST API event monitoring data that contains information useful for assessing org usage trends and user behavior.
Event monitoring is accessed through the Lightning Platform SOAP API and REST API by way of the EventLogFile object. Therefore, you
can integrate log data with your own back-end storage and data marts to correlate data from multiple orgs and across disparate systems.

[Note: For the supported event types that you can use with event monitoring, see Object Reference for Salesforce and Lightning](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)
[Platform: EventLogFile Object.](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

**•** In the unlikely case where no log files are generated for 24 hours, contact Salesforce Customer Support.

**•** Log data is read only. You can’t insert, update, or delete log data. However, you can delete event log files.

**•** To determine which files were generated for your org, use the `EventType` field.

**•** An event generates log data in real time. However, daily log files are generated during nonpeak hours the day after an event takes
place. Therefore, daily log file data is unavailable for at least 1 day after an event. For hourly log files, depending on event delivery


-----

and final processing time, expect an event to take place 3–6 hours from the time of the event to be available in the log file. However,
it can take longer.

**•** Log files are generated only when at least one event of a type, represented by the `EventType` field, occurs for the day or hour.
If no events took place, the file isn’t generated.

**•** Log files are available for 30 days after their CreatedDatein orgs with Event Monitoring licenses, after which they’re automatically
deleted. In all Developer Edition orgs, log files are available for 1 day.

**•** All event monitoring logs are exposed to the API through the EventLogFile object. However, there’s no access through the user
interface, except through the Event Monitoring Analytics app.

**•** Log files don’t count towards your org’s data or file storage allocations.

**•** Event Monitoring log files aren’t a system of record for user activity. They’re a source of truth, but they aren’t durable. During Salesforce
site switches, instance refreshes, or unplanned system outages, data loss can occur. For example, if Salesforce moves your production
org instance, your event log files can have a gap in data. Salesforce makes commercially reasonable efforts to preserve event log file
data integrity and avoid data loss. When Salesforce performs a site switch or instance refresh, it uses an automated process to replicate
event logs.

**•** Hourly event log files are provided for you to review events in your orgs on an accelerated basis. However, it’s possible that you don’t
get all event log data in hourly event log files, especially during site switches, instance refreshes, or unplanned system outages. For
complete data, use the daily log files.

**•** If event transmission failures take too long to recover from, log files are retransmitted to ensure that they’re delivered at least one
time. As a result, latent log files can sometimes contain duplicate event data. When your application consumes latent log files, make
sure that your application handles duplicate event delivery.

**•** When a daily incremental log file is delivered, a new file replaces the original file with the full set of available logs for that date. To
ensure that you’re looking at the most recent log file, check the `CreatedDate` field.

**•** We recommend that you always query the EventLogFile object for new log files to ensure that you also include latent ones. To
identify newly created log files, use the EventLogFile CreatedDate field. Hourly and daily incremental logs are delivered differently.
For details, see Differences Between Hourly and 24-Hour Event Logs.

All queries and examples in this section require the View Event Log Files and API Enabled user permissions. Users with the View All Data
permission can also view event monitoring data.

IN THIS SECTION:

Describe Event Monitoring Using REST
Use the sObject Describe resource to retrieve all metadata for an object, including information about fields, URLs, and child relationships.

Query Event Monitoring Data with REST
Use the Query resource to retrieve field values from a record. Specify the fields you want to retrieve in the fields parameter and use
the `GET` method of the resource.

Get Event Monitoring Content from a Record
Use the sObject Blob Retrieve resource to retrieve BLOB data for a given record.

Download Large Event Log Files Using cURL with REST
You might have some event log files that are larger than your tool can handle. A command line tool such as cURL is one method to
download files larger than 100 MB using the sObject Blob Get object

Delete Event Monitoring Data
You can delete event log files that contain a user’s log data. Deleting log files helps you comply with data protection and privacy
regulations and controls the information that others can access. You can’t delete individual rows from event logs. Instead, you must
delete the entire log file that contains the user activity.


-----

Query or View Hourly Event Log Files
To review events in your org on an accelerated basis, get event log files in hourly increments for recent activity. Hourly event log
files can give you quicker visibility into security anomalies and custom code performance issues.

#### Describe Event Monitoring Using REST

Use the sObject Describe resource to retrieve all metadata for an object, including information about fields, URLs, and child relationships.

**Example**

You can use REST API to describe event log files. Use a GET request like this:
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/EventLogFile/describe
   -H "Authorization: Bearer token"

```
**Example raw response**
```
  {
    "actionOverrides" : [ ],
    "activateable" : false,
    "childRelationships" : [ ],
    "compactLayoutable" : false,
    "createable" : false,
    "custom" : false,
    "customSetting" : false,
    "deletable" : false,
    "deprecatedAndHidden" : false,
    "feedEnabled" : false,
    "fields" : [ {
     "autoNumber" : false,
     "byteLength" : 18,
     "calculated" : false,
     "calculatedFormula" : null,
     "cascadeDelete" : false,
     "caseSensitive" : false,
     "controllerName" : null,
     "createable" : false,
     ...
  }

#### Query Event Monitoring Data with REST

```
Use the Query resource to retrieve field values from a record. Specify the fields you want to retrieve in the fields parameter and use the
`GET` method of the resource.

You can use REST API to query event monitoring data. To retrieve event monitoring records based on `LogDate` and `EventType,`
use a GET request like this:


-----

**Example raw response**
```
  {
    "totalSize" : 4,
    "done" : true,
    "records" : [ {
     "attributes" : {
      "type" : "EventLogFile",
      "url" : "/services/data/v62.0/sobjects/EventLogFile/0ATD000000001bROAQ"
     "Id" : "0ATD000000001bROAQ",
     "EventType" : "API",
     "LogFile" : "/services/data/v62.0/sobjects/EventLogFile/0ATD000000001bROAQ/LogFile",
     "LogDate" : "2014-03-14T00:00:00.000+0000",
     "LogFileLength" : 2692.0
    }, {
     "attributes" : {
      "type" : "EventLogFile",
      "url" : "/services/data/v62.0/sobjects/EventLogFile/0ATD000000001SdOAI"
      "Id" : "0ATD000000001SdOAI",
      "EventType" : "API",
      "LogFile" :
  "/services/data/v62.0/sobjects/EventLogFile/0ATD000000001SdOAI/LogFile",
      "LogDate" : "2014-03-13T00:00:00.000+0000",
      "LogFileLength" : 1345.0
    }, {
      "attributes" : {
       "type" : "EventLogFile",
       "url" : "/services/data/v62.0/sobjects/EventLogFile/0ATD000000003p1OAA"
       "Id" : "0ATD000000003p1OAA",
       "EventType" : "API",
       "LogFile" :
  "/services/data/v62.0/sobjects/EventLogFile/0ATD000000003p1OAA/LogFile",
       "LogDate" : "2014-06-21T00:00:00.000+0000",
       "LogFileLength" : 605.0 },
   { "attributes" : {
      "type" : "EventLogFile",
      "url" : "/services/data/v62.0/sobjects/EventLogFile/0ATD0000000055eOAA"
      "Id" : "0ATD0000000055eOAA",
      "EventType" : "API",
      "LogFile" :
  "/services/data/v62.0/sobjects/EventLogFile/0ATD0000000055eOAA/LogFile",
      "LogDate" : "2014-07-03T00:00:00.000+0000",
      "LogFileLength" : 605.0
     } ]
  }

#### Get Event Monitoring Content from a Record

```
Use the sObject Blob Retrieve resource to retrieve BLOB data for a given record.


-----

**Example**

You can use REST API to retrieve BLOB data for event monitoring. Use a GET request similar to this:
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/EventLogFile/0ATD000000000pyOAA/LogFile
   -H "Authorization: Bearer token"

```
**Example response body**
Event monitoring content is returned in binary form. Note that the response content type won’t be JSON or XML because the returned
data is binary.
```
  HTTP/1.1 200 OK
  Date: Tue, 06 Aug 2013 16:46:10 GMT
  Sforce-Limit-Info: api-usage=135/5000
  Content-Type: application/octetstream
  Transfer-Encoding: chunked
  "EVENT_TYPE", "ORGANIZATION_ID", "TIMESTAMP","USER_ID", "CLIENT_IP",
  "URI", "REFERRER_URI", "RUN_TIME"
  "URI", "00DD0000000K5xD", "20130728185606.020", "005D0000001REDy",
  "10.0.62.141", "/secur/contentDoor", "https-//login-salesforce-com/",
  "11"
  "URI", "00DD0000000K5xD", "20130728185556.930", "005D0000001REI0",
  "10.0.62.141", "/secur/logout.jsp", "https-//MyDomainName-my-salesforce-com/00O/o",
  "54"
  "URI", "00DD0000000K5xD", "20130728185536.725", "005D0000001REI0",
  "10.0.62.141", "/00OD0000001ckx3",
  "https-//MyDomainName-my-salesforce-com/00OD0000001ckx3", "93"

#### Download Large Event Log Files Using cURL with REST

```
You might have some event log files that are larger than your tool can handle. A command line tool such as cURL is one method to
download files larger than 100 MB using the sObject Blob Get object

**Example: Use the “X-PrettyPrint” header and the “-o” flag to output large files to .csv formats**
This command downloads a file onto your machine into your downloads folder.
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/EventLogFile/0AT30000000000uGAA/LogFile
  -H "Authorization: Bearer token" -H "X-PrettyPrint:1" -o ~/downloads/outputLogFile.csv

```
We recommend using compression when downloading large event log files. See Compression Headers.

#### Delete Event Monitoring Data

You can delete event log files that contain a user’s log data. Deleting log files helps you comply with data protection and privacy
regulations and controls the information that others can access. You can’t delete individual rows from event logs. Instead, you must
delete the entire log file that contains the user activity.

To delete an event log file, enable deletion in Setup, create a permission set that includes the Delete Event Monitoring Records user
permission, and assign this permission set to your users. (Alternatively, you can assign the user permission to a custom profile.) Then
those users can query and delete the EventLogFile record by using Query and Delete resources in REST or `delete()` in SOAP.


-----

Note: You can’t delete individual rows from event logs. Because event logs are stored in blob format in the database, you must
delete the entire log file that contains the user activity.

**1. In Setup, in the Quick Find box, enter** `Event, and then select Event Monitoring Settings.`

**2. Enable deletion of event monitoring data. This action is recorded in Setup Audit Trail.**

The Delete Event Monitoring Records user permission is now available to assign to a permission set. (Alternatively, you can assign
the user permission to a custom profile.)

**3. In Setup, in the Quick Find box, enter** `Permission, and then select Permission Sets.`

**4. Create a permission set that includes the Delete Event Monitoring Records user permission, and save the permission set.**

**5. In Setup, in the Quick Find box, enter** `users, and then select Users.`

**6. Select the user you want to grant permission to delete event monitoring data.**

**7. In the Permission Set Assignment section for this user, assign the permission set, and click Save. This action is recorded in Setup**
Audit Trail.
Users assigned this permission set (or any custom profile that includes the Delete Event Monitoring Records user permission) can
now delete event monitoring data. The next steps show you how to use the API to delete the data.

**8. To locate the logs containing the user activity that you want to delete, query the EventLogFile object. For details, see Query Event**
Monitoring Data with REST on page 92.

**9. Note the IDs of the returned logs.**

**10. Use the sObject Rows resource to delete records. Specify the record ID, and use the DELETE method. For more information, see**

Delete a Record on page 47.


-----

#### Query or View Hourly Event Log Files

To review events in your org on an accelerated basis, get event log files in hourly increments for
recent activity. Hourly event log files can give you quicker visibility into security anomalies and
custom code performance issues.

**Examples**

Suppose you’re a security analyst monitoring for anomalous user behavior. By pulling more frequent
updates into your security system, you can be alerted that a suspicious event has taken place within
hours, rather than one or two days later.

In another example, let’s say you’re a developer. You’ve identified a series of Apex failures in your
org, and you want to proactively refactor your Apex code to improve performance. You review
hourly log files to pinpoint the issues and fix your code in hours, before your end users start
complaining about poor performance.

**Considerations**

**•** Hourly event log file integration with the Event Monitoring Analytics app is unavailable.

**•** Depending on event delivery and final processing time, an event is expected to take three to
six hours from the time of the event to be available in the log file. However, it can take longer.


###### EDITIONS


Available in: Enterprise,
**Performance, Unlimited,**
and Developer Editions


###### USER PERMISSIONS


To access the API and query
log files:

**•** API Enabled AND View
Event Log Files

To view event log files:

**•** View All Data



**•** When delays in processing occur and event logs for a particular hour arrive later, a new log file is created for the event/date/hour
and lists only the new events. Use the creation date and an incremental sequence number to identify a new log file. Always use the
most recently processed event log file for a particular date. However, if event log files have already been pulled into a third-party
application, they could require deduplication in that application.

If both hourly and daily logs are enabled, daily logs always have a sequence number of 0 because there is only one file per daily
interval. CreatedDate indicates when the file was generated. If CreatedDate is after the last event log file download, there are new
events to be processed.

For best practices, use CreatedDate in the WHERE clause to select logs created after the last downloaded event log file. For example,
if the last downloaded file was at 12PM 2/1/2018, to find the next log file, use +CreatedDate+>+"2018-02-01T12:00:00Z" in the
WHERE clause.

**•** Your event log files may show a gap in data during site switches, instance refreshes, or unplanned system outages. However, during
site switches and instance refreshes, Salesforce makes a commercially reasonable effort to avoid such data loss by using an automated
process to replicate event logs.

**•** In the unlikely case in which no log files are generated for 24 hours, contact Salesforce Support.

IN THIS SECTION:

Query Hourly Event Log Files
You query hourly event log files in the same way you query 24-hour log files.

Differences Between Hourly and 24-Hour Event Logs
You receive event log files approximately every hour in addition to 24-hour log files. Review the differences between the two logs
so that you can filter your files to analyze the event data you want.

##### Query Hourly Event Log Files

You query hourly event log files in the same way you query 24-hour log files.


-----

Suppose you’re an administrator. Your Chief Security Officer asks you to identify who modified specific accounts and opportunities in
the past two hours. You query the hourly URI event log files using the EventLogFile object to review the page requests and request
status. Because EventLogFile also returns 24-hour log files, use this SOQL syntax to filter out the 24-hour log files.
```
curl https://MyDomainName.my.salesforce.com/services/data/v62.0/query?q=SELECT+Id+,
+EventType+,+Interval+,+LogDate+,+LogFile+FROM+EventLogFile+WHERE+EventType+=+'URI'+
AND+Interval+=+'Hourly' -H "Authorization: Bearer token"

```
In the query, `Interval=Hourly` makes sure that only hourly event log file data is returned. Alternatively, you can use Sequence
to filter out 24-hour event log files (Sequence!=0). To get both hourly and 24-hour files, use Sequence>=0.

If your sandbox org has URI events, you see log file records in your query results. You can also download the event log files to review the
[data in a CSV file. For more information, see Trailhead: Download and Visualize Event Log Files.](https://trailhead.salesforce.com/event_monitoring/event_monitoring_download)

##### Differences Between Hourly and 24-Hour Event Logs

You receive event log files approximately every hour in addition to 24-hour log files. Review the differences between the two logs so
that you can filter your files to analyze the event data you want.

**Hourly Log Files** **24-Hour Log Files**

One or more files generated for every hour of activity. One file generated for every 24 hours of activity.

Available in the API. You can manually import data into third-party Available in the API and integrated with the Event Monitoring
visualization apps. Analytics app and third-party visualization apps.

Key values in the EventLogFile object are: Key values in the EventLogFile object are:

**•** `Interval—Hourly` **•** `Interval—Daily`

**•** `CreatedDate—Timestamp of when the log file was` **•** `CreatedDate—Timestamp of when the log file was`
created. Use this field to identify new files. created. Use this field to identify new files.

**•** `LogDate—Timestamp that marks the beginning of the` **•** `LogDate—Timestamp that marks the beginning of the`
interval when the events occurred. For example, for events interval when the events occurred. For example, for events
that occurred between 11:00 AM and 12:00 PM on 3/7/2016, that occurred on 3/7/2016, this field’s value is
this field’s value is 2016-03-07T11:00:00.000Z. 2016-03-07T00:00:00.000+0000.

**•** `Sequence—1+. This value increases by 1 when events are` **•** `Sequence—0`
added in the same hour after the latest event log file is created.
The value resets to 1 in the subsequent hour.

See also these Considerations regarding hourly event logs.

When an hourly incremental log file is delivered, a file with new When a daily incremental log file is delivered, a new file replaces
logs for that hour is created. The Sequence field is incremented the original file with the full set of available logs for that date. The
for each new file. `CreatedDate field is updated.`

Note: Like with 24-hour event monitoring, hourly event log data is available for the past 30 days.

|Hourly Log Files|24-Hour Log Files|
|---|---|
|One or more files generated for every hour of activity.|One file generated for every 24 hours of activity.|
|Available in the API. You can manually import data into third-party visualization apps.|Available in the API and integrated with the Event Monitoring Analytics app and third-party visualization apps.|
|Key values in the EventLogFile object are: • Interval—Hourly • CreatedDate—Timestamp of when the log file was created. Use this field to identify new files. • LogDate—Timestamp that marks the beginning of the interval when the events occurred. For example, for events that occurred between 11:00 AM and 12:00 PM on 3/7/2016, this field’s value is 2016-03-07T11:00:00.000Z. • Sequence—1+. This value increases by 1 when events are added in the same hour after the latest event log file is created. The value resets to 1 in the subsequent hour. See also these Considerations regarding hourly event logs.|Key values in the EventLogFile object are: • Interval—Daily • CreatedDate—Timestamp of when the log file was created. Use this field to identify new files. • LogDate—Timestamp that marks the beginning of the interval when the events occurred. For example, for events that occurred on 3/7/2016, this field’s value is 2016-03-07T00:00:00.000+0000. • Sequence—0|
|When an hourly incremental log file is delivered, a file with new logs for that hour is created. The Sequence field is incremented for each new file.|When a daily incremental log file is delivered, a new file replaces the original file with the full set of available logs for that date. The CreatedDate field is updated.|


-----
