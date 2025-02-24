### sObject Collections

```
Executes actions on multiple records in one request. Use sObject Collections to reduce the number of round-trips between the client
and server. The response bodies and HTTP statuses of the requests are returned in a single response body. The entire request counts as
a single call toward your API limits. This resource is available in API version 42.0 and later.

The parameters, request body, and response body of an sObject Collections request depend on the HTTP method. For details, see the
specific operation.

#### Create Records Using sObject Collections

Use a POST request with sObject Collections to add up to 200 records, returning a list of SaveResult objects. You can choose whether to
roll back the entire request when an error occurs.

**•** The list can contain up to 200 objects.

**•** The list can contain objects of different types, including custom objects.

**•** Each object must contain an attributes map. The map must contain a value for `type.`

Note: Using sObject Collections to insert blob data requires more values in the attributes map. For more information, see
Using sObject Collections to Insert a Collection of Blob Records.

**•** Objects are created in the order they’re listed. The SaveResult objects are returned in the order in which the create requests were
specified.


-----

**•** If the request body includes objects of more than one type, they are processed as chunks. For example, if the incoming objects are
```
  {account1, account2, contact1, account3}, the request is processed in three chunks: {{account1,

```
`account2}, {contact1}, {account3}}.` A single request can process up to 10 chunks.

**•** You can’t create records for multiple object types in one call when one of the types is related to a feature in the Salesforce Setup
area.

If the request isn’t well formed, the API returns a `400 Bad Request` HTTP Status. Fix the syntax of the request and try again. If the
request is well formed, the API returns a `200 OK HTTP Status. If an item was processed successfully, the` `success` flag shows for
that item. Error information is returned in the `errors` array.

##### Syntax

**URI**
```
  /services/data/vXX.X/composite/sobjects

```
**Formats**
JSON, XML

**HTTP Method**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

```
allOrNone

```

Optional. Indicates whether to roll back the entire request when the creation of any
object fails (true) or to continue with the independent creation of other objects in
the request. The default is `false.`

Note: If the sObject Collections request is embedded in a Composite request,
the Composite request’s `allOrNone` parameter can also affect the results.
See allOrNone Parameters in Composite and Collections Requests.


`records` Required. A list of sObjects. In a POST request using sObject Collections, set the type
attribute for each object, but don’t set the `id` field for any object.

##### Example

**Example Request**
```
  curl -X POST
  https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/sobjects/ -H
  "Authorization: Bearer token" -H "Content-Type: application/json" -d
  "@exampleRequestBody.json"

```
**Example Request Body**


-----

**Example Response Body**
```
  HTTP/1.1 200 OK
  [
    {
      "id" : "001RM000003oLnnYAE",
      "success" : true,
      "errors" : [ ]
    },
    {
      "id" : "003RM0000068xV6YAI",
      "success" : true,
      "errors" : [ ]
    }
  ]

```
**Example Response Body (Some Items Failed and** `allOrNone` **is** `false)`
```
  HTTP/1.1 200 OK
  [
    {
      "success" : false,
      "errors" : [
       {
         "statusCode" : "DUPLICATES_DETECTED",
         "message" : "Use one of these records?",
         "fields" : [ ]
       }
      ]
    },
    {
      "id" : "003RM0000068xVCYAY",
      "success" : true,
      "errors" : [ ]
    }
  ]

```
**Example Response Body (Some Items Failed and** `allOrNone` **is** `true)`


-----

#### Get Records Using sObject Collections

Use a GET request with sObject Collections to get one or more records of the same object type. A list of sObjects that represents the
individual records of the specified type is returned. The number of sObjects returned matches the number of IDs passed in the request.

You can specify approximately 800 IDs before the URL length causes the HTTP 414 error `URI too long.`

Note: The sObject Blob Retrieve on page 159 resource isn’t compatible with Composite API requests, because it returns binary
data instead of data in JSON or XML formats. Instead, make individual sObject Blob Retrieve requests to retrieve blob data.

**•** If you specify an invalid field name or a field name that you don’t have permission to read, HTTP 400 Bad Request is returned.

**•** If you don’t have access to an object, or if a passed ID is invalid, the array returns null for that object.

##### Syntax

**URI**
```
  /services/data/vXX.X/composite/sobjects/sObject

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

