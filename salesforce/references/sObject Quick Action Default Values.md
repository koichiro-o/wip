### sObject Quick Action Default Values

```
Retrieves the default values, including default field values, for a specific action on an object.

When working with actions, also refer to Quick Actions.

IN THIS SECTION:

Get sObject Quick Action Default Values
Returns a specific action’s default values, including field values. This resource is available in REST API version 28.0 and later.

Return Headers Using sObject Quick Action Default Values
Returns only the headers that are returned by sending a GET request to the sObject Quick Actions resource. This gives you a chance
to see the header values before retrieving the content of the resource. This resource is available in REST API version 28.0 and later.

#### Get sObject Quick Action Default Values

Returns a specific action’s default values, including field values. This resource is available in REST API version 28.0 and later.

When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/actionName/defaultValues/

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


-----

#### Return Headers Using sObject Quick Action Default Values

Returns only the headers that are returned by sending a GET request to the sObject Quick Actions resource. This gives you a chance to
see the header values before retrieving the content of the resource. This resource is available in REST API version 28.0 and later.

When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/actionName/defaultValues/

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/quickActions/CreateContact/defaultValues/
   -H "Authorization: Bearer token"
