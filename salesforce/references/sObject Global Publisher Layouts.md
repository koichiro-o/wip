### sObject Global Publisher Layouts

```
Retrieves lists of global publisher layouts. Global publisher layouts customize the actions on global pages (like the Home page). In
Lightning Experience, these layouts populate the Global Actions menu.

IN THIS SECTION:

Get Global Publisher Layouts and Descriptions
Retrieves lists of global publisher layouts and their descriptions. Global publisher layouts customize the actions on global pages (like
the Home page). In Lightning Experience, these layouts populate the Global Actions menu.

Return Headers for All Global Publisher Layouts
Returns only the headers that are returned by a GET request to sObject Layouts resources. This gives you a chance to see header
values ahead of time before retrieving the content of the resource.

#### Get Global Publisher Layouts and Descriptions

Retrieves lists of global publisher layouts and their descriptions. Global publisher layouts customize the actions on global pages (like the
Home page). In Lightning Experience, these layouts populate the Global Actions menu.


-----

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/Global/describe/layouts/

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Global/describe/layouts/
   -H "Authorization: Bearer token"

```
**Example Response Body**


-----

#### Return Headers for All Global Publisher Layouts

Returns only the headers that are returned by a GET request to sObject Layouts resources. This gives you a chance to see header values
ahead of time before retrieving the content of the resource.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/Global/describe/layouts/

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


-----

##### Example

**Example Request**
```
  curl -X HEAD
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Global/describe/layouts/
   -H "Authorization: Bearer token"
