### Tabs

Returns a list of all tabs—including Lightning page tabs—available to the current user, regardless of whether the user has chosen to
hide tabs via the All Tabs (+) tab customization feature. This resource is available in REST API version 31.0 and later.

IN THIS SECTION:

Get Tabs
Gets a list of all tabs—including Lightning page tabs—available to the current user, regardless of whether the user has chosen to
hide tabs via the All Tabs (+) tab customization feature. This resource is available in REST API version 31.0 and later.

Return Headers Using Tabs
Returns only the headers that are returned by a GET request to Tabs resources. This gives you a chance to see header values before
retrieving the content of the resource. This resource is available in REST API version 31.0 and later.

#### Get Tabs

Gets a list of all tabs—including Lightning page tabs—available to the current user, regardless of whether the user has chosen to hide
tabs via the All Tabs (+) tab customization feature. This resource is available in REST API version 31.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/tabs/

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
None

##### Example

**Example Request**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/tabs -H "Authentication:
   Bearer token"

```
**Example Response Body**
This is a partial code sample, representing the Accounts tab.


-----

-----

#### Return Headers Using Tabs

Returns only the headers that are returned by a GET request to Tabs resources. This gives you a chance to see header values before
retrieving the content of the resource. This resource is available in REST API version 31.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/tabs/

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
None

##### Example

**Return headers of request for all tabs**
```
  curl -X HEAD --head https://MyDomainName.my.salesforce.com/services/data/v62.0/tabs -H
   "Authorization: Bearer token"
