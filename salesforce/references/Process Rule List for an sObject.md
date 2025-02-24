### Process Rule List for an sObject

```
Accesses a list of all active workflow rules for an sObject. Use the GET method to retrieve records or fields. Use the HEAD method to
retrieve information in HTTP headers.

Cross-object workflow rules can’t be invoked using REST API.

To access all workflow rules, use the Process Rules resource. To access a specific workflow rule that is associated with a specific sObject,
use the Process Rule for an sObject resource.

IN THIS SECTION:

Get Process Rules for an sObject
Gets all active workflow rules for an sObject. This resource is available in REST API version 30.0 and later.

Return HTTP Headers for Process Rules of an sObject
Returns only the headers that are returned by sending a GET request to the process rules resource for all process rules of an sObject.
This gives you a chance to see returned header values of the GET request before retrieving the content. This resource is available in
REST API version 30.0 and later.

#### Get Process Rules for an sObject

Gets all active workflow rules for an sObject. This resource is available in REST API version 30.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/process/rules/sObject

```
**Formats**
JSON, XML

**HTTP methods**
GET


-----

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required

**Request body**
None required

##### Example

**Example Request**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/Account
  -H "Authorization: Bearer token"

```
**Example Response Body**
```
  {
   "rules" : {
    "Account" : [ {
      "actions" : [ {
       "id" : "01VD0000000D2w7",
       "name" : "ApprovalProcessTask",
       "type" : "Task"
      } ],
      "description" : null,
      "id" : "01QD0000000APli",
      "name" : "My Rule",
      "namespacePrefix" : null,
      "object" : "Account"
    } ]
   }
  }

#### Return HTTP Headers for Process Rules of an sObject

```
Returns only the headers that are returned by sending a GET request to the process rules resource for all process rules of an sObject. This
gives you a chance to see returned header values of the GET request before retrieving the content. This resource is available in REST API
version 30.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/process/rules/sObject

```
**Formats**
JSON, XML

**HTTP methods**
HEAD


-----

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required

**Request body**
None required

##### Example

**Example Request**
```
  curl -X HEAD --head
  https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/Account/ -H
  "Authorization: Bearer token"

```
**Example Response Body**
```
  HTTP/1.1 200 OK
  Date: Mon, 21 Nov 2022 22:56:26 GMT
