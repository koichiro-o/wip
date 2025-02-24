### Lightning Exit by Page Metrics

```
Returns frequency metrics about the standard pages within which users switched from Lightning Experience to Salesforce Classic. This
resource is available in REST API version 44.0 and later.

Use this object with the following APIs:

**•** Platform

**•** Metadata API

**•** Tooling API

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/LightningExitByPageMetrics

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
Authorization: Bearer token

```
**Request parameters**

**Parameter** **Description**

`MetricsDate` The date the data was recorded.

`PageName` Current Page from which User Switched from Lightning to Aloha


-----

`RecordCount` The number of records per user and page.

`UserId` The user ID.

#### Example
```
SELECT PageName PageName, SUM(RecordCount) Total FROM LightningExitByPageMetrics WHERE
MetricsDate = Last_N_DAYS:7 GROUP BY PageName ORDER BY SUM(RecordCount) Desc Limit 10
