### sObject Quick Actions

Access an object’s actions and the action details. This resource is available in REST API version 28.0 and later.

When working with actions, also refer to Quick Actions.

IN THIS SECTION:

Get sObject Quick Actions
Returns a specific object’s actions as well as global actions. This resource is available in REST API version 28.0 and later.


-----

Return Headers Using sObject Quick Actions
Returns only the headers that are returned by sending a GET request to the sObject Quick Actions resource. This gives you a chance
to see the header values before retrieving the content of the resource. This resource is available in REST API version 28.0 and later.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Get sObject Quick Actions

Returns a specific object’s actions as well as global actions. This resource is available in REST API version 28.0 and later.

This resource returns all actions—both global and standard—in addition to the ones requested.

When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/quickActions/
   -H "Authorization: Bearer token"

#### Return Headers Using sObject Quick Actions

```
Returns only the headers that are returned by sending a GET request to the sObject Quick Actions resource. This gives you a chance to
see the header values before retrieving the content of the resource. This resource is available in REST API version 28.0 and later.

This resource returns all actions—both global and standard—in addition to the ones requested.

When working with actions, also refer to Quick Actions.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/quickActions/

```

-----

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
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/quickActions/
   -H "Authorization: Bearer token"
