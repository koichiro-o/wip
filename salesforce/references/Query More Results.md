### Query More Results

Returns the next batch of results from a SOQL query using a query locator.

If the number of results returned from a SOQL query exceeds the number of requested records or the limit, the response contains a
batch of results, a `false` value for `done, and a query locator. Use the query locator in another request to retrieve the next batch of`
records. If there are still more records to be returned, the response contains a new query locator and done is false. You can continue
retrieving results from the initial query until `done` is `true, which indicates that all results are returned.`

The response contains the total number of records returned by the QueryAll request (totalSize), a boolean indicating whether there
are no more results (done), the URI of the next set of records (nextRecordsUrl), and an array of query result records (records).

#### Syntax

**URI**
```
  /services/data/vXX.X/query/queryLocator

```
**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```

-----

**Parameters**

**Parameter** **Description**

`queryLocator` A string used to retrieve the next set of query results. If there are more results to be retrieved, the
previous set of query results contains the query locator in the `nextRecordsUrl` field.

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
**•** [For an example of how to use the query locator see Execute a SOQL Query.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/dome_query.htm)

**•** [For another option to change the batch size, see Query Options Header.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/headers_queryoptions.htm)

**•** [For more information on SOQL in general, see the SOQL and SOSL Reference.](https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_sosl_intro.htm)
