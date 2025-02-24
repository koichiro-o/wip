### Lightning Usage by Page

```
Represents standard pages users viewed most frequently in Lightning Experience. This resource is available in REST API version 44.0 and
later.

Use this object with the following APIs:

**•** Platform

**•** Metadata API

**•** Tooling API

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/LightningUsageByPageMetrics

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
Authorization: Bearer token

```
**Parameter** **Description**

`EptBin3To5` Number of times that a page loaded between 3-5 seconds.

`EptBin5To8` Number of times that a page loaded between 5-8 seconds.

`EptBin8To10` Number of times that a page loaded between 8-10 seconds.

`EptBinOver10` Number of times that a page loaded over 10 seconds.

`EptBinUnder3` Number of times that a page loaded under 3 seconds.

`PageName` The name of the page.

`MetricsDate` The date the metric was recorded.


-----

`RecordCountEPT` Number of records for a page/user where the valid EPT was recorded.

`SumEPT` Sum of the EPT values for a page/user.

`TotalCount` Total records for a page/user.

`UserId` User ID.

#### Example
```
SELECT TotalCount FROM LightningUsageByPageMetrics ORDER BY PageName ASC NULLS FIRST LIMIT
 10
