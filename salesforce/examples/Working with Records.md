### Working with Records

The examples in this section use REST API resources to create, retrieve, update, and delete records, along with other record-related
operations.

IN THIS SECTION:

Create a Record
Use the sObject Basic Information resource to create new records. You supply the required field values in the request data, and send
the request using the POST HTTP method. The response body contains the ID of the new record if the call is successful.

Update a Record
You use the sObject Rows resource to update records. Provide the updated record information in your request data and use the
PATCH method of the resource with a specific record ID to update that record. Records in a single file must be of the same object
type.


-----

Delete a Record
Use the sObject Rows resource to delete records. Specify the record ID and use the DELETE method of the resource to delete a record.

Get Field Values from a Standard Object Record
You use the GET method of the sObject Rows resource to retrieve field values from a record.

Get Field Values from an External Object Record by Using the Salesforce ID
You use the sObject Rows resource to retrieve field values from a record. Specify the fields you want to retrieve in the `fields`
parameter and use the GET method of the resource.

Get Field Values from an External Object Record by Using the External ID Standard Field
You use the sObject Rows resource to retrieve field values from a record. Specify the fields you want to retrieve in the `fields`
parameter and use the GET method of the resource.

Get a Record Using an External ID
You can use the GET method of the sObject Rows by External ID resource to get records with a specific external ID.

Insert or Update (Upsert) a Record Using an External ID
You can use the sObject Rows by External ID resource to create records or update existing records (upsert) based on the value of a
specified external ID field.

Traverse Relationships with Friendly URLs
You can traverse relationship fields in standard and custom objects by constructing friendly URLs using the sObject Relationship
resource. This approach allows you to directly access records associated by relationships. Using friendly URLs is an easier alternative
to accessing records by obtaining object IDs from relationship fields and then inspecting the associated object ID record.

Get a List of Deleted Records Within a Given Timeframe
Use the sObject Get Deleted resource to get a list of deleted records for the specified object. Specify the date and time range within
which the records for the given object were deleted. Deleted records are written to a delete log (that is periodically purged), and
will be filtered out of most operations, such as sObject Rows or Query (although QueryAll will include deleted records in results).

Get a List of Updated Records Within a Given Timeframe
Use the sObject Get Updated resource to get a list of updated (modified or added) records for the specified object. Specify the date
and time range within which the records for the given object were updated.

#### Create a Record

Use the sObject Basic Information resource to create new records. You supply the required field values in the request data, and send the
request using the POST HTTP method. The response body contains the ID of the new record if the call is successful.

The following example request creates a new Account record, with the field values for the new record provided in newaccount.json.
Only the name field is specified in this example, but you could also provide values for other Account fields.

**Example for creating a new Account**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/ -H
  "Authorization: Bearer token" -H "Content-Type: application/json" -d "@newaccount.json"

```
**Example request body** `newaccount.json` **file for creating a new Account**


-----

**Example response body after successfully creating a new Account**
```
  {
   "id" : "001D000000IqhSLIAZ",
   "errors" : [ ],
   "success" : true
  }

```
**Example of error list after creating a new Account**
```
  "errors" : [
       // Example of one error object
       {
         "statusCode" : "MALFORMED_ID",
         "message" : "Contact ID: id value of incorrect type: 001xx000003DGb2999",
         "fields" : [
           "Id"
         ]
       },
       //Second error object,
       //Third error object
      ]

#### Update a Record

```
You use the sObject Rows resource to update records. Provide the updated record information in your request data and use the PATCH
method of the resource with a specific record ID to update that record. Records in a single file must be of the same object type.

In the following example, the Billing City within an Account is updated. The updated record information is provided in
```
patchaccount.json.

```
**Example for updating an Account object**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/001D000000INjVe
   -H "Authorization: Bearer token" -H "Content-Type: application/json" -d
  @patchaccount.json -X PATCH

```
**Example request body** `patchaccount.json` **file for updating fields in an Account object**
```
  {
    "BillingCity" : "San Francisco"
  }

```
**Example response body for updating fields in an Account object**
none returned

**Error response**
See Status Codes and Error Responses on page 16.

