### sObject Rows by External ID

Creates, retrieves, upserts, or deletes records based on the value of a specified external ID field. By using the PATCH method with this
resource, you can send upsert requests to Salesforce.


-----

IN THIS SECTION:

Get Records Using sObject Rows by External ID
Retrieves a record based on the value of the specified external ID field.

Create Records Using sObject Rows by External ID
Creates a new record based on the field values included in the request body. This resource does not require the use of an external
ID field.

Upsert Records Using sObject Rows by External ID
Upserts a record based on the value of the specified external ID field. Based on whether the value of the external ID exists, the request
either creates a record or updates an existing one.

Delete Records Using sObject Rows by External ID
Deletes a record based on the value of the specified external ID field.

Return Headers Using sObject Rows by External ID
Returns only the headers that are returned by sending a GET request to the sObject Rows by External ID resource. This gives you a
chance to see returned header values of the GET request before retrieving the content itself.

#### Get Records Using sObject Rows by External ID

Retrieves a record based on the value of the specified external ID field.

Note: For security reasons, some Top Level Domains (TLD) can conflict with certain file format extensions. Adjust your
implementation to work around such cases.

For example, using an email address, such as `example@email.inc, as the External ID returns a “404 not found” error.`

There are several workarounds to handle conflicting TLDs.

**•** Use a different External ID field.

**•** Create a new External ID field that is the same as the email field and replace the "." with an "_" to handle this case.

**•** Run a query for emails ending in ".inc" to retrieve the record ID and use that for the upsert request.

**•** Use SOAP API instead of REST API for upsert requests.

**•** Accept the email as a query parameter instead of a path parameter by creating a custom Apex REST API. Use Apex to perform
the upsert request.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/fieldName/fieldValue

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
None


-----

##### Example

For an example of retrieving a record based on an external ID, see Get a Record Using an External ID on page 49.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Create Records Using sObject Rows by External ID

Creates a new record based on the field values included in the request body. This resource does not require the use of an external ID
field.

As a special case, in API version 37.0 and later, you can create a record with a POST request to
`/services/data/vXX.X/sobjects/sObjectName/Id. Because` `Id` has a `null` value, it is omitted from the request,
and the record is created according to the request body. Creating records with this resource is useful because you can use the same URI
in each POST request for each new record. In this case, you are not required to specify an external ID to create a record.

Note: Do not specify `Id` or an external ID field in the request body or an error is generated.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/Id

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
None

##### Example

**Example Request**
```
  curl -X POST
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Account/Id -H
  "Authorization: Bearer token" -H "Content-Type: application/json" -d "@newaccount.json"

```
SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Upsert Records Using sObject Rows by External ID

Upserts a record based on the value of the specified external ID field. Based on whether the value of the external ID exists, the request
either creates a record or updates an existing one.


-----

**•** If the external ID doesn't match an existing record, then a new record is created according to the request body. To prevent a new
record from being created, use the updateOnly parameter.

**•** If the external ID matches one existing record, then the existing record is updated according to the request body.

**•** If the external ID matches multiple existing records, then a 300 error is returned, and no records are created or updated.

If you’re upserting a record for an object that has a custom field with both the External ID and `Unique` attributes selected (a
unique index), you don’t need any special permissions. The Unique attribute prevents the creation of duplicates. If you’re upserting
a record for an object that has the `External ID` attribute selected but not the `Unique attribute selected (a non-unique index),`
your client application must have the permission “View All Data” to execute this call.

Note: For security reasons, some Top Level Domains (TLD) can conflict with certain file format extensions. Adjust your
implementation to work around such cases.

For example, using an email address, such as `example@email.inc, as the External ID returns a “404 not found” error.`

There are several workarounds to handle conflicting TLDs.

**•** Use a different External ID field.

**•** Create a new External ID field that is the same as the email field and replace the "." with an "_" to handle this case.

**•** Run a query for emails ending in ".inc" to retrieve the record ID and use that for the upsert request.

**•** Use SOAP API instead of REST API for upsert requests.

**•** Accept the email as a query parameter instead of a path parameter by creating a custom Apex REST API. Use Apex to perform
the upsert request.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/fieldName/fieldValue

```
**Formats**
JSON, XML

**HTTP Method**
PATCH

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

```
updateOnly

```

An optional parameter that prevents a new record from being created. Forces the
upsert to behave like an update when updateOnly=true is used.


-----

##### Example

For examples of creating and updating records based on external IDs, see Insert or Update (Upsert) a Record Using an External ID on
page 50.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Delete Records Using sObject Rows by External ID

Deletes a record based on the value of the specified external ID field.

Note: For security reasons, some Top Level Domains (TLD) can conflict with certain file format extensions. Adjust your
implementation to work around such cases.

For example, using an email address, such as `example@email.inc, as the External ID returns a “404 not found” error.`

There are several workarounds to handle conflicting TLDs.

**•** Use a different External ID field.

**•** Create a new External ID field that is the same as the email field and replace the "." with an "_" to handle this case.

**•** Run a query for emails ending in ".inc" to retrieve the record ID and use that for the upsert request.

**•** Use SOAP API instead of REST API for upsert requests.

**•** Accept the email as a query parameter instead of a path parameter by creating a custom Apex REST API. Use Apex to perform
the upsert request.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/fieldName/fieldValue

```
**Formats**
JSON, XML

**HTTP Method**
DELETE

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Return Headers Using sObject Rows by External ID

Returns only the headers that are returned by sending a GET request to the sObject Rows by External ID resource. This gives you a chance
to see returned header values of the GET request before retrieving the content itself.


-----

Note: For security reasons, some Top Level Domains (TLD) can conflict with certain file format extensions. Adjust your
implementation to work around such cases.

For example, using an email address, such as `example@email.inc, as the External ID returns a “404 not found” error.`

There are several workarounds to handle conflicting TLDs.

**•** Use a different External ID field.

**•** Create a new External ID field that is the same as the email field and replace the "." with an "_" to handle this case.

**•** Run a query for emails ending in ".inc" to retrieve the record ID and use that for the upsert request.

**•** Use SOAP API instead of REST API for upsert requests.

**•** Accept the email as a query parameter instead of a path parameter by creating a custom Apex REST API. Use Apex to perform
the upsert request.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/fieldName/fieldValue

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
None

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)
