### sObject Tree

```
Creates one or more sObject trees with root records of the specified type. An sObject tree is a collection of nested, parent-child records
with a single root record.

In the request data, you supply the record hierarchies, required and optional field values, each record’s type, and a reference ID for each
record. Objects are created in the same order that they’re listed in the request. Upon success, the response contains the IDs of the created
records. If an error occurs while creating a record, the entire request fails. In this case, the response contains only the reference ID of the
record that caused the error and the error information. The response bodies and HTTP statuses of the requests are returned in a single
response body. The entire request counts as a single call toward your API limits.

The request can contain the following:


-----

**•** Up to a total of 200 records across all trees

**•** Up to five records of different types

**•** sObject trees up to five levels deep

Because an sObject tree can contain a single record, you can use this resource to create up to 200 unrelated records of the same type.

When the request is processed and records are created, triggers, processes, and workflow rules fire separately for each of the following
groups of records.

**•** Root records across all sObject trees in the request

**•** All second-level records of the same type—for example, second-level Contacts across all sObject trees in the request

**•** All third-level records of the same type

**•** All fourth-level records of the same type

**•** All fifth-level records of the same type

#### Syntax

**URI**
```
  /services/data/vXX.X/composite/tree/sObjectName

```
**Formats**
JSON, XML

**HTTP method**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

**Request body**

sObject Tree Request Body on page 393

**Response body**

sObject Tree Response Body on page 396

#### Example

**•** For an example of creating unrelated records of the same type, see Create Multiple Records on page 106.

**•** For an example of creating nested records, see Create Nested Records on page 104.

#### sObject Tree Request Body

Describes a collection of sObject trees to create with the sObject Tree resource.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### sObject Tree Collection Input

The request body contains a `records` collection that includes sObject trees.


-----

**Properties**

**Name** **Type**

`records` sObject Tree Input[]

**Root XML Tag**
```
  <SObjectTreeRequest>

```
**JSON example**
```
  {
  "records" :[{
    "name" : "SampleAccount",
    "phone" : "1234567890",
    "website" : "www.salesforce.com",
    "numberOfEmployees" : "100",
    "industry" : "Banking",
    "Contacts" : {
      "records" : [{
       "lastname" : "Smith",
       "title" : "President",
       "email" : "sample@salesforce.com"
       },{
       "lastname" : "Evans",
       "title" : "Vice President",
       "email" : "sample@salesforce.com"
       }]
      }
    },{
    "name" : "SampleAccount2",
    "phone" : "1234567890",
    "website" : "www.salesforce2.com",
    "numberOfEmployees" : "100",
    "industry" : "Banking"
     }]
  }

```
**XML example**


Collection of record trees to create. Each tree’s Required
root record type must correspond to the sObject
specified in the sObject Tree URI.


-----

##### sObject Tree Input

An sObject tree is a recursive data structure that contains a root record, its data, and its child records represented as other sObject trees.

**Properties**

**Name** **Type** **Description** **Required or**
**Optional**

`attributes` Collection Attributes for this record. The attributes property contains Required
two subproperties:

**•** `type` (required)—This record’s type.

**•** `referenceId` (required)—Reference ID for this record.
Must be unique in the context of the request and start with
an alphanumeric character.

In XML, include attributes inside the `records` element.

Required object fields Depends on Required fields and field values for this record. Required
field

Optional object fields Depends on Optional fields and field values for this record. Optional
field


Child relationships


sObject Tree This record’s child relationships, such as an account’s child Optional
Collection contacts. Child relationships are either master-detail or lookup
Input relationships. To view an object’s valid child relationships, use

the sObject Describe resource or Schema Builder. The value of
this property is an sObject Tree Collection Input that contains
child sObject trees.


-----

**Root XML Tag**
```
  <records>

```
**JSON example**
```
  {
  "attributes" : {"type" : "Account", "referenceId" : "ref1"},
  "name" : "SampleAccount",
  "phone" : "1234567890",
  "website" : "www.salesforce.com",
  "NumberOfEmployees" : "100",
  "industry" : "Banking",
  "Contacts" : {
   "records" : [{
     "lastname" : "Smith",
     "title" : "President",
     "email" : "sample@salesforce.com"
      },{
     "lastname" : "Evans",
     "title" : "Vice President",
     "email" : "sample@salesforce.com"
     }]
   }
  }

```
**XML example**
```
  <records type="Account" referenceId="ref1">
    <name>SampleAccount</name>
    <phone>1234567890</phone>
    <website>www.salesforce.com</website>
    <numberOfEmployees>100</numberOfEmployees>
    <industry>Banking</industry>
    <Contacts>
       <records type="Contact" referenceId="ref2">
         <lastname>Smith</lastname>
         <title>President</title>
         <email>sample@salesforce.com</email>
       </records>
       <records type="Contact" referenceId="ref3">
         <lastname>Evans</lastname>
         <title>Vice President</title>
         <email>sample@salesforce.com</email>
       </records>
    </Contacts>
  </records>

#### sObject Tree Response Body

```
Describes the result of an sObject Tree request.


-----

**Properties**

**Name** **Type** **Description**

`hasErrors` Boolean `true` if an error occurred while creating a record; `false` otherwise.

`results` Collection Upon success, `results` contains the reference ID of each requested
record and its new record ID. Upon failure, it contains only the reference

ID of the record that caused the error, error status code, error message,
and fields related to the error. In the case of duplicate reference IDs,
`results` contains one item for each instance of the duplicate ID.

**JSON example upon success**
```
  {
    "hasErrors" : false,
    "results" : [{
     "referenceId" : "ref1",
     "id" : "001D000000K0fXOIAZ"
     },{
     "referenceId" : "ref4",
     "id" : "001D000000K0fXPIAZ"
     },{
     "referenceId" : "ref2",
     "id" : "003D000000QV9n2IAD"
     },{
     "referenceId" : "ref3",
     "id" : "003D000000QV9n3IAD"
     }]
  }

```
**XML example upon success**


-----

**JSON example upon failure**
```
  {
    "hasErrors" : true,
    "results" : [{
     "referenceId" : "ref2",
     "errors" : [{
      "statusCode" : "INVALID_EMAIL_ADDRESS",
      "message" : "Email: invalid email address: 123",
      "fields" : [ "Email" ]
      }]
     }]
  }

```
**XML example upon failure**
```
  <SObjectTreeResponse>
    <hasErrors>true</hasErrors>
    <results>
       <errors>
         <fields>Email</fields>
         <message>Email: invalid email address: 123</message>
         <statusCode>INVALID_EMAIL_ADDRESS</statusCode>
       </errors>
       <referenceId>ref2</referenceId>
    </results>
  </SObjectTreeResponse>