The following example uses Java and HttpClient to update a record using REST API. Note that there is no PatchMethod in HttpClient, so
PostMethod is overridden to return “PATCH” as its method name. This example assumes the resource URL has been passed in and
contains the object name and record ID.


-----

If you use an HTTP library that doesn't allow overriding or setting an arbitrary HTTP method name, you can send a POST request and
provide an override to the HTTP method via the query string parameter `_HttpMethod. In the PATCH example, you can replace the`
PostMethod line with one that doesn't use override:
```
PostMethod m = new PostMethod(url + "?_HttpMethod=PATCH");

```
SEE ALSO:

sObject Rows

Conditional Request Headers

#### Delete a Record

Use the sObject Rows resource to delete records. Specify the record ID and use the DELETE method of the resource to delete a record.

**Example for deleting an Account record**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/001D000000INjVe
   -H "Authorization: Bearer token" -X DELETE

```
**Example request body**
None needed

**Example response body**
None returned


-----

#### Get Field Values from a Standard Object Record

You use the GET method of the sObject Rows resource to retrieve field values from a record.

You can specify the fields you want to retrieve with the optional fields parameter. If you specify fields that don’t exist or are inaccessible
to you by field-level security, a 400 error response is returned.

If you don’t use the `fields` parameter, the request retrieves all standard and custom fields from the record. These retrieved fields are
the same as the fields returned by an sObject Describe request for the object. Fields that are inaccessible to you by field-level security
are not returned in the response body.

In the following example, the Account Number and Billing Postal Code are retrieved from an Account.

**Example for retrieving values from fields on an Account object**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/001D000000INjVe
  ?fields=AccountNumber,BillingPostalCode -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example response body**
```
  {
    "AccountNumber" : "CD656092",
    "BillingPostalCode" : "27215",
  }

#### Get Field Values from an External Object Record by Using the Salesforce ID

```
You use the sObject Rows resource to retrieve field values from a record. Specify the fields you want to retrieve in the fields parameter
and use the GET method of the resource.

In the following example, the `Country__c` custom field is retrieved from an external object that’s associated with a
non-high-data-volume external data source.

**Example for retrieving values from fields on the Customer external object**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Customer__x/x01D0000000002RIAQ?fields=Country__c
   -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example response body**


-----

External ID Standard Field

#### Get Field Values from an External Object Record by Using the External ID Standard Field

You use the sObject Rows resource to retrieve field values from a record. Specify the fields you want to retrieve in the fields parameter
and use the GET method of the resource.

In the following example, the `Country__c` custom field is retrieved from an external object. Notice that the `id (CACTU) isn’t a`
Salesforce ID. Instead, it’s the External ID standard field of the external object.

**Example for retrieving values from fields on the Customer external object**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Customer__x/CACTU?fields=Country__c
   -H "Authorization: Bearer token"

```
**Example request body**
None required

**Example response body**
```
  {
   "attributes" : {
    "type" : "Customer__x",
    "url" : "/services/data/v62.0/sobjects/Customer__x/CACTU"
   },
   "Country__c" : "Argentina",
   "ExternalId" : "CACTU"
  }

#### Get a Record Using an External ID

```
You can use the GET method of the sObject Rows by External ID resource to get records with a specific external ID.

The following example assumes there is a Merchandise__c custom object with a MerchandiseExtID__c external ID field.

**Example usage for retrieving a Merchandise__c record using an external ID**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/MerchandiseExtID__c/123
   -H "Authorization: Bearer token"

