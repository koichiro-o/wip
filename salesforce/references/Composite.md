### Composite

```
Executes a series of REST API requests in a single POST request, or retrieves a list of other composite resources with a GET request.


-----

IN THIS SECTION:

Send Multiple Requests Using Composite
Executes a series of REST API requests in a single call. You can use the output of one request as the input to a subsequent request.
The response bodies and HTTP statuses of the requests are returned in a single response body. The entire series of requests counts
as a single call toward your API limits.

Get a List of Composite Resources
Gets a list of URIs for other composite resources.

#### Send Multiple Requests Using Composite

Executes a series of REST API requests in a single call. You can use the output of one request as the input to a subsequent request. The
response bodies and HTTP statuses of the requests are returned in a single response body. The entire series of requests counts as a single
call toward your API limits.

The requests in a composite call are called subrequests. All subrequests are executed in the context of the same user. In a subrequest’s
body, you specify a reference ID that maps to the subrequest’s response. You can then refer to the ID in the url or body fields of later
subrequests by using a JavaScript-like reference notation.

For example, the following composite request body includes two subrequests. The first creates an account and designates the output
as `refAccount. The second creates a contact parented under the new account by referencing` `refAccount` in the subrequest
body.
```
{
"compositeRequest" : [{
  "method" : "POST",
  "url" : "/services/data/v62.0/sobjects/Account",
  "referenceId" : "refAccount",
  "body" : { "Name" : "Sample Account" }
  },{
  "method" : "POST",
  "url" : "/services/data/v62.0/sobjects/Contact",
  "referenceId" : "refContact",
  "body" : {
   "LastName" : "Sample Contact",
   "AccountId" : "@{refAccount.id}"
   }
  }]
}

```
You can specify whether an error in a subrequest causes the whole composite request to roll back or just the subrequests that depend
on it. You can also specify headers for each subrequest.

Composite is supported for the following resources.

**•** All sObject resources (/services/data/vXX.X/sobjects/), including sObject Rows by External ID on page 154 and
excluding sObject Blob Get

**•** The Query resource (/services/data/vXX.X/query/?q=soql)

**•** The QueryAll resource (/services/data/vXX.X/queryAll/?q=soql)

**•** The sObject Collections resource (/services/data/vXX.X/composite/sobjects). Available in API version 43.0 and
later.

Note: You can have up to 25 subrequests in a single call. Up to 5 of these subrequests can be sObject Collections or query
operations, including Query and QueryAll requests.


-----

##### Syntax

**URI**
```
  /services/data/vXX.X/composite

```
**Formats**
JSON

**HTTP method**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

**Request body**

Composite Request Body

**Response body**

Composite Response Body

##### Example

For examples of using the Composite resource, see Execute Dependent Requests in a Single API Call and Update an Account, Create a
Contact, and Link Them with a Junction Object.

IN THIS SECTION:

Composite Subrequest Result
The composite subrequest result describes the result for a subrequest.

##### Composite Request Body

Describes a collection of subrequests to execute with the Composite resource.

###### Composite Collection Input

The request body contains an `allOrNone` flag that specifies how to roll back errors and a `compositeRequest` collection that
includes subrequests to execute.

**Properties**


`allOrNone` Boolean


Optional
Specifies what to do when an error occurs while processing a
subrequest. If the value is `true, the entire composite request`

is rolled back. The top-level request returns HTTP 200 and
includes responses for each subrequest.

If the value is `false, the remaining subrequests that don’t`
depend on the failed subrequest are executed. Dependent
subrequests aren’t executed.


-----

`collateSubrequests` Boolean


In either case, the top-level request returns HTTP 200 and
includes responses for each subrequest.

Note: If the Composite request includes an sObject
Collections request, the sObject Collections request’s
```
  allOrNone parameter can also affect the results. See

