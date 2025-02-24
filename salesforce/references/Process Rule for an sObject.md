### Process Rule for an sObject

```
Accesses an active workflow rule for an sObject. Use the GET method to retrieve the record or fields. Use the HEAD method to retrieve
information in HTTP headers. Use the POST method to trigger the workflow rule.

Cross-object workflow rules can’t be invoked using REST API.

To access all workflow rules, use the Process Rules resource. To access a specific workflow rule that is associated with a specific sObject,
use the Process Rule List for an sObject resource.


-----

IN THIS SECTION:

Get a Process Rule for an sObject
Gets the fields of a specific workflow rule for a specific sObject.

Trigger a Process Rule for an sObject
Triggers an active workflow rule regardless of the evaluation criteria.

Return HTTP Headers for a Process Rule of an sObject
Returns only the headers that are returned by sending a GET request to the process rules resource for a specific process rule of an
sObject. This gives you a chance to see returned header values of the GET request before retrieving the content.

#### Get a Process Rule for an sObject

Gets the fields of a specific workflow rule for a specific sObject.

Cross-object workflow rules can’t be invoked using REST API.

**URI**
```
  /services/data/vXX.X/process/rules/sObjectName/workflowRuleId

```
**Available since release**
30.0

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

**Example usage**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/Account/01QD0000000APli
   -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example JSON response body**


-----

#### Trigger a Process Rule for an sObject

Triggers an active workflow rule regardless of the evaluation criteria.

**URI**
```
  /services/data/vXX.X/process/rules/sObjectName/workflowRuleId

```
**Available since release**
30.0

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
None required

**Example usage**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/Account/01XXX000000XxxXXX
   -H "Authorization: Bearer token"

```
**Example JSON response body**
```
  {
   "errors" : null,
   "success" : true
  }

#### Return HTTP Headers for a Process Rule of an sObject

```
Returns only the headers that are returned by sending a GET request to the process rules resource for a specific process rule of an sObject.
This gives you a chance to see returned header values of the GET request before retrieving the content.

**URI**
```
  /services/data/vXX.X/process/rules/sObjectName/workflowRuleId

```
**Available since release**
30.0

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

**Example usage**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/Account/01XXX000000/
   -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example response body**
```
  HTTP/1.1 200 OK
  Date: Mon, 21 Nov 2022 22:56:26 GMT
