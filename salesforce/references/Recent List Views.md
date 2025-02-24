### Recent List Views

```
Returns the list of recently used list views for the given sObject type. This resource is available in REST API version 32.0 and later.

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/listviews/recent

```
**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None


-----

#### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/listviews/recent
   -H "Authorization: Bearer token"

```
**Example Response Body**
```
  {
   "done" : true,
   "listviews" : [ {
    "describeUrl" :
  "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcCNMA0/describe",
    "developerName" : "MyAccounts",
    "id" : "00BD0000005WcCNMA0",
    "label" : "My Accounts",
    "resultsUrl" :
  "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcCNMA0/results",
    "soqlCompatible" : true,
    "url" : "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcCNMA0"
   }, {
    "describeUrl" :
  "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcBeMAK/describe",
    "developerName" : "NewThisWeek",
    "id" : "00BD0000005WcBeMAK",
    "label" : "New This Week",
    "resultsUrl" :
  "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcBeMAK/results",
    "soqlCompatible" : true,
    "url" : "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcBeMAK"
   }, {
    "describeUrl" :
  "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcCFMA0/describe",
    "developerName" : "AllAccounts",
    "id" : "00BD0000005WcCFMA0",
    "label" : "All Accounts",
    "resultsUrl" :
  "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcCFMA0/results",
    "soqlCompatible" : true,
    "url" : "/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcCFMA0"
   } ],
   "nextRecordsUrl" : null,
   "size" : 3,
   "sobjectType" : "Account"
  }
