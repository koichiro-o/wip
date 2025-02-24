### QueryAll

Executes the specified SOQL query. Unlike the Query resource, QueryAll returns records that are soft deleted due to a merge or delete.
After these records are permanently removed from the recycle bin, you can no longer query them. QueryAll also returns information
about archived task and event records. This resource is available in REST API version 29.0 and later.

When a QueryAll request is executed, up to 2,000 records can be returned at a time in a synchronous request. However, to optimize
performance, the returned batch can include fewer records than the limit or what's set in the request, based on the size and complexity
of records queried. If the total number of results exceeds the limit or the requested number of results, the response contains a batch of
results, a false value for done, and a query locator. The query locator can be used with the QueryAll More Results resource to retrieve
the next batch of records.

Although the `nextRecordsUrl` has `query` in the URL, it still provides the remaining results from the initial QueryAll request. The
remaining results include deleted records that matched the initial query.


-----

The response contains the total number of records returned by the QueryAll request (totalSize), a boolean indicating whether there
are no more results (done), the URI of the next set of records (nextRecordsUrl), and an array of query result records (records).

#### Syntax

**URI**
```
  /services/data/vXX.X/queryAll?q=query

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

`q` A SOQL query. To create a valid URI, replace spaces with a plus sign `+` in the query
string. For example: SELECT+Name+FROM+MyObject.

#### Example

**Example Response Body**
```
  {
   "totalSize": 3222,
   "done": false,
   "nextRecordsUrl": "/services/data/v62.0/query/01gRO0000016PIAYA2-500",
   "records": [
    {
      "attributes": {
       "type": "Contact",
       "url": "/services/data/v62.0/sobjects/Contact/003RO0000035WQgYAM"
      },
      "Id": "003RO0000035WQgYAM",
      "Name": "John Smith"
    },
    ...
   ]
  }

#### Resources for Executing SOQL Queries

```
**•** [To run a query that includes deleted items, see Execute a SOQL Query that Includes Deleted Items.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/dome_queryall.htm)

**•** [To increase the batch size of query results, use the query identifier described in Execute a SOQL Query or use the Query Options](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/dome_query.htm)
[Header.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/headers_queryoptions.htm)

**•** [For more information about SOQL generally, see the SOQL and SOSL Reference.](https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_sosl_intro.htm)


-----