```
allOrNone Parameters in Composite and Collections
Requests.

Optional
Controls whether the API collates unrelated subrequests to
bulkify them (true) or not (false).

When subrequests are collated, the processing speed is faster,
but the order of execution is not guaranteed (unless there is an
explicit dependency between the subrequests).

If collation is disabled, then the subrequests are executed in the
order in which they are received.

Subrequests that contain valid HTTP headers are not collated.

In API version 49.0 and later, the default value is true. In version
48.0, the default value is `false.`

Subrequests can be collated if they meet these conditions:

**•** The HTTP methods are the same.

**•** The API versions of the resources are the same.

**•** The parents of the resources are `/sobjects` resources.

**•** No more than five sObjects resources are present across a
grouping of subrequests.

Note: Collation can cause issues if there are implicit but
not explicit dependencies between items. For example,
consider a request that creates

**•** an Account

**•** a Contact related to the Account

**•** a custom object that has a trigger dependent on the
account name.

The Account and the custom object are collated, since
there is no explicit dependency. But the custom object’s
trigger may fail because there is no guarantee that the
Account is created first.

If you have relationships like this where you need to
control the order of execution, set
`collateSubrequests` to `false.`

Available in API version 48.0 and later. (In earlier versions,
subrequests cannot be collated.)


-----

`compositeRequest` Composite Collection of subrequests to execute. Required
Subrequest[]

**JSON example**
```
  {
    "allOrNone" : true,
    "collateSubrequests": true,
    "compositeRequest" : [{
     Composite Subrequest
      },{
     Composite Subrequest
      },{
     Composite Subrequest
    }]
  }

###### Composite Subrequest

```
Contains the resource, method, headers, body, and reference ID for the subrequest.

**Properties**


`body` Varies

`httpHeaders` Map<String,
String>


The input body for the subrequest. Optional

The type depends on the request specified in the url property.
The referenceable types are DateTime, String, Boolean, Byte,
Character, Short, Integer, Long, Double, and Float.

Request headers and their values to include with the subrequest. Optional
You can include any header supported by the requested resource
except for the following three headers.

**•** Accept

**•** Authorization

**•** Content-Type

Subrequests inherit these three header values from the top-level
request. Don’t specify these headers in a subrequest. If you do,
the top-level request fails and returns an HTTP 400 response.

Note: Subrequests that contain valid HTTP headers
cannot be collated, which slows the processing speed of
the request.


`method` String The method to use with the requested resource. Possible values Required
are `POST,` `PUT,` `PATCH, GET, and` `DELETE` (case-sensitive).


-----

For a list of valid methods, refer to the documentation for the
requested resource.

`referenceId` String Reference ID that maps to the subrequest’s response and can Required
be used to reference the response in later subrequests. You can

reference the `referenceId` in either the body or URL of a
subrequest. Use this syntax to include a reference:
```
                @{referenceId.FieldName}.

```
You can use two operators with the reference ID.

The `.` operator references a field on a JSON object in the
response. For example, let’s say you retrieve an account record’s
data in one subrequest and assign the reference ID
`Account1Data` to the output. You can refer to the account’s
name in later subrequests like this:
```
                @{Account1Data.Name}.

```
The [] operator indexes a JSON collection in the response. For
example, let’s say you request basic account information with
the sObject Basic Information resource in one subrequest and
assign the reference ID `AccountInfo` to the output. Part of
the response includes a collection of recently created accounts.
You can refer to the ID of the first account in the recent items
collection like this:
```
                @{AccountInfo.recentItems[0].Id}.

```
You can use each operator recursively as long as it makes sense
in the context of the response. For example, to refer to the billing
city component of an account’s compound address field:
```
                @{NewAccount.BillingAddress.city}.

```
`referenceId` is case-sensitive, so pay close attention to the
case of the fields you’re referring to. See Usage.

Note:

**•** The `referenceId` must start with a letter or a
number.

**•** The `referenceId` must not contain anything
besides letters, numbers, or underscores (’_’).

`url` String The resource to request. Required

**•** The URL can include any query string parameters that the
subrequest supports. The query string must be URL-encoded.

**•** You can use parameters to filter response bodies.

**•** The URL must start with `/services/data/vXX.X/.`


-----

**JSON examples**

**Example 1**
```
  {
    "method" : "GET",
    "url" : "/services/data/v62.0/sobjects/Account/describe",
    "httpHeaders" : { "If-Modified-Since" : "Tue, 31 May 2016 18:00:00 GMT" },
    "referenceId" : "AccountInfo"
  }

```
**Example 2**
```
  {
    "method" : "POST",
    "url" : "/services/data/v62.0/sobjects/Account",
    "referenceId" : "refAccount",
    "body" : { "Name" : "Sample Account" }
  }

```
**Example 3**
```
  {
    "method" : "GET",
    "url" : "/services/data/v62.0/sobjects/Account/@{refAccount.id}",
    "referenceId" : "NewAccountFields"
  }

```
**Example 4**
```
  {
    "method" : "PATCH",
    "url" : "/services/data/v62.0/sobjects/Account/ExternalAcctId__c/ID12345",
    "referenceID" : "NewAccount",
    "body" : { "Name" : "Acme" }
  }

