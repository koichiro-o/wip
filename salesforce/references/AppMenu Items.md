### AppMenu Items

```
Accesses App Menu items from the Salesforce app dropdown menu. To retrieve a list of App Menu items, use the GET method. To retrieve
the headers returned by a request for App Menu items, use the HEAD method.

IN THIS SECTION:

Get AppMenu Items
Gets a list of the App Menu items in the Salesforce Lightning dropdown menu. This resource is available in REST API version 29.0
and later.


-----

Return Headers of App Menu Item Requests
Returns only the headers that are returned by a GET request for the Salesforce app dropdown menu items. Use this URI to see the
header values before you retrieve the content of the resource. This resource is available in REST API version 29.0 and later.

#### Get AppMenu Items

Gets a list of the App Menu items in the Salesforce Lightning dropdown menu. This resource is available in REST API version 29.0 and
later.

##### Syntax

**URI**
```
  /services/data/vXX.X/appMenu/AppSwitcher/

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
None

**Request parameters**
None required

##### Example

**Example Request**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/appMenu/AppSwitcher -H
  "Authorization: Bearer token"

#### Return Headers of App Menu Item Requests

```
Returns only the headers that are returned by a GET request for the Salesforce app dropdown menu items. Use this URI to see the header
values before you retrieve the content of the resource. This resource is available in REST API version 29.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/appMenu/AppSwitcher/

```
**Formats**
JSON, XML

**HTTP method**
HEAD


-----

**Authentication**
```
  Authorization: Bearer token

```
**Request body**
None

**Request parameters**
None required

##### Example

**Example Request**
```
  curl -X HEAD --head
  https://MyDomainName.my.salesforce.com/services/data/v62.0/appMenu/AppSwitcher -H
  "Authorization: Bearer token"
