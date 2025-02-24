### Working with Searches and Queries

The examples in this section use REST API resources to search and query records using Salesforce Object Search Language (SOSL) and
[Salesforce Object Query Language (SOQL), and other search APIs. For more information on SOSL and SOQL see the SOQL and SOSL](https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/)
_[Reference.](https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/)_

IN THIS SECTION:

Execute a SOQL Query
Use the Query resource to execute a SOQL query that returns all the results in a single response, or if needed, returns part of the
results and a locator used to retrieve the remaining results.

Execute a SOQL Query that Includes Deleted Items
Use the QueryAll resource to execute a SOQL query that includes information about records that have been deleted because of a
merge or delete. Use QueryAll rather than Query, because the Query resource will automatically filter out items that have been
deleted.

Get Feedback on Query Performance (Beta)
[To get feedback on how Salesforce executes your query, report, or list view, use the Query resource along with the](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/resources_query.htm) `explain`
parameter. Salesforce analyzes each query to find the optimal approach to obtain the query results. Depending on the query and
query filters, Salesforce uses an index or internal optimization. To return details on how Salesforce optimizes your query, without
actually running the query, use the `explain` parameter. Based on the response, decide whether to fine-tune the performance of
your query, like adding filters to make the query more selective.

Search for a String
Use the Search resource to execute a SOSL search or use the Parameterized Search resource to execute a simple RESTful search
without SOSL.

Get the Default Search Scope and Order
Use the Search Scope and Order resource to retrieve the default global search scope and order for the logged-in user, including any
pinned objects in the user’s search results page.

Get Search Result Layouts for Objects
Use the Search Result Layouts resource to retrieve the search result layout configuration for each object specified in the query string.

View Relevant Items
Use the Relevant Items resource to get a list of relevant records.

#### Execute a SOQL Query

Use the Query resource to execute a SOQL query that returns all the results in a single response, or if needed, returns part of the results
and a locator used to retrieve the remaining results.


-----

The following query requests the value from `name` fields from all Account records.

**Example usage for executing a query**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/query/?q=SELECT+name,id+from+Account
   -H "Authorization: Bearer token"

```
**Example request body for executing a query**
none required

**Example response body for executing a query**
```
  {
    "done" : true,
    "totalSize" : 14,
    "records" :
    [
       {
         "attributes" :
         {
            "type" : "Account",
            "url" : "/services/data/v62.0/sobjects/Account/001D000000IRFmaIAH"
         },
         "Name" : "Test 1"
       },
       {
         "attributes" :
         {
            "type" : "Account",
            "url" : "/services/data/v62.0/sobjects/Account/001D000000IomazIAB"
         },
         "Name" : "Test 2"
       },
       ...
    ]
  }

##### Retrieving the Remaining SOQL Query Results

```
If the initial query returns only part of the results, the end of the response contains a field called `nextRecordsUrl:`
```
"nextRecordsUrl" : "/services/data/v62.0/query/01gD0000002HU6KIAW-2000"

```
In such cases, request the next batch of records and repeat until all records have been retrieved. These requests use nextRecordsUrl,
and don't include any parameters.

**Example usage for retrieving the remaining query results**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/query/01gD0000002HU6KIAW-2000
   -H "Authorization: Bearer token"

```
**Example request body for retrieving the remaining query results**
none required


-----

**Example response body for retrieving the remaining query results**
```
  {
    "done" : true,
    "totalSize" : 3214,
    "records" : [...]
  }

#### Execute a SOQL Query that Includes Deleted Items

```
Use the QueryAll resource to execute a SOQL query that includes information about records that have been deleted because of a merge
or delete. Use QueryAll rather than Query, because the Query resource will automatically filter out items that have been deleted.

The following query requests the value from the `Name` field from all deleted Merchandise__c records, in an organization that has one
deleted Merchandise__c record. The same query using Query instead of QueryAll would return no records, because Query automatically
filters out any deleted record from the result set.

**Example usage for executing a query for deleted Merchandise__c records**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/queryAll/?q=SELECT+Name+from+Merchandise__c+WHERE+isDeleted+=+TRUE
   -H "Authorization: Bearer token"

```
**Example request body for executing a query**
none required

**Example response body for executing a query**
```
  {
    "done" : true,
    "totalSize" : 1,
    "records" :
    [
       {
         "attributes" :
         {
            "type" : "Merchandise__c",
          "url" : "/services/data/v62.0/sobjects/Merchandise__c/a00D0000008pQRAIX2"
         },
         "Name" : "Merchandise 1"
       },
    ]
  }

