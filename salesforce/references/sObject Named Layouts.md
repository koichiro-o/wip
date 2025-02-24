### sObject Named Layouts

Retrieves information about alternate named layouts for a given object. This resource is available in REST API version 31.0 and later.

Use this resource to get information on a named layout for a given object. You must provide a valid named layout name as part of the
resource URI.

To get a list of named layouts for a given object, use the sObject Describe resource and look for the “namedLayoutInfos” field in the
response body.

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/describe/namedLayouts/layoutName

```
**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request body**
None

#### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/User/describe/namedLayouts/UserAlt
   -H "Authorization: Bearer token"

```
SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)
