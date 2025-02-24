### List Views for an Object

Returns the list of list views for the specified sObject, including the ID and other basic information about each list view. This resource is
available in REST API version 32.0 and later.

**URI**
```
  /services/data/vXX.X/sobjects/sObject/listviews

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
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/listviews
  -H "Authorization: Bearer token"

```
**Example Response Body**


-----

-----
