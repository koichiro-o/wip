### Embedded Service Configuration Describe

```
Retrieves the values for your Embedded Service deployment configuration or the headers returned by a request.


-----

IN THIS SECTION:

Get Embedded Service Configuration
Get the values for your Embedded Service deployment configuration, including the branding colors, font, and site URL. This resource
is available in REST API version 45.0 and later.

Return Headers for Embedded Service Configuration
Returns only the headers from a GET request to the Embedded Service Configuration Describe resource. This gives you a chance to
see header values ahead of time before retrieving the content of the resource. You must be logged in to the account that owns the
EmbeddedServiceConfigDeveloperName you are querying. This resource is available in REST API version 45.0 and later.

#### Get Embedded Service Configuration

Get the values for your Embedded Service deployment configuration, including the branding colors, font, and site URL. This resource is
available in REST API version 45.0 and later.

You must be logged in to the account that owns the EmbeddedServiceConfigDeveloperName you are querying.

##### Syntax

**URI**
```
  /services/data/vXX.X/support/embeddedservice/configuration/embeddedServiceConfigDeveloperName

```
**Formats**
JSON

**HTTP method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/support/embeddedservice/configuration/TestOne
   -H "Authorization: Bearer token"

```
**Example Response Body**


-----

#### Return Headers for Embedded Service Configuration

Returns only the headers from a GET request to the Embedded Service Configuration Describe resource. This gives you a chance to see
header values ahead of time before retrieving the content of the resource. You must be logged in to the account that owns the
EmbeddedServiceConfigDeveloperName you are querying. This resource is available in REST API version 45.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/support/embeddedservice/configuration/embeddedServiceConfigDeveloperName

```

-----

**Formats**
JSON

**HTTP method**
HEAD

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None
