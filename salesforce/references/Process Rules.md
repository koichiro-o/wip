### Process Rules

```
Accesses a list of all active workflow rules. Use the GET method to retrieve records or fields. Use the HEAD method to retrieve information
in HTTP headers. Use the POST method to trigger all active workflow rules.

To access all workflow rules that are associated with a specific sObject, use the Process Rule List for an sObject resource. To access a
specific workflow rule that is associated with a specific sObject, use the Process Rule for an sObject resource.

Cross-object workflow rules can’t be invoked using REST API.

IN THIS SECTION:

Get Process Rules
Gets all active workflow rules. This resource is available in REST API version 30.0 and later.

Trigger Process Rules
Triggers all active workflow rules. All rules associated with the specified ID are evaluated, regardless of the evaluation criteria. All IDs
must be for records on the same object. This resource is available in REST API version 30.0 and later.


-----

Return HTTP Headers for Process Rules
Returns only the headers that are returned by sending a GET request to the process rules resource. This gives you a chance to see
returned header values of the GET request before retrieving the content. This resource is available in REST API version 30.0 and later.

#### Get Process Rules

Gets all active workflow rules. This resource is available in REST API version 30.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/process/rules/

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
None required

##### Example

See Get a List of Process Rules.

#### Trigger Process Rules

Triggers all active workflow rules. All rules associated with the specified ID are evaluated, regardless of the evaluation criteria. All IDs
must be for records on the same object. This resource is available in REST API version 30.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/process/rules/

```
**Formats**
JSON, XML

**HTTP methods**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required

**Request body**
The request body contains an array of context IDs:


-----

`contextIds` ID[] An array of IDs of the items that are being acted upon.

##### Example

See Trigger Process Rules.

#### Return HTTP Headers for Process Rules

Returns only the headers that are returned by sending a GET request to the process rules resource. This gives you a chance to see returned
header values of the GET request before retrieving the content. This resource is available in REST API version 30.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/process/rules/

```
**Formats**
JSON, XML

**HTTP methods**
HEAD

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required

##### Example

**Example Request**
```
  curl -X HEAD --head
  https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/ -H
  "Authorization: Bearer token"

```
**Example Response Body**
```
  HTTP/1.1 200 OK
  Date: Mon, 21 Nov 2022 22:56:26 GMT
