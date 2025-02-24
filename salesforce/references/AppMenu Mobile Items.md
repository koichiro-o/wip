### AppMenu Mobile Items

```
Accesses App Menu items from the Salesforce mobile app for Android and iOS and the mobile web navigation menu.

IN THIS SECTION:

Get AppMenu Mobile Items
Gets a list of the App Menu items in the Salesforce mobile app for Android and iOS and the mobile web navigation menu. This
resource is available in REST API version 29.0 and later.

Return Headers of AppMenu Mobile Item Requests
Returns only the headers that are returned by a GET request to the Salesforce mobile app for Android and iOS and the mobile web
navigation menu. Use this URI to see the header values before you retrieve the content of the resource. This resource is available in
REST API version 29.0 and later.

#### Get AppMenu Mobile Items

Gets a list of the App Menu items in the Salesforce mobile app for Android and iOS and the mobile web navigation menu. This resource
is available in REST API version 29.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/appMenu/Salesforce1/

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer token

```

-----

**Request body**
None

**Request parameters**
None required

##### Example

**Example Request**
```
  curl https://
  -H "Authorization: Bearer

```
**Example Response Body**


-----

-----

#### Return Headers of AppMenu Mobile Item Requests

Returns only the headers that are returned by a GET request to the Salesforce mobile app for Android and iOS and the mobile web
navigation menu. Use this URI to see the header values before you retrieve the content of the resource. This resource is available in REST
API version 29.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/appMenu/Salesforce1/

```
**Formats**
JSON, XML

**HTTP methods**
HEAD

**Authentication**
```
  Authorization: Bearer token

```
**Request body**
None

**Request parameters**
None required


-----

##### Example

**Example Request**
```
  curl -X HEAD --head
  https://MyDomainName.my.salesforce.com/services/data/v62.0/appMenu/Salesforce1 -H
  "Authorization: Bearer token"
