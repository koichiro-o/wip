### sObject Rows

Accesses records based on a specified object and record ID. Retrieves, updates, or deletes records based on the HTTP method. Use the
GET method to retrieve records or specific field values, the DELETE method to delete records, or the PATCH method to update records.

To create new records, use the sObject Basic Information or sObject Rows by External ID resources.

IN THIS SECTION:

Get Records Using sObject Rows
Gets a record based on the specified object and record ID. The fields and field values of the record are returned in the response body.
This resource can be used with external objects in API version 32.0 and later.


-----

Update Records Using sObject Rows
Updates a record based on the specified object and record ID. Field values provided in the request body replace the existing values
in the record. This resource can be used with external objects in API version 32.0 and later.

Delete Records Using sObject Rows
Deletes records based on the specified object and record ID. This resource can be used with external objects in API version 32.0 and
later.

#### Get Records Using sObject Rows

Gets a record based on the specified object and record ID. The fields and field values of the record are returned in the response body.
This resource can be used with external objects in API version 32.0 and later.

External objects that are associated with non-high-data-volume external data sources use the 18-character Salesforce ID for the `id.`
Otherwise, external objects use the External ID standard field of the external object for the id.

[For information about the items in the response body, see DescribeSObjectResult in the SOAP API Developer’s Guide.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm)

If the object is an Account object, the response also contains an ETag header. For example: `ETag:`
`"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip"` This ETag can be used with the `If-Match` and
`If-None-Match` headers. For more information, see Conditional Request Headers.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/id/

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
The identifier of the object. For example, `001R0000005hDFYIA2.`

```
fields

```

A comma-delimited list of fields specifying the fields and values returned in the response
body. For example,
```
?fields=name,description,numberofemployees,industry.

```

-----

```
  If-Match
  If-None-Match
  If-Modified-Since
  If-Unmodified-Since

##### Example

```

An optional header specifying a comma-delimited list of one or more ETags. This only
has an effect when used with Account objects. The request is only processed if the
Account’s ETag matches one of the ETags in the list.

For example: `If-Match:`
```
"94C83JSreaVMGpL+lUzv8Dr3inI0kCvuKATVJcTuApA=--gzip",
"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip".

```
An optional header specifying a comma-delimited list of one or more ETags. This only
has an effect when used with Account objects. The request is only processed if the
Account’s ETag does not match one of the ETags in the list.

For example: `If-None-Match:`
```
"94C83JSreaVMGpL+lUzv8Dr3inI0kCvuKATVJcTuApA=--gzip",
"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip".

```
An optional header specifying a date and time. The request returns records that have
been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z`

For example: `If-Modified-Since: Mon, 30 Nov 2020 08:34:54`
```
MST.

```
An optional header specifying a date and time. The request returns records that have
not been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z`

For example: If-Unmodified-Since: Mon, 30 Nov 2020 08:34:54
```
MST.

```

For examples of retrieving records, see Get Field Values from a Standard Object Record.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Update Records Using sObject Rows

Updates a record based on the specified object and record ID. Field values provided in the request body replace the existing values in
the record. This resource can be used with external objects in API version 32.0 and later.

External objects that are associated with non-high-data-volume external data sources use the 18-character Salesforce ID for the `id.`
Otherwise, external objects use the External ID standard field of the external object for the id.

[For information about the items in the response body, see DescribeSObjectResult in the SOAP API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm)


-----

If the object is an Account object, the response also contains an ETag header. For example: `ETag:`
`"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip"` This ETag can be used with the `If-Match` and
`If-None-Match` headers. For more information, see Conditional Request Headers.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/id/

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
Content-Type

```

An optional header that specifies the format for the request and response. The possible
header values are:

**•** `Content-Type: application/json`

**•** `Content-Type: application/xml`

```
sObject

```
The name of the object. For example, `Account` and `CustomObject__c.`
```
id

```
The identifier of the object. For example, `001R0000005hDFYIA2.`

```
If-Match
If-None-Match
If-Modified-Since

```

An optional header specifying a comma-delimited list of one or more ETags. This only
has an effect when used with Account objects. The request is only processed if the
Account’s ETag matches one of the ETags in the list.

For example: `If-Match:`
```
"94C83JSreaVMGpL+lUzv8Dr3inI0kCvuKATVJcTuApA=--gzip",
"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip".

```
An optional header specifying a comma-delimited list of one or more ETags. This only
has an effect when used with Account objects. The request is only processed if the
Account’s ETag does not match one of the ETags in the list.

For example: `If-None-Match:`
```
"94C83JSreaVMGpL+lUzv8Dr3inI0kCvuKATVJcTuApA=--gzip",
"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip".

```
An optional header specifying a date and time. The request returns records that have
been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z`


-----

```
  If-Unmodified-Since

##### Example

```

For example: `If-Modified-Since: Mon, 30 Nov 2020 08:34:54`
```
MST.

```
An optional header specifying a date and time. The request returns records that have
not been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z`

For example: If-Unmodified-Since: Mon, 30 Nov 2020 08:34:54
```
MST.

```

For an example of updating a record using PATCH, see Update a Record.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

Conditional Request Headers

#### Delete Records Using sObject Rows

Deletes records based on the specified object and record ID. This resource can be used with external objects in API version 32.0 and
later.

External objects that are associated with non-high-data-volume external data sources use the 18-character Salesforce ID for the `id.`
Otherwise, external objects use the External ID standard field of the external object for the id.

If the object is an Account object, the response also contains an ETag header. For example: `ETag:`
`"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip"` This ETag can be used with the `If-Match` and
`If-None-Match` headers. For more information, see Conditional Request Headers.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/id/

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
The name of the object. For example, `Account.`


-----

```
id

```
The identifier of the record. For example, `001R0000005hDFYIA2.`

```
  If-Match
  If-None-Match
  If-Modified-Since
  If-Unmodified-Since

##### Example

```

An optional header specifying a comma-delimited list of one or more ETags. This only
has an effect when used with Account objects. The request is only processed if the
Account’s ETag matches one of the ETags in the list.

For example: `If-Match:`
```
"94C83JSreaVMGpL+lUzv8Dr3inI0kCvuKATVJcTuApA=--gzip",
"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip".

```
An optional header specifying a comma-delimited list of one or more ETags. This only
has an effect when used with Account objects. The request is only processed if the
Account’s ETag does not match one of the ETags in the list.

For example: `If-None-Match:`
```
"94C83JSreaVMGpL+lUzv8Dr3inI0kCvuKATVJcTuApA=--gzip",
"ddpAdaTHz+GcV35e7NLJ9iKD3XXVqAzXT1Sl2ykkP7g=--gzip".

```
An optional header specifying a date and time. The request returns records that have
been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z`

For example: `If-Modified-Since: Mon, 30 Nov 2020 08:34:54`
```
MST.

```
An optional header specifying a date and time. The request returns records that have
not been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z`

For example: If-Unmodified-Since: Mon, 30 Nov 2020 08:34:54
```
MST.

```

For an example of deleting a record using DELETE, see Delete a Record.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)
