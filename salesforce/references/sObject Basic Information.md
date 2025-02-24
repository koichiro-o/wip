### sObject Basic Information

Retrieves basic metadata for a specified object, or creates a new record for the specified object.

For example, this resource can be used to retrieve the metadata for the Account object using the GET method, or create a new Account
object using the POST method.

IN THIS SECTION:

Get Object Metadata Using sObject Basic Information
Gets basic metadata for a specified object, including some object properties, recent items, and URIs for other resources related to
the object.

Create Records Using sObject Basic Information
Creates a new record for a specified object based on field values in the request body.

#### Get Object Metadata Using sObject Basic Information

Gets basic metadata for a specified object, including some object properties, recent items, and URIs for other resources related to the
object.

To retrieve the complete metadata for an object, use the sObject Describe resource.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/

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


-----

##### Example

For an example of retrieving metadata for an object, see Get Metadata for an Object on page 42.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Create Records Using sObject Basic Information

Creates a new record for a specified object based on field values in the request body.

You must specify values for required fields in the request body. Specifying values for other fields is optional.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/

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

```
Content-Type

```

An optional header, specifying the format for the request and response. Possible choices
are:

**•** `Content-Type: application/json`

**•** `Content-Type: application/xml`

```
  sObject

```
The name of the object. For example, `Account.`

A required path parameter.

##### Example

**•** For an example of creating a new record using POST, see Create a Record on page 45.

**•** For an example of create a new record along with providing blob data for the record, see Insert or Update Blob Data on page 75.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)


-----
