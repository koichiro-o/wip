### Query

```
Executes the specified SOQL query.

When a SOQL query is executed, up to 2,000 records can be returned at a time in a synchronous request. However, to optimize performance,
the returned batch can include fewer records than the limit or what's set in the request, based on the size and complexity of records
queried. If the total number of results exceeds the limit or the requested number of results, the response contains the first batch of


-----

records, a false value for done, and a query locator. The query locator can be used with the Query More Results on page 307 resource
to retrieve the next batch of records.

The response contains the total number of records returned by the QueryAll request (totalSize), a boolean indicating whether there
are no more results (done), the URI of the next set of records (nextRecordsUrl), and an array of query result records (records).

#### Syntax

**URI**
```
  /services/data/vXX.X/query?q=query

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

```
  q

#### Example

```
**Example Response Body**


A SOQL query. To create a valid URI, replace spaces in the query string with a plus sign `+` or with
```
%20. For example: SELECT+Name+FROM+MyObject. If the SOQL query string is invalid, a

```
MALFORMED_QUERY response is returned.


#### Resources for Executing SOQL Queries

**•** [For an example, see Execute a SOQL Query.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/dome_query.htm)

**•** [To change the batch size, see Query Options Header.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/headers_queryoptions.htm)


-----

**•** To get feedback on a query and a report using the explain [parameter, see Get Feedback on Query Performance](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/dome_query_explain.htm)

**•** [For more information on SOQL in general, see the SOQL and SOSL Reference.](https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_sosl_intro.htm)

#### Data Cloud Query Profile Parameters

Data Cloud Query and Unified Profile parameters allow you to leverage Salesforce REST API Query endpoint to execute SOQL queries
against the Unified Profile, Data Source objects, or Data Model objects within your org. This functionality is supported using API version
51.0 or later.

[For general information about using the Query REST call, see Execute a SOQL Query and Query.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_rest.meta/api_rest/dome_query.htm)

##### Supported SOQL Parameters

The following SOQL parameters are supported for use with Data Cloud:

**•** `SELECT` statement on a single object

**•** `SELECT` clause: count()

**•** `SOQL WHERE` clause: contains operators

**•** `SOQL LIKE`

**•** `SOQL LIMIT` clause

The default limit is set to 100. The max limit is 2,000 records in a single call.

**•** `SOQL OFFSET` clause

**•** `SOQL ORDER BY` clause

##### SOQL Limitations

The following queries are not supported for use with Data Cloud:

**•** `SOQL` Subqueries

**•** `SELECT` clause: aggregate functions

**•** `SELECT` clause: date functions

**•** `SOQL HAVING` clause

##### Sample Queries


**Data Preview:**

Examine data that has been ingested
into a data lake object.

**Consent Lookup:**


**Get Email Click Events SELECT** SubscriberKey__c, EngagementChannel__c, EmailName__c,
SubjectLine__c FROM sfmc_email_engagement_click_{EID}__dll LIMIT =100

**Get Individual IDs by Email Address**


Retrieve Individual IDs from Contact `SELECT` PartyId__c FROM ContactPointEmail__dlm WHERE
Point Data Model objects based on EmailAddress__c=’jjones@email.com’ LIMIT =100
email address, phone number, or first
**Get Individual IDs by Phone Number SELECT** PartyId__c FROM ContactPointPhone__dlm
and last name.
`WHERE` TelephoneNumber__c=’555-123-4567’ LIMIT =100


-----

**Unified Profile Lookup:**


**Get Individual IDs by Name SELECT** IndividualId__c FROM Individual__dlm WHERE
FirstName__c=’Jimmy’ AND LastName__c=’Smith’ LIMIT =100

**Step 1:**


Retrieve Unified Individual and **Get Unified Record Id by Source Record Id**
Unified Contact Points by Source
`SELECT` UnifiedRecordId__c FROM IndividualIdentityLink__dlm WHERE
Record Id.
SourceRecordID__c='{sourceID}' LIMIT =100

**Step 2:**


**Query Unified Individual by Unified Profile ID**

`SELECT` FirstName__c, LastName__c FROM UnifiedIndividual__dlm WHERE
Id__c='{UnifiedRecordId__c}' LIMIT =100

**Step 3:**

**Query Unified Contact Point Details by Unified Profile ID**

_Unified Contact Point Email SELECT_ EmailAddress__c FROM UnifiedContactPointEmail__dlm
`WHERE` PartyId__c={UnifiedRecordId__c} LIMIT =100

_Unified Contact Point Phone SELECT_ TelephoneNumber__c FROM
UnifiedContactPointPhone__dlm WHERE PartyId__c={UnifiedRecordId__c} LIMIT =100
