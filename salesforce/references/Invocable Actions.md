### Invocable Actions

Represents standard and custom invocable actions. Use actions to add more functionality to your applications. Choose from standard
actions, such as posting to Chatter or sending email, or create actions based on your company’s needs.

IN THIS SECTION:

Get Invocable Actions
Gets standard and custom invocable action URIs from Salesforce. This resource is available in REST API version 32.0 and later.

Return HTTP Headers for Invocable Actions
Returns only the headers that are returned by sending a GET request to the invocable actions resource. This gives you a chance to
see returned header values of the GET request before retrieving the content. This resource is available in REST API version 32.0 and
later.

SEE ALSO:

_[Apex Developer Guide : InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.252.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)_

#### Get Invocable Actions

Gets standard and custom invocable action URIs from Salesforce. This resource is available in REST API version 32.0 and later.

##### Example

 URI
```
/services/data/vXX.X/actions

 Formats

```
JSON, XML

##### HTTP Methods

GET


-----

##### Authentication
```
Authorization: Bearer token

 Request parameters

```
None required

##### Example

Example Request
```
curl https://MyDomainName.my.salesforce.com/services/data/v62.0/actions -H "Authorization:
 Bearer token"

```
Example Response Body
```
{
  "standard" : "/services/data/v62.0/actions/standard",
  "custom" : "/services/data/v62.0/actions/custom"
}

#### Return HTTP Headers for Invocable Actions

```
Returns only the headers that are returned by sending a GET request to the invocable actions resource. This gives you a chance to see
returned header values of the GET request before retrieving the content. This resource is available in REST API version 32.0 and later.

##### URI
```
/services/data/vXX.X/actions

 Formats

```
JSON, XML

##### HTTP Methods

HEAD

##### Authentication
```
Authorization: Bearer token

 Request parameters

```
None required


-----

##### Example

Example Request
```
curl -X HEAD --head https://MyDomainName.my.salesforce.com/services/data/v62.0/actions -H
 "Authorization: Bearer token"

```
Example Response Body
```
HTTP/1.1 200 OK
Date: Mon, 21 Nov 2022 22:56:26 GMT
