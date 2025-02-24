### sObject Specific Quick Actions

```
Access a specific action for an object. By using the POST method with this resource, you can create records using an object’s quick actions.

When working with actions, also refer to Quick Actions.

IN THIS SECTION:

Get Specific sObject Quick Actions
Gets a specific action for an object, as well as the action’s details. This resource is available in REST API version 28.0 and later.

Create Records Using Specific sObject Quick Actions
Creates a record via the specified quick action based on the field values included in the request body. This resource is available in
REST API version 28.0 and later.

Return Headers Using Specific sObject Quick Actions
Returns only the headers that are returned by sending a GET request to the sObject Quick Actions resource. This gives you a chance
to see the header values before retrieving the content of the resource. This resource is available in REST API version 28.0 and later.

#### Get Specific sObject Quick Actions

Gets a specific action for an object, as well as the action’s details. This resource is available in REST API version 28.0 and later.

When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/actionName

```
**Formats**
JSON, XML


-----

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/quickActions/CreateContact
   -H "Authorization: Bearer token"

#### Create Records Using Specific sObject Quick Actions

```
Creates a record via the specified quick action based on the field values included in the request body. This resource is available in REST
API version 28.0 and later.

When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/actionName

```
**Formats**
JSON, XML

**HTTP Method**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

##### Example

**Example Request**
```
  curl -X POST
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/quickActions/CreateContact
  -H 'Authorization: Bearer token -H "Content-Type: application/json" -d @newcontact.json'

```
**Example Request Body**


-----

#### Return Headers Using Specific sObject Quick Actions

Returns only the headers that are returned by sending a GET request to the sObject Quick Actions resource. This gives you a chance to
see the header values before retrieving the content of the resource. This resource is available in REST API version 28.0 and later.

When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/actionName

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/quickActions/CreateContact
   -H "Authorization: Bearer token"
