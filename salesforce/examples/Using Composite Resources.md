### Using Composite Resources

The examples in this section use composite resources to improve your application’s performance by minimizing the number of round-trips
between the client and server.

IN THIS SECTION:

Execute Dependent Requests in a Single API Call
The following example uses the Composite resource to execute several dependent requests all in a single call. First, it creates an
account and retrieves its information. Next it uses the account data and the Composite resource’s reference ID functionality to create
a contact and populate its fields based on the account data. Then it retrieves specific information about the account’s owner by
using query parameters in the request string. Finally, if the metadata has been modified since a certain date, it retrieves account
metadata. The `composite.json` file contains the composite request and subrequest data.

Update an Account, Create a Contact, and Link Them with a Junction Object
The following example uses the Composite resource to update some fields on an account, create a contact, and link the two records
with a junction object called `AccountContactJunction. All these requests are executed in a single call. The`
`composite.json` file contains the composite request and subrequest data.

Update a Record and Get Its Field Values in a Single Request
Use the Composite Batch resource to execute multiple requests in a single API call.

Upsert an Account and Create a Contact
The following example uses the Composite resource to upsert an account and create a contact that is linked to the account. All these
requests are executed in a single call. The `composite.json` file contains the composite request and subrequest data.

Create Nested Records
Use the sObject Tree resource to create nested records that share a root record type. For example, in a single request, you can create
an account along with its child contacts, and a second account along with its child accounts and contacts. Once the request is
processed, the records are created and parents and children are automatically linked by ID. In the request data, you supply the record
hierarchies, required and optional field values, each record’s type, and a reference ID for each record, and then use the POST method
of the resource. The response body will contain the IDs of the created records if the request is successful. Otherwise, the response
contains only the reference ID of the record that caused the error and the error information.

Create Multiple Records
While the resource can be used to create nested records, you can also create multiple, unrelated records of the same type. In a single
request, you can create up to two hundred records. In the request data, you supply the required and optional field values for each
record, each record’s type, and a reference ID for each record, and then use the POST method of the resource. The response body
will contain the IDs of the created records if the request is successful. Otherwise, the response contains only the reference ID of the
record that caused the error and the error information.

Using Composite Graphs
Composite graphs provide an enhanced way to perform composite requests, which execute a series of REST API requests in a single
call.

Using a Composite Graph
This example shows how to use a composite graph. It also demonstrates how one request can use more than one composite graph.

allOrNone Parameters in Composite and Collections Requests
If a Composite request uses sObject Collections, there are two or more `allOrNone` parameters that can interact, one on the
Composite request and one on each sObject Collections subrequest.


-----

#### Execute Dependent Requests in a Single API Call

The following example uses the Composite resource to execute several dependent requests all in a single call. First, it creates an account
and retrieves its information. Next it uses the account data and the Composite resource’s reference ID functionality to create a contact
and populate its fields based on the account data. Then it retrieves specific information about the account’s owner by using query
parameters in the request string. Finally, if the metadata has been modified since a certain date, it retrieves account metadata. The
`composite.json` file contains the composite request and subrequest data.

**Execute dependent requests in a single API call**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/ -H
  "Authorization: Bearer token -H "Content-Type: application/json" -d "@composite.json"

```
**Request body** `composite.json` **file**


-----

**Response body after successfully executing the composite request**


-----

a Junction Object
```
       "httpHeaders" : { },
       "httpStatusCode" : 200,
       "referenceId" : "NewAccountOwner"
    },{
       "body" : null,
       "httpHeaders" : {
         "ETag" : "\"f2293620\"",
         "Last-Modified" : "Fri, 22 Jul 2016 18:45:56 GMT"
       },
       "httpStatusCode" : 304,
       "referenceId" : "AccountMetadata"
    }]
  }

#### Update an Account, Create a Contact, and Link Them with a Junction Object

```
The following example uses the Composite resource to update some fields on an account, create a contact, and link the two records
with a junction object called AccountContactJunction. All these requests are executed in a single call. The composite.json
file contains the composite request and subrequest data.

**Update an account, create a contact, and link them with a junction object**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/ -H
  "Authorization: Bearer token -H "Content-Type: application/json" -d "@composite.json"

```
**Request body** `composite.json` **file**


