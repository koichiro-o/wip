### Get AppMenu Types

Gets a list of App Menu types in the Salesforce app dropdown menu. This resource is available in REST API version 29.0 and later.

#### Syntax

**URI**
```
  /services/data/vXX.X/appMenu/

```
**Formats**
JSON, XML

**HTTP method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request body**
None

**Request parameters**
None required

#### Example

**Example Request**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/appMenu/ -H
  "Authorization: Bearer token"
