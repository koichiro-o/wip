### Compact Layouts

```
Returns a list of compact layouts for multiple objects. This resource is available in REST API version 31.0 and later.

This resource returns the primary compact layout for a set of objects. The set of objects is specified using a query parameter. Up to 100
objects can be queried at once.

Note: PersonAccount isn’t supported for bulk queries. If you want to get the primary compact layout for PersonAccount, get it
directly from
```
  /services/data/v62.0/sobjects/Account/describe/compactLayouts/primaryPersonAccount.

#### Syntax

```
**URI**
```
  /services/data/vXX.X/compactLayouts?q=objectList

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

`q` A comma-delimited list of objects. The primary compact layout for each object in this
list will be returned in the response of this resource.

#### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/compactLayouts?q=Account,Contact,CustomObj__c
   -H "Authorization: Bearer token"

```
**Example Response Body**


-----

-----