-----

**Response body after successfully executing the composite request**
```
  {
   "compositeResponse" : [{
    "body" : null,
    "httpHeaders" : { },
    "httpStatusCode" : 204,
    "referenceId" : "UpdatedAccount"
   }, {
    "body" : {
      "id" : "003R00000025R22IAE",
      "success" : true,
      "errors" : [ ]
    },
    "httpHeaders" : {
      "Location" : "/services/data/v62.0/sobjects/Contact/003R00000025R22IAE"
    },
    "httpStatusCode" : 201,
    "referenceId" : "NewContact"
   }, {
    "body" : {
      "id" : "a00R0000000iN4gIAE",
      "success" : true,
      "errors" : [ ]
    },
    "httpHeaders" : {
      "Location" :
  "/services/data/v62.0/sobjects/AccountContactJunction__c/a00R0000000iN4gIAE"
    },
    "httpStatusCode" : 201,
    "referenceId" : "JunctionRecord"
   }]
  }

#### Update a Record and Get Its Field Values in a Single Request

```
Use the Composite Batch resource to execute multiple requests in a single API call.

The following example updates the name on an account and gets some of the account’s field values in a single request. The batch.json
file contains the subrequest data.

**Update a record and query its name and billing postal code in a single request**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/batch/ -H
  "Authorization: Bearer token -H "Content-Type: application/json" -d "@batch.json"

```
**Request body** `batch.json` **file**


-----

**Response body after successfully executing the subrequests**
```
  {
    "hasErrors" : false,
    "results" : [{
      "statusCode" : 204,
      "result" : null
      },{
      "statusCode" : 200,
      "result": {
       "attributes" : {
         "type" : "Account",
         "url" : "/services/data/v62.0/sobjects/Account/001D000000K0fXOIAZ"
       },
       "Name" : "NewName",
       "BillingPostalCode" : "94105",
       "Id" : "001D000000K0fXOIAZ"
      }
    }]
  }

```
SEE ALSO:

Composite Batch

#### Upsert an Account and Create a Contact

The following example uses the Composite resource to upsert an account and create a contact that is linked to the account. All these
requests are executed in a single call. The `composite.json` file contains the composite request and subrequest data.

**Upsert an account and create a contact**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/ -H
  "Authorization: Bearer token -H "Content-Type: application/json" -d "@composite.json"

```
**Request body** `composite.json` **file**


-----

**Response body after successfully executing the composite request**
```
  {
    "compositeResponse" : [{
       "body" : {
         "id" : "0016g00000Wqu1EAAR",
         "success" : true,
         "errors" : [ ],
         "created" : true
       },
       "httpHeaders" : {
         "Location" : "/services/data/v62.0/sobjects/Account/0016g00000Wqu1EAAR"
       },
       "httpStatusCode" : 201,
       "referenceId" : "NewAccount"
    },{
       "body" : {
         "id" : "0036g00000WKnfLAAT",
         "success" : true,
         "errors" : [ ]
       },
       "httpHeaders" : {
         "Location" : "/services/data/v62.0/sobjects/Contact/0036g00000WKnfLAAT"
       },
       "httpStatusCode" : 201,
       "referenceId" : "newContact"
    }]
  }

```
SEE ALSO:

sObject Rows by External ID

#### Create Nested Records

Use the sObject Tree resource to create nested records that share a root record type. For example, in a single request, you can create an
account along with its child contacts, and a second account along with its child accounts and contacts. Once the request is processed,
the records are created and parents and children are automatically linked by ID. In the request data, you supply the record hierarchies,
required and optional field values, each record’s type, and a reference ID for each record, and then use the POST method of the resource.
The response body will contain the IDs of the created records if the request is successful. Otherwise, the response contains only the
reference ID of the record that caused the error and the error information.


-----

The following example creates two sets of nested records. The first set includes an account and two child contact records. The second
set includes an account, one child account record, and one child contact record. The record data is provided in `newrecords.json.`