**Parameter** **Description**

`ids` Required. A list of one or more IDs of the objects to return. All IDs must belong to the
same object type.


-----

`fields` Required. A list of fields to include in the response. The field names you specify must
be valid, and you must have read-level permissions to each field.

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/sobjects/Account?ids=001xx000003DGb1AAG,001xx000003DGb0AAG,001xx000003DGb9AAG&fields=id,name
   -H "Authorization: Bearer token"

```
**Example Response Body**
```
  [
    {
      "attributes" : {
       "type" : "Account",
       "url" : "/services/data/v62.0/sobjects/Account/001xx000003DGb1AAG"
      },
      "Id" : "001xx000003DGb1AAG",
      "Name" : "Acme"
    },
    {
      "attributes" : {
       "type" : "Account",
       "url" : "/services/data/v62.0/sobjects/Account/001xx000003DGb0AAG"
      },
      "Id" : "001xx000003DGb0AAG",
      "Name" : "Global Media"
    },
    null
  ]

#### Get Records With a Request Body Using sObject Collections

```
Use a POST request with sObject Collections to get one or more records of the same object type. A list of sObjects that represents the
individual records of the specified type is returned. The number of sObjects returned matches the number of IDs passed in the request.

The request retrieves up to 2,000 records of the same object type

**•** If you specify an invalid field name or a field name that you don’t have permission to read, HTTP 400 Bad Request is returned.

**•** If you don’t have access to an object, or if a passed ID is invalid, the array returns null for that object.

Note: The sObject Blob Retrieve on page 159 resource isn’t compatible with Composite API requests, because it returns binary
data instead of data in JSON or XML formats. Instead, make individual sObject Blob Retrieve requests to retrieve blob data.

##### Syntax

**URI**
```
  /services/data/vXX.X/composite/sobjects/sObject

```

-----

**Formats**
JSON, XML

**HTTP Method**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Request Body**
```
  {
    "ids" : ["recordIds"],
    "fields" : ["fieldName"]
  }

```
**Parameters**

**Parameter** **Description**

`recordIds` Required. A list of one or more IDs of the objects to return. All IDs must belong to the
same object type.

`fieldNames` Required. A list of fields to include in the response. The field names you specify must
be valid, and you must have read-level permissions to each field.

##### Example

**Example Request**
```
  curl -X POST
  https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/sobjects/Account
  -H "Authorization: Bearer token" -H "Content-Type: application/json" -d
  "@exampleRequestBody.json"

```
**Example Request Body**
```
  {
    "ids" : ["001xx000003DGb1AAG", "001xx000003DGb0AAG", "001xx000003DGb9AAG"],
    "fields" : ["id", "name"]
  }

```
**Example Response Body**


-----

#### Update Records Using sObject Collections

Use a PATCH request with sObject Collections to update up to 200 records, returning a list of SaveResult objects. You can choose whether
to roll back the entire request when an error occurs.

**•** The list can contain up to 200 objects.

**•** The list can contain objects of different types, including custom objects.

**•** Each object must contain an attributes map. The map must contain a value for `type.`

Note: Using sObject Collections to update blob data requires more values in the attributes map. For more information, see
Using sObject Collections to Insert a Collection of Blob Records.

**•** Each object must contain an `id` field with a valid ID value.

**•** Objects are updated in the order they’re listed. The SaveResult objects are returned in the order in which the update requests were
specified.

**•** If the request body includes objects of more than one type, they are processed as chunks. For example, if the incoming objects are
```
  {account1, account2, contact1, account3}, the request is processed in three chunks: {{account1,

```
`account2}, {contact1}, {account3}}.` A single request can process up to 10 chunks.

**•** You can’t update records for multiple object types in one call when one of those types is related to a feature in the Salesforce Setup
area.

If the request isn’t well formed, the API returns a `400 Bad Request` HTTP Status. Fix the syntax of the request and try again. If the
request is well formed, the API returns a `200 OK HTTP Status. If an item was processed successfully, the` `success` flag shows for
that item. Error information is returned in the `errors` array.

##### Syntax

**URI**
```
  /services/data/vXX.X/composite/sobjects/

