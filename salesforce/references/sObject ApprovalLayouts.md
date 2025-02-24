### sObject ApprovalLayouts

Retrieve a list of approval layouts for a specified object. This resource is available in REST API version 30.0 and later.

IN THIS SECTION:

Get Approval Layouts
Gets a list of approval layouts for a specified object. This resource is available in REST API version 30.0 and later.

Return Headers for Approval Layouts
Returns only the headers that are returned by a GET request to sObject ApprovalLayouts resources. This gives you a chance to see
header values before retrieving the content of the resource. This resource is available in REST API version 30.0 and later.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Get Approval Layouts

Gets a list of approval layouts for a specified object. This resource is available in REST API version 30.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/describe/approvalLayouts/

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


-----

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/describe/approvalLayouts/
   -H "Authorization: Bearer token"

```
**Example Response Body**
```
  {
   "approvalLayouts" : [ {
    "id" : "04aD00000008Py9IAE",
    "label" : "MyApprovalProcessName",
    "layoutItems" : [...],
    "name" : "MyApprovalProcessName"
    }, {
    "id" : "04aD00000008Q0KIAU",
    "label" : "Process1",
    "layoutItems" : [...],
    "name" : "Process1"
   } ]
  }

```
If you haven’t defined any approval layouts for an object, the response is {"approvalLayouts" : [ ]}.

#### Return Headers for Approval Layouts

Returns only the headers that are returned by a GET request to sObject ApprovalLayouts resources. This gives you a chance to see header
values before retrieving the content of the resource. This resource is available in REST API version 30.0 and later.

##### Syntax

**URI**
To return headers of a request for an approval layout description for a specified object, use
```
  /services/data/vXX.X/sobjects/sObject/describe/approvalLayouts/

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


-----

##### Example

**Example Request**
```
  curl -X HEAD --head
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/describe/approvalLayouts/
   -H "Authorization: Bearer token"