```
**Example request body**
none required

**Example response body**


-----

#### Insert or Update (Upsert) a Record Using an External ID

You can use the sObject Rows by External ID resource to create records or update existing records (upsert) based on the value of a
specified external ID field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

**•** If the external ID isn’t matched, then a new record is created according to the request body. To prevent a new record from being
created, use the `updateOnly` parameter.

**•** If the external ID is matched one time, then the record is updated according to the request body.

**•** If the external ID is matched multiple times, then a 300 error is reported, and the record isn’t created or updated.

The following sections show you how to work with the external ID resource to retrieve records by external ID and upsert records.

##### Upserting New Records

This example uses the PATCH method to insert a new record. It assumes that an external ID field, “customExtIdField__c,” has been added
to Account. It also assumes that an Account record with a customExtIdField value of 11999 doesn’t exist.

**Example for upserting a record that doesn’t yet exist**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/customExtIdField__c/11999
  -H "Authorization: Bearer token" -H "Content-Type: application/json" -d @newrecord.json
   -X PATCH

```
If you want to update a record but not create it if it doesn't exist, add the `updateOnly` parameter to the URL. For example:
```
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/customExtIdField__c/11999?updateOnly=true

```
**Example JSON request body** `newrecord.json` **file**
```
  {
    "Name" : "California Wheat Corporation",
    "Type" : "New Customer"
  }

```
**Example JSON response**
The successful response is:


-----

The HTTP status code is 201 (Created).

Note: The `created` parameter is present in the response in API version 46.0 and later. It doesn't appear in earlier versions.

**Error responses**
Incorrect external ID field:
```
  {
    "message" : "The requested resource does not exist",
    "errorCode" : "NOT_FOUND"
  }

```
For more information, see Status Codes and Error Responses on page 16.

##### Inserting New Records Using Id as the External ID

This example uses the POST method as a special case to insert a record where the `Id` field is treated as the external ID. Because the
value of Id is null, it’s omitted from the request. This pattern is useful when you’re writing code to upsert multiple records by different
external IDs and you don’t want to request a separate resource. POST using `Id` is available in API version 37.0 and later.

**Example of inserting a record that doesn’t yet exist**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/Id -H
   "Authorization: Bearer token" -H "Content-Type: application/json" -d @newrecord.json
  -X POST

```
**Example JSON request body** `newrecord.json` **file**
```
  {
    "Name" : "California Wheat Corporation",
    "Type" : "New Customer"
  }

```
**Example JSON response**
The successful response is:
```
  {
    "id" : "001D000000Kv3g5IAB",
    "success" : true,
    "errors" : [ ],
    "created": true
  }

```
The HTTP status code is 201 (Created).

Note: The `created` parameter is present in the response in API version 46.0 and later. It doesn't appear in earlier versions.

##### Upserting Existing Records

This example uses the PATCH method to update an existing record. It assumes that an external ID field, “customExtIdField__c,” has been
added to Account and an Account record with a customExtIdField value of 11999 exists. The request uses updates.json to specify
the updated field values.


-----

**Example of upserting an existing record**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/customExtIdField__c/11999
   -H "Authorization: Bearer token" -H "Content-Type: application/json" -d @updates.json
   -X PATCH

```
**Example JSON request body** `updates.json` **file**
```
  {
    "BillingCity" : "San Francisco"
  }

```
**Example JSON response**
In API version 46.0 and later, the HTTP status code is 200 (OK) and the successful response is:
```
  {
    "id" : "001D000000Kv3g5IAB",
    "success" : true,
    "errors" : [ ],
    "created": false
  }

```
In API version 45.0 and earlier, the HTTP status code is 204 (No Content) and there isn’t a response body.

**Error responses**
If the external ID value isn't unique, an HTTP status code 300 is returned, plus a list of the records that matched the query. For more
information about errors, see Status Codes and Error Responses on page 16.

If the external ID field doesn't exist, an error message and code is returned:
```
  {
    "message" : "The requested resource does not exist",
    "errorCode" : "NOT_FOUND"
  }

##### Upserting Records and Associating with an External ID

```
If you have an object that references another object using a relationship, you can use REST API to both insert or update a record and
reference another object using an external ID.

The following example creates a record and associates it with a parent record via external ID. It assumes the following:

**•** A Merchandise__c custom object that has an external ID field named MerchandiseExtID__c.

**•** A Line_Item__c custom object that has an external ID field named LineItemExtID__c, and a relationship to Merchandise__c.

**•** A Merchandise__c record exists that has a MerchandiseExtID__c value of 123.

**•** A Line_Item__c record with a LineItemExtID__c value of 456 does not exist. This record gets created and related to the
Merchandise__c record.

**Example of upserting a record and referencing a related object**


-----

