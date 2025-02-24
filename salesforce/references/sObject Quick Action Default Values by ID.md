### sObject Quick Action Default Values by ID

```
Evaluates the default values for a specific action on an object. Responses include default field values.

When working with actions, also refer to Quick Actions.

IN THIS SECTION:

Get sObject Quick Action Default Values by ID
Returns the default values for an action specific to the `context_id object. This resource is available in REST API version 29.0 and`
later.

Return Headers Using sObject Quick Action Default Values by ID
Returns only the headers that are returned by sending a GET request to the sObject Quick Actions resource. This gives you a chance
to see the header values before retrieving the content of the resource. This resource is available in REST API version 29.0 and later.

#### Get sObject Quick Action Default Values by ID

Returns the default values for an action specific to the `context_id object. This resource is available in REST API version 29.0 and`
later.


-----

by ID


In API version 28.0, to evaluate the default values for an action, use
```
/services/data/vXX.X/sobjects/sObject/quickActions/action_name/defaultValues/parent_id.

```
When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/actionName/defaultValues/contextId

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/quickActions/CreateContact/defaultValues/001D000000JRWBd
   -H "Authorization: Bearer token"

#### Return Headers Using sObject Quick Action Default Values by ID

```
Returns only the headers that are returned by sending a GET request to the sObject Quick Actions resource. This gives you a chance to
see the header values before retrieving the content of the resource. This resource is available in REST API version 29.0 and later.

In API version 28.0, to evaluate the default values for an action, use
```
/services/data/vXX.X/sobjects/sObject/quickActions/action_name/defaultValues/parent_id.

```
When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/actionName/defaultValues/contextId

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
  curl -X HEAD --head
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/quickActions/CreateContact/defaultValues/001D000000JRWBd
   -H "Authorization: Bearer token"
