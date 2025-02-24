### Invocable Actions Standard

```
Represents standard invocable actions that can be statically invoked. You can also get basic information for each type of action.

IN THIS SECTION:

Get Standard Invocable Actions
Gets the list of standard invocable actions that are provided by Salesforce. Some actions require special access. This resource is
available in REST API version 32.0 and later.

Return HTTP Headers for Standard Invocable Actions
Returns only the headers that are returned by sending a GET request to the standard invocable actions resource. This gives you a
chance to see returned header values of the GET request before retrieving the content. This resource is available in REST API version
32.0 and later.

SEE ALSO:

_[Apex Developer Guide : InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.252.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)_

#### Get Standard Invocable Actions

Gets the list of standard invocable actions that are provided by Salesforce. Some actions require special access. This resource is available
in REST API version 32.0 and later.

For Salesforce Omnichannel Inventory and Salesforce Order Management, you can also call the corresponding Connect REST API endpoints
[or Apex ConnectApi methods. For more information, see Salesforce Omnichannel Inventory Resources and Salesforce Order Management](https://developer.salesforce.com/docs/atlas.en-us.252.0.chatterapi.meta/chatterapi/connect_resources_omnichannel_inventory_resources.htm)
[Resources in the Connect REST API Developer Guide, and ConnectApi Namespace in the Apex Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.252.0.chatterapi.meta/chatterapi/connect_resources_order_management_resources.htm)

The Post to Chatter action supports the following features using a special format in the body post. For example, the string `Hi`
`@[005000000000001], check out #[some_topic]` is stored appropriately as `Hi @Joe, check out`
`#some_topic` where “@Joe” and “#some_topic” are links to the user and topic, respectively.

**•** @mentions using `@[<id>]`

**•** Topic links using `#[<topicString>]`

For more information about actions, see the Actions Developer Guide.


-----

##### Syntax

 URI
```
/services/data/vXX.X/actions/standard

 Formats

```
JSON, XML

##### HTTP Methods

GET

##### Authentication
```
Authorization: Bearer token

 Request parameters

```
None required

##### Example

Example Request
```
curl https://MyDomainName
"Authorization: Bearer token"

```
Example Response Body


-----

#### Return HTTP Headers for Standard Invocable Actions

Returns only the headers that are returned by sending a GET request to the standard invocable actions resource. This gives you a chance
to see returned header values of the GET request before retrieving the content. This resource is available in REST API version 32.0 and
later.

##### Syntax

 URI
```
/services/data/vXX.X/actions/standard

 Formats

```
JSON, XML


-----

##### HTTP Methods

HEAD

##### Authentication
```
Authorization: Bearer token

 Request parameters

```
None required

##### Example

Example Request
```
curl -X HEAD --head
https://MyDomainName.my.salesforce.com/services/data/v62.0/actions/standard -H
"Authorization: Bearer token"

```
Example Response Body
```
HTTP/1.1 200 OK
Date: Mon, 21 Nov 2022 22:56:26 GMT
