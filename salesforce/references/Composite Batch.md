### Composite Batch


500

(For example, there can be one graph with 500 nodes, or 50 graphs
with 10 nodes each.)


Executes up to 25 subrequests in a single request. The response bodies and HTTP statuses of the subrequests in the batch are returned
in a single response body. Each subrequest counts against rate limits.

The requests in a batch are called subrequests. All subrequests are executed in the context of the same user. Subrequests are independent,
and you can’t pass information between them. Subrequests execute serially in their order in the request body. When a subrequest
executes successfully, it commits its data. Commits are reflected in the output of later subrequests. If a subrequest fails, commits made
by previous subrequests aren’t rolled back. If a batch request doesn’t complete within 10 minutes, the batch times out and the remaining
subrequests aren’t executed.

Batching for the following resources and resource groups is available in API version 34.0 and later.

**•** Limits—/services/data/vXX.X/limits

**•** sObject resources (except sObject Blob Retrieve and sObject Rich Text Image Retrieve)—/services/data/vXX.X/sobjects/

**•** Query—/services/data/vXX.X/query/?q=soql

**•** QueryAll—/services/data/vXX.X/queryAll/?q=soql

**•** Search—/services/data/vXX.X/search/?q=sosl

**•** Connect resources—/services/data/vXX.X/connect/

**•** Chatter resources—/services/data/vXX.X/chatter/

Batching for the following resources and resource groups is available in API version 35.0 and later.

**•** Actions—vXX.X/actions

The API version of the resource accessed in each subrequest must be no earlier than 34.0 and no later than the Batch version in the
top-level request. For example, if you post a Batch request to /services/data/v35.0/composite/batch, you can include
subrequests that access version 34.0 or 35.0 resources. But if you post a Batch request to
```
/services/data/v34.0/composite/batch, you can only include subrequests that access version 34.0 resources.

#### Syntax

```
**URI**
```
  /services/data/vXX.X/composite/batch

```
**Formats**
JSON, XML


-----

**HTTP method**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

**Request body**

Batch Request Body on page 389

**Response body**

Batch Response Body on page 391

#### Example

For an example of using the Composite Batch resource, see Update a Record and Get Its Field Values in a Single Request on page 102.

#### Batch Request Body

Describes a collection of subrequests to execute with the Composite Batch resource.

##### Batch Collection Input

The request body contains a `batchRequests` collection that includes subrequests to execute.

**Properties**

**Name** **Type** **Description** **Required or**
**Optional**

`batchRequests` Subrequest[] Collection of subrequests to execute. Required


`haltOnError` Boolean


Controls whether a batch continues to process after a subrequest Optional
fails. The default is `false.`

If the value is `false` and a subrequest in the batch doesn’t
complete, Salesforce attempts to execute the subsequent
subrequests in the batch.

If the value is `true` and a subrequest in the batch doesn’t
complete due to an HTTP response in the 400 or 500 range,
Salesforce halts execution. It returns an HTTP 412 status code
and a `BATCH_PROCESSING_HALTED` error message for
each subsequent subrequest. The top-level request to
`/composite/batch` returns HTTP 200, and the
`hasErrors` property in the response is set to `true.`

This setting is only applied during subrequest processing, and
not during initial request deserialization. If an error is detected
during deserialization, such as a syntax error in the Subrequest
request data, Salesforce returns an HTTP 400 `Bad Request`
error without processing any subrequests, regardless of the value


-----

of `haltOnError. An example where this could occur is if a`
subrequest has an invalid `method` or `url` field.

**Root XML Tag**
```
  <batch>

```
**JSON example**
```
  {
  "batchRequests" : [
    {
    "method" : "PATCH",
    "url" : "v62.0/sobjects/account/001D000000K0fXOIAZ",
    "richInput" : {"Name" : "NewName"}
    },{
    "method" : "GET",
    "url" : "v62.0/sobjects/account/001D000000K0fXOIAZ?fields=Name,BillingPostalCode"
    }]
  }

##### Subrequest

```
Contains the resource, method, and accompanying information for the subrequest.

**Properties**


`binaryPartName` String

`binaryPartNameAlias` String


The name of the binary part in the multipart request. Optional

When multiple binary parts are uploaded in one batch request,
this value is used to map a request to its binary part. To prevent

name collisions, use a unique value for each
`binaryPartName` property in a batch request.

If this value exists, a `binaryPartNameAlias` value must
also exist.

The `name` parameter in the Content-Disposition header of the Optional
binary body part. Different resources expect different values. See
Insert or Update Blob Data.

If this value exists, a binaryPartName value must also exist.


`method` String The method to use with the requested resource. For a list of valid Required
methods, refer to the documentation for the requested resource.

```
richInput

```

The input body for the request. Optional

The type depends on the request specified in the url property.


-----

`url` String The resource to request. Required

**•** The URL can include any query string parameters that the
subrequest supports. The query string must be URL-encoded.

**•** You can use parameters to filter response bodies.

**•** You cannot apply headers at the subrequest level.

**Root XML Tag**
```
  <request>

```
**JSON example**
```
  {
    "method" : "GET",
    "url" : "v62.0/sobjects/account/001D000000K0fXOIAZ?fields=Name,BillingPostalCode"
  }

#### Batch Response Body

```
Describes the result of a Composite Batch request.

##### Batch Results

**Properties**

**Name** **Type** **Description**

`hasErrors` Boolean `true` if at least one of the results in the result set is an HTTP status code
in the 400 or 500 range; `false` otherwise.

`results` Subrequest Result[] Collection of subrequest results.

**JSON example**


-----

##### Subrequest Result

**Properties**

**Name**
```
  result

```

The type depends on the The response body of this subrequest.
response type of the
subrequest.

Important: If the
result is an error,
the type is a
collection
containing the
error message and
error code.


`statusCode` Integer An HTTP status code indicating the status of this subrequest.

**JSON example**
```
  {
    "attributes" : {
      "type" : "Account",
      "url" : "/services/data/v62.0/sobjects/Account/001D000000K0fXOIAZ"
    },
    "Name" : "NewName",
    "BillingPostalCode" : "94015",
    "Id" : "001D000000K0fXOIAZ"
  }
