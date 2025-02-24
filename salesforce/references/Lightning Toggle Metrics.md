### Lightning Toggle Metrics

Returns details about users who switched between Salesforce Classic and Lightning Experience. This resource is available in REST API
version 44.0 and later.

Use this object with the following APIs:

**•** Platform

**•** Metadata API

**•** Tooling API

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/LightningToggleMetrics

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer tokens

```
**Request parameters**

**Parameter** **Description**

`UserId` The user ID.

`RecordCount` The count of records returned.

|Property|Type|Description|
|---|---|---|
|field|String|Object and field name formatted with a period separating. For example: Account.Name.|
|format|String|The type of date field, such as the date only or date and time. Only date related types are specified; otherwise, null.|
|label|String|Name as it appears to users|
|name|String|API name|


-----

`MetricsDate` The date the switch was recorded.

`Action` Did the user switch to Salesforce Classic or Lightning Experience.

#### Example
```
SELECT sum(RecordCount) Total FROM LightningToggleMetrics WHERE MetricsDate = LAST_MONTH
AND Action = 'switchToAloha'
