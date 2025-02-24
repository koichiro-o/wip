### Quick Actions

Access global quick actions and object-specific quick actions. By using the POST method with this resource, you can create records using
a quick action. This resource is available in REST API version 28.0 and later.

When working with actions, also refer to sObject Quick Actions.

IN THIS SECTION:

Get Quick Actions
Gets a list of quick actions. This resource is available in REST API version 28.0 and later.

Create Records Using Quick Actions
Creates a record via a quick action. This resource is available in REST API version 28.0 and later.

Return Headers of Quick Actions
Returns only the headers that are returned by sending a GET request to the Quick Actions resource. This gives you a chance to see
the header values before retrieving the content of the resource. This resource is available in REST API version 28.0 and later.

#### Get Quick Actions

Gets a list of quick actions. This resource is available in REST API version 28.0 and later.

Add all required fields to an object before you create a quick action for that object. If you add a required field after creating a quick action,
the field doesn’t appear in the quick action’s describe results. Then, when the quick action runs, the field isn’t available and an error
occurs for the missing field. If you don’t want the required field to appear in the quick action’s layout, set a default value for the field.

When working with actions, also refer to sObject Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/quickActions/

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


-----

##### Example

**Example Request**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/quickActions/ -H
  "Authorization: Bearer token"

#### Create Records Using Quick Actions

```
Creates a record via a quick action. This resource is available in REST API version 28.0 and later.

Add all required fields to an object before you create a quick action for that object. If you add a required field after creating a quick action,
the field doesn’t appear in the quick action’s describe results. Then, when the quick action runs, the field isn’t available and an error
occurs for the missing field. If you don’t want the required field to appear in the quick action’s layout, set a default value for the field.

When working with actions, also refer to sObject Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/quickActions/

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/quickActions/CreateContact
  -H "Authorization: Bearer token" -H "Content-Type: application/json" -d
  @exampleRequestBody.json

```
**Example Request Body**


-----

#### Return Headers of Quick Actions

Returns only the headers that are returned by sending a GET request to the Quick Actions resource. This gives you a chance to see the
header values before retrieving the content of the resource. This resource is available in REST API version 28.0 and later.

Add all required fields to an object before you create a quick action for that object. If you add a required field after creating a quick action,
the field doesn’t appear in the quick action’s describe results. Then, when the quick action runs, the field isn’t available and an error
occurs for the missing field. If you don’t want the required field to appear in the quick action’s layout, set a default value for the field.

When working with actions, also refer to sObject Quick Actions.

**URI**
```
  /services/data/vXX.X/quickActions/

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/quickActions/ -H
  "Authorization: Bearer token"