```
**Formats**
JSON, XML

**HTTP Method**
PATCH

**Authentication**
```
  Authorization: Bearer token

```

-----

**Parameters**

**Parameter**
```
  allOrNone

```

Optional. Indicates whether to roll back the entire request when the update of any
object fails (true) or to continue with the independent update of other objects in
the request. The default is `false.`

Note: If the sObject Collections request is embedded in a Composite request,
the Composite request’s `allOrNone` parameter can also affect the results.
See allOrNone Parameters in Composite and Collections Requests.


`records` Required. A list of records. Set the `id` and `type` attribute for each record.

##### Example

**Example Request**
```
  curl -X PATCH
  https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/sobjects/ -H
  "Authorization: Bearer token" -H "Content-Type: application/json" -d
  "@exampleRequestBody.json"

```
**Example Request Body**
```
  {
    "allOrNone" : false,
    "records" : [{
      "attributes" : {"type" : "Account"},
      "id" : "001xx000003DGb2AAG",
      "NumberOfEmployees" : 27000
    },{
      "attributes" : {"type" : "Contact"},
      "id" : "003xx000004TmiQAAS",
      "Title" : "Lead Engineer"
    }]
  }

```
**Example Response Body**


-----

**Example Response Body (Some Items Failed and** `allOrNone` **is** `false)`
```
  HTTP/1.1 200 OK
  [
    {
      "id" : "001RM000003oCprYAE",
      "success" : true,
      "errors" : [ ]
    },
    {
      "success" : false,
      "errors" : [
       {
         "statusCode" : "MALFORMED_ID",
         "message" : "Contact ID: id value of incorrect type: 001xx000003DGb2999",
         "fields" : [
           "Id"
         ]
       }
      ]
    }
  ]

```
**Example Response Body (Some Items Failed and** `allOrNone` **is** `true)`


-----

#### Upsert Records Using sObject Collections

Use a PATCH request with sObject Collections to either create or update (upsert) up to 200 records based on an external ID field. This
method returns a list of UpsertResult objects. You can choose whether to roll back the entire request when an error occurs. This request
is available in API version 46 and later.

**•** The list can contain up to 200 objects.

**•** The list can contain objects only of the type indicated in the request URI.

**•** Each object in the request body must contain an attributes map. The map must contain a value for `type.`

Note: Using sObject Collections to insert blob data requires more values in the attributes map. For more information, see
Using sObject Collections to Insert a Collection of Blob Records.

**•** Objects are created or updated in the order they’re listed in the request body. The UpsertResult objects are returned in the same
order.

**•** Only external ids are supported. Don’t use record ids.

If the request isn’t well formed, the API returns a `400 Bad Request` HTTP Status. Fix the syntax of the request and try again. If the
request is well formed, the API returns a `200 OK HTTP Status. If an item was processed successfully, the` `success` flag shows for
that item. Error information is returned in the `errors` array.

##### Syntax

**URI**
```
  /services/data/vXX.X/composite/sobjects/SobjectName/ExternalIdFieldName

```
**Formats**
JSON, XML

**HTTP Method**
PATCH

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

```
allOrNone
records

```

Optional. Indicates whether to roll back the entire request when the creation of any
object fails (true) or to continue with the independent creation of other objects in
the request. The default is `false.`

Note: If the sObject Collections request is embedded in a Composite request,
the Composite request’s `allOrNone` parameter can also affect the results.
See allOrNone Parameters in Composite and Collections Requests.

Required. A list of sObjects. In a PATCH request using sObject Collections, set the type
attribute for each object. Don’t set the id field for any object. Instead, use the external
ID field specified in the request URI.


-----

##### Example

**Example Request**
```
  curl -X PATCH
  https://MyDomainName
   -H "Authorization: Bearer token
  "@exampleRequestBody.json"

