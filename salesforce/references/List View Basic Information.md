### List View Basic Information

```
Returns basic information for a specific list view, including the label, API name, and ID. This resource is available in REST API version 32.0
and later.

**URI**
```
  /services/data/vXX.X/sobjects/sObject/listviews/listViewID

```
**Formats**
JSON, XML

**HTTP Methods**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None

#### Example

**Example Request**


-----

**Example Response Body**
```
  {
   "describeUrl" :
  "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcBeMAK/describe",
   "developerName" : "NewThisWeek",
   "id" : "00BD0000005WcBeMAK",
   "label" : "New This Week",
   "resultsUrl" :
  "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcBeMAK/results",
   "soqlCompatible" : true,
   "url" : "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcBeMAK"
  }
