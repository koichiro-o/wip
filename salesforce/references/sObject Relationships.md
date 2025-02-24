### sObject Relationships

Accesses records by traversing object relationships via friendly URLs. You can retrieve, update, or delete the record associated with the
traversed relationship field. If there are multiple related records, you can retrieve the complete set of associated records. This resource
is available in REST API version 36.0 and later.

IN THIS SECTION:

Get Records Using sObject Relationships
Gets a record based on the specified object, record ID, and relationship field. The fields and field values of the record are returned
in the response body. If there are multiple related records, you can retrieve the complete set of associated records.

Update Records Using sObject Relationships
Updates a parent record based on the specified object, record ID, and relationship field name. Field values provided in the request
body replace the existing values in the record. Only a child-to-parent relationship can be traversed when you update records.

Delete Records Using sObject Relationships
Deletes a parent record based on the specified object, record ID, and relationship field name. Only a child-to-parent relationship can
be traversed when you delete records.

#### Get Records Using sObject Relationships

Gets a record based on the specified object, record ID, and relationship field. The fields and field values of the record are returned in the
response body. If there are multiple related records, you can retrieve the complete set of associated records.

If there’s no record associated with a relationship field, a 404 error response is returned. If the relationship field normally resolves to
multiple records and no relationship set exists, a 200 response is returned. If the `fields parameter is used with fields that don’t exist`
or aren’t visible to the consumer by field-level security, a 400 error response is returned. For other error messages, see Status Codes and
Error Responses.


-----

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/id/relationshipFieldName

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
```
  id

```
The identifier of the record. For example, `001R0000005hDFYIA2.`
```
  relationshipFieldName

```
The name of the field that contains the relationship. For example, Opportunities.

```
  fields

##### Example

```

Optional for GET. A comma-delimited list of fields in the associated relationship record
returned in the response body. For example:


For examples of using sObject Relationships to access relationship fields, see Traverse Relationships with Friendly URLs.

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Merchandise__c/a01D000000INjVe/Distributor__r
   -H “Authorization: Bearer token”

```
**Example Response Body**
The response body is the contents of the record associated with the relationship field. Here’s an example of a request and JSON
response body for a simple relationship traversal that returns the Distributor__c record associated with a relationship field on custom
object Merchandise__c.


-----

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Update Records Using sObject Relationships

Updates a parent record based on the specified object, record ID, and relationship field name. Field values provided in the request body
replace the existing values in the record. Only a child-to-parent relationship can be traversed when you update records.

If the fields parameter is used with fields that don’t exist or aren’t visible to the consumer by field-level security, a 400 error response
is returned. For other error messages, see Status Codes and Error Responses.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/id/relationshipFieldName

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

**Parameter** **Description**
```
  sObject

```
The name of the object. For example, `Contact.`
```
  id

```
The identifier of the record. For example, `003R0000005hDFYIA2, the contact ID.`

```
  relationshipFieldName

##### Example

```

The name of the field that contains the relationship. For example, Account. Account
is the name of the relationship on the child Contact object.


For an example of updating a record using PATCH, see


-----

Update a Record.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Delete Records Using sObject Relationships

Deletes a parent record based on the specified object, record ID, and relationship field name. Only a child-to-parent relationship can be
traversed when you delete records.

If the fields parameter is used with fields that don’t exist or aren’t visible to the consumer by field-level security, a 400 error response
is returned. For other error messages, see Status Codes and Error Responses.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/id/relationshipFieldName

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

**Parameter** **Description**
```
  sObject

```
The name of the object. For example, `Contact.`
```
  id

```
The identifier of the record. For example, `003R0000005hDFYIA2, the contact ID.`

```
relationshipFieldName

```

The name of the field that contains the relationship. For example, Account. Account
is the name of the relationship on the child Contact object.


When you delete a parent record, it deletes all child records that have a master-detail relationship to the parent record.

##### Example

For examples of using sObject Relationships to delete a relationship record, see Traverse Relationships with Friendly URLs.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)


-----
