### sObject Layouts

```
Retrieves lists of page layouts and their descriptions. You can request information for all of a specific object’s layouts or for layouts
associated with a specified record type on a specific object.

IN THIS SECTION:

Get Layouts and Descriptions for a Specified Object
Retrieves lists of layouts and their descriptions for a single object.

Return Layout Headers for a Specified Object
Returns only the headers that are returned by a GET request to sObject Layouts resources. This gives you a chance to see header
values ahead of time before retrieving the content of the resource.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Get Layouts and Descriptions for a Specified Object

Retrieves lists of layouts and their descriptions for a single object.


-----

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/describe/layouts/

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Battle_Station__c/describe/layouts/
   -H "Authorization: Bearer token"

```
**Example Response Body**


-----

#### Return Layout Headers for a Specified Object

Returns only the headers that are returned by a GET request to sObject Layouts resources. This gives you a chance to see header values
ahead of time before retrieving the content of the resource.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/describe/layouts/

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
  curl -X HEAD --head
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Battle_Station__c/describe/layouts/
   -H "Authorization: Bearer token"
