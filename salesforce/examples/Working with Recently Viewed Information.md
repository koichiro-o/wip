### Working with Recently Viewed Information

The examples in this section use REST API Query and Recently Viewed resources to programmatically retrieve and update recently viewed
record information.

IN THIS SECTION:

View Recently Viewed Records
Use the Recently Viewed Items resource to get a list of recently viewed records.

Mark Records as Recently Viewed
To mark a record as recently viewed using REST API, use the Query resource with a FOR VIEW or FOR REFERENCE clause. Use
SOQL to mark records as recently viewed to ensure that information such as the date and time the record was viewed is correctly
set.

#### View Recently Viewed Records

Use the Recently Viewed Items resource to get a list of recently viewed records.

**Example usage for getting the last two most recently viewed records**


-----

**Example request body**
none required

**Example response body**
```
  {
    "attributes" :
    {
       "type" : "Account",
       "url" : "/services/data/v62.0/sobjects/Account/a06U000000CelH0IAJ"
    },
    "Id" : "a06U000000CelH0IAJ",
    "Name" : "Acme"
  },
  {
    "attributes" :
    {
       "type" : "Opportunity",
       "url" : "/services/data/v62.0/sobjects/Opportunity/a06U000000CelGvIAJ"
    },
    "Id" : "a06U000000CelGvIAJ",
    "Name" : "Acme - 600 Widgets"
  }

#### Mark Records as Recently Viewed

```
To mark a record as recently viewed using REST API, use the Query resource with a `FOR VIEW` or `FOR REFERENCE` clause. Use
SOQL to mark records as recently viewed to ensure that information such as the date and time the record was viewed is correctly set.

Use `FOR VIEW` to notify Salesforce when a record is viewed from a custom interface, such as a mobile application or from a custom
page. Use `FOR REFERENCE` when a record is referenced from a custom interface. A record is referenced every time a related record
is viewed. For more information, see “FOR VIEW” and “FOR REFERENCE” in the SOQL and SOSL Reference.

**Example usage for executing a query that marks one Account record as recently viewed**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/query/?q=SELECT+Name+FROM+Account+LIMIT+1+FOR+VIEW
   -H "Authorization: Bearer token"

```
**Example request body for executing a query**
none required

**Example response body for executing a query**


-----

SEE ALSO:

Query
