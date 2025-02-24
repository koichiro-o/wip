### Get Knowledge Language Settings

Gets the existing Knowledge language settings, including the default knowledge language and a list of supported Knowledge language
information. This resource can be used in API version 31.0 and later.

Salesforce Knowledge must be enabled in your organization. It gets the Knowledge language settings, including the default knowledge
language and a list of supported Knowledge language information.

#### Syntax

**URI**
```
  /services/data/vXX.X/knowledgeManagement/settings

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request body**
None required

**Request parameters**
None


-----

#### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/knowledgeManagement/settings
   -H "Authorization: Bearer token"

```
**Example Response Body**
```
  {
    "defaultLanguage" : "en_US",
    "knowledgeEnabled" : true,
    "languages" : [ {
    "active" : true,
    "name" : "en_US"
    }, {
    "active" : true,
    "name" : "it"
    }, {
    "active" : true,
    "name" : "zh_CN"
    }, {
    "active" : true,
    "name" : "fr"
    } ]
  }
