### sObject Describe

Completely describes the individual metadata at all levels for the specified object. For example, this can be used to retrieve the fields,
URLs, and child relationships for the Account object.

[For more information about the metadata that is retrieved, see DescribesObjectResult in the SOAP API Developers Guide.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm)

You can use the `If-Modified-Since` or `If-Unmodified-Since` header with this resource. When using the
`If-Modified-Since` header, if no available object’s metadata has changed since the provided date, a `304 Not Modified`
status code is returned with no response body.

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/describe/

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

**Parameter** **Description**
```
  sObject

```
The name of the object. For example, `Account.`

A required path parameter.

```
If-Modified-Since
If-Unmodified-Since

```

An optional header specifying a date and time. The request returns records that have
been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z. For example:`
```
If-Modified-Since: Mon, 30 Nov 2020 08:34:54 MST.

```
An optional header specifying a date and time. The request returns records that have
not been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z. For example:`
```
If-Unmodified-Since: Mon, 30 Nov 2020 08:34:54 MST.

```

-----

#### Example

See Get Field and Other Metadata for an Object. For an example that uses the `If-Modified-Since` HTTP header, see Get Object
Metadata Changes.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

Conditional Request Headers
