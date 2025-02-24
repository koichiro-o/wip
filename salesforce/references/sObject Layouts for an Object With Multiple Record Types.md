### sObject Layouts for an Object With Multiple Record Types

```
Retrieves lists of page layouts and their descriptions for objects that have more than one record type defined.

#### Get Layouts and Descriptions for an Object With Multiple Record Types

Retrieves lists of layouts and their descriptions.

For a layout description for objects that have more than one record type defined, the `recordTypeId` can be obtained from the
result from `/services/data/vXX.X/sobjects/sObject/describe/layouts/`

A GET request for objects that have more than one record type defined returns `null` for the layouts section of the response.


-----

Record Types


##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/describe/layouts/recordTypeId

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
None required

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Chocolate__c
   -H "Authorization: Bearer token"

```
**Example Response Body**


-----

Types


#### Return Layout Headers for an Object With Multiple Record Types

Returns only the headers that are returned by a GET request to sObject Layouts resources. This gives you a chance to see header values
ahead of time before retrieving the content of the resource.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/describe/layouts/recordTypeId

```
**Formats**
JSON, XML

**HTTP Method**
HEAD

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

##### Example

**Example Request**
```
  curl -X HEAD
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Chocolate__c/describe/layouts/0125c000000oIN9AAM
   -H "Authorization: Bearer token"