**Example for creating two new accounts and their child records**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/tree/Account/
  -H "Authorization: Bearer token -H "Content-Type: application/json" -d "@newrecords.json"

```
**Example request body** `newrecords.json` **file for creating two new Accounts and their child records**


-----

**Example response body after successfully creating records and relationships**
```
  {
    "hasErrors" : false,
    "results" : [{
     "referenceId" : "ref1",
     "id" : "001D000000K0fXOIAZ"
     },{
     "referenceId" : "ref4",
     "id" : "001D000000K0fXPIAZ"
     },{
     "referenceId" : "ref2",
     "id" : "003D000000QV9n2IAD"
     },{
     "referenceId" : "ref3",
     "id" : "003D000000QV9n3IAD"
     },{
     "referenceId" : "ref5",
     "id" : "001D000000K0fXQIAZ"
     },{
     "referenceId" : "ref6",
     "id" : "003D000000QV9n4IAD"
     }]
  }

```
Once the request is processed, all six records are created with the parent-child relationships specified in the request.

SEE ALSO:

sObject Tree

#### Create Multiple Records

While the resource can be used to create nested records, you can also create multiple, unrelated records of the same type. In a single
request, you can create up to two hundred records. In the request data, you supply the required and optional field values for each record,
each record’s type, and a reference ID for each record, and then use the POST method of the resource. The response body will contain
the IDs of the created records if the request is successful. Otherwise, the response contains only the reference ID of the record that caused
the error and the error information.

The following example creates four new accounts. The record data is provided in `newrecords.json.`

**Example for creating four new accounts**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/tree/Account/
  -H "Authorization: Bearer token -H "Content-Type: application/json" -d "@newrecords.json"

```
**Example request body** `newrecords.json` **file for creating four new accounts**


-----

**Example response body after successfully creating records**
```
  {
    "hasErrors" : false,
    "results" : [{
     "referenceId" : "ref1",
     "id" : "001D000000K1YFjIAN"
     },{
     "referenceId" : "ref2",
     "id" : "001D000000K1YFkIAN"
     },{
     "referenceId" : "ref3",
     "id" : "001D000000K1YFlIAN"
     },{
     "referenceId" : "ref4",
     "id" : "001D000000K1YFmIAN"
     }]
  }

```
SEE ALSO:

sObject Tree

#### Using Composite Graphs

Composite graphs provide an enhanced way to perform composite requests, which execute a series of REST API requests in a single call.


-----

**•** Regular composite requests allow you to execute a series of REST API requests in a single call. And you can use the output of one
request as the input to a subsequent request.

**•** Composite graphs extend regular composite requests by allowing you to assemble a more complicated and complete series of
related objects and records.

**•** Composite graphs also enable you to ensure that the steps in a given set of requests are either all completed or all not completed.
If you use this option, you don’t have to check which requests were successful.

**•** Regular composite requests have a limit of 25 subrequests. Composite graphs increase this limit to 500.

##### Defining Composite Graphs

In general, a graph is a collection of connected nodes.

In the context of composite graph operations, the nodes are composite subrequests. For example, a node can be a composite subrequest
like this:
```
{
   "url" : "/services/data/v62.0/sobjects/Account/",
   "body" : {
     "name" : "Cloudy Consulting"
   },
   "method" : "POST",
   "referenceId" : "reference_id_account_1"
}

```
Each node features an endpoint representing a record.

Composite graph requests support only these URLs.

```
/services/data/vXX.X/sobjects/sObject
/services/data/vXX.X/sobjects/sObject/id
/services/data/vXX.X/sobjects/sObject/customFieldName/externalId

```

POST

See sObject Basic Information.

DELETE, GET, PATCH

See sObject Rows.

DELETE, GET, PATCH, POST

See sObject Rows by External ID.


-----

A composite graph can be directed meaning that some nodes use information from other nodes. For example, a node that creates a
Contact can use the ID of an Account node to link the Contact with the Account.