```
**Example Request Body**
```
  {
    "allOrNone" : false,
    "records" : [{
       "attributes" : {"type" : "Account"},
       "Name" : "Company One",
       "MyExtId__c" : "AAA"
    }, {
       "attributes" : {"type" : "Account"},
       "Name" : "Company Two",
       "MyExtId__c" : "BBB"
    }]
  }

```
**Example Response Body**
```
  HTTP/1.1 200 OK
  [
    {
       "id": "001xx0000004GxDAAU",
       "success": true,
       "errors": [],
       "created": true
    },
    {
       "id": "001xx0000004GxEAAU",
       "success": true,
       "errors": [],
       "created": false
    }
  ]

```
**Example Response Body (Some Items Failed and** `allOrNone` **is** `false)`


-----

**Example Response Body (Some Items Failed and** `allOrNone` **is** `true)`
```
  HTTP/1.1 200 OK
  [
    {
      "id" : "001xx0000004GxDAAU",
      "success" : false,
      "errors" : [
       {
         "statusCode" : "ALL_OR_NONE_OPERATION_ROLLED_BACK",
         "message" : "Record rolled back because not all records were valid and the
   request was using AllOrNone header",
         "fields" : [ ]
       }
      ]
    },
    {
      "success" : false,
      "errors" : [
       {
         "statusCode" : "MALFORMED_ID",
         "message" : "Contact ID: id value of incorrect type: 001xx0000004GxEAAU",
         "fields" : [
           "Id"
         ]
       }
      ]
    }
  ]

```
SEE ALSO:

sObject Rows by External ID

#### Delete Records Using sObject Collections

Use a DELETE request with sObject Collections to delete up to 200 records, returning a list of DeleteResult objects. You can choose to
roll back the entire request when an error occurs.

**•** The DeleteResult objects are returned in the order in which the IDs of the deleted objects were specified.

**•** You can't delete records for multiple object types in one call when one of those types is related to a feature in the Salesforce Setup
area.


-----

If the request isn’t well formed, the API returns a `400 Bad Request` HTTP Status. Fix the syntax of the request and try again. If the
request is well formed, the API returns a `200 OK HTTP Status. If an item was processed successfully, the` `success` flag shows for
that item. Error information is returned in the `errors` array.

##### Syntax

**URI**
```
  /services/data/vXX.X/composite/sobjects?ids=recordId,recordId

```
**Formats**
JSON, XML

**HTTP Method**
DELETE

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

```
allOrNone

```

Optional. Indicates whether to roll back the entire request when the deletion of any
object fails (true) or to continue with the independent deletion of other objects in
the request. The default is `false.`

Note: If the sObject Collections request is embedded in a Composite request,
the Composite request’s `allOrNone` parameter can also affect the results.
See allOrNone Parameters in Composite and Collections Requests.


`ids` Required. A list of up to 200 IDs of objects to be deleted. The IDs can belong to different
object types, including custom objects.

##### Example

**Example Request**
```
  curl -X DELETE
  https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/sobjects?ids=001xx000003DGb2AAG,003xx000004TmiQAAS&allOrNone=false
   -H "Authorization: Bearer token"

```
**Example Response Body**


-----

**Example Response Body (Some Items Failed and** `allOrNone` **is** `false)`
```
  HTTP/1.1 200 OK
  [
    {
      "id" : "001RM000003oLrfYAE",
      "success" : true,
      "errors" : [ ]
    },
    {
      "success" : false,
      "errors" : [
       {
         "statusCode" : "MALFORMED_ID",
         "message" : "malformed id 001RM000003oLrB000",
         "fields" : [ ]
       }
      ]
    }
  ]

```
**Example Response Body (Some Items Failed and** `allOrNone` **is** `true)`


-----

