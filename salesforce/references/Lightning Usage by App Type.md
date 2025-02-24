### Lightning Usage by App Type

```
Returns the total number of Lightning Experience and Salesforce Mobile users. This resource is available in REST API version 44.0 and
later.

Use this object with the following APIs:

**•** Platform

**•** Metadata API

**•** Tooling API

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/LightningUsageByAppTypeMetrics

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
```
  AppExperience

```
The app used:

**•** Salesforce Mobile

**•** Lightning Experience

`MetricsDate` The date the data was recorded.

`UserID` The user ID.


-----

#### Example
```
SELECT MetricsDate,user.profile.name,COUNT_DISTINCT(user.id) Total FROM
LightningUsageByAppTypeMetrics WHERE MetricsDate = LAST_N_DAYS:30 AND AppExperience =
'Salesforce Mobile' GROUP BY MetricsDate,user.profile.name