For example:
```
{
  "graphs": [{
    "graphId": "graph1",
    "compositeRequest": [{
        "body": {
         "name": "Cloudy Consulting"
        },
        "method": "POST",
        "referenceId": "reference_id_account_1",
        "url": "/services/data/v62.0/sobjects/Account/"
      },
      {
        "body": {
         "FirstName": "Nellie",
         "LastName": "Cashman",
         "AccountId": "@{reference_id_account_1.id}"
        },
        "method": "POST",
        "referenceId": "reference_id_contact_1",
        "url": "/services/data/v62.0/sobjects/Contact/"
      }
    ]
  }]
}

##### Defining Composite Graphs in JSON

```
A composite graph is defined in JSON like this:
```
{
   "graphId" : "graphId",
   graph
}

```
In other words, like this, where each `compositeSubrequest` is a composite subrequest:


-----

The `graphId parameters enable you to identify the graphs when viewing the response. They need not be numeric, but they must`
follow these restrictions:

**•** They must be unique within each composite graph operation.

**•** They must begin with an alphanumeric character.

**•** They must be less that 40 characters long.

**•** They can’t contain a period (’.’).

A single composite graph request can use one or more composite graphs. See Using a Composite Graph.

##### Example: Create Accounts, Contacts, Campaigns, Opportunities, Leads, and CampaignMembers with a Composite Graph Request

This example shows a composite graph that performs the following actions:

**1. Create Account 1.**

**2. Create Account 2 as a child of Account 1.**

**3. Create:**

**a. Contact 1, linked to Account 2.**

**b. Contact 2, who reports to Contact 1.**

**c.** Contact 3 who reports to Contact 2.

**4. Create a Campaign.**

**5. Create an Opportunity linked to Account 2 and the Campaign.**

**6. Create a Lead.**

**7. Create a CampaignMember linked to the Lead and the Campaign.**

The JSON for this graph is:


-----

-----

##### Example: GET Details About a Resource and Then Use Them in a Composite Graph Request

This example shows how you can use GET on a resource, and then use properties of that resource in subsequent requests.


-----

##### Graph Depth

**•** Nodes with no parents are considered to be at depth 1.

**•** The depth of another node is the maximum number of edges in the graph from depth 1 to that node. An edge between two nodes
occurs when the one node uses a property (such as `@{reference_account.id}` ) from another node.

##### The AllOrNone Parameter

In standard composite operations, the only control over what happens if an error occurs is the allOrNone parameter. If the value is
```
true, the entire composite request is rolled back. If the value is false, the remaining subrequests that don’t depend on the failed

```
subrequest are executed. Dependent subrequests aren’t executed, which can lead to a mix of processed and unprocessed records.

Composite graphs have the advantage that each graph is guaranteed to either complete all its subrequests successfully or to be rolled
back completely. In other words, the allOrNone parameter is implicitly considered to be `true` for each graph. A composite graph
request never results in a mix of processed and unprocessed records.

To ensure that graphs are independent, the following rules apply.

**1. Subrequests in one graph can’t reference subrequests from another graph.**

**2. Each graph in one composite graph operation must be independent. If one graph can’t be processed successfully, that must not**
prevent other graphs in the same operation from being processed.

##### Best Practices

As a general practice, keep your graphs as small as possible. For example, it’s more efficient to have 50 graphs with 10 nodes rather than
1 graph with 500 nodes. Keeping graphs small has two advantages:

**•** If one item in a graph fails, only the items in that graph are rolled back. It’s easier to identify and handle errors in smaller graphs.

**•** The server can process multiple, smaller graphs faster and more efficiently.


-----

##### Example: Submitting a Composite Graph Job

For an example showing how to submit a composite graph job, see Using a Composite Graph.

#### Using a Composite Graph

This example shows how to use a composite graph. It also demonstrates how one request can use more than one composite graph.

**•** Regular composite requests allow you to execute a series of REST API requests in a single call. And you can use the output of one
request as the input to a subsequent request.

**•** Composite graphs extend regular composite requests by allowing you to assemble a more complicated and complete series of
related objects and records.

