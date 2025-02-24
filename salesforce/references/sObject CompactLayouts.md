### sObject CompactLayouts

```
Retrieve a list of compact layouts for a specific object. This resource is available in REST API version 29.0 and later.

IN THIS SECTION:

Get Compact Layouts Using sObject CompactLayouts
Retrieves a list of compact layouts for a specific object. This resource is available in REST API version 29.0 and later.

Return Headers Using sObject CompactLayouts
Returns only the headers that are returned by a GET request to the sObject CompactLayouts resource. This gives you a chance to
see header values ahead of time before retrieving the content of the resource. This resource is available in REST API version 29.0 and
later.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Get Compact Layouts Using sObject CompactLayouts

Retrieves a list of compact layouts for a specific object. This resource is available in REST API version 29.0 and later.


-----

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/describe/compactLayouts/

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/describe/compactLayouts
   -H "Authorization: Bearer token"

```
**Example Response Body**
This sample JSON response is for compact layouts created on the Account object. In this example, only one custom compact layout
was created for Account. The custom compact layout is assigned as the primary compact layout for the object, and it contains two
fields: `Account Name` and `Phone.`


-----

-----

-----

-----

If you haven’t defined any compact layouts for an object, the `compactLayoutId` returns as `Null.`


-----

#### Return Headers Using sObject CompactLayouts

Returns only the headers that are returned by a GET request to the sObject CompactLayouts resource. This gives you a chance to see
header values ahead of time before retrieving the content of the resource. This resource is available in REST API version 29.0 and later.

##### Syntax

**URI**
For a compact layout description for a specific object, use
```
  /services/data/vXX.X/sobjects/sObject/describe/compactLayouts/

```
**Formats**
JSON, XML

**HTTP methods**
HEAD

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required

##### Example

**Example Request**
```
  curl -X HEAD --head
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/describe/compactLayouts
   -H "Authorization: Bearer token"
