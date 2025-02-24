### Working with Object Metadata

The examples in this section use REST API resources to retrieve object metadata information. For modifying or creating object metadata
[information, see the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_meta.meta/api_meta/)

IN THIS SECTION:

Get Metadata for an Object
Use the sObject Basic Information resource to get metadata for an object.

Get Field and Other Metadata for an Object
Use the sObject Describe resource to retrieve all the metadata for an object, including information about each field, URLs, and child
relationships.

Get Object Metadata Changes
Use the sObject Describe resource and the `If-Modified-Since` HTTP header to determine if object metadata has changed.


-----

#### Get Metadata for an Object

Use the sObject Basic Information resource to get metadata for an object.

**Example for getting Account metadata**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/ -H
  "Authorization: Bearer token"

```
**Example request body for getting Account metadata**
none required

**Example response body for getting Account metadata**
```
  {
   "objectDescribe" :
   {
    "name" : "Account",
    "updateable" : true,
    "label" : "Account",
    "keyPrefix" : "001",
    ...
    "replicateable" : true,
    "retrieveable" : true,
    "undeletable" : true,
    "triggerable" : true
   },
   "recentItems" :
   [
    {
      "attributes" :
      {
       "type" : "Account",
       "url" : "/services/data/v62.0/sobjects/Account/001D000000INjVeIAL"
      },
      "Id" : "001D000000INjVeIAL",
      "Name" : "asdasdasd"
    },
    ...
   ]
  }

```
To get a complete description of an object, including field names and their metadata, see Get a List of Objects.

#### Get Field and Other Metadata for an Object

Use the sObject Describe resource to retrieve all the metadata for an object, including information about each field, URLs, and child
relationships.


-----

**Example**
```
  curl
  https://MyDomainName
  -H "Authorization: Bearer

```
**Example request body**
none required

**Example response body**


-----

[For more information about the items in the request body, see DescribesObjectResult in the SOAP API Developers Guide.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm)

#### Get Object Metadata Changes

Use the sObject Describe resource and the `If-Modified-Since` HTTP header to determine if object metadata has changed.

You can include the `If-Modified-Since` header with a date in `EEE, dd MMM yyyy HH:mm:ss z` format when you use
the sObject Describe resource. If you do, response metadata will only be returned if the object metadata has changed since the provided
date. If the metadata has not been modified since the provided date, a 304 Not Modified status code is returned, with no response
body.

The following example assumes that no changes, such as new custom fields, have been made to the Merchandise__c object after July
3rd, 2013.

**Example sObject Describe request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/describe
   -H "Authorization: Bearer token" -H "If-Modified-Since: Wed, 3 Jul 2013 19:43:31 GMT"

```
**Example response body**
No response body returned

**Example response status code**
```
  HTTP/1.1 304 Not Modified
  Date: Fri, 12 Jul 2013 05:03:24 GMT

```
If there were changes to Merchandise__c made after July 3rd, 2013, the response body would contain the metadata for Merchandise__c.
See Get Field and Other Metadata for an Object for an example.