##### Retrieving the Remaining SOQL Query Results

```
If the initial query returns only part of the results, the end of the response will contain a field called `nextRecordsUrl. For example,`
you might find this attribute at the end of your query:
```
"nextRecordsUrl" : "/services/data/v62.0/query/01gD0000002HU6KIAW-2000"

```
In such cases, request the next batch of records and repeat until all records have been retrieved. These requests use nextRecordsUrl,
and do not include any parameters.


-----

Although the `nextRecordsUrl` has `query` in the URL, it still provides the remaining results from the initial QueryAll request. The
remaining results include deleted records that matched the initial query.

**Example usage for retrieving the remaining results**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/query/01gD0000002HU6KIAW-2000
   -H "Authorization: Bearer token"

```
**Example request body for retrieving the remaining results**
none required

**Example response body for retrieving the remaining results**
```
  {
    "done" : true,
    "totalSize" : 3214,
    "records" : [...]
  }

#### Get Feedback on Query Performance (Beta)

```
[To get feedback on how Salesforce executes your query, report, or list view, use the Query resource along with the explain](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/resources_query.htm) parameter.
Salesforce analyzes each query to find the optimal approach to obtain the query results. Depending on the query and query filters,
Salesforce uses an index or internal optimization. To return details on how Salesforce optimizes your query, without actually running
the query, use the explain parameter. Based on the response, decide whether to fine-tune the performance of your query, like adding
filters to make the query more selective.

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
[is subject to the applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

The response contains one or more query execution plans, sorted from most optimal to least optimal. The most optimal plan is the plan
that’s used when the query, report, or list view is executed.

For more details on the fields returned when using `explain, see the` `explain` [parameter in Query Options Headers. For more](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/headers_queryoptions.htm)
[information on making queries more selective, see Working with Very Large SOQL Queries in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.252.0.apexcode.meta/apexcode/langCon_apex_SOQL_VLSQ.htm)

##### Example: Feedback on Query Performance

The following performance feedback query uses `Merchandise__c:`
```
curl https://MyDomainName.my.salesforce.com/services/data/v62.0/query/?explain=
SELECT+Name+FROM+Merchandise__c+WHERE+CreatedDate+=+TODAY+AND+Price__c+>+10.0

```
The response body for a performance feedback query looks like this:


-----

This response indicates that Salesforce found two possible execution plans for this query. The first plan uses the CreatedDate index field
to improve the performance of this query. The second plan scans all records without using an index. If the query is executed, the first
plan is used. Both plans note that there’s no secondary optimization for filtering out records marked as deleted because the IsDeleted
field isn’t indexed.

#### Search for a String

Use the Search resource to execute a SOSL search or use the Parameterized Search resource to execute a simple RESTful search without
SOSL.

##### Example SOSL Search Using the GET Method

The following example executes a SOSL search for `Acme. The search string in this example must be URL-encoded.`

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/search/?q=FIND+%7BAcme%7D
   -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example response body**


-----

##### Example Parameterized Search Using the GET Method

The following example executes a parameterized search for `Acme. The search string in this example must be URL-encoded.`

**Example usages**
**Global search for all results containing Acme**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/parameterizedSearch/?q=Acme
   -H "Authorization: Bearer token"

```
**Account search for results containing Acme, returning the id and name fields**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/parameterizedSearch/?q=Acme&sobject=Account&Account.fields=id,name&Account.limit=10
   -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example response body**
```
  {
   "searchRecords" : [ {
    "attributes" : {
      "type" : "Account",
      "url" : "/services/data/v62.0/sobjects/Account/001D000000IqhSLIAZ"
    },
    "Id" : "001D000000IqhSLIAZ"
   }, {
    "attributes" : {
      "type" : "Account",
      "url" : "/services/data/v62.0/sobjects/Account/001D000000IomazIAB"
    },
    "Id" : "001D000000IomazIAB"
   } ]
  }

```
**Example response body with** `metadata` **parameter**

Note: The `metadata` parameter is only returned if the request specified `metadata=LABELS.`


-----

##### Example Parameterized Search Using the POST Method

Execute a parameterized search using the POST method to access all search features available.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/parameterizedSearch
  "Authorization: Bearer token" -H "Content-Type: application/json” -d "@search.json”

```
**Example request body**
None required

**Example JSON file**
```
  {
    "q":"Smith",
    "fields" : ["id", "firstName", "lastName"],
    "sobjects":[{"fields":["id", "NumberOfEmployees"],
         "name": "Account",
         "limit":20},
        {"name": "Contact"}],
    "in":"ALL",
    "overallLimit":100,
    "defaultLimit":10
  }

```
**Example response body**


-----

SEE ALSO:

Search

Parameterized Search

#### Get the Default Search Scope and Order

Use the Search Scope and Order resource to retrieve the default global search scope and order for the logged-in user, including any
pinned objects in the user’s search results page.

In the following example, the default global search scope of the logged-in user consists of the site, idea, case, opportunity, account, and
user objects, in the order in which they are returned in the response body.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/search/scopeOrder -H
  "Authorization: Bearer token"

```
**Example request body**
none required

**Example response body**


-----

#### Get Search Result Layouts for Objects

Use the Search Result Layouts resource to retrieve the search result layout configuration for each object specified in the query string.

**Example usage**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/search/layout/?q=Account,Contact,Lead,Asset
   "Authorization: Bearer token"

```
**Example request body**
None required

**Example response body**


-----

-----

#### View Relevant Items

Use the Relevant Items resource to get a list of relevant records.

**Example usage for getting a list of the current user’s most relevant records**
```
  curl https://MyDomainName
   -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example response body**
```
  [ {
    "apiName" : "Contact",
    "key" : "003",
    "label" : "Contacts",
    "lastUpdatedId" : "135866748",
    "recordIds" : [ "003xx000004TxBA" ]
  }, { "apiName" : "Account",
    "key" : "001",
    "label" : "Accounts",
    "lastUpdatedId" : "193640553",
    "recordIds" : [ "001xx000003DWsT" ]
  }, {
    "apiName" : "User",
    "key" : "005",
    "label" : "Users",
    "lastUpdatedId" : "-199920321",
    "recordIds" : [ "005xx000001Svqw", "005xx000001SvwK", "005xx000001SvwA" ]
  }, { "apiName" : "Case",
    "key" : "069",
    "label" : "Cases",
    "lastUpdatedId" : "1033471693",
    "recordIds" : [ "069xx0000000006", "069xx0000000001", "069xx0000000002" ]
  } ]

```
**Example usage for filtering the response to certain objects**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/relevantItems?sobjects=Account,User
   -H "Authorization: Bearer token"

```
**Example request body**
None required


-----

**Example response body**
```
  [ {
    "apiName" : "Account",
    "key" : "001",
    "label" : "Accounts",
    "lastUpdatedId" : "193640553",
    "recordIds" : [ "001xx000003DWsT" ]
  }, {
   "apiName" : "User",
    "key" : "005",
    "label" : "Users",
    "lastUpdatedId" : "102959935",
    "recordIds" : [ "005xx000001Svqw", "005xx000001SvwK", "005xx000001SvwA" ]
  } ]

```
**Example usage for comparing the user’s current list of relevant records to a previous version**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/relevantItems?lastUpdatedId=102959935
   -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example response header**
```
  lastUpdatedId: 102959935
  newResultSetSinceLastQuery: true

```
**Example response body**
```
  [ {
    "apiName" : "User",
    "key" : "003",
    "label" : "Users",
    "lastUpdatedId" : "102959935",
    "recordIds" : [ "003xx000004TxBA" ]
  }, {
    "apiName" : "Account",
    "key" : "001",
    "label" : "Accounts",
    "lastUpdatedId" : "193640553",
    "recordIds" : [ "001xx000003DWsT" ]
  }, {
    "apiName" : "Case",
    "key" : "005",
    "label" : "Cases",
   "lastUpdatedId" : "1740766611",
    "recordIds" : [ "005xx000001Svqw", "005xx000001SvwA" ]
  } ]

```
**Example usage for comparing the user’s current list of relevant records to a previous version for a particular object**


-----

**Example request body**
None required

**Example response body**
```
  [ {
    "apiName" : "Account",
    "key" : "001",
    "label" : "Accounts",
    "lastUpdatedId" : "193640553",
    "recordIds" : [ "001xx000003DWsT" ]
  } ]

```
SEE ALSO:

sObject Relevant Items