**Example JSON request body** `new.json` **file**
Notice that the related Merchandise__c record is referenced using the Merchandise__c’s external ID field.
```
  {
    "Name" : "LineItemCreatedViaExtID",
    "Merchandise__r" :
    {
      "MerchandiseExtID__c" : 123
    }
  }

```
**Example JSON response**
The successful response is:
```
  {
    "id" : "a02D0000006YUHrIAO",
    "errors" : [ ],
    "success" : true,
    "created": true
  }

```
The HTTP status code is 201 (Created).

Note: The `created` parameter is present in the response in API version 46.0 and later. It doesn't appear in earlier versions.

**Error responses**
If the external ID value isn't unique, an HTTP status code 300 is returned, plus a list of the records that matched the query. For more
information about errors, see Status Codes and Error Responses on page 16.

If the external ID field doesn't exist, an error message and code is returned:
```
  {
    "message" : "The requested resource does not exist",
    "errorCode" : "NOT_FOUND"
  }

```
You can also use this approach to update existing records. For example, if you created the Line_Item__c shown in the example above,
you can try to update the related Merchandise__c using another request.

**Example for updating a record**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Line_Item__c/LineItemExtID__c/456
   -H "Authorization: Bearer token" -H "Content-Type: application/json" -d @updates.json
   -X PATCH

```
**Example JSON request body** `updates.json` **file**
This assumes another Merchandise__c record exists with a MerchandiseExtID__c value of 333.


-----

**Example JSON response**
In API version 46.0 and later, the HTTP status code is 200 (OK) and the successful response is:
```
  {
    "id" : "001D000000Kv3g5IAB",
    "success" : true,
    "errors" : [ ],
    "created": false
  }

```
In API version 45.0 and earlier, the HTTP status code is 204 (No Content) and there isn’t a response body.

If the relationship type is master-detail and the relationship is set to not allow reparenting, and you try to update the parent external ID,
you get an HTTP status code 400 error with an error code of INVALID_FIELD_FOR_INSERT_UPDATE.

SEE ALSO:

sObject Rows by External ID

#### Traverse Relationships with Friendly URLs

You can traverse relationship fields in standard and custom objects by constructing friendly URLs using the sObject Relationship resource.
This approach allows you to directly access records associated by relationships. Using friendly URLs is an easier alternative to accessing
records by obtaining object IDs from relationship fields and then inspecting the associated object ID record.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Relationship names follow certain conventions that depend on the direction (parent to child, or child to parent) of the relationship and
[the name of the related object. The conventions are described in Understanding Relationship Names in the SOQL and SOSL Reference.](https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_understanding.htm)

There are limits to the number of relationship traversals you can make in a single REST API call. These limits are the same as the limits
[for SOQL, as described in Understanding Relationship Query Limitations in the SOQL and SOSL Reference. Keep the following limitations](https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_query_limits.htm)
in mind when traversing relationships.

**•** When specifying child-to-parent relationships, no more than five levels can be traversed. The following traverses two child-to-parent
relationships.
```
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/ChildOfChild__c/record
  id/Child__r/ParentOfChild__r

```
**•** When specifying parent-to-child relationships, no more than one level can be traversed. The following traverses one parent-to-child
relationship.


-----

##### Traversing Standard Objects

The standard object Contact contains a relationship field to the Account standard object. The following example retrieves the Account
record related to a Contact record.
```
curl
https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Contact/0035e00000PiemmAAB/Account
 -H "Authorization: Bearer token"

```
**Example request body for traversing a standard object relationship**
none required

**Example response body for traversing a standard object simple relationship**
```
  {
    "attributes": {
       "type": "Account",
       "url": "/services/data/v62.0/sobjects/Account/0015e00000TwULCAA3"
    },
    "Id": "0015e00000TwULCAA3",
    "IsDeleted": false,
    "Name": "relationshipAccountName",
    "PhotoUrl": "/services/images/photo/0015e00000TwULCAA3",
    "OwnerId": "0055e000003E8ooAAC",
    "CreatedDate": "2021-11-06T17:38:40.000+0000",
    "CreatedById": "0055e000003E8ooAAC",
    "LastModifiedDate": "2021-11-06T17:38:40.000+0000",
    "LastModifiedById": "0055e000003E8ooAAC",
    "SystemModstamp": "2021-11-06T17:38:40.000+0000",
    "LastActivityDate": null,
    "LastViewedDate": "2021-11-06T17:40:50.000+0000",
    "LastReferencedDate": "2021-11-06T17:40:50.000+0000"
  }