**•** Composite graphs also enable you to ensure that the steps in a given set of requests are either all completed or all not completed.
If you use this option, you don’t have to check which requests were successful.

**•** Regular composite requests have a limit of 25 subrequests. Composite graphs increase this limit to 500.

Create a request:
```
curl -X POST curl https://MyDomainName.my.salesforce.com/services/data/v62.0/composite/graph
 -H "Authorization: Bearer token" -H "Content-Type: application/json" --data @data.json

```
where the file `data.json` contains the definition of the graphs. The general format for the request body is:
```
{
  "graphs": [
   {
    "graphId": "graphId",
    "compositeRequest": [
     compositeSubrequest,
     compositeSubrequest,
     ...
    ]
   },
   {
    "graphId": "graphId",
    "compositeRequest": [
     compositeSubrequest,
     compositeSubrequest,
     ...
    ]
   },
   ...
  ]
}

```
where `compositeSubrequest` is a composite subrequest result on page 371.

For example, two composite graph requests each create an Account and then create related records:


-----

-----

The response is:


-----

For more information, see Using Composite Graphs.
```
allOrNone Parameters in Composite and Collections Requests

```
If a Composite request uses sObject Collections, there are two or more allOrNone parameters that can interact, one on the Composite
request and one on each sObject Collections subrequest.

**•** If the Composite request has allOrNone set to true, then the all-or-none behavior also applies to each of the sObject Collections
subrequests, overriding the value of `allOrNone` in the subrequests.

**•** If the Composite request has allOrNone set to false, then each sObject Collections subrequest behaves according to its value
of `allOrNone.`


-----

Consider, for example, what happens with this job where a Composite request includes two items: an sObject Collections request and
a request to create a Contact. The sObject Collections request tries to create two Accounts, one of which fails because there is already
an existing Account with the same information.
```
POST https://MyDomainName.my.salesforce.com/services/data/v62.0/composite -H "Authorization:
 Bearer token"
{
  "allOrNone" : outerFlag,
  "collateSubrequests" : false,
  "compositeRequest" : [
    {
      "method" : "POST",
      "url" : "/services/data/v62.0/composite/sobjects",
      "body" : {
        "allOrNone" : innerFlag,
        "records" : [
         {
           "attributes" : { "type" : "Account" },
           "Name" : "Northern Trail Outfitters",
           "BillingCity" : "San Francisco"
         },
         {
           "attributes" : { "type" : "Account" },
           "Name" : "Easy Spaces",
           "BillingCity" : "Calgary"
         }
        ]
      },
      "referenceId" : "newAccounts"
    },
    {
      "method" : "POST",
      "url" : "/services/data/v62.0/sObject/Contact",
      "body" : {
          "FirstName" : "John",
          "LastName" : "Smith"
      },
      "referenceId" : "newContact"
    }
  ]
}

```
The `outerFlag` and `innerFlag` parameters are either `true` or `false, which leads to four possible cases.`

**Case 1:** `outerFlag` **=** `false,` `innerFlag` **=** `false`

In this case, neither request has `allOrNone` set to `true, so neither request is rolled back. One account is created and one fails.`


-----

**Case 2:** `outerFlag` **=** `false,` `innerFlag` **=** `true`

In this case, the inner sObject Collections request has `allOrNone` set to `true, so it is rolled back. The outer Composite request is`
not rolled back.

**Case 3:** `outerFlag =` `true,` `innerFlag` **=** `true`

In this case, both requests have `allOrNone` set to `true, so they are both rolled back.`


-----

**Case 4:** `outerFlag =` `true,` `innerFlag` **=** `false`

The response body for this case is:


-----

In this case, the inner sObject Collections request has `allOrNone` set to `false, so it is not immediately rolled back. However, the`
outer Composite request has allOrNone set to true so it is rolled back, which also rolls back the inner sObject Collections request.

Note: Even though the response body for sObject Collections request shows `"success" : true` for the creation of the
first Account, the fact that the Composite request is rolled back means that the Account creation is rolled back. The final result is
that the new Account is not created.


-----
