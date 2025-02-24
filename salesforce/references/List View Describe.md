### List View Describe

```
Returns detailed information about a list view, including the ID, the columns, and the SOQL query.

This resource is available in REST API version 32.0 and later.

**URI**
```
  /services/data/vXX.X/sobjects/sObject/listviews/queryLocator/describe

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

#### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/listviews/00BD0000005WcBeMAK/describe
   -H "Authorization: Bearer token"

```
**Example Response Body**


-----

-----

-----