```
**Example of traversing a simple relationship**
This custom object named Merchandise__c contains a lookup relationship field to a child Distributor__c custom object. The following
example retrieves the Distributor__c record related to a Merchandise__c record.
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/a01D000000INjVe/Distributor__r
   -H "Authorization: Bearer token"

```
**Example request body for traversing a simple relationship**
none required

**Example response body for traversing a simple relationship**


-----

If no related record is associated with the relationship name, the REST API call fails, because the relationship can’t be traversed. Using
the previous example, if the Distributor__c field in the Merchandise__c record was set to `null, the GET call would return a 404 error`
response.

You can traverse multiple relationships within the same relationship hierarchy in a single REST API call as long as you don’t exceed the
relationship query limits. If a Line_Item__c custom object is the child in a relationship to a Merchandise__c custom object, and
Merchandise__c also has a child Distributor__c custom object, you can access the Distributor__c record starting from the Line_Item__c
record using something like the following.
```
curl
https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Line_Item__c/a02D0000006YL7XIAW/Merchandise__r/Distributor__r
 -H "Authorization: Bearer token"

```
Relationship traversal also supports PATCH and DELETE methods for relationships that resolve to a single record. Using the PATCH
method, you can update the related record.

**Example of using PATCH to update a relationship record**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/a01D000000INjVe/Distributor__r
   -H "Authorization: Bearer token" -d @update_info.json -X PATCH

```
**Example JSON request body for updating a relationship record contained in** `update_info.json`
```
  {
    "Location__c" : "New York"
  }

```
**Example response body for updating relationship record**
none returned

Finally, using the DELETE method, you can delete the related record.

**Example using DELETE to delete a relationship record**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/a01D000000INjVe/Distributor__r
   -H "Authorization: Bearer token" -X DELETE

```
**Example request body for deleting a relationship record**
none required

**Example response body for update relationship record**
none returned

##### Traversing Relationships with Multiple Records

You can traverse relationships with multiple records, and get a response that contains the set of records. For relationships that resolve
to multiple records, only GET methods are supported.


-----

**Example traversing a relationship with multiple records**
If we have a custom object named Merchandise__c that contains a master—detail relationship field to a Line_Item__c custom
object, the following example retrieves the set of Line_Item__c records related to a Merchandise__c record.
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/a01D000000INjVe/Line_Items__r
   -H "Authorization: Bearer token"

```
**Example request body for traversing a relationship with multiple records**
none required

**Example response body for traversing a relationship with multiple records**
For this example, two Line_Item__c records were retrieved.


-----

The serialized structure for the result data is the same format as result data from executing a SOQL query via REST API. See Query on
page 304 for more details on executing SOQL queries via REST API

If no related records are associated with the relationship name, the REST API call returns a 200 response with no record data in the
response body. This result is in contrast to the results when traversing an empty relationship to a single record, which returns a 404 error
response. This behavior is because the single record case resolves to a REST resource that can be used with PATCH or DELETE methods.
In contrast, the multiple record case can only be queried.

If an initial GET request for a relationship with multiple records returns only part of the results, the end of the response contains the field
```
nextRecordsUrl. For example, you could get a field like the following at the end of your response.
"nextRecordsUrl" : "/services/data/v62.0/query/01gD0000002HU6KIAW-2000"

```
You can request the next batch of records using the provided URL with your instance and session information, and repeat until all records
have been retrieved. These requests use `nextRecordsUrl` and don’t include any parameters. The final batch of records doesn’t
have a `nextRecordsUrl` field.

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
    "totalSize" : 3200,
    "records" : [...]
  }

##### Filtering Result Fields

```
When retrieving records via relationship traversals, you can optionally specify only a subset of the record fields be returned by using the
`fields` parameter. Multiple fields are separated by commas. The following example retrieves just the Location__c field from the
Distributor__c record associated with a Merchandise__c record:
```
curl
https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/a01D000000INjVe/Distributor__r?fields=Location__c
 -H "Authorization: Bearer token"

```
The JSON response data would look like the following:


-----

Similarly, for requests that result in multiple records, you can use a list of fields to specify the fields returned in the record set. For example,
assume you have a relationship that was associated with two Line_Item__c records. You want just the Name and Units_Sold__c fields
from those records. You could use the following call.
```
curl
https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/a01D000000INjVe/Line_Items__r?fields=Name,Units_Sold__c
 -H "Authorization: Bearer token"

```
The response data would look like the following.
```
{
   "done" : true,
   "totalSize" : 2,
   "records" :
   [
     {
        "attributes" :
        {
          "type" : "Line_Item__c",
          "url" : "/services/data/v62.0/sobjects/Line_Item__c/a02D0000006YL7XIAW"
        },
        "Name" : "LineItem1",
        "Units_Sold__c" : 10.0
     },
     {
        "attributes" :
        {
          "type" : "Line_Item__c",
          "url" : "/services/data/v62.0/sobjects/Line_Item__c/a02D0000006YL7YIAW"
        },
        "Name" : "LineItem2",
        "Units_Sold__c" : 8.0
     }
   ]
}

```
If any field listed in the fields parameter set isn’t visible to the active user, the REST API call fails. In the previous example, if the Units_Sold_c
field was hidden from the active user by field-level security, the call would return a 400 error response.

#### Get a List of Deleted Records Within a Given Timeframe

Use the sObject Get Deleted resource to get a list of deleted records for the specified object. Specify the date and time range within
which the records for the given object were deleted. Deleted records are written to a delete log (that is periodically purged), and will
be filtered out of most operations, such as sObject Rows or Query (although QueryAll will include deleted records in results).


-----

**Example usage for getting a list of Merchandise__c records that were deleted between May 5th, 2013 and May 10th, 2013**
```
  curl https://MyDomainName.my/services/data/v62.0/sobjects/Merchandise__c/deleted/
  ?start=2013-05-05T00%3A00%3A00%2B00%3A00&end=2013-05-10T00%3A00%3A00%2B00%3A00 -H
  "Authorization: Bearer token"

```
**Example request body**
None required

**JSON example response body**
```
  {
    "deletedRecords" :
    [
       {
         "id" : "a00D0000008pQRAIA2",
         "deletedDate" : "2013-05-07T22:07:19.000+0000"
       }
    ],
    "earliestDateAvailable" : "2013-05-03T15:57:00.000+0000",
    "latestDateCovered" : "2013-05-08T21:20:00.000+0000"
  }

```
**XML example response body**
```
  <?xml version="1.0" encoding="UTF-8"?>
  <Merchandise__c>
    <deletedRecords>
       <deletedDate>2013-05-07T22:07:19.000Z</deletedDate>
       <id>a00D0000008pQRAIA2</id>
    </deletedRecords>
    <earliestDateAvailable>2013-05-03T15:57:00.000Z</earliestDateAvailable>
    <latestDateCovered>2013-05-08T21:20:00.000Z</latestDateCovered>
  </Merchandise__c>

#### Get a List of Updated Records Within a Given Timeframe

```
Use the sObject Get Updated resource to get a list of updated (modified or added) records for the specified object. Specify the date and
time range within which the records for the given object were updated.

**Example usage for getting a list of Merchandise__c records that were updated between May 6th, 2013 and May 10th, 2013**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/updated/
  ?start=2013-05-06T00%3A00%3A00%2B00%3A00&end=2013-05-10T00%3A00%3A00%2B00%3A00 -H
  "Authorization: Bearer token"

```
**Example request body**
None required

**JSON example response body**


-----

**XML example response body**
```
  <?xml version="1.0" encoding="UTF-8"?>
  <Merchandise__c>
    <ids>a00D0000008pQR5IAM</ids>
    <ids>a00D0000008pQRGIA2</ids>
    <ids>a00D0000008pQRFIA2</ids>
    <latestDateCovered>2013-05-08T21:20:00.000Z</latestDateCovered>
  </Merchandise__c>