```
**Usage**
Because `referenceId` is case-sensitive, it’s important to note the case of the fields that you’re referring to. The same field can
use different cases in different contexts. For example, when you create a record, the ID field appears as `id` in the response. But
when you access a record’s data with the sObject Rows resource, the ID field appears as Id. In Example 3, the @{refAccount.id}
reference is valid because `refAccount` refers to the response from a POST like that shown in Example 2. If you use `Id` instead
(mixed case rather than all lowercase), as in @{refAccount.Id}, you get an error when sending the request because the
reference ID uses the wrong case.

Note: You can have up to 25 subrequests in a single call. Up to 5 of these subrequests can be sObject Collections or query
operations, including Query and QueryAll requests.

##### Composite Response Body

Describes the result of a Composite request.


-----

###### Composite Results

**Properties**

**Name** **Type** **Description**

compositeResponse Composite Subrequest Collection of subrequest results
Result on page 371[]

**JSON example**
```
  {
    "compositeResponse" : [{
     Composite Subrequest Result
      },{
     Composite Subrequest Result
      },{
     Composite Subrequest Result
    }]
  }

##### Composite Subrequest Result

```
The composite subrequest result describes the result for a subrequest.

###### Properties


`body` The type depends on the response type of
the subrequest.


The response body of this subrequest. See
the documentation for the subrequest
resource for more information.

If the subrequest returns an error, the body
includes the error code and message. For
more details on error responses, see Status
Codes and Error Responses.


`httpHeaders` Map<String, String> Response headers and their values for this
subrequest. The Composite resource doesn’t

support the Content-Length header, so
subrequest responses don’t include this
header and neither does the top-level
response.

`httpStatusCode` Integer An HTTP status code for this subrequest. If
`allOrNone` is set to true in the

composite request and a subrequest returns
an error, all other subrequests return the
400 HTTP status code.


-----

`referenceId` String

###### Example


The reference ID specified in the subrequest.
This property lets you easily associate
subrequests with their results.


The following example shows the response for a subrequest that had an error while trying to create a Contact:
```
{
  "body" : [ {
   "message" : "Email: invalid email address: Not a real email address",
   "errorCode" : "INVALID_EMAIL_ADDRESS",
   "fields" : [ "Email" ]
  } ],
  "httpHeaders" : { },
  "httpStatusCode" : 400,
  "referenceId" : "badContact"
}

###### Behavior and Responses If There Are Illegal Characters in Reference IDs

```
The `referenceIds must not contain anything besides letters, numbers, and underscores (’_’).`

The API’s behavior if there are illegal characters depends on the API version and the release. (The pertinent API version is that used to
make the composite request. That version isn’t necessarily the same as the API version specified in the url parameters in the subrequests.)

For example, consider the following request. It attempts to do the following:

**•** Create an account named “Cloudy Consulting”.

**•** Create a Contact, “Mary Smith”, linked to the Cloudy Consulting account.

**•** Create another new account, named “Easy Spaces”.

It has illegal characters in the first reference ID, `refNewAccount[1].`


-----

**Version 51.0 and Earlier**

In API version 51.0 and earlier, illegal characters in a reference ID cause all the subrequests that use that reference ID to fail. In this example,
the response is:


-----

The two accounts are created (even though the first account uses illegal characters in its reference ID). But the attempt to create a contact
(using the reference ID containing illegal characters) fails.

**Responses for Version 51.0 and Earlier in Previous Releases**

The response shown above is that for the Summer ’21 release and later. In releases before Summer ’21, problematic reference IDs in the
response were truncated if the IDs contained ‘(’ or ‘[’. So the response would have been:
```
{
  "compositeResponse" : [
    {
      "body" : {
        "id" : "001R0000006hfeZIAQ",
        "success" : true,
        "errors" : [ ]
      },
      "httpHeaders" : {
        "Location" : "/services/data/v51.0/sobjects/Account/001R0000006hfeZIAQ"
      },
      "httpStatusCode" : 201,
      "referenceId" : "refNewAccount"
    },
   ...
}

```
Starting with the Summer ’21 release, problematic reference IDs are no longer truncated. This change makes it easier to match the parts
of the response to the request.

**Version 52.0 and Later**

In API version 52.0 and later, any illegal characters in reference IDs cause the whole request to fail. The response to the example above
is:


-----

**Summary**

###### Behavior for References to Null Fields

The API’s behavior if there are references to null fields depends on the API version. (The pertinent API version is that used to make the
composite request. That version isn’t necessarily the same as the API version specified in the `url` parameters in the subrequests.)

Note: This behavior only applies to requests where the parent request uses an sObject Rows resource (for example,
```
  /services/data/vXX.X/sobjects/Contact/id).

