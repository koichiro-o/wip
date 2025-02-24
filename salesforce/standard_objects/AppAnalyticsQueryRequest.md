#### AppAnalyticsQueryRequest

Represents a request for AppExchange App Analytics data.

AppExchange App Analytics is available for packages that passed security review and are registered to a License Management App
(LMA). Usage data is provided as package usage logs, as month-based package usage summaries, or as point-in-time subscriber snapshots.
Usage logs, monthly usage summaries, and subscriber snapshots are downloadable comma-separated value (.csv) files. For information
[on how to optimize your use of App Analytics, see AppExchange App Analytics Best Practices.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_best_practices.htm)

[Note: Usage data from Government Cloud and Government Cloud Plus orgs isn’t available in App Analytics.](https://www.salesforce.com/solutions/industries/government1/products/government-cloud/)

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```

-----

##### Special Access Rules

[See Get Started with AppExchange App Analytics in the Second-Generation Managed Packaging Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_intro_2gp.htm)

##### Fields

```
AvailableSince
DataType

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

An optional value used to limit the requested results file to data newly arrived in
the data lake after the specified date and time. This field is always transferred in
the Coordinated Universal Time (UTC) time zone. Use the AvailableSince
field as part of your catch-up query strategy.

`AvailableSince must be later than` `StartTime` and `EndTime, if`
specified. AvailableSince must be earlier than now. A query must include
```
  StartTime,AvailableSince, or both.

```
For example, to schedule a catch-up query on `2021-04-03T18:00:00Z`
for this date range:

**•** `StartTime=2021-03-29T00:00:00Z`

**•** `EndTime=2021-03-30T00:00:00Z`

Valid `AvailableSince` values range from `2021-03-30T00:00:00Z`
```
  to 2021-04-03T18:00:00Z.

```
For more information on `AvailableSince` and catch-up queries, read
[AppExchange App Analytics Best Practices.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_best_practices.htm)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The type of usage data being requested. Valid values include:

**•** `PackageUsageLog`

**•** `PackageUsageSummary`

**•** `SubscriberSnapshot`


-----

```
DownloadExpirationTime
DownloadSize
DownloadUrl
EndTime

```

Note: In Summer ’20, we changed the enum names from
`CustomObjectUsageSummary` and CustomObjectUsageLog
to `PackageUsageSummary` and `PackageUsageLog.`

If you wrote integrations using `CustomObjectUsageSummary` or
```
    CustomObjectUsageLog, they continue to work only with v47 and

```
earlier. After you upgrade to v48, you must update the DataType to
`PackageUsageSummary` and `PackageUsageLog.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The time when the download URL is no longer valid. The expiration time is 60
minutes after the query is completed.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the AppExchange App Analytics results file available for download,
in bytes.

**Type**
textarea

**Properties**
Nillable

**Description**

URL that the user can download data from. Populated after the request is
completed. This URL expires and is removed after the expiration time is reached.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Enter end time in format yyyy-MM-ddTHH:mm:ss.

Example:

2019-04-15T12:00:00


-----

```
ErrorMessage
FileCompression
FileType

```

For Package Usage Summaries, we recommend that StartTime corresponds to
midnight UTC at beginning of the desired month and EndTime corresponds to
midnight UTC at the beginning of the following month.

For example, to retrieve the Package Usage Summary for December 2024 specify:

**•** `StartTime=2024-12-01T00:00:00Z`

**•** `EndTime=2025-01-01T00:00:00Z`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Stores error message text that results from this query.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The file compression format of your requested results file. FileCompression
and `FileType` must align. If `FileType` is csv, `FileCompression`
defaults to `none` and can be `none` or `gzip. If` `FileType` is `parquet,`
`FileCompression` is snappy by default and can be snappy, gzip, or
```
  none.

```
Valid values include:

**•** `gzip`

**•** `snappy`

**•** `none`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The data format of your requested results file. The default is `csv.`
`FileCompression` and `FileType` must align. If `FileType` is csv,
`FileCompression defaults to` `none` and can be `none` or `gzip. If`
`FileType` is parquet, FileCompression is snappy by default and
can be `snappy,` `gzip, or` `none.`

Valid values include:


-----

```
LastReferencedDate
LastViewedDate
Name
OrganizationIds
PackageIds

```


**•** `csv`

**•** `parquet`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced (LastReferencedDate) and not
viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The auto-generated name of the App Analytics query request.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

Optional. Enter up to 16 comma-separated org IDs without spaces between IDs.
Or enter up to 15 comma-separated org IDs with spaces between the IDs.

To request data for all the orgs the package is installed in, leave the field blank.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
QuerySubmittedTime
RequestState
StartTime

```

**Description**

Optional. Enter up to 16 comma-separated package IDs without spaces between
IDs. Or enter up to 15 comma-separated package IDs with spaces between the
IDs. Use the subscriber package ID that begins with 033. To retrieve a list of your
second-generation managed package IDs, run `sf package list`
`--verbose` in Salesforce CLI.

To request data on all packages registered to this License Management App,
leave the field blank.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time that the App Analytics query request was received for
processing, in Coordinated Universal Time (UTC). `QuerySubmittedTime`
is read only.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Status of the query request. Valid values are:

**•** `New`

**•** `Pending`

**•** `Complete`

**•** `Expired`

**•** `Failed`

**•** `NoData`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Enter start time in format yyyy-MM-ddTHH:mm:ss. All App Analytics query requests
must include `StartTime or` `AvailableSince or both.`

Example:

2019-04-14T12:00:00


-----

For Package Usage Summaries, we recommend that StartTime corresponds to
midnight UTC at beginning of the desired month and EndTime corresponds to
midnight UTC at the beginning of the following month.

For example, to retrieve the Package Usage Summary for December 2024 specify:

**•** `StartTime=2024-12-01T00:00:00Z`

**•** `EndTime=2025-01-01T00:00:00Z`

##### Usage

To request usage data, log in to the License Management Org (LMO) that your package is registered to, and initiate the API request from
the LMO. In a 24-hour period, you can download a maximum 20 GB of AppExchange App Analytics data.

[See Download Package Usage Logs, Package Usage Summaries, and Subscriber Snapshots in the Second Generation Managed Packaging](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_download_mp_logs.htm)
_Developer Guide._

If requests to view package usage log or subscriber snapshot data are inactive for 90 days, we reserve the right to stop collecting this
[data. To resume data collection, log a support case in the Salesforce Partner Community. For product, specify Partner Programs &](https://partners.salesforce.com)
**Benefits. For topic, specify ISV Technology Request.**