```
For example, consider this request. It locates an existing Contact and then uses `@{refContact.FirstName}` and
`@{refContact.LastName}` to create a record.


-----

What happens if the Contact’s first name is null (not set)?

**Responses for Version 51.0 and Earlier**

In API version 51.0 and earlier, the fact that the Contact’s FirstName field is null causes the dependent subrequest to fail.
```
{
  "compositeResponse" : [
    {
      "body" : {
        "attributes" : {
         "type" : "Contact",
         "url" : "/services/data/v51.0/sobjects/Contact/003RO0000016kOuYAI"
        },
        "FirstName" : null,
        "LastName" : "Wong",
        "Id" : "003RO0000016kOuYAI"
      },
      "httpHeaders" : { },
      "httpStatusCode" : 200,
      "referenceId" : "refContact"
    },
    {
      "body" : [
        {
         "errorCode" : "PROCESSING_HALTED",
         "message" : "Invalid reference specified. No value for refContact.FirstName
 found in refContact.
         Provided referenceId ('refContact.FirstName') must start with a letter or a
 number,
         and it can contain only letters, numbers and underscores ('_')."
        }
      ],
      "httpHeaders" : { },
      "httpStatusCode" : 400,
      "referenceId" : "newContact"
    }
  ]
}

```
That example assumes that allOrNone is set to false. If it’s true, the whole composite request is rolled back. See allOrNone Parameters
in Composite and Collections Requests.

**Responses for Version 52.0 and Later**


-----

In API version 52.0 and later, the request succeeds.
```
{
  "compositeResponse" : [
    {
      "body" : {
        "attributes" : {
         "type" : "Contact",
         "url" : "/services/data/v51.0/sobjects/Contact/003RO0000016kOuYAI"
        },
        "FirstName" : null,
        "LastName" : "Wong",
        "Id" : "003RO0000016kOuYAI"
      },
      "httpHeaders" : { },
      "httpStatusCode" : 200,
      "referenceId" : "refContact"
    },
    {
      "body" : {
        "id" : "003RO0000016kRAYAY",
        "success" : true,
        "errors" : [ ]
      },
      "httpHeaders" : {
        "Location" : "/services/data/v51.0/sobjects/Contact/003RO0000016kRAYAY"
      },
      "httpStatusCode" : 201,
      "referenceId" : "newContact"
    }
  ]
}

###### Behavior for References to Fields That Aren’t Specified in the Parent Request

```
In dependent subrequests, you must always only use fields that are explicitly selected in parent requests. If this practice isn’t followed,
the API’s behavior depends on the API version. (The pertinent API version is that used to make the composite request. That version isn’t
necessarily the same as the API version specified in the `url parameters in the subrequests.)`

For example, consider the following request. It attempts to:

**1. Locate a specific Contact.**

**2. Use** `@{refContact.records[0].AccountId}` to get that Contact’s Account ID.

However, the parent request doesn’t explicitly query for the `AccountId.`


-----

**Responses for Version 51.0 and Earlier**

In API version 51.0 and earlier, there are rare cases where such a request succeeds.

Note: The fact that a request like this sometimes succeeds should never be relied upon. If you plan to use a field from a parent
request’s result, you should always explicitly select that field in the parent request.

**Responses for Version 52.0 and Later**

In API version 52.0 and later, the request always fails:


-----

To make such a request work, you must explicitly obtain the `AccountId` in the parent request:
```
{
  "compositeRequest" : [
    {
      "method" : "GET",
      "url" : "/services/data/v51.0/query?q=select Id, Account.Name,
Contact where Id='003RO0000016kOuYAI'",
      "referenceId" : "refContact"
    },
    {
      "method" : "GET",
      "url" : "/services/data/v50.0/query?q=select Name from Account where Id =
'@{refContact.records[0].AccountId}'",
      "referenceId" : "refAccount"
    }
  ]
}

#### Get a List of Composite Resources

```
Gets a list of URIs for other composite resources.

##### Syntax

**URI**
```
  /services/data/vXX.X/composite

```
**Formats**
JSON

**HTTP method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

**Request body**
None required


-----

##### Example

**Example Request**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/ -H
  "Authorization: Bearer token"

```
**Example Response Body**
```
  {
    "tree": "/services/data/v54.0/composite/tree",
    "batch": "/services/data/v54.0/composite/batch",
    "sobjects": "/services/data/v54.0/composite/sobjects",
    "graph": "/services/data/v54.0/composite/graph"
  }
